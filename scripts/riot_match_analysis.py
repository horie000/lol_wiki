#!/usr/bin/env python3
"""Riot Match-v5 データ解析用の共通読込・正規化ユーティリティ。"""

from __future__ import annotations

import csv
import hashlib
import json
import math
import re
import tarfile
import unicodedata
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Any, Iterable, Iterator, Mapping, Optional, Sequence


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_DATA_DRAGON = ROOT / "raw" / "sources" / "dragontail-16.18.1.tgz"

KNOWN_ROLES = ("TOP", "JUNGLE", "MIDDLE", "BOTTOM", "UTILITY")
ROLE_ALIASES = {
    "TOP": "TOP",
    "JUNGLE": "JUNGLE",
    "MIDDLE": "MIDDLE",
    "MID": "MIDDLE",
    "BOTTOM": "BOTTOM",
    "BOT": "BOTTOM",
    "CARRY": "BOTTOM",
    "ADC": "BOTTOM",
    "UTILITY": "UTILITY",
    "SUPPORT": "UTILITY",
    "SUP": "UTILITY",
}
UNKNOWN_VALUES = {"", "NONE", "INVALID", "UNKNOWN", "UNSELECTED", "N/A"}


def as_int(value: Any) -> Optional[int]:
    try:
        if value is None or value == "":
            return None
        return int(value)
    except (TypeError, ValueError):
        return None


def as_bool(value: Any) -> Optional[bool]:
    if isinstance(value, bool):
        return value
    if isinstance(value, str):
        lowered = value.strip().lower()
        if lowered in {"true", "1", "yes", "win", "won"}:
            return True
        if lowered in {"false", "0", "no", "loss", "lose"}:
            return False
    if isinstance(value, (int, float)) and value in (0, 1):
        return bool(value)
    return None


def as_float(value: Any) -> Optional[float]:
    try:
        if value is None or value == "":
            return None
        number = float(value)
        return number if math.isfinite(number) else None
    except (TypeError, ValueError):
        return None


def normalize_role(*values: Any) -> str:
    for value in values:
        if value is None:
            continue
        text = str(value).strip().upper()
        if text in UNKNOWN_VALUES:
            continue
        if text in ROLE_ALIASES:
            return ROLE_ALIASES[text]
    return "UNKNOWN"


def normalize_alias(value: Any) -> str:
    text = unicodedata.normalize("NFKC", str(value or "")).strip().casefold()
    return "".join(character for character in text if character.isalnum())


def normalize_tiers(value: Optional[str | Sequence[str]]) -> set[str]:
    if value is None:
        return set()
    if isinstance(value, str):
        values = value.split(",")
    else:
        values = value
    return {str(item).strip().upper() for item in values if str(item).strip()}


def parse_formats(value: str) -> set[str]:
    formats = {item.strip().lower() for item in value.split(",") if item.strip()}
    allowed = {"markdown", "csv", "json"}
    invalid = formats - allowed
    if invalid or not formats:
        raise ValueError(f"--format の不正な値: {', '.join(sorted(invalid or {'空'}))}")
    return formats


def normalize_timestamp(value: Any) -> Optional[int]:
    timestamp = as_int(value)
    if timestamp is None:
        return None
    return timestamp if timestamp >= 10**12 else timestamp * 1000


def utc_date(timestamp_ms: Optional[int]) -> Optional[str]:
    if timestamp_ms is None:
        return None
    return datetime.fromtimestamp(timestamp_ms / 1000, tz=timezone.utc).date().isoformat()


def utc_iso(timestamp_ms: Optional[int]) -> Optional[str]:
    if timestamp_ms is None:
        return None
    return datetime.fromtimestamp(timestamp_ms / 1000, tz=timezone.utc).isoformat().replace("+00:00", "Z")


def patch_prefix(game_version: Any) -> str:
    text = str(game_version or "UNKNOWN")
    return text.split(".", 2)[0] + "." + text.split(".", 2)[1] if text.count(".") >= 1 else text


def stable_json_hash(value: Any) -> str:
    content = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(content.encode("utf-8")).hexdigest()


