#!/usr/bin/env python3
"""既存のMatch-v5試合IDから、Riot APIのTimelineデータを取得する。

Match-v5の ``matches.jsonl`` を入力にして試合IDを重複排除し、
``/lol/match/v5/matches/{matchId}/timeline`` を取得する。出力は分析用の
個人識別情報を除いたJSONLであり、APIレスポンスの ``metadata`` に含まれる
PUUID等は保存しない。APIキーは ``RIOT_API_KEY`` 環境変数からのみ読み込む。

Usage:
    python3 scripts/riot_match_timeline_collector.py \
        --input raw/sources/riot-ranked-matches/jp1/ranked-solo-5x5/gold/matches.jsonl \
        --limit 10 --dry-run
    RIOT_API_KEY='RGAPI-...' \
    python3 scripts/riot_match_timeline_collector.py \
        --input raw/sources/riot-ranked-matches \
        --limit 100
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import sys
import time
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Iterable, Mapping, Optional, Sequence
from urllib.parse import quote


SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

from riot_ranked_match_collector import (  # noqa: E402
    RiotApiError,
    RiotClient,
    atomic_write_json,
    atomic_write_text,
    format_elapsed,
    now_iso,
    progress,
    progress_bar,
    resolve_regional_route,
)


ROOT = Path(__file__).resolve().parents[1]
RAW_ROOT = ROOT / "raw"
DEFAULT_INPUT = RAW_ROOT / "sources" / "riot-ranked-matches"
DEFAULT_OUTPUT = ROOT / "reports" / "riot-match-timeline"
MATCH_ID_RE = re.compile(r"^[A-Za-z0-9_.:-]+$")
PII_KEYS = frozenset(
    {
        "puuid",
        "summonerid",
        "summonername",
        "riotidgamename",
        "riotidtagline",
    }
)


@dataclass
class MatchCandidate:
    """Timeline取得対象として必要な最小限の試合メタデータ。"""

    match_id: str
    start_timestamp: Optional[int] = None
    queue_id: Optional[int] = None
    patch: str = "UNKNOWN"
    source_files: set[str] = field(default_factory=set)
    observed_tiers: set[str] = field(default_factory=set)
    observed_divisions: set[str] = field(default_factory=set)


def as_int(value: Any) -> Optional[int]:
    try:
        if value is None or value == "":
            return None
        return int(value)
    except (TypeError, ValueError):
        return None


def normalize_timestamp(value: Any) -> Optional[int]:
    timestamp = as_int(value)
    if timestamp is None:
        return None
    return timestamp if timestamp >= 10**12 else timestamp * 1000


def patch_prefix(value: Any) -> str:
    text = str(value or "UNKNOWN")
    parts = text.split(".")
    return ".".join(parts[:2]) if len(parts) >= 2 else text


def utc_date(timestamp_ms: Optional[int]) -> Optional[str]:
    if timestamp_ms is None:
        return None
    return dt.datetime.fromtimestamp(timestamp_ms / 1000, tz=dt.timezone.utc).date().isoformat()


def safe_match_id(match_id: str) -> str:
    return re.sub(r"[^A-Za-z0-9_.-]", "_", match_id)


def relative_path(path: Path) -> str:
    try:
        return str(path.resolve().relative_to(ROOT.resolve()))
    except ValueError:
        return str(path.resolve())


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def input_files(input_path: Path, include_cache: bool) -> list[Path]:
    """指定パスから、試合詳細を含む入力ファイルだけを決定的に列挙する。"""

    path = input_path if input_path.is_absolute() else ROOT / input_path
    path = path.resolve()
    if not path.exists():
        raise ValueError(f"入力が存在しません: {path}")
    if path.is_file():
        return [path]

    files = sorted(path.rglob("matches.jsonl"))
    if include_cache:
        cache_dir = path / ".cache" / "matches"
        if cache_dir.exists():
            files.extend(sorted(cache_dir.glob("*.json")))
    return files


def match_payload(value: Any) -> Optional[Mapping[str, Any]]:
    if not isinstance(value, Mapping):
        return None
    nested = value.get("match")
    if isinstance(nested, Mapping):
        return nested
    if isinstance(value.get("info"), Mapping):
        return value
    return None


def candidate_from_record(value: Any, source_file: Path) -> Optional[MatchCandidate]:
    if not isinstance(value, Mapping):
        return None
    match = match_payload(value)
    if match is None:
        return None
    metadata = match.get("metadata")
    info = match.get("info")
    metadata = metadata if isinstance(metadata, Mapping) else {}
    info = info if isinstance(info, Mapping) else {}
    match_id = str(value.get("match_id") or metadata.get("matchId") or "").strip()
    if not match_id or not MATCH_ID_RE.match(match_id):
        return None

    timestamp = normalize_timestamp(
        value.get("game_start_timestamp")
        or info.get("gameStartTimestamp")
        or info.get("gameCreation")
    )
    observed_tier = str(value.get("observed_tier") or "UNKNOWN").upper()
    divisions = value.get("observed_divisions")
    if not isinstance(divisions, list):
        divisions = []
    candidate = MatchCandidate(
        match_id=match_id,
        start_timestamp=timestamp,
        queue_id=as_int(info.get("queueId")),
        patch=patch_prefix(info.get("gameVersion")),
        source_files={relative_path(source_file)},
        observed_tiers={observed_tier},
        observed_divisions={str(item).upper() for item in divisions if str(item).strip()},
    )
    return candidate


def iter_records(path: Path) -> Iterable[tuple[int, Any]]:
    if path.suffix.lower() == ".jsonl":
        with path.open("r", encoding="utf-8") as handle:
            for line_number, line in enumerate(handle, start=1):
                if not line.strip():
                    continue
                try:
                    yield line_number, json.loads(line)
                except json.JSONDecodeError:
                    yield line_number, None
        return
    try:
        yield 1, load_json(path)
    except json.JSONDecodeError:
        yield 1, None


def collect_candidates(
    paths: Sequence[Path],
) -> tuple[dict[str, MatchCandidate], Counter[str]]:
    candidates: dict[str, MatchCandidate] = {}
    quality: Counter[str] = Counter()
    for path in paths:
        for line_number, value in iter_records(path):
            if value is None:
                quality["invalid_json"] += 1
                continue
            candidate = candidate_from_record(value, path)
            if candidate is None:
                quality["invalid_or_missing_match_id"] += 1
                continue
            existing = candidates.get(candidate.match_id)
            if existing is None:
                candidates[candidate.match_id] = candidate
                continue
            quality["duplicate_match_ids"] += 1
            existing.source_files.update(candidate.source_files)
            existing.observed_tiers.update(candidate.observed_tiers)
            existing.observed_divisions.update(candidate.observed_divisions)
            if existing.start_timestamp is None and candidate.start_timestamp is not None:
                existing.start_timestamp = candidate.start_timestamp
            if existing.queue_id is None and candidate.queue_id is not None:
                existing.queue_id = candidate.queue_id
            if existing.patch == "UNKNOWN" and candidate.patch != "UNKNOWN":
                existing.patch = candidate.patch
    return candidates, quality


def parse_date(value: Optional[str]) -> Optional[dt.date]:
    if not value:
        return None
    try:
        return dt.date.fromisoformat(value)
    except ValueError as error:
        raise ValueError(f"日付はYYYY-MM-DDで指定してください: {value}") from error


def select_candidates(
    candidates: Mapping[str, MatchCandidate],
    *,
    queue_id: int,
    patch: Optional[str],
    date_from: Optional[dt.date],
    date_to: Optional[dt.date],
    match_ids: Sequence[str],
    limit: int,
) -> list[MatchCandidate]:
    explicit_ids = {item for item in match_ids if item}
    selected: list[MatchCandidate] = []
    for candidate in candidates.values():
        if explicit_ids and candidate.match_id not in explicit_ids:
            continue
        if queue_id and candidate.queue_id is not None and candidate.queue_id != queue_id:
            continue
        if patch and candidate.patch != patch and not candidate.patch.startswith(f"{patch}."):
            continue
        candidate_date = utc_date(candidate.start_timestamp)
        if date_from and (candidate_date is None or candidate_date < date_from.isoformat()):
            continue
        if date_to and (candidate_date is None or candidate_date > date_to.isoformat()):
            continue
        selected.append(candidate)

    for match_id in explicit_ids - set(candidates):
        selected.append(MatchCandidate(match_id=match_id))

    selected.sort(
        key=lambda item: (item.start_timestamp or 0, item.match_id),
        reverse=True,
    )
    return selected if limit == 0 else selected[:limit]


def sanitize(value: Any) -> Any:
    """Timeline JSONから個人識別フィールドを再帰的に除去する。"""

    if isinstance(value, Mapping):
        return {
            str(key): sanitize(item)
            for key, item in value.items()
            if str(key).replace("_", "").lower() not in PII_KEYS
        }
    if isinstance(value, list):
        return [sanitize(item) for item in value]
    return value


def validate_timeline(value: Any) -> Mapping[str, Any]:
    if not isinstance(value, Mapping):
        raise ValueError("TimelineレスポンスがJSONオブジェクトではありません")
    info = value.get("info")
    if not isinstance(info, Mapping) or not isinstance(info.get("frames"), list):
        raise ValueError("Timelineレスポンスにinfo.framesがありません")
    return sanitize(value)


def timeline_cache_path(cache_root: Path, match_id: str) -> Path:
    return cache_root / f"{safe_match_id(match_id)}.json"


def load_cached_timeline(cache_root: Path, match_id: str) -> Optional[Mapping[str, Any]]:
    path = timeline_cache_path(cache_root, match_id)
    if not path.exists():
        return None
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None
    if not isinstance(payload, Mapping) or payload.get("match_id") != match_id:
        return None
    timeline = payload.get("timeline")
    return timeline if isinstance(timeline, Mapping) else None


def save_cached_timeline(cache_root: Path, match_id: str, timeline: Mapping[str, Any]) -> None:
    atomic_write_json(
        timeline_cache_path(cache_root, match_id),
        {
            "schema_version": 1,
            "cached_at": now_iso(),
            "match_id": match_id,
            "timeline": timeline,
        },
    )


def resolve_output_root(value: Path) -> Path:
    candidate = (value if value.is_absolute() else ROOT / value).resolve()
    try:
        candidate.relative_to(ROOT.resolve())
    except ValueError as error:
        raise ValueError(f"--outputはリポジトリ内に指定してください: {candidate}") from error
    try:
        candidate.relative_to(RAW_ROOT.resolve())
    except ValueError:
        return candidate
    raise ValueError("Timeline出力はraw/へ書き込まず、reports/などへ指定してください")


def create_run_dir(output_root: Path, run_id: Optional[str], overwrite: bool) -> Path:
    name = run_id or f"run-{dt.datetime.now(dt.timezone.utc).strftime('%Y%m%dT%H%M%SZ')}"
    if not re.match(r"^run-[A-Za-z0-9_.-]+$", name):
        raise ValueError("--run-idはrun-で始まる安全な名前を指定してください")
    run_dir = output_root / name
    if run_dir.exists() and not overwrite:
        raise ValueError(f"既存の実行ディレクトリがあります: {run_dir}（--overwriteで上書き）")
    run_dir.mkdir(parents=True, exist_ok=True)
    return run_dir


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, default=DEFAULT_INPUT, help=f"Match-v5入力（既定: {DEFAULT_INPUT}）")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT, help=f"出力ルート（既定: {DEFAULT_OUTPUT}）")
    parser.add_argument("--platform", default="jp1", help="プラットフォームID（既定: jp1）")
    parser.add_argument(
        "--regional-route",
        default="auto",
        choices=("auto", "americas", "asia", "europe", "sea"),
        help="Match-v5の地域ルート（既定: platformから自動判定）",
    )
    parser.add_argument("--queue-id", type=int, default=420, help="対象キューID。0はキューを限定しない（既定: 420）")
    parser.add_argument("--patch", help="gameVersionのパッチ接頭辞（例: 16.18）")
    parser.add_argument("--date-from", help="試合開始日の下限（UTC、YYYY-MM-DD）")
    parser.add_argument("--date-to", help="試合開始日の上限（UTC、YYYY-MM-DD）")
    parser.add_argument("--match-id", action="append", default=[], help="取得対象の試合ID。複数指定可")
    parser.add_argument("--limit", type=int, default=100, help="取得対象の最大件数。0は全件（既定: 100）")
    parser.add_argument("--include-cache", action="store_true", help="入力ディレクトリのMatch-v5キャッシュも読む")
    parser.add_argument("--refresh", action="store_true", help="既存Timelineキャッシュを無視して再取得する")
    parser.add_argument("--run-id", help="出力実行名（既定: UTC時刻から生成）")
    parser.add_argument("--overwrite", action="store_true", help="既存の実行ディレクトリを上書きする")
    parser.add_argument("--rate-limit-count", type=int, default=100, help="ルートごとのローカル上限（既定: 100）")
    parser.add_argument("--rate-limit-window", type=float, default=120.0, help="上限の時間窓（秒、既定: 120）")
    parser.add_argument("--min-interval", type=float, default=0.06, help="同一ルートの最小間隔（秒、既定: 0.06）")
    parser.add_argument("--timeout", type=float, default=30.0, help="HTTPタイムアウト（秒、既定: 30）")
    parser.add_argument("--max-retries", type=int, default=6, help="429/5xx/通信エラーの再試行回数（既定: 6）")
    parser.add_argument("--dry-run", action="store_true", help="APIへ接続せず、入力と選択件数だけ確認する")
    return parser


def validate_args(args: argparse.Namespace) -> tuple[Path, list[Path], Optional[dt.date], Optional[dt.date]]:
    if args.queue_id < 0:
        raise ValueError("--queue-idは0以上が必要です")
    if args.limit < 0:
        raise ValueError("--limitは0以上が必要です")
    if args.rate_limit_count < 0:
        raise ValueError("--rate-limit-countは0以上が必要です")
    if args.rate_limit_window <= 0 or args.timeout <= 0:
        raise ValueError("--rate-limit-windowと--timeoutは正の値が必要です")
    if args.min_interval < 0 or args.max_retries < 0:
        raise ValueError("--min-intervalは0以上、--max-retriesは0以上が必要です")
    for match_id in args.match_id:
        if not MATCH_ID_RE.match(match_id):
            raise ValueError(f"不正な試合ID: {match_id}")
    output_root = resolve_output_root(args.output)
    paths = input_files(args.input, args.include_cache)
    date_from = parse_date(args.date_from)
    date_to = parse_date(args.date_to)
    if date_from and date_to and date_from > date_to:
        raise ValueError("--date-fromは--date-to以前である必要があります")
    return output_root, paths, date_from, date_to


def dry_run_summary(
    *,
    args: argparse.Namespace,
    output_root: Path,
    paths: Sequence[Path],
    candidates: Mapping[str, MatchCandidate],
    quality: Counter[str],
    selected: Sequence[MatchCandidate],
) -> dict[str, Any]:
    return {
        "mode": "dry-run",
        "input_files": len(paths),
        "input_paths": [relative_path(path) for path in paths],
        "input_records": sum(1 for _ in candidates.values()) + quality.get("duplicate_match_ids", 0),
        "unique_match_ids": len(candidates),
        "selected_match_ids": len(selected),
        "queue_id": args.queue_id,
        "patch": args.patch or "ALL",
        "date_from": args.date_from,
        "date_to": args.date_to,
        "limit": args.limit,
        "output": str(output_root),
        "quality": dict(sorted(quality.items())),
    }


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    started_at = time.monotonic()
    try:
        output_root, paths, date_from, date_to = validate_args(args)
        candidates, quality = collect_candidates(paths)
        selected = select_candidates(
            candidates,
            queue_id=args.queue_id,
            patch=args.patch,
            date_from=date_from,
            date_to=date_to,
            match_ids=args.match_id,
            limit=args.limit,
        )
        if args.dry_run:
            print(json.dumps(
                dry_run_summary(
                    args=args,
                    output_root=output_root,
                    paths=paths,
                    candidates=candidates,
                    quality=quality,
                    selected=selected,
                ),
                ensure_ascii=False,
                indent=2,
            ))
            progress(f"ドライラン完了: 所要時間 {format_elapsed(time.monotonic() - started_at)}")
            return 0

        api_key = os.environ.get("RIOT_API_KEY", "").strip()
        if not api_key:
            raise ValueError("RIOT_API_KEY環境変数を設定してください")
        regional_route = resolve_regional_route(args.platform.lower(), args.regional_route)
        run_dir = create_run_dir(output_root, args.run_id, args.overwrite)
        cache_root = output_root / ".cache" / "timelines"
        cache_root.mkdir(parents=True, exist_ok=True)
        client = RiotClient(
            api_key,
            timeout=args.timeout,
            max_retries=args.max_retries,
            rate_limit_count=args.rate_limit_count,
            rate_limit_window=args.rate_limit_window,
            min_interval=args.min_interval,
            user_agent="llm-wiki/riot-match-timeline-collector",
        )

        records: list[dict[str, Any]] = []
        errors: list[dict[str, Any]] = []
        cached_count = 0
        fetched_count = 0
        progress(f"Timeline取得開始: 対象={len(selected)}件、route={regional_route}")
        progress_bar("Timeline取得", 0, len(selected))
        for index, candidate in enumerate(selected, start=1):
            timeline = None if args.refresh else load_cached_timeline(cache_root, candidate.match_id)
            if timeline is not None:
                cached_count += 1
            else:
                try:
                    payload = client.get_json(
                        regional_route,
                        f"/lol/match/v5/matches/{quote(candidate.match_id, safe='')}/timeline",
                    )
                    timeline = validate_timeline(payload)
                    save_cached_timeline(cache_root, candidate.match_id, timeline)
                    fetched_count += 1
                except RiotApiError as error:
                    if error.status in {401, 403}:
                        raise RuntimeError(
                            f"Timeline APIの認証・権限エラーです（HTTP {error.status}）。APIキーと利用権限を確認してください"
                        ) from error
                    errors.append(
                        {
                            "match_id": candidate.match_id,
                            "status": error.status,
                            "reason": "api_error",
                        }
                    )
                except (OSError, ValueError, TypeError) as error:
                    errors.append(
                        {
                            "match_id": candidate.match_id,
                            "status": 0,
                            "reason": type(error).__name__,
                        }
                    )
            if timeline is not None:
                records.append(
                    {
                        "schema_version": 1,
                        "match_id": candidate.match_id,
                        "game_start_timestamp": candidate.start_timestamp,
                        "game_version": candidate.patch,
                        "queue_id": candidate.queue_id,
                        "observed_tiers": sorted(candidate.observed_tiers),
                        "observed_divisions": sorted(candidate.observed_divisions),
                        "timeline": timeline,
                    }
                )
            if index == 1 or index % 10 == 0 or index == len(selected):
                progress_bar("Timeline取得", index, len(selected), complete=index == len(selected))
        records.sort(key=lambda item: (item["game_start_timestamp"] or 0, item["match_id"]), reverse=True)
        timelines_path = run_dir / "timelines.jsonl"
        errors_path = run_dir / "errors.jsonl"
        manifest_path = run_dir / "manifest.json"
        atomic_write_text(
            timelines_path,
            "".join(json.dumps(record, ensure_ascii=False, separators=(",", ":")) + "\n" for record in records),
        )
        atomic_write_text(
            errors_path,
            "".join(json.dumps(error, ensure_ascii=False, separators=(",", ":")) + "\n" for error in errors),
        )
        status = "complete" if len(records) == len(selected) else ("partial" if records else "empty")
        manifest = {
            "schema_version": 1,
            "collector": "scripts/riot_match_timeline_collector.py",
            "collected_at": now_iso(),
            "status": status,
            "input_paths": [relative_path(path) for path in paths],
            "platform": args.platform.lower(),
            "regional_route": regional_route,
            "endpoint": "/lol/match/v5/matches/{matchId}/timeline",
            "queue_id": args.queue_id,
            "patch": args.patch or "ALL",
            "date_from": args.date_from,
            "date_to": args.date_to,
            "requested_limit": args.limit,
            "candidate_match_ids": len(candidates),
            "selected_match_ids": len(selected),
            "timeline_records": len(records),
            "cached_records": cached_count,
            "fetched_records": fetched_count,
            "failed_records": len(errors),
            "input_quality": dict(sorted(quality.items())),
            "privacy": "Timeline metadataからPUUID、summonerId、summonerName、Riot IDを再帰的に除去した分析用出力",
            "cache": str(cache_root.relative_to(output_root)),
            "files": {
                "timelines": str(timelines_path.relative_to(output_root)),
                "errors": str(errors_path.relative_to(output_root)),
            },
        }
        atomic_write_json(manifest_path, manifest)
        progress(
            f"Timeline取得完了: 成功={len(records)}件（cache={cached_count}, API={fetched_count})、"
            f"失敗={len(errors)}件、所要時間 {format_elapsed(time.monotonic() - started_at)}"
        )
        return 0 if status != "empty" or not selected else 2
    except (RiotApiError, RuntimeError, ValueError, OSError) as error:
        print(f"エラー: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
