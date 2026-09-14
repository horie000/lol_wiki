#!/usr/bin/env python3
"""Riot API からランク戦の直近試合をランク帯ごとに収集する。

このスクリプトは League-v4 で現在のランク帯に所属するプレイヤーを取得し、
Match-v5 の PUUID 別試合履歴から候補を集める。試合詳細を取得した後、
``gameStartTimestamp`` の降順で重複を除去し、ランク帯ごとに指定件数を保存する。

API キーは ``RIOT_API_KEY`` 環境変数からのみ読み込む。標準設定は Riot の
個人キーを想定した 100 リクエスト / 120 秒のローカル制限であり、429 応答の
``Retry-After`` も尊重する。出力は JSONL の試合データと収集メタデータである。
収集データの出力先はリポジトリ内の ``raw/`` 配下に限定する。

Usage:
    RIOT_API_KEY='RGAPI-...' python3 scripts/riot_ranked_match_collector.py \
        --platform jp1 --output raw/sources/riot-ranked-matches --overwrite
    python3 scripts/riot_ranked_match_collector.py --platform jp1 --dry-run
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import random
import re
import sys
import tempfile
import time
from collections import defaultdict, deque
from dataclasses import dataclass
from pathlib import Path
from typing import Any, DefaultDict, Dict, Iterable, List, Mapping, Optional, Sequence, Tuple
from urllib.error import HTTPError, URLError
from urllib.parse import quote, urlencode
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[1]
RAW_ROOT = ROOT / "raw"
DEFAULT_OUTPUT = ROOT / "raw" / "sources" / "riot-ranked-matches"
_PROGRESS_BAR_ACTIVE = False

# Riot の公式ドキュメントで示されるプラットフォームと地域ルーティング。
PLATFORM_TO_REGIONAL_ROUTE: Dict[str, str] = {
    "br1": "americas",
    "eun1": "europe",
    "euw1": "europe",
    "jp1": "asia",
    "kr": "asia",
    "la1": "americas",
    "la2": "americas",
    "na1": "americas",
    "oc1": "sea",
    "ph2": "sea",
    "ru": "europe",
    "sg2": "sea",
    "th2": "sea",
    "tr1": "europe",
    "tw2": "sea",
    "vn2": "sea",
}

QUEUE_CONFIG: Dict[str, Tuple[int, str]] = {
    "RANKED_SOLO_5x5": (420, "ranked-solo-5x5"),
    "RANKED_FLEX_SR": (440, "ranked-flex-sr"),
}

STANDARD_TIERS: Tuple[str, ...] = (
    "IRON",
    "BRONZE",
    "SILVER",
    "GOLD",
    "PLATINUM",
    "EMERALD",
    "DIAMOND",
)
HIGH_TIERS: Tuple[str, ...] = ("MASTER", "GRANDMASTER", "CHALLENGER")
ALL_TIERS: Tuple[str, ...] = STANDARD_TIERS + HIGH_TIERS
DIVISIONS: Tuple[str, ...] = ("I", "II", "III", "IV")
MATCH_ID_RE = re.compile(r"^[A-Za-z0-9_.:-]+$")


class RiotApiError(RuntimeError):
    """Riot API が再試行しても成功しなかった場合のエラー。"""

    def __init__(self, status: int, url: str, message: str) -> None:
        super().__init__(f"Riot API {status}: {url}: {message}")
        self.status = status
        self.url = url
        self.message = message


def sleep_in_chunks(seconds: float) -> None:
    """長いレート制限待ちでも一定間隔で停止を分割する。"""

    remaining = max(0.0, seconds)
    while remaining > 0:
        delay = min(remaining, 30.0)
        time.sleep(delay)
        remaining -= delay


class WindowLimiter:
    """ルートごとのスライディングウィンドウ制限。"""

    def __init__(self, limit: int, window_seconds: float, min_interval: float) -> None:
        self.limit = limit
        self.window_seconds = window_seconds
        self.min_interval = min_interval
        self.timestamps: deque[float] = deque()
        self.last_request = 0.0

    def wait(self) -> None:
        while True:
            now = time.monotonic()
            while self.timestamps and now - self.timestamps[0] >= self.window_seconds:
                self.timestamps.popleft()

            interval_wait = self.min_interval - (now - self.last_request)
            window_wait = 0.0
            if self.limit > 0 and len(self.timestamps) >= self.limit:
                window_wait = self.window_seconds - (now - self.timestamps[0])
            wait_for = max(interval_wait, window_wait, 0.0)
            if wait_for <= 0:
                self.timestamps.append(now)
                self.last_request = now
                return
            sleep_in_chunks(wait_for)


class RiotClient:
    """API キー、地域ルーティング、再試行、レート制限を一元管理する。"""

    def __init__(
        self,
        api_key: str,
        *,
        timeout: float,
        max_retries: int,
        rate_limit_count: int,
        rate_limit_window: float,
        min_interval: float,
        user_agent: str,
    ) -> None:
        self.api_key = api_key
        self.timeout = timeout
        self.max_retries = max_retries
        self.rate_limit_count = rate_limit_count
        self.rate_limit_window = rate_limit_window
        self.min_interval = min_interval
        self.user_agent = user_agent
        self.limiters: Dict[str, WindowLimiter] = {}

    def _limiter(self, route: str) -> WindowLimiter:
        if route not in self.limiters:
            self.limiters[route] = WindowLimiter(
                self.rate_limit_count,
                self.rate_limit_window,
                self.min_interval,
            )
        return self.limiters[route]

    @staticmethod
    def _url(route: str, path: str, params: Optional[Mapping[str, Any]]) -> str:
        base = f"https://{route}.api.riotgames.com"
        query = urlencode({key: value for key, value in (params or {}).items() if value is not None})
        return f"{base}{path}" + (f"?{query}" if query else "")

    @staticmethod
    def _retry_after(error: HTTPError) -> float:
        value = error.headers.get("Retry-After")
        if value is None:
            return 1.0
        try:
            return max(float(value), 0.1)
        except ValueError:
            return 1.0

    @staticmethod
    def _error_body(error: HTTPError) -> str:
        try:
            body = error.read().decode("utf-8", errors="replace")
        except OSError:
            return error.reason if error.reason else "unknown error"
        return body[:1000] or (error.reason if error.reason else "empty response")

    def get_json(
        self,
        route: str,
        path: str,
        params: Optional[Mapping[str, Any]] = None,
    ) -> Any:
        url = self._url(route, path, params)
        for attempt in range(self.max_retries + 1):
            self._limiter(route).wait()
            request = Request(
                url,
                headers={
                    "Accept": "application/json",
                    "User-Agent": self.user_agent,
                    "X-Riot-Token": self.api_key,
                },
                method="GET",
            )
            try:
                with urlopen(request, timeout=self.timeout) as response:
                    raw = response.read()
                if not raw:
                    return None
                return json.loads(raw.decode("utf-8"))
            except HTTPError as error:
                if error.code == 429:
                    delay = self._retry_after(error)
                    if attempt >= self.max_retries:
                        raise RiotApiError(error.code, url, self._error_body(error)) from error
                    print(
                        f"429 rate limit: {route}; {delay:.1f}秒待機して再試行します",
                        file=sys.stderr,
                    )
                    sleep_in_chunks(delay)
                    continue
                if error.code in {500, 502, 503, 504} and attempt < self.max_retries:
                    delay = min(60.0, (2**attempt) + random.random())
                    print(
                        f"HTTP {error.code}: {route}; {delay:.1f}秒後に再試行します",
                        file=sys.stderr,
                    )
                    sleep_in_chunks(delay)
                    continue
                raise RiotApiError(error.code, url, self._error_body(error)) from error
            except (URLError, TimeoutError, OSError) as error:
                if attempt >= self.max_retries:
                    raise RiotApiError(0, url, str(error)) from error
                delay = min(60.0, (2**attempt) + random.random())
                print(
                    f"通信エラー: {route}; {delay:.1f}秒後に再試行します ({error})",
                    file=sys.stderr,
                )
                sleep_in_chunks(delay)
        raise AssertionError("unreachable")


@dataclass(frozen=True)
class RankedPlayer:
    puuid: str
    tier: str
    division: str


def now_iso() -> str:
    return dt.datetime.now(dt.timezone.utc).isoformat().replace("+00:00", "Z")


def progress(message: str) -> None:
    """進捗を標準出力へ即時表示する。"""

    global _PROGRESS_BAR_ACTIVE
    if _PROGRESS_BAR_ACTIVE:
        print(file=sys.stdout, flush=True)
        _PROGRESS_BAR_ACTIVE = False
    print(message, file=sys.stdout, flush=True)


def progress_bar(
    label: str,
    current: int,
    total: int,
    *,
    width: int = 32,
    complete: bool = False,
) -> None:
    """シーケンス進捗を標準出力へ描画する。"""

    global _PROGRESS_BAR_ACTIVE
    if total > 0:
        bounded_current = min(max(current, 0), total)
        ratio = bounded_current / total
        count = int(round(width * ratio))
        status = f"{bounded_current}/{total} ({ratio * 100:5.1f}%)"
    else:
        count = 0
        status = f"{max(current, 0)}/0 (--.-%)"
    bar = "#" * count + "-" * (width - count)
    end = "\n" if complete else ""
    print(f"\r{label} [{bar}] {status}", end=end, flush=True)
    _PROGRESS_BAR_ACTIVE = not complete


def format_elapsed(seconds: float) -> str:
    """経過秒数を日本語の読みやすい表記へ変換する。"""

    total_seconds = max(0.0, seconds)
    hours = int(total_seconds // 3600)
    minutes = int((total_seconds - hours * 3600) // 60)
    remaining = total_seconds - hours * 3600 - minutes * 60
    parts: List[str] = []
    if hours:
        parts.append(f"{hours}時間")
    if minutes or hours:
        parts.append(f"{minutes}分")
    parts.append(f"{remaining:.1f}秒")
    return "".join(parts)


def atomic_write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(
        mode="w",
        encoding="utf-8",
        dir=path.parent,
        prefix=f".{path.name}.",
        suffix=".tmp",
        delete=False,
    ) as handle:
        temporary = Path(handle.name)
        handle.write(text)
    os.replace(temporary, path)


def atomic_write_json(path: Path, value: Any) -> None:
    atomic_write_text(path, json.dumps(value, ensure_ascii=False, indent=2) + "\n")


def load_json(path: Path, default: Any) -> Any:
    if not path.exists():
        return default
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return default


def normalize_tiers(value: str) -> List[str]:
    tiers = [part.strip().upper() for part in value.split(",") if part.strip()]
    if not tiers:
        raise argparse.ArgumentTypeError("--tiers は1つ以上指定してください")
    invalid = [tier for tier in tiers if tier not in ALL_TIERS]
    if invalid:
        raise argparse.ArgumentTypeError(
            f"未知のランク帯: {', '.join(invalid)}（使用可能: {', '.join(ALL_TIERS)}）"
        )
    result: List[str] = []
    for tier in tiers:
        if tier not in result:
            result.append(tier)
    return result


def resolve_regional_route(platform: str, requested: str) -> str:
    route = requested.lower()
    if route != "auto":
        if route not in {"americas", "asia", "europe", "sea"}:
            raise ValueError("--regional-route は americas/asia/europe/sea/auto のいずれかです")
        return route
    try:
        return PLATFORM_TO_REGIONAL_ROUTE[platform.lower()]
    except KeyError as error:
        supported = ", ".join(sorted(PLATFORM_TO_REGIONAL_ROUTE))
        raise ValueError(f"未知のプラットフォーム {platform!r}。対応値: {supported}") from error


def resolve_output_root(value: Path) -> Path:
    """収集データの出力先をリポジトリ内の ``raw/`` 配下に限定する。"""

    candidate = value if value.is_absolute() else ROOT / value
    candidate = candidate.resolve()
    raw_root = RAW_ROOT.resolve()
    try:
        candidate.relative_to(raw_root)
    except ValueError as error:
        raise ValueError(
            f"--output は raw/ 配下に指定してください: {candidate}"
        ) from error
    return candidate


def queue_settings(queue: str) -> Tuple[int, str]:
    try:
        return QUEUE_CONFIG[queue]
    except KeyError as error:
        raise ValueError(f"未対応のキュー: {queue}") from error


def entry_key(entry: Mapping[str, Any], fallback: str) -> str:
    return str(entry.get("puuid") or entry.get("summonerId") or fallback)


def evenly_sample(entries: Sequence[Mapping[str, Any]], limit: int) -> List[Mapping[str, Any]]:
    """ランク帯内のエントリを決定的に均等サンプルする。limit=0 は全件。"""

    if limit <= 0 or len(entries) <= limit:
        return list(entries)
    if limit == 1:
        return [entries[0]]
    indices = [round(index * (len(entries) - 1) / (limit - 1)) for index in range(limit)]
    result: List[Mapping[str, Any]] = []
    seen: set[str] = set()
    for index in indices:
        entry = entries[index]
        key = entry_key(entry, str(index))
        if key not in seen:
            result.append(entry)
            seen.add(key)
    return result


def fetch_standard_entries(
    client: RiotClient,
    platform: str,
    queue: str,
    tier: str,
    max_pages: int,
) -> List[Dict[str, Any]]:
    entries: List[Dict[str, Any]] = []
    seen: set[str] = set()
    for division in DIVISIONS:
        progress(f"[{tier}] ランク一覧 {division} を取得中")
        previous_page_keys: set[str] = set()
        for page in range(1, max_pages + 1):
            payload = client.get_json(
                platform,
                f"/lol/league/v4/entries/{queue}/{tier}/{division}",
                {"page": page},
            )
            if not isinstance(payload, list) or not payload:
                break
            page_keys = {entry_key(item, f"{division}:{page}:{index}") for index, item in enumerate(payload) if isinstance(item, Mapping)}
            if not page_keys or page_keys.issubset(previous_page_keys):
                break
            previous_page_keys.update(page_keys)
            for index, item in enumerate(payload):
                if not isinstance(item, Mapping):
                    continue
                item_copy = dict(item)
                item_copy["_tier"] = tier
                item_copy["_division"] = str(item.get("rank") or division)
                key = entry_key(item_copy, f"{division}:{page}:{index}")
                if key not in seen:
                    entries.append(item_copy)
                    seen.add(key)
            if page == 1 or page % 10 == 0:
                progress(f"[{tier}] ランク一覧 {division}: page={page}, 累計={len(entries)}件")
            if len(payload) < 100:
                break
    return entries


def fetch_high_entries(
    client: RiotClient,
    platform: str,
    queue: str,
    tier: str,
) -> List[Dict[str, Any]]:
    progress(f"[{tier}] 上位ランク一覧を取得中")
    endpoint = {
        "MASTER": "masterleagues",
        "GRANDMASTER": "grandmasterleagues",
        "CHALLENGER": "challengerleagues",
    }[tier]
    payload = client.get_json(platform, f"/lol/league/v4/{endpoint}/by-queue/{queue}")
    if not isinstance(payload, Mapping):
        raise RuntimeError(f"{tier} のリーグ応答がオブジェクトではありません")
    entries = payload.get("entries", [])
    if not isinstance(entries, list):
        raise RuntimeError(f"{tier} の entries が配列ではありません")
    result: List[Dict[str, Any]] = []
    seen: set[str] = set()
    for index, item in enumerate(entries):
        if not isinstance(item, Mapping):
            continue
        item_copy = dict(item)
        item_copy["_tier"] = tier
        item_copy["_division"] = str(item.get("rank") or "I")
        key = entry_key(item_copy, f"{tier}:{index}")
        if key not in seen:
            result.append(item_copy)
            seen.add(key)
    return result


def fetch_entries(
    client: RiotClient,
    platform: str,
    queue: str,
    tier: str,
    max_league_pages: int,
) -> List[Dict[str, Any]]:
    if tier in STANDARD_TIERS:
        return fetch_standard_entries(client, platform, queue, tier, max_league_pages)
    return fetch_high_entries(client, platform, queue, tier)


def resolve_players(
    client: RiotClient,
    platform: str,
    entries: Sequence[Mapping[str, Any]],
    cache: Dict[str, str],
    progress_label: str = "",
) -> Tuple[List[RankedPlayer], int]:
    players: List[RankedPlayer] = []
    unresolved = 0
    seen_puuids: set[str] = set()
    total = len(entries)
    for index, entry in enumerate(entries, start=1):
        puuid = str(entry.get("puuid") or "")
        summoner_id = str(entry.get("summonerId") or "")
        if not puuid and summoner_id:
            cache_key = f"{platform}:{summoner_id}"
            puuid = cache.get(cache_key, "")
            if not puuid:
                payload = client.get_json(
                    platform,
                    f"/lol/summoner/v4/summoners/{quote(summoner_id, safe='')}",
                )
                if isinstance(payload, Mapping):
                    puuid = str(payload.get("puuid") or "")
                if puuid:
                    cache[cache_key] = puuid
        if not puuid or puuid in seen_puuids:
            unresolved += 1
            if index == 1 or index % 10 == 0 or index == total:
                progress_bar(
                    f"{progress_label}PUUID解決",
                    index,
                    total,
                    complete=index == total,
                )
            continue
        seen_puuids.add(puuid)
        players.append(
            RankedPlayer(
                puuid=puuid,
                tier=str(entry.get("_tier") or "UNKNOWN"),
                division=str(entry.get("_division") or "I"),
            )
        )
        if index == 1 or index % 10 == 0 or index == total:
            progress_bar(
                f"{progress_label}PUUID解決",
                index,
                total,
                complete=index == total,
            )
    if not total:
        progress_bar(f"{progress_label}PUUID解決", 0, 0, complete=True)
    return players, unresolved


def collect_candidate_ids(
    client: RiotClient,
    regional_route: str,
    queue_id: int,
    players: Sequence[RankedPlayer],
    candidate_target: int,
    max_pages_per_player: int,
    progress_label: str = "",
) -> Tuple[List[str], Dict[str, List[Dict[str, str]]]]:
    ordered_ids: List[str] = []
    observations: DefaultDict[str, List[Dict[str, str]]] = defaultdict(list)
    total = len(players)
    for player_index, player in enumerate(players, start=1):
        for page in range(max_pages_per_player):
            payload = client.get_json(
                regional_route,
                f"/lol/match/v5/matches/by-puuid/{quote(player.puuid, safe='')}/ids",
                {
                    "queue": queue_id,
                    "type": "ranked",
                    "start": page * 100,
                    "count": 100,
                },
            )
            if not isinstance(payload, list) or not payload:
                break
            for raw_match_id in payload:
                match_id = str(raw_match_id)
                if not MATCH_ID_RE.match(match_id):
                    continue
                if match_id not in observations:
                    ordered_ids.append(match_id)
                observation = {"tier": player.tier, "division": player.division}
                if observation not in observations[match_id]:
                    observations[match_id].append(observation)
            if len(ordered_ids) >= candidate_target:
                progress_bar(
                    f"{progress_label}試合ID候補取得",
                    player_index,
                    total,
                    complete=True,
                )
                return ordered_ids, dict(observations)
            if len(payload) < 100:
                break
        if player_index == 1 or player_index % 10 == 0 or player_index == total:
            progress_bar(
                f"{progress_label}試合ID候補取得",
                player_index,
                total,
                complete=player_index == total,
            )
    if not total:
        progress_bar(f"{progress_label}試合ID候補取得", 0, 0, complete=True)
    return ordered_ids, dict(observations)


def cache_file(cache_dir: Path, match_id: str) -> Path:
    safe_match_id = re.sub(r"[^A-Za-z0-9_.-]", "_", match_id)
    return cache_dir / "matches" / f"{safe_match_id}.json"


def load_cached_match(cache_dir: Path, match_id: str) -> Optional[Mapping[str, Any]]:
    payload = load_json(cache_file(cache_dir, match_id), None)
    if not isinstance(payload, Mapping):
        return None
    match = payload.get("match")
    return match if isinstance(match, Mapping) else None


def save_cached_match(cache_dir: Path, match_id: str, match: Mapping[str, Any]) -> None:
    atomic_write_json(
        cache_file(cache_dir, match_id),
        {"schema_version": 1, "cached_at": now_iso(), "match": match},
    )


def match_start_timestamp(match: Mapping[str, Any]) -> Optional[int]:
    info = match.get("info")
    if not isinstance(info, Mapping):
        return None
    value = info.get("gameStartTimestamp")
    if value is None:
        value = info.get("gameCreation")
    try:
        timestamp = int(value)
    except (TypeError, ValueError):
        return None
    # gameCreation は ms、古い形式の秒値も受け付ける。
    return timestamp if timestamp >= 10**12 else timestamp * 1000


def fetch_match_records(
    client: RiotClient,
    regional_route: str,
    queue_id: int,
    candidate_ids: Sequence[str],
    observations: Mapping[str, Sequence[Mapping[str, str]]],
    cache_dir: Path,
    progress_label: str = "",
) -> Tuple[List[Dict[str, Any]], List[str]]:
    records: List[Dict[str, Any]] = []
    skipped: List[str] = []
    total = len(candidate_ids)
    if total:
        progress_bar(f"{progress_label}試合詳細取得", 0, total)
    for index, match_id in enumerate(candidate_ids, start=1):
        match = load_cached_match(cache_dir, match_id)
        if match is None:
            try:
                payload = client.get_json(
                    regional_route,
                    f"/lol/match/v5/matches/{quote(match_id, safe='')}",
                )
            except RiotApiError as error:
                if error.status == 404:
                    skipped.append(match_id)
                    continue
                raise
            if not isinstance(payload, Mapping):
                skipped.append(match_id)
                continue
            match = payload
            save_cached_match(cache_dir, match_id, match)
        info = match.get("info")
        if not isinstance(info, Mapping) or info.get("queueId") != queue_id:
            skipped.append(match_id)
            continue
        timestamp = match_start_timestamp(match)
        if timestamp is None:
            skipped.append(match_id)
            continue
        raw_observations = observations.get(match_id, [])
        normalized_observations = sorted(
            {
                (str(item.get("tier") or "UNKNOWN"), str(item.get("division") or "I"))
                for item in raw_observations
            }
        )
        records.append(
            {
                "schema_version": 1,
                "match_id": match_id,
                "game_start_timestamp": timestamp,
                "observed_tier": normalized_observations[0][0] if normalized_observations else "UNKNOWN",
                "observed_divisions": [division for _, division in normalized_observations],
                "match": match,
            }
        )
        if index == 1 or index % 100 == 0 or index == total:
            progress_bar(
                f"{progress_label}試合詳細取得",
                index,
                total,
                complete=index == total,
            )
    if not total:
        progress_bar(f"{progress_label}試合詳細取得", 0, 0, complete=True)
    records.sort(key=lambda item: (item["game_start_timestamp"], item["match_id"]), reverse=True)
    return records, skipped


def write_matches(path: Path, records: Sequence[Mapping[str, Any]]) -> None:
    content = "".join(
        json.dumps(record, ensure_ascii=False, separators=(",", ":")) + "\n"
        for record in records
    )
    atomic_write_text(path, content)


def tier_output_dir(output_root: Path, platform: str, queue_slug: str, tier: str) -> Path:
    return output_root / platform.lower() / queue_slug / tier.lower()


def collect_tier(
    client: RiotClient,
    *,
    tier_index: int,
    tier_total: int,
    platform: str,
    regional_route: str,
    queue: str,
    queue_id: int,
    queue_slug: str,
    tier: str,
    target_count: int,
    max_players: int,
    candidate_multiplier: float,
    max_pages_per_player: int,
    max_league_pages: int,
    output_root: Path,
    identity_cache: Dict[str, str],
    allow_incomplete: bool,
    overwrite: bool,
) -> None:
    progress(f"[{tier_index}/{tier_total}] [{tier}] 収集開始")
    output_dir = tier_output_dir(output_root, platform, queue_slug, tier)
    matches_path = output_dir / "matches.jsonl"
    manifest_path = output_dir / "manifest.json"
    if not overwrite and (matches_path.exists() or manifest_path.exists()):
        raise RuntimeError(
            f"既存の出力があります: {output_dir}。上書きする場合は --overwrite を指定してください"
        )

    progress(f"[{tier}] ランク帯エントリを取得中")
    raw_entries = fetch_entries(client, platform, queue, tier, max_league_pages)
    progress(f"[{tier}] ランク帯エントリ取得完了: {len(raw_entries)}件")
    selected_entries = evenly_sample(raw_entries, max_players)
    progress(f"[{tier}] 対象プレイヤーを解決中: {len(selected_entries)}人")
    players, unresolved = resolve_players(
        client,
        platform,
        selected_entries,
        identity_cache,
        progress_label=f"[{tier}] ",
    )
    progress(f"[{tier}] プレイヤー解決完了: 成功={len(players)}人、未解決={unresolved}人")
    candidate_target = max(target_count, int(target_count * candidate_multiplier + 0.999999))
    progress(f"[{tier}] 試合ID候補を取得中: 目標={candidate_target}件")
    candidate_ids, observations = collect_candidate_ids(
        client,
        regional_route,
        queue_id,
        players,
        candidate_target,
        max_pages_per_player,
        progress_label=f"[{tier}] ",
    )
    progress(f"[{tier}] 試合ID候補取得完了: {len(candidate_ids)}件")
    cache_dir = output_root / ".cache"
    progress(f"[{tier}] 試合詳細を取得中: {len(candidate_ids)}件")
    records, skipped = fetch_match_records(
        client,
        regional_route,
        queue_id,
        candidate_ids,
        observations,
        cache_dir,
        progress_label=f"[{tier}] ",
    )
    progress(f"[{tier}] 試合詳細取得完了: 有効={len(records)}件、除外={len(skipped)}件")
    selected_records = records[:target_count]
    if len(selected_records) < target_count and not allow_incomplete:
        raise RuntimeError(
            f"{tier}: {len(selected_records)}件しか選択できませんでした（要求 {target_count}件）。"
            "プレイヤー数・履歴ページ数を増やすか --allow-incomplete を指定してください"
        )

    write_matches(matches_path, selected_records)
    manifest = {
        "schema_version": 1,
        "collector": "scripts/riot_ranked_match_collector.py",
        "collected_at": now_iso(),
        "platform": platform.lower(),
        "regional_route": regional_route,
        "queue": queue,
        "queue_id": queue_id,
        "tier": tier,
        "requested_matches": target_count,
        "collected_matches": len(selected_records),
        "complete": len(selected_records) == target_count,
        "source_entries": len(raw_entries),
        "sampled_entries": len(selected_entries),
        "resolved_players": len(players),
        "unresolved_players": unresolved,
        "candidate_match_ids": len(candidate_ids),
        "valid_match_details": len(records),
        "skipped_match_ids": len(skipped),
        "max_players_per_tier": max_players,
        "candidate_multiplier": candidate_multiplier,
        "rank_observation": "収集時点のLeague-v4所属ランク帯。試合時点のランクを表さない。",
        "selection": "重複除去後、Match-v5のgameStartTimestamp降順で選択",
        "files": {"matches": str(matches_path.relative_to(output_root)), "manifest": str(manifest_path.relative_to(output_root))},
    }
    atomic_write_json(manifest_path, manifest)
    progress(
        f"[{tier}] entries={len(raw_entries)} players={len(players)} "
        f"candidates={len(candidate_ids)} valid={len(records)} selected={len(selected_records)}"
    )
    progress(f"[{tier_index}/{tier_total}] [{tier}] 保存完了")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--platform", default="jp1", help="プラットフォームID（既定: jp1）")
    parser.add_argument(
        "--regional-route",
        default="auto",
        choices=("auto", "americas", "asia", "europe", "sea"),
        help="Match-v5の地域ルート（既定: platformから自動判定）",
    )
    parser.add_argument(
        "--queue",
        default="RANKED_SOLO_5x5",
        choices=tuple(QUEUE_CONFIG),
        help="収集キュー（既定: RANKED_SOLO_5x5）",
    )
    parser.add_argument(
        "--tiers",
        type=normalize_tiers,
        default=list(ALL_TIERS),
        help="対象ランク帯をカンマ区切りで指定（既定: 全10帯）",
    )
    parser.add_argument(
        "--match-count",
        type=int,
        default=1000,
        help="ランク帯ごとの収集件数（既定: 1000）",
    )
    parser.add_argument(
        "--max-players-per-tier",
        type=int,
        default=100,
        help="ランク帯ごとに履歴取得へ使うプレイヤー数。0は全員（既定: 100）",
    )
    parser.add_argument(
        "--candidate-multiplier",
        type=float,
        default=2.0,
        help="詳細取得候補の倍率（既定: 2.0。欠損を考慮して目標件数の2倍）",
    )
    parser.add_argument(
        "--max-pages-per-player",
        type=int,
        default=5,
        help="プレイヤーごとのMatch-v5履歴ページ数（1ページ100件、既定: 5）",
    )
    parser.add_argument(
        "--max-league-pages",
        type=int,
        default=100,
        help="通常ランク帯のLeague-v4ページ上限（既定: 100）",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT,
        help=f"出力ルート（既定: {DEFAULT_OUTPUT}）",
    )
    parser.add_argument(
        "--rate-limit-count",
        type=int,
        default=100,
        help="ルートごとのローカル上限（既定: 100）",
    )
    parser.add_argument(
        "--rate-limit-window",
        type=float,
        default=120.0,
        help="ローカル上限の秒数（既定: 120）",
    )
    parser.add_argument(
        "--min-interval",
        type=float,
        default=0.06,
        help="同一ルートの最小リクエスト間隔（秒、既定: 0.06）",
    )
    parser.add_argument("--timeout", type=float, default=30.0, help="HTTPタイムアウト秒（既定: 30）")
    parser.add_argument("--max-retries", type=int, default=6, help="429/5xx/通信失敗の再試行回数（既定: 6）")
    parser.add_argument(
        "--allow-incomplete",
        action="store_true",
        help="1000件未満でもファイルを書き出す（既定は不足時に失敗）",
    )
    parser.add_argument("--overwrite", action="store_true", help="既存のランク帯出力を上書きする")
    parser.add_argument("--dry-run", action="store_true", help="APIへ接続せず設定だけ表示する")
    return parser


def validate_args(args: argparse.Namespace) -> None:
    positive = {
        "match_count": args.match_count,
        "candidate_multiplier": args.candidate_multiplier,
        "max_pages_per_player": args.max_pages_per_player,
        "max_league_pages": args.max_league_pages,
        "rate_limit_window": args.rate_limit_window,
        "timeout": args.timeout,
    }
    for name, value in positive.items():
        if value <= 0:
            raise ValueError(f"--{name.replace('_', '-')} は正の値が必要です")
    if args.max_players_per_tier < 0:
        raise ValueError("--max-players-per-tier は0以上が必要です")
    if args.rate_limit_count < 0:
        raise ValueError("--rate-limit-count は0以上が必要です（0は無制限）")
    if args.min_interval < 0:
        raise ValueError("--min-interval は0以上が必要です")
    if not args.platform.strip():
        raise ValueError("--platform が空です")


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    started_at = time.monotonic()
    try:
        validate_args(args)
        platform = args.platform.lower()
        regional_route = resolve_regional_route(platform, args.regional_route)
        queue_id, queue_slug = queue_settings(args.queue)
        output_root = resolve_output_root(args.output)
        progress(
            json.dumps(
                {
                    "platform": platform,
                    "regional_route": regional_route,
                    "queue": args.queue,
                    "queue_id": queue_id,
                    "tiers": args.tiers,
                    "match_count": args.match_count,
                    "output": str(output_root),
                },
                ensure_ascii=False,
            )
        )
        if args.dry_run:
            progress(f"ドライラン完了: 所要時間 {format_elapsed(time.monotonic() - started_at)}")
            return 0
        api_key = os.environ.get("RIOT_API_KEY", "").strip()
        if not api_key:
            raise ValueError("RIOT_API_KEY 環境変数を設定してください")

        output_root.mkdir(parents=True, exist_ok=True)
        cache_dir = output_root / ".cache"
        identity_cache_path = cache_dir / "summoner-puuids.json"
        identity_cache = load_json(identity_cache_path, {})
        if not isinstance(identity_cache, dict):
            identity_cache = {}

        client = RiotClient(
            api_key,
            timeout=args.timeout,
            max_retries=args.max_retries,
            rate_limit_count=args.rate_limit_count,
            rate_limit_window=args.rate_limit_window,
            min_interval=args.min_interval,
            user_agent="llm-wiki/riot-ranked-match-collector",
        )
        tier_total = len(args.tiers)
        progress(
            f"収集開始: {tier_total}ランク帯、各{args.match_count}件、"
            f"出力先={output_root}"
        )
        progress_bar("全体進捗", 0, tier_total)
        for tier_index, tier in enumerate(args.tiers, start=1):
            collect_tier(
                client,
                tier_index=tier_index,
                tier_total=tier_total,
                platform=platform,
                regional_route=regional_route,
                queue=args.queue,
                queue_id=queue_id,
                queue_slug=queue_slug,
                tier=tier,
                target_count=args.match_count,
                max_players=args.max_players_per_tier,
                candidate_multiplier=args.candidate_multiplier,
                max_pages_per_player=args.max_pages_per_player,
                max_league_pages=args.max_league_pages,
                output_root=output_root,
                identity_cache=identity_cache,
                allow_incomplete=args.allow_incomplete,
                overwrite=args.overwrite,
            )
            atomic_write_json(identity_cache_path, identity_cache)
            progress_bar("全体進捗", tier_index, tier_total, complete=tier_index == tier_total)
        progress(
            f"収集完了: {tier_total}ランク帯、所要時間 "
            f"{format_elapsed(time.monotonic() - started_at)}"
        )
        return 0
    except (RiotApiError, RuntimeError, ValueError) as error:
        print(f"エラー: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