def quantile(values: Sequence[float], probability: float) -> Optional[float]:
    if not values:
        return None
    ordered = sorted(values)
    if len(ordered) == 1:
        return ordered[0]
    position = (len(ordered) - 1) * probability
    lower = math.floor(position)
    upper = math.ceil(position)
    if lower == upper:
        return ordered[lower]
    fraction = position - lower
    return ordered[lower] + (ordered[upper] - ordered[lower]) * fraction


def mean(values: Iterable[Optional[float]]) -> Optional[float]:
    numbers = [value for value in values if value is not None]
    return sum(numbers) / len(numbers) if numbers else None


def ratio(numerator: int | float, denominator: int | float) -> Optional[float]:
    return numerator / denominator if denominator else None


def display_number(value: Any, digits: int = 3) -> str:
    if value is None:
        return ""
    if isinstance(value, float):
        return f"{value:.{digits}f}".rstrip("0").rstrip(".")
    return str(value)


class Quality:
    """個人情報を含めずに入力品質を収集する。"""

    def __init__(self) -> None:
        self.counts: Counter[str] = Counter()
        self.examples: defaultdict[str, list[str]] = defaultdict(list)

    def add(self, reason: str, example: Optional[str] = None) -> None:
        self.counts[reason] += 1
        if example and len(self.examples[reason]) < 10 and example not in self.examples[reason]:
            self.examples[reason].append(example)

    def as_dict(self) -> dict[str, Any]:
        return {
            "counts": dict(sorted(self.counts.items())),
            "examples": {key: value for key, value in sorted(self.examples.items())},
        }


@dataclass
class NormalizedMatch:
    match_id: str
    payload: Mapping[str, Any]
    info: Mapping[str, Any]
    metadata: Mapping[str, Any]
    start_timestamp: Optional[int]
    queue_id: Optional[int]
    game_version: str
    observed_tiers: set[str] = field(default_factory=set)
    observed_divisions: set[str] = field(default_factory=set)
    source_files: set[str] = field(default_factory=set)
    payload_hash: str = ""
    conflicting_payload: bool = False
    duplicate_count: int = 0

    @property
    def patch(self) -> str:
        return patch_prefix(self.game_version)

    @property
    def start_date(self) -> Optional[str]:
        return utc_date(self.start_timestamp)

    @property
    def participants(self) -> list[Mapping[str, Any]]:
        raw = self.info.get("participants")
        return list(raw) if isinstance(raw, list) else []

    @property
    def effective_tiers(self) -> set[str]:
        known = {tier for tier in self.observed_tiers if tier != "UNKNOWN"}
        return known or {"UNKNOWN"}

    def team_win_map(self) -> dict[str, bool]:
        result: dict[str, bool] = {}
        teams = self.info.get("teams")
        if isinstance(teams, list):
            for team in teams:
                if not isinstance(team, Mapping):
                    continue
                team_id = team.get("teamId")
                win = as_bool(team.get("win"))
                if team_id is not None and win is not None:
                    result[str(team_id)] = win
        if len(result) < 2:
            for participant in self.participants:
                if not isinstance(participant, Mapping):
                    continue
                team_id = participant.get("teamId")
                win = as_bool(participant.get("win"))
                if team_id is None or win is None:
                    continue
                result.setdefault(str(team_id), win)
        return result

    def is_complete(self) -> bool:
        participants = self.participants
        if len(participants) != 10:
            return False
        participant_ids = [as_int(item.get("participantId")) for item in participants if isinstance(item, Mapping)]
        if len(participant_ids) != 10 or len(set(participant_ids)) != 10 or None in participant_ids:
            return False
        team_ids = [str(item.get("teamId")) for item in participants if isinstance(item, Mapping) and item.get("teamId") is not None]
        if len(team_ids) != 10 or len(set(team_ids)) != 2 or any(team_ids.count(team) != 5 for team in set(team_ids)):
            return False
        if len(self.team_win_map()) != 2:
            return False
        return self.start_timestamp is not None and as_float(self.info.get("gameDuration")) is not None


@dataclass
class ScopedMatch:
    match: NormalizedMatch
    observed_tier: str


@dataclass
class ScopeGroup:
    scope: str
    observed_tier: str
    entries: list[ScopedMatch]


@dataclass
class ParticipantView:
    match: NormalizedMatch
    scope_tier: str
    raw: Mapping[str, Any]
    participant_id: int
    team_id: str
    champion_id: Optional[int]
    champion_name: str
    role: str
    win: Optional[bool]

    @property
    def items(self) -> list[tuple[int, int]]:
        result: list[tuple[int, int]] = []
        for slot in range(7):
            item_id = as_int(self.raw.get(f"item{slot}"))
            if item_id and item_id > 0:
                result.append((item_id, slot))
        return result

    @property
    def runes(self) -> list[dict[str, Any]]:
        perks = self.raw.get("perks")
        if not isinstance(perks, Mapping):
            return []
        result: list[dict[str, Any]] = []
        styles = perks.get("styles")
        if isinstance(styles, list):
            for style in styles:
                if not isinstance(style, Mapping):
                    continue
                style_id = as_int(style.get("style"))
                selections = style.get("selections")
                if not isinstance(selections, list):
                    continue
                for index, selection in enumerate(selections):
                    if not isinstance(selection, Mapping):
                        continue
                    perk_id = as_int(selection.get("perk"))
                    if perk_id:
                        result.append(
                            {
                                "id": perk_id,
                                "kind": "keystone" if index == 0 and len(result) == 0 else "rune",
                                "style_id": style_id,
                                "slot": index,
                            }
                        )
        stat_perks = perks.get("statPerks")
        if isinstance(stat_perks, Mapping):
            for slot_name in ("offense", "flex", "defense"):
                perk_id = as_int(stat_perks.get(slot_name))
                if perk_id:
                    result.append({"id": perk_id, "kind": "shard", "style_id": None, "slot": slot_name})
        return result

    @property
    def rune_set(self) -> Optional[dict[str, Any]]:
        """Match-v5 の主系・副系・シャードを一つの正規化セットとして返す。

        個別ルーンの集計と異なり、ページへ掲載するセットは選択順を意味する
        キーストーンを先頭に保持し、statPerks は API の slot 順で固定する。
        必須枠が欠けた参加者は不完全なセットとして ``None`` を返す。
        """
        perks = self.raw.get("perks")
        if not isinstance(perks, Mapping):
            return None
        raw_styles = perks.get("styles")
        if not isinstance(raw_styles, list):
            return None
        styles = [style for style in raw_styles if isinstance(style, Mapping)]
        if len(styles) < 2:
            return None

        def style_for(description: str, fallback_index: int) -> Optional[Mapping[str, Any]]:
            for style in styles:
                if str(style.get("description") or "") == description:
                    return style
            return styles[fallback_index] if len(styles) > fallback_index else None

        primary = style_for("primaryStyle", 0)
        secondary = style_for("subStyle", 1)
        if primary is None or secondary is None:
            return None

        def selections(style: Mapping[str, Any]) -> Optional[list[int]]:
            raw_selections = style.get("selections")
            if not isinstance(raw_selections, list):
                return None
            result: list[int] = []
            for selection in raw_selections:
                if not isinstance(selection, Mapping):
                    return None
                perk_id = as_int(selection.get("perk"))
                if perk_id is None or perk_id <= 0:
                    return None
                result.append(perk_id)
            return result

        primary_selections = selections(primary)
        secondary_selections = selections(secondary)
        if primary_selections is None or len(primary_selections) != 4:
            return None
        if secondary_selections is None or len(secondary_selections) != 2:
            return None

        stat_perks = perks.get("statPerks")
        if not isinstance(stat_perks, Mapping):
            return None
        shards: list[int] = []
        for slot_name in ("offense", "flex", "defense"):
            shard_id = as_int(stat_perks.get(slot_name))
            if shard_id is None or shard_id <= 0:
                return None
            shards.append(shard_id)

        primary_style_id = as_int(primary.get("style"))
        secondary_style_id = as_int(secondary.get("style"))
        if primary_style_id is None or secondary_style_id is None:
            return None
        return {
            "primary_style_id": primary_style_id,
            "primary_keystone_id": primary_selections[0],
            "primary_rune_ids": primary_selections[1:],
            "secondary_style_id": secondary_style_id,
            "secondary_rune_ids": secondary_selections,
            "shard_ids": shards,
        }

    @property
    def summoner_spells(self) -> list[int]:
        return [
            spell_id
            for spell_id in (as_int(self.raw.get("summoner1Id")), as_int(self.raw.get("summoner2Id")))
            if spell_id is not None
        ]

    def metric(self, key: str) -> Optional[float]:
        return as_float(self.raw.get(key))


@dataclass
class Dataset:
    matches: list[NormalizedMatch]
    input_files: list[str]
    quality: Quality


class DataDragonCatalog:
    """Data Dragonの日本語表示名をローカルアーカイブから読む。"""

    def __init__(self, archive_path: Path = DEFAULT_DATA_DRAGON) -> None:
        self.archive_path = archive_path
        self.items: dict[int, str] = {}
        self.runes: dict[int, str] = {}
        self.rune_styles: dict[int, str] = {}
        self.spells: dict[int, str] = {}
        self.champions: dict[str, dict[str, Any]] = {}
        self.aliases: defaultdict[str, set[str]] = defaultdict(set)
        self.loaded = False

    def load(self) -> "DataDragonCatalog":
        if self.loaded or not self.archive_path.exists():
            self.loaded = True
            return self
        try:
            with tarfile.open(self.archive_path, "r:gz") as archive:
                for member in archive.getmembers():
                    name = member.name
                    if not member.isfile() or "/data/ja_JP/" not in name or not name.endswith(".json"):
                        continue
                    if name.endswith("/item.json"):
                        self._load_items(archive, member)
                    elif name.endswith("/runesReforged.json"):
                        self._load_runes(archive, member)
                    elif name.endswith("/summoner.json"):
                        self._load_spells(archive, member)
                    elif "/data/ja_JP/champion/" in name:
                        self._load_champion(archive, member)
        except (OSError, tarfile.TarError, json.JSONDecodeError):
            # 表示名解決は補助情報なので、アーカイブ破損時もID集計は続行する。
            pass
        self.loaded = True
        return self

    @staticmethod
    def _read_json(archive: tarfile.TarFile, member: tarfile.TarInfo) -> Any:
        handle = archive.extractfile(member)
        if handle is None:
            return None
        return json.load(handle)

    def _load_items(self, archive: tarfile.TarFile, member: tarfile.TarInfo) -> None:
        payload = self._read_json(archive, member)
        data = payload.get("data", {}) if isinstance(payload, Mapping) else {}
        if isinstance(data, Mapping):
            for key, item in data.items():
                item_id = as_int(key)
                if item_id is not None and isinstance(item, Mapping):
                    self.items[item_id] = str(item.get("name") or f"UNKNOWN({item_id})")

    def _load_runes(self, archive: tarfile.TarFile, member: tarfile.TarInfo) -> None:
        payload = self._read_json(archive, member)
        if not isinstance(payload, list):
            return
        for style in payload:
            if not isinstance(style, Mapping):
                continue
            style_id = as_int(style.get("id"))
            if style_id is not None:
                self.rune_styles[style_id] = str(style.get("name") or f"UNKNOWN({style_id})")
            for slot in style.get("slots", []):
                if not isinstance(slot, Mapping):
                    continue
                for rune in slot.get("runes", []):
                    if not isinstance(rune, Mapping):
                        continue
                    rune_id = as_int(rune.get("id"))
                    if rune_id is not None:
                        self.runes[rune_id] = str(rune.get("name") or rune.get("longDesc") or f"UNKNOWN({rune_id})")

    def _load_spells(self, archive: tarfile.TarFile, member: tarfile.TarInfo) -> None:
        payload = self._read_json(archive, member)
        data = payload.get("data", {}) if isinstance(payload, Mapping) else {}
        if isinstance(data, Mapping):
            for key, spell in data.items():
                if not isinstance(spell, Mapping):
                    continue
                spell_id = as_int(spell.get("key") or key)
                if spell_id is not None:
                    self.spells[spell_id] = str(spell.get("name") or f"UNKNOWN({spell_id})")

    def _load_champion(self, archive: tarfile.TarFile, member: tarfile.TarInfo) -> None:
        payload = self._read_json(archive, member)
        data = payload.get("data", {}) if isinstance(payload, Mapping) else {}
        if not isinstance(data, Mapping):
            return
        for key, champion in data.items():
            if not isinstance(champion, Mapping):
                continue
            champion_id = str(champion.get("key") or key)
            entry = {
                "id": champion_id,
                "name": str(champion.get("name") or key),
                "english_id": str(champion.get("id") or key),
            }
            self.champions[champion_id] = entry
            for alias in (champion_id, entry["name"], entry["english_id"]):
                self.aliases[normalize_alias(alias)].add(champion_id)

    def item_name(self, item_id: Optional[int]) -> str:
        return self.items.get(item_id or -1, f"UNKNOWN({item_id})")

    def rune_name(self, rune_id: Optional[int]) -> str:
        return self.runes.get(rune_id or -1, f"UNKNOWN({rune_id})")

    def rune_style_name(self, style_id: Optional[int]) -> str:
        return self.rune_styles.get(style_id or -1, f"UNKNOWN({style_id})")

    def spell_name(self, spell_id: Optional[int]) -> str:
        return self.spells.get(spell_id or -1, f"UNKNOWN({spell_id})")

    def champion_candidates(self, value: Any) -> set[str]:
        alias = normalize_alias(value)
        result = set(self.aliases.get(alias, set()))
        if result:
            return result
        for champion_id, entry in self.champions.items():
            if alias and alias in {normalize_alias(entry.get("name")), normalize_alias(entry.get("english_id"))}:
                result.add(champion_id)
        return result


def _candidate_files(inputs: Sequence[Path]) -> list[Path]:
    files: set[Path] = set()
    for input_path in inputs:
        path = input_path.expanduser().resolve()
        if not path.exists():
            raise ValueError(f"入力パスが存在しません: {input_path}")
        if path.is_file():
            if path.suffix.lower() in {".json", ".jsonl"}:
                files.add(path)
            continue
        for child in path.rglob("*"):
            if child.is_file() and child.suffix.lower() in {".json", ".jsonl"}:
                files.add(child)
    return sorted(files)


def _read_json_objects(path: Path, quality: Quality) -> Iterator[Mapping[str, Any]]:
    if path.suffix.lower() == ".jsonl":
        try:
            with path.open("r", encoding="utf-8") as handle:
                for line_number, line in enumerate(handle, start=1):
                    if not line.strip():
                        continue
                    try:
                        value = json.loads(line)
                    except json.JSONDecodeError:
                        quality.add("invalid_json", f"{path}:{line_number}")
                        continue
                    if isinstance(value, Mapping):
                        yield value
                    else:
                        quality.add("invalid_record", f"{path}:{line_number}")
            return
        except OSError:
            quality.add("unreadable_file", str(path))
            return
    try:
        with path.open("r", encoding="utf-8") as handle:
            value = json.load(handle)
    except (OSError, json.JSONDecodeError):
        quality.add("invalid_json", str(path))
        return
    if isinstance(value, Mapping):
        yield value
    else:
        quality.add("invalid_record", str(path))


def _extract_match(value: Mapping[str, Any]) -> tuple[Mapping[str, Any], Mapping[str, Any]] | None:
    nested = value.get("match")
    if isinstance(nested, Mapping) and isinstance(nested.get("info"), Mapping):
        return value, nested
    if isinstance(value.get("info"), Mapping):
        return {}, value
    return None


def _build_match(wrapper: Mapping[str, Any], payload: Mapping[str, Any], source: Path, quality: Quality) -> Optional[NormalizedMatch]:
    metadata = payload.get("metadata")
    info = payload.get("info")
    metadata = metadata if isinstance(metadata, Mapping) else {}
    info = info if isinstance(info, Mapping) else {}
    match_id = wrapper.get("match_id") or metadata.get("matchId")
    if match_id is None or not str(match_id).strip():
        quality.add("missing_match_id", str(source))
        return None
    timestamp = normalize_timestamp(wrapper.get("game_start_timestamp"))
    if timestamp is None:
        timestamp = normalize_timestamp(info.get("gameStartTimestamp"))
    if timestamp is None:
        timestamp = normalize_timestamp(info.get("gameCreation"))
    if timestamp is None:
        quality.add("missing_timestamp", str(match_id))
    queue_id = as_int(info.get("queueId"))
    game_version = str(info.get("gameVersion") or "UNKNOWN")
    observed_tier = str(wrapper.get("observed_tier") or "UNKNOWN").strip().upper()
    divisions = wrapper.get("observed_divisions")
    if not isinstance(divisions, list):
        divisions = []
    return NormalizedMatch(
        match_id=str(match_id),
        payload=payload,
        info=info,
        metadata=metadata,
        start_timestamp=timestamp,
        queue_id=queue_id,
        game_version=game_version,
        observed_tiers={observed_tier or "UNKNOWN"},
        observed_divisions={str(value).strip().upper() for value in divisions if str(value).strip()},
        source_files={str(source)},
        payload_hash=stable_json_hash(payload),
    )


def load_dataset(inputs: Sequence[Path]) -> Dataset:
    quality = Quality()
    files = _candidate_files(inputs)
    quality.counts["input_files"] = len(files)
    matches: dict[str, NormalizedMatch] = {}
    for path in files:
        for value in _read_json_objects(path, quality):
            extracted = _extract_match(value)
            if extracted is None:
                quality.add("ignored_non_match_json")
                continue
            wrapper, payload = extracted
            record = _build_match(wrapper, payload, path, quality)
            if record is None:
                continue
            quality.counts["input_records"] += 1
            previous = matches.get(record.match_id)
            if previous is None:
                matches[record.match_id] = record
                continue
            previous.duplicate_count += 1
            quality.add("duplicate_match", record.match_id)
            previous.source_files.update(record.source_files)
            previous.observed_tiers.update(record.observed_tiers)
            previous.observed_divisions.update(record.observed_divisions)
            if previous.payload_hash != record.payload_hash:
                previous.conflicting_payload = True
                quality.add("conflicting_payload", record.match_id)
    ordered = sorted(
        matches.values(),
        key=lambda item: (item.start_timestamp or 0, item.match_id),
        reverse=True,
    )
    quality.counts["unique_matches"] = len(ordered)
    quality.counts["conflicting_matches"] = sum(1 for match in ordered if match.conflicting_payload)
    quality.counts["complete_matches"] = sum(1 for match in ordered if match.is_complete())
    quality.counts["incomplete_matches"] = sum(1 for match in ordered if not match.is_complete())
    return Dataset(matches=ordered, input_files=[str(path) for path in files], quality=quality)


def select_scopes(
    matches: Sequence[NormalizedMatch],
    *,
    queue_id: Optional[int],
    tier_mode: str,
    tiers: set[str],
    patch: Optional[str],
    date_from: Optional[str],
    date_to: Optional[str],
    include_conflicts: bool = False,
) -> tuple[list[ScopedMatch], dict[str, int]]:
    if tier_mode not in {"all", "observed"}:
        raise ValueError("tier mode は all または observed が必要です")
    stats: Counter[str] = Counter()
    selected: list[ScopedMatch] = []
    for match in matches:
        if match.conflicting_payload and not include_conflicts:
            stats["conflicting_payload"] += 1
            continue
        if queue_id is not None and match.queue_id != queue_id:
            stats["queue_mismatch"] += 1
            continue
        if patch and not match.game_version.startswith(patch):
            stats["patch_mismatch"] += 1
            continue
        if date_from and (match.start_date is None or match.start_date < date_from):
            stats["date_before"] += 1
            continue
        if date_to and (match.start_date is None or match.start_date > date_to):
            stats["date_after"] += 1
            continue
        effective_tiers = match.effective_tiers
        if tier_mode == "all":
            if tiers and not effective_tiers.intersection(tiers):
                stats["tier_mismatch"] += 1
                continue
            selected.append(ScopedMatch(match=match, observed_tier="MIXED"))
            continue
        selected_tiers = sorted(effective_tiers.intersection(tiers)) if tiers else sorted(effective_tiers)
        if not selected_tiers:
            stats["tier_mismatch"] += 1
            continue
        for tier in selected_tiers:
            selected.append(ScopedMatch(match=match, observed_tier=tier))
    selected.sort(key=lambda item: (item.match.start_timestamp or 0, item.match.match_id, item.observed_tier), reverse=True)
    stats["selected_scopes"] = len(selected)
    stats["selected_unique_matches"] = len({item.match.match_id for item in selected})
    return selected, dict(stats)


def scope_groups(scopes: Sequence[ScopedMatch], tier_mode: str) -> list[ScopeGroup]:
    by_match: dict[str, ScopedMatch] = {}
    for scoped in scopes:
        by_match.setdefault(scoped.match.match_id, scoped)
    overall = sorted(by_match.values(), key=lambda item: (item.match.start_timestamp or 0, item.match.match_id), reverse=True)
    if tier_mode == "all":
        return [ScopeGroup(scope="overall", observed_tier="MIXED", entries=overall)]
    groups = [ScopeGroup(scope="overall", observed_tier="ALL", entries=overall)]
    tiers = sorted({item.observed_tier for item in scopes})
    for tier in tiers:
        entries = [item for item in scopes if item.observed_tier == tier]
        groups.append(ScopeGroup(scope="tier", observed_tier=tier, entries=entries))
    return groups


def participant_views(scoped: ScopedMatch) -> list[ParticipantView]:
    team_wins = scoped.match.team_win_map()
    result: list[ParticipantView] = []
    for raw in scoped.match.participants:
        if not isinstance(raw, Mapping):
            continue
        participant_id = as_int(raw.get("participantId"))
        team_id = raw.get("teamId")
        if participant_id is None or team_id is None:
            continue
        team_key = str(team_id)
        win = team_wins.get(team_key)
        if win is None:
            win = as_bool(raw.get("win"))
        result.append(
            ParticipantView(
                match=scoped.match,
                scope_tier=scoped.observed_tier,
                raw=raw,
                participant_id=participant_id,
                team_id=team_key,
                champion_id=as_int(raw.get("championId")),
                champion_name=str(raw.get("championName") or "UNKNOWN"),
                role=normalize_role(raw.get("teamPosition"), raw.get("individualPosition"), raw.get("lane")),
                win=win,
            )
        )
    return result


def valid_participants(scoped: ScopedMatch, include_incomplete: bool = False) -> list[ParticipantView]:
    if not include_incomplete and not scoped.match.is_complete():
        return []
    return participant_views(scoped)


def participant_key(view: ParticipantView) -> str:
    if view.champion_id is not None:
        return str(view.champion_id)
    return normalize_alias(view.champion_name)


def champion_label(view: ParticipantView) -> str:
    if view.champion_name and view.champion_name != "UNKNOWN":
        return view.champion_name
    return str(view.champion_id or "UNKNOWN")


def extract_bans(match: NormalizedMatch) -> list[int]:
    result: list[int] = []
    teams = match.info.get("teams")
    if not isinstance(teams, list):
        return result
    for team in teams:
        if not isinstance(team, Mapping):
            continue
        bans = team.get("bans")
        if not isinstance(bans, list):
            continue
        for ban in bans:
            if not isinstance(ban, Mapping):
                continue
            champion_id = as_int(ban.get("championId"))
            if champion_id is not None and champion_id > 0:
                result.append(champion_id)
    return result


def rows_to_csv(path: Path, rows: Sequence[Mapping[str, Any]], fieldnames: Sequence[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(fieldnames), extrasaction="ignore", lineterminator="\n")
        writer.writeheader()
        for row in rows:
            converted = {}
            for fieldname in fieldnames:
                value = row.get(fieldname)
                if isinstance(value, (list, tuple)):
                    # リスト／タプルはルーン枠などの順序を意味するため保持する。
                    value = ",".join(str(item) for item in value)
                elif isinstance(value, set):
                    value = ",".join(str(item) for item in sorted(value, key=str))
                converted[fieldname] = "" if value is None else value
            writer.writerow(converted)


def json_write(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def safe_slug(value: str) -> str:
    text = unicodedata.normalize("NFKC", value).strip()
    text = re.sub(r"[^\w.-]+", "-", text, flags=re.UNICODE).strip("-.")
    return text[:80] or "unknown"


def markdown_table(rows: Sequence[Mapping[str, Any]], columns: Sequence[tuple[str, str]], limit: int = 20) -> str:
    selected = rows[:limit]
    if not selected:
        return "（該当なし）"
    header = "| " + " | ".join(label for _, label in columns) + " |"
    separator = "| " + " | ".join("---" for _ in columns) + " |"
    lines = [header, separator]
    for row in selected:
        values = []
        for key, _ in columns:
            value = row.get(key, "")
            if isinstance(value, float):
                value = display_number(value)
            values.append(str(value).replace("|", "\\|"))
        lines.append("| " + " | ".join(values) + " |")
    return "\n".join(lines)
