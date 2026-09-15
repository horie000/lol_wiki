#!/usr/bin/env python3
"""実試合データからチャンピオン・アイテムの記述的な相関を集計する。"""

from __future__ import annotations

import argparse
import json
import sys
import tarfile
from collections import Counter, defaultdict
from datetime import datetime, timezone
from itertools import combinations
from pathlib import Path
from typing import Any, Mapping, Optional, Sequence

from riot_match_analysis import (
    DEFAULT_DATA_DRAGON,
    DataDragonCatalog,
    Dataset,
    ParticipantView,
    ScopeGroup,
    as_int,
    as_float,
    champion_label,
    display_number,
    json_write,
    load_dataset,
    markdown_table,
    normalize_alias,
    normalize_role,
    normalize_tiers,
    parse_formats,
    participant_views,
    patch_prefix,
    ratio,
    rows_to_csv,
    scope_groups,
    select_scopes,
)


SCRIPT_NAME = "scripts/riot_champion_item_synergy.py"
SCHEMA_VERSION = 2
DEFAULT_REPORT_MIN_GAMES = 30
MAX_THEORETICAL_ROWS_PER_CHAMPION_ROLE = 50
UTILITY_ITEM_TAGS = frozenset({"Consumable", "Trinket", "Vision", "Stealth", "GoldPer"})

# Data Dragon item.json の stats に存在するキーだけを使う。説明文に書かれた
# 発動効果やアイテム固有効果は、同じステータス群として推測しない。
STATUS_GROUP_SPECS: dict[str, tuple[str, ...]] = {
    "critical_chance": ("FlatCritChanceMod",),
    "attack_damage": ("FlatPhysicalDamageMod",),
    "attack_speed": ("PercentAttackSpeedMod",),
    "ability_power": ("FlatMagicDamageMod",),
    "health": ("FlatHPPoolMod",),
    "armor": ("FlatArmorMod",),
    "magic_resist": ("FlatSpellBlockMod",),
    "mana": ("FlatMPPoolMod",),
    "health_regen": ("FlatHPRegenMod",),
    "movement_speed": ("FlatMovementSpeedMod", "PercentMovementSpeedMod"),
    "lifesteal": ("PercentLifeStealMod",),
}
STATUS_GROUP_NAMES = {
    "critical_chance": "クリティカル率",
    "attack_damage": "攻撃力",
    "attack_speed": "攻撃速度",
    "ability_power": "魔力",
    "health": "体力",
    "armor": "物理防御",
    "magic_resist": "魔法防御",
    "mana": "マナ",
    "health_regen": "体力再生",
    "movement_speed": "移動速度",
    "lifesteal": "ライフスティール",
}

CSV_FIELDS = (
    "scope",
    "observed_tier",
    "patch",
    "patches",
    "champion_id",
    "champion_name",
    "role",
    "item_id",
    "item_name",
    "item_tags",
    "item_is_utility",
    "item_is_completed",
    "champion_games",
    "champion_wins",
    "champion_baseline_win_rate",
    "item_games",
    "item_wins",
    "item_losses",
    "item_win_rate",
    "item_pick_rate",
    "without_item_games",
    "without_item_wins",
    "without_item_losses",
    "without_item_win_rate",
    "win_rate_lift_vs_without",
    "min_games_applied",
)

STATUS_CSV_FIELDS = (
    "scope",
    "observed_tier",
    "patch",
    "patches",
    "champion_id",
    "champion_name",
    "role",
    "status_group_id",
    "status_group_name",
    "status_keys",
    "champion_games",
    "champion_wins",
    "champion_baseline_win_rate",
    "status_games",
    "status_wins",
    "status_losses",
    "status_win_rate",
    "status_pick_rate",
    "without_status_games",
    "without_status_wins",
    "without_status_losses",
    "without_status_win_rate",
    "win_rate_lift_vs_without",
    "min_games_applied",
)

BUILD_CSV_FIELDS = (
    "scope",
    "observed_tier",
    "patch",
    "patches",
    "champion_id",
    "champion_name",
    "role",
    "build_size",
    "build_item_ids",
    "build_item_names",
    "build_name",
    "champion_games",
    "champion_wins",
    "champion_baseline_win_rate",
    "build_games",
    "build_wins",
    "build_losses",
    "build_win_rate",
    "build_pick_rate",
    "without_build_games",
    "without_build_wins",
    "without_build_losses",
    "without_build_win_rate",
    "win_rate_lift_vs_without",
    "min_games_applied",
)

THEORY_CSV_FIELDS = BUILD_CSV_FIELDS + (
    "theory_type",
    "shared_status_groups",
    "theory_reason",
)


def parse_date(value: Optional[str], option: str) -> Optional[str]:
    if not value:
        return None
    try:
        return datetime.strptime(value, "%Y-%m-%d").date().isoformat()
    except ValueError as error:
        raise ValueError(f"{option} は YYYY-MM-DD 形式が必要です: {value}") from error


def parse_roles(value: Optional[str]) -> set[str]:
    if not value:
        return set()
    roles = {normalize_role(item) for item in value.split(",") if item.strip()}
    invalid = {role for role in roles if role == "UNKNOWN"}
    if invalid:
        raise ValueError(f"不明なロールです: {value}")
    return roles


def resolve_root_path(value: str) -> Path:
    path = Path(value).expanduser()
    return path if path.is_absolute() else Path(__file__).resolve().parents[1] / path


def reject_raw_output(path: Path) -> None:
    root = Path(__file__).resolve().parents[1]
    raw_root = (root / "raw").resolve()
    resolved = path.resolve()
    if resolved == raw_root or raw_root in resolved.parents:
        raise ValueError("解析結果を raw/ 配下へ書き出すことはできません")


def manifest_input_paths(paths: Sequence[str]) -> list[str]:
    """個人識別情報を扱う補助キャッシュのファイル名をmanifestから除外する。"""
    private_markers = ("puuid", "summoner", "riotid")
    return [
        path
        for path in paths
        if not any(marker in Path(path).name.casefold() for marker in private_markers)
    ]


def resolve_champion_ids(
    values: Optional[str],
    dataset: Dataset,
    catalog: DataDragonCatalog,
) -> set[str]:
    if not values:
        return set()
    available: defaultdict[str, set[str]] = defaultdict(set)
    for match in dataset.matches:
        for raw in match.participants:
            if not isinstance(raw, Mapping):
                continue
            champion_id = as_int(raw.get("championId"))
            if champion_id is None:
                continue
            key = str(champion_id)
            available[key].add(key)
            available[normalize_alias(raw.get("championName"))].add(key)
    resolved: set[str] = set()
    for value in values.split(","):
        token = value.strip()
        if not token:
            continue
        direct = as_int(token)
        candidates = set(catalog.champion_candidates(token))
        candidates.update(available.get(normalize_alias(token), set()))
        if direct is not None:
            candidates.add(str(direct))
        if not candidates:
            raise ValueError(f"チャンピオンを解決できません: {token}")
        resolved.update(candidates)
    return resolved


def load_item_metadata(archive_path: Path) -> dict[int, dict[str, Any]]:
    """Data Dragonのアイテムタグだけを読み、所持率の対象判定に使う。"""
    if not archive_path.exists():
        return {}
    try:
        with tarfile.open(archive_path, "r:gz") as archive:
            member = next(
                (
                    item
                    for item in archive.getmembers()
                    if item.isfile() and item.name.endswith("/data/ja_JP/item.json")
                ),
                None,
            )
            if member is None:
                return {}
            handle = archive.extractfile(member)
            if handle is None:
                return {}
            payload = json.load(handle)
    except (OSError, tarfile.TarError, json.JSONDecodeError):
        return {}
    data = payload.get("data", {}) if isinstance(payload, Mapping) else {}
    result: dict[int, dict[str, Any]] = {}
    if not isinstance(data, Mapping):
        return result
    for key, value in data.items():
        item_id = as_int(key)
        if item_id is not None and isinstance(value, Mapping):
            result[item_id] = dict(value)
    return result


def item_tags(item_metadata: Mapping[int, Mapping[str, Any]], item_id: int) -> set[str]:
    raw_tags = item_metadata.get(item_id, {}).get("tags", [])
    if not isinstance(raw_tags, list):
        return set()
    return {str(tag) for tag in raw_tags if str(tag).strip()}


def is_utility_item(item_metadata: Mapping[int, Mapping[str, Any]], item_id: int) -> bool:
    return bool(item_tags(item_metadata, item_id).intersection(UTILITY_ITEM_TAGS))


def is_summoners_rift_item(
    item_metadata: Mapping[int, Mapping[str, Any]], item_id: int
) -> bool:
    maps = item_metadata.get(item_id, {}).get("maps", {})
    return isinstance(maps, Mapping) and maps.get("11") is True


def is_completed_build_item(
    item_metadata: Mapping[int, Mapping[str, Any]], item_id: int
) -> bool:
    """ビルド中核に使う完成品を選ぶ。開始アイテム・素材・utilityは除外する。"""
    metadata = item_metadata.get(item_id, {})
    if (
        not metadata
        or not is_summoners_rift_item(item_metadata, item_id)
        or is_utility_item(item_metadata, item_id)
    ):
        return False
    if "Lane" in item_tags(item_metadata, item_id) or "Jungle" in item_tags(item_metadata, item_id):
        return False
    return not bool(metadata.get("into"))


def item_status_groups(
    item_metadata: Mapping[int, Mapping[str, Any]], item_id: int
) -> dict[str, tuple[str, ...]]:
    """アイテムの非ゼロな Data Dragon stats をステータス群へ写像する。"""
    raw_stats = item_metadata.get(item_id, {}).get("stats", {})
    if not isinstance(raw_stats, Mapping):
        return {}
    result: dict[str, tuple[str, ...]] = {}
    for group_id, keys in STATUS_GROUP_SPECS.items():
        matched = tuple(
            key
            for key in keys
            if (value := as_float(raw_stats.get(key))) is not None and value != 0
        )
        if matched:
            result[group_id] = matched
    return result


def parse_status_groups(value: Optional[str]) -> set[str]:
    if not value:
        return set()
    aliases = {
        normalize_alias(group_id): group_id for group_id in STATUS_GROUP_SPECS
    }
    aliases.update(
        {normalize_alias(name): group_id for group_id, name in STATUS_GROUP_NAMES.items()}
    )
    selected: set[str] = set()
    invalid: list[str] = []
    for raw_value in value.split(","):
        token = raw_value.strip()
        if not token:
            continue
        group_id = aliases.get(normalize_alias(token))
        if group_id is None:
            invalid.append(token)
        else:
            selected.add(group_id)
    if invalid:
        raise ValueError(
            "不明なステータス群です: "
            + ", ".join(invalid)
            + "。選択肢: "
            + ", ".join(STATUS_GROUP_SPECS)
        )
    return selected


def parse_build_sizes(value: Optional[str]) -> tuple[int, ...]:
    if not value:
        return (2, 3)
    sizes: set[int] = set()
    for raw_value in value.split(","):
        token = raw_value.strip()
        if not token:
            continue
        try:
            size = int(token)
        except ValueError as error:
            raise ValueError(f"ビルドサイズは整数が必要です: {token}") from error
        if size not in {2, 3}:
            raise ValueError("ビルドサイズは2または3を指定してください")
        sizes.add(size)
    if not sizes:
        raise ValueError("ビルドサイズを1つ以上指定してください")
    return tuple(sorted(sizes))


def complete_entries(entries: Sequence[Any], include_incomplete: bool) -> list[Any]:
    if include_incomplete:
        return list(entries)
    return [entry for entry in entries if entry.match.is_complete()]


def participant_matches_filters(
    view: ParticipantView,
    *,
    roles: set[str],
    champion_ids: set[str],
) -> bool:
    if roles and view.role not in roles:
        return False
    if champion_ids and str(view.champion_id or "") not in champion_ids:
        return False
    return True


def _patch_label(patches: set[str]) -> str:
    ordered = sorted(patches)
    return ordered[0] if len(ordered) == 1 else "ALL"


def _name_from_counter(counter: Counter[str], fallback: str) -> str:
    if not counter:
        return fallback
    return sorted(counter, key=lambda value: (-counter[value], value))[0]


def _base_key(view: ParticipantView) -> tuple[str, str]:
    return str(view.champion_id or normalize_alias(view.champion_name)), view.role


def build_rows(
    group: ScopeGroup,
    *,
    catalog: DataDragonCatalog,
    item_metadata: Mapping[int, Mapping[str, Any]],
    roles: set[str],
    champion_ids: set[str],
    min_games: int,
    include_incomplete: bool,
    include_utility: bool,
    build_sizes: Sequence[int],
    selected_status_groups: set[str],
) -> tuple[
    list[dict[str, Any]],
    list[dict[str, Any]],
    list[dict[str, Any]],
    list[dict[str, Any]],
    dict[str, int],
]:
    entries = complete_entries(group.entries, include_incomplete)
    baseline: defaultdict[tuple[str, str], dict[str, Any]] = defaultdict(
        lambda: {
            "games": 0,
            "wins": 0,
            "names": Counter(),
            "patches": set(),
        }
    )
    pairs: defaultdict[tuple[tuple[str, str], int], dict[str, Any]] = defaultdict(
        lambda: {
            "games": 0,
            "wins": 0,
            "names": Counter(),
            "patches": set(),
            "tiers": set(),
        }
    )
    status_pairs: defaultdict[tuple[tuple[str, str], str], dict[str, Any]] = defaultdict(
        lambda: {
            "games": 0,
            "wins": 0,
            "names": Counter(),
            "patches": set(),
            "tiers": set(),
            "status_keys": set(),
        }
    )
    build_pairs: defaultdict[tuple[tuple[str, str], tuple[int, ...]], dict[str, Any]] = defaultdict(
        lambda: {
            "games": 0,
            "wins": 0,
            "names": Counter(),
            "patches": set(),
            "tiers": set(),
        }
    )
    item_pool: defaultdict[tuple[str, str], set[int]] = defaultdict(set)
    item_status_cache: dict[int, dict[str, tuple[str, ...]]] = {}
    stats: Counter[str] = Counter()

    def statuses_for(item_id: int) -> dict[str, tuple[str, ...]]:
        if item_id not in item_status_cache:
            item_status_cache[item_id] = item_status_groups(item_metadata, item_id)
        return item_status_cache[item_id]

    for entry in entries:
        stats["complete_or_included_matches"] += 1
        for view in participant_views(entry):
            if view.champion_id is None or view.win is None:
                stats["excluded_participants_missing_champion_or_win"] += 1
                continue
            if not participant_matches_filters(view, roles=roles, champion_ids=champion_ids):
                continue
            key = _base_key(view)
            baseline_row = baseline[key]
            baseline_row["games"] += 1
            baseline_row["wins"] += int(view.win)
            baseline_row["names"][champion_label(view)] += 1
            baseline_row["patches"].add(patch_prefix(view.match.game_version))
            item_ids = {
                item_id
                for item_id, slot in view.items
                if 0 <= slot <= 5 and (include_utility or not is_utility_item(item_metadata, item_id))
            }
            stats["eligible_participants"] += 1
            stats["eligible_item_slots_unique"] += len(item_ids)
            completed_item_ids = {
                item_id for item_id in item_ids if is_completed_build_item(item_metadata, item_id)
            }
            item_pool[key].update(completed_item_ids)
            participant_statuses: defaultdict[str, set[str]] = defaultdict(set)
            for item_id in item_ids:
                if not is_summoners_rift_item(item_metadata, item_id):
                    continue
                for status_group_id, status_keys in statuses_for(item_id).items():
                    if selected_status_groups and status_group_id not in selected_status_groups:
                        continue
                    participant_statuses[status_group_id].update(status_keys)
            for status_group_id, status_keys in participant_statuses.items():
                status_pair = status_pairs[(key, status_group_id)]
                status_pair["games"] += 1
                status_pair["wins"] += int(view.win)
                status_pair["names"][champion_label(view)] += 1
                status_pair["patches"].add(patch_prefix(view.match.game_version))
                status_pair["tiers"].add(entry.observed_tier)
                status_pair["status_keys"].update(status_keys)
            stats["eligible_status_observations"] += len(participant_statuses)
            for item_id in item_ids:
                if item_id not in catalog.items:
                    stats["unknown_item_observations"] += 1
                pair = pairs[(key, item_id)]
                pair["games"] += 1
                pair["wins"] += int(view.win)
                pair["names"][champion_label(view)] += 1
                pair["patches"].add(patch_prefix(view.match.game_version))
                pair["tiers"].add(entry.observed_tier)
            for build_size in build_sizes:
                for build_item_ids in combinations(sorted(completed_item_ids), build_size):
                    build_pair = build_pairs[(key, build_item_ids)]
                    build_pair["games"] += 1
                    build_pair["wins"] += int(view.win)
                    build_pair["names"][champion_label(view)] += 1
                    build_pair["patches"].add(patch_prefix(view.match.game_version))
                    build_pair["tiers"].add(entry.observed_tier)

    rows: list[dict[str, Any]] = []
    for (key, item_id), pair in pairs.items():
        if pair["games"] < min_games:
            stats["pairs_below_min_games"] += 1
            continue
        champion_id, role = key
        base = baseline[key]
        champion_games = int(base["games"])
        champion_wins = int(base["wins"])
        item_games = int(pair["games"])
        item_wins = int(pair["wins"])
        without_games = champion_games - item_games
        without_wins = champion_wins - item_wins
        item_rate = ratio(item_wins, item_games)
        without_rate = ratio(without_wins, without_games)
        row = {
            "scope": group.scope,
            "observed_tier": group.observed_tier,
            "patch": _patch_label(pair["patches"]),
            "patches": sorted(pair["patches"]),
            "champion_id": champion_id,
            "champion_name": _name_from_counter(pair["names"], champion_id),
            "role": role,
            "item_id": item_id,
            "item_name": catalog.item_name(item_id),
            "item_tags": sorted(item_tags(item_metadata, item_id)),
            "item_is_utility": is_utility_item(item_metadata, item_id),
            "item_is_completed": is_completed_build_item(item_metadata, item_id),
            "champion_games": champion_games,
            "champion_wins": champion_wins,
            "champion_baseline_win_rate": ratio(champion_wins, champion_games),
            "item_games": item_games,
            "item_wins": item_wins,
            "item_losses": item_games - item_wins,
            "item_win_rate": item_rate,
            "item_pick_rate": ratio(item_games, champion_games),
            "without_item_games": without_games,
            "without_item_wins": without_wins,
            "without_item_losses": without_games - without_wins,
            "without_item_win_rate": without_rate,
            "win_rate_lift_vs_without": item_rate - without_rate if item_rate is not None and without_rate is not None else None,
            "min_games_applied": min_games,
        }
        rows.append(row)
    rows.sort(
        key=lambda row: (
            str(row["scope"]),
            str(row["observed_tier"]),
            str(row["champion_name"]),
            str(row["role"]),
            -int(row["item_games"]),
            str(row["item_name"]),
            int(row["item_id"]),
        )
    )
    stats["eligible_pairs"] = len(rows)

    status_rows: list[dict[str, Any]] = []
    for (key, status_group_id), pair in status_pairs.items():
        if pair["games"] < min_games:
            stats["status_pairs_below_min_games"] += 1
            continue
        champion_id, role = key
        base = baseline[key]
        champion_games = int(base["games"])
        champion_wins = int(base["wins"])
        status_games = int(pair["games"])
        status_wins = int(pair["wins"])
        without_games = champion_games - status_games
        without_wins = champion_wins - status_wins
        status_rate = ratio(status_wins, status_games)
        without_rate = ratio(without_wins, without_games)
        status_rows.append(
            {
                "scope": group.scope,
                "observed_tier": group.observed_tier,
                "patch": _patch_label(pair["patches"]),
                "patches": sorted(pair["patches"]),
                "champion_id": champion_id,
                "champion_name": _name_from_counter(pair["names"], champion_id),
                "role": role,
                "status_group_id": status_group_id,
                "status_group_name": STATUS_GROUP_NAMES.get(status_group_id, status_group_id),
                "status_keys": sorted(pair["status_keys"]),
                "champion_games": champion_games,
                "champion_wins": champion_wins,
                "champion_baseline_win_rate": ratio(champion_wins, champion_games),
                "status_games": status_games,
                "status_wins": status_wins,
                "status_losses": status_games - status_wins,
                "status_win_rate": status_rate,
                "status_pick_rate": ratio(status_games, champion_games),
                "without_status_games": without_games,
                "without_status_wins": without_wins,
                "without_status_losses": without_games - without_wins,
                "without_status_win_rate": without_rate,
                "win_rate_lift_vs_without": status_rate - without_rate
                if status_rate is not None and without_rate is not None
                else None,
                "min_games_applied": min_games,
            }
        )
    status_rows.sort(
        key=lambda row: (
            str(row["scope"]),
            str(row["observed_tier"]),
            str(row["champion_name"]),
            str(row["role"]),
            -int(row["status_games"]),
            str(row["status_group_name"]),
        )
    )
    stats["eligible_status_pairs"] = len(status_rows)

    build_rows: list[dict[str, Any]] = []
    theory_rows: list[dict[str, Any]] = []
    for key, pool in item_pool.items():
        base = baseline[key]
        champion_id, role = key
        key_theory_rows: list[dict[str, Any]] = []
        for build_size in build_sizes:
            for build_item_ids in combinations(sorted(pool), build_size):
                pair = build_pairs.get((key, build_item_ids))
                if pair is None:
                    pair = {
                        "games": 0,
                        "wins": 0,
                        "names": Counter(),
                        "patches": set(),
                        "tiers": set(),
                    }
                build_games = int(pair["games"])
                build_wins = int(pair["wins"])
                champion_games = int(base["games"])
                champion_wins = int(base["wins"])
                without_games = champion_games - build_games
                without_wins = champion_wins - build_wins
                build_rate = ratio(build_wins, build_games)
                without_rate = ratio(without_wins, without_games)
                item_names = [catalog.item_name(item_id) for item_id in build_item_ids]
                build_row = {
                    "scope": group.scope,
                    "observed_tier": group.observed_tier,
                    "patch": _patch_label(pair["patches"]),
                    "patches": sorted(pair["patches"]),
                    "champion_id": champion_id,
                    "champion_name": _name_from_counter(pair["names"], champion_id),
                    "role": role,
                    "build_size": build_size,
                    "build_item_ids": list(build_item_ids),
                    "build_item_names": item_names,
                    "build_name": " + ".join(item_names),
                    "champion_games": champion_games,
                    "champion_wins": champion_wins,
                    "champion_baseline_win_rate": ratio(champion_wins, champion_games),
                    "build_games": build_games,
                    "build_wins": build_wins,
                    "build_losses": build_games - build_wins,
                    "build_win_rate": build_rate,
                    "build_pick_rate": ratio(build_games, champion_games),
                    "without_build_games": without_games,
                    "without_build_wins": without_wins,
                    "without_build_losses": without_games - without_wins,
                    "without_build_win_rate": without_rate,
                    "win_rate_lift_vs_without": build_rate - without_rate
                    if build_rate is not None and without_rate is not None
                    else None,
                    "min_games_applied": min_games,
                }
                if build_games >= min_games:
                    build_rows.append(build_row)
                else:
                    shared_statuses = set(statuses_for(build_item_ids[0]))
                    for item_id in build_item_ids[1:]:
                        shared_statuses.intersection_update(statuses_for(item_id))
                    if selected_status_groups:
                        shared_statuses.intersection_update(selected_status_groups)
                    if shared_statuses:
                        theory_row = dict(build_row)
                        theory_row.update(
                            {
                                "theory_type": "not_observed"
                                if build_games == 0
                                else "below_min_games",
                                "shared_status_groups": sorted(shared_statuses),
                                "theory_reason": "Data Dragonのstats上で共通するステータス: "
                                + ", ".join(
                                    STATUS_GROUP_NAMES.get(status_id, status_id)
                                    for status_id in sorted(shared_statuses)
                                ),
                            }
                        )
                        key_theory_rows.append(theory_row)
                stats["build_candidates"] += 1
        key_theory_rows.sort(
            key=lambda row: (
                -len(row["shared_status_groups"]),
                -int(row["build_games"] or 0),
                int(row["build_size"] or 0),
                str(row["build_name"]),
            )
        )
        theory_rows.extend(key_theory_rows[:MAX_THEORETICAL_ROWS_PER_CHAMPION_ROLE])
    build_rows.sort(
        key=lambda row: (
            str(row["scope"]),
            str(row["observed_tier"]),
            str(row["champion_name"]),
            str(row["role"]),
            int(row["build_size"]),
            -int(row["build_games"]),
            str(row["build_name"]),
        )
    )
    theory_rows.sort(
        key=lambda row: (
            str(row["scope"]),
            str(row["observed_tier"]),
            str(row["champion_name"]),
            str(row["role"]),
            -len(row["shared_status_groups"]),
            -int(row["build_games"]),
            str(row["build_name"]),
        )
    )
    stats["eligible_builds"] = len(build_rows)
    stats["theoretical_build_candidates"] = len(theory_rows)
    stats["unique_champions_roles"] = len(baseline)
    return rows, status_rows, build_rows, theory_rows, dict(stats)


def _overall_rows(rows: Sequence[Mapping[str, Any]]) -> list[dict[str, Any]]:
    return [dict(row) for row in rows if row.get("scope") == "overall"]


def _rank_positive(rows: Sequence[Mapping[str, Any]], minimum_games: int, limit: int) -> list[dict[str, Any]]:
    selected = [
        dict(row)
        for row in rows
        if int(row.get("item_games") or 0) >= minimum_games
        and int(row.get("without_item_games") or 0) >= minimum_games
        and row.get("item_is_completed", True)
        and row.get("win_rate_lift_vs_without") is not None
        and float(row["win_rate_lift_vs_without"]) > 0
    ]
    selected.sort(
        key=lambda row: (
            -float(row["win_rate_lift_vs_without"]),
            -int(row["item_games"] or 0),
            str(row.get("champion_name") or ""),
            str(row.get("role") or ""),
            str(row.get("item_name") or ""),
        )
    )
    return selected[:limit]


def _rank_negative(rows: Sequence[Mapping[str, Any]], minimum_games: int, limit: int) -> list[dict[str, Any]]:
    selected = [
        dict(row)
        for row in rows
        if int(row.get("item_games") or 0) >= minimum_games
        and int(row.get("without_item_games") or 0) >= minimum_games
        and row.get("item_is_completed", True)
        and row.get("win_rate_lift_vs_without") is not None
        and float(row["win_rate_lift_vs_without"]) < 0
    ]
    selected.sort(
        key=lambda row: (
            float(row["win_rate_lift_vs_without"]),
            -int(row["item_games"] or 0),
            str(row.get("champion_name") or ""),
            str(row.get("role") or ""),
            str(row.get("item_name") or ""),
        )
    )
    return selected[:limit]


def _rank_common(rows: Sequence[Mapping[str, Any]], minimum_games: int, limit: int) -> list[dict[str, Any]]:
    selected = [
        dict(row)
        for row in rows
        if int(row.get("item_games") or 0) >= minimum_games
        and int(row.get("without_item_games") or 0) >= minimum_games
        and row.get("item_is_completed", True)
    ]
    selected.sort(
        key=lambda row: (
            -int(row.get("item_games") or 0),
            -(float(row.get("item_pick_rate")) if row.get("item_pick_rate") is not None else 0.0),
            str(row.get("champion_name") or ""),
            str(row.get("role") or ""),
            str(row.get("item_name") or ""),
        )
    )
    return selected[:limit]


def _rank_champion_examples(rows: Sequence[Mapping[str, Any]], minimum_games: int, limit: int) -> list[dict[str, Any]]:
    selected = [
        dict(row)
        for row in rows
        if int(row.get("item_games") or 0) >= minimum_games
        and int(row.get("without_item_games") or 0) >= minimum_games
        and row.get("item_is_completed", True)
        and row.get("win_rate_lift_vs_without") is not None
        and float(row["win_rate_lift_vs_without"]) > 0
    ]
    by_champion: defaultdict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)
    for row in selected:
        by_champion[(str(row.get("champion_id") or ""), str(row.get("role") or ""))].append(row)
    best: list[dict[str, Any]] = []
    for candidates in by_champion.values():
        candidates.sort(
            key=lambda row: (
                -float(row["win_rate_lift_vs_without"]),
                -int(row.get("item_games") or 0),
                str(row.get("item_name") or ""),
            )
        )
        best.append(candidates[0])
    best.sort(
        key=lambda row: (
            -float(row["win_rate_lift_vs_without"]),
            -int(row.get("item_games") or 0),
            str(row.get("champion_name") or ""),
            str(row.get("role") or ""),
        )
    )
    return best[:limit]


def _rank_status_positive(
    rows: Sequence[Mapping[str, Any]], minimum_games: int, limit: int
) -> list[dict[str, Any]]:
    selected = [
        dict(row)
        for row in rows
        if int(row.get("status_games") or 0) >= minimum_games
        and int(row.get("without_status_games") or 0) >= minimum_games
        and row.get("win_rate_lift_vs_without") is not None
        and float(row["win_rate_lift_vs_without"]) > 0
    ]
    selected.sort(
        key=lambda row: (
            -float(row["win_rate_lift_vs_without"]),
            -int(row.get("status_games") or 0),
            str(row.get("champion_name") or ""),
            str(row.get("role") or ""),
            str(row.get("status_group_name") or ""),
        )
    )
    return selected[:limit]


def _rank_status_negative(
    rows: Sequence[Mapping[str, Any]], minimum_games: int, limit: int
) -> list[dict[str, Any]]:
    selected = [
        dict(row)
        for row in rows
        if int(row.get("status_games") or 0) >= minimum_games
        and int(row.get("without_status_games") or 0) >= minimum_games
        and row.get("win_rate_lift_vs_without") is not None
        and float(row["win_rate_lift_vs_without"]) < 0
    ]
    selected.sort(
        key=lambda row: (
            float(row["win_rate_lift_vs_without"]),
            -int(row.get("status_games") or 0),
            str(row.get("champion_name") or ""),
            str(row.get("role") or ""),
            str(row.get("status_group_name") or ""),
        )
    )
    return selected[:limit]


def _rank_status_common(
    rows: Sequence[Mapping[str, Any]], minimum_games: int, limit: int
) -> list[dict[str, Any]]:
    selected = [
        dict(row)
        for row in rows
        if int(row.get("status_games") or 0) >= minimum_games
        and int(row.get("without_status_games") or 0) >= minimum_games
    ]
    selected.sort(
        key=lambda row: (
            -int(row.get("status_games") or 0),
            -(float(row.get("status_pick_rate")) if row.get("status_pick_rate") is not None else 0.0),
            str(row.get("champion_name") or ""),
            str(row.get("role") or ""),
            str(row.get("status_group_name") or ""),
        )
    )
    return selected[:limit]


def _rank_build_positive(
    rows: Sequence[Mapping[str, Any]], minimum_games: int, limit: int
) -> list[dict[str, Any]]:
    selected = [
        dict(row)
        for row in rows
        if int(row.get("build_games") or 0) >= minimum_games
        and int(row.get("without_build_games") or 0) >= minimum_games
        and row.get("win_rate_lift_vs_without") is not None
        and float(row["win_rate_lift_vs_without"]) > 0
    ]
    selected.sort(
        key=lambda row: (
            -float(row["win_rate_lift_vs_without"]),
            -int(row.get("build_games") or 0),
            str(row.get("champion_name") or ""),
            str(row.get("role") or ""),
            int(row.get("build_size") or 0),
            str(row.get("build_name") or ""),
        )
    )
    return selected[:limit]


def _rank_build_common(
    rows: Sequence[Mapping[str, Any]], minimum_games: int, limit: int
) -> list[dict[str, Any]]:
    selected = [
        dict(row)
        for row in rows
        if int(row.get("build_games") or 0) >= minimum_games
        and int(row.get("without_build_games") or 0) >= minimum_games
    ]
    selected.sort(
        key=lambda row: (
            -int(row.get("build_games") or 0),
            -(float(row.get("build_pick_rate")) if row.get("build_pick_rate") is not None else 0.0),
            str(row.get("champion_name") or ""),
            str(row.get("role") or ""),
            int(row.get("build_size") or 0),
            str(row.get("build_name") or ""),
        )
    )
    return selected[:limit]


def _rank_theoretical(rows: Sequence[Mapping[str, Any]], limit: int) -> list[dict[str, Any]]:
    selected = [dict(row) for row in rows]
    selected.sort(
        key=lambda row: (
            -len(row.get("shared_status_groups") or []),
            -int(row.get("build_games") or 0),
            int(row.get("build_size") or 0),
            str(row.get("build_name") or ""),
        )
    )
    return selected[:limit]


def _display_rows(rows: Sequence[Mapping[str, Any]]) -> list[dict[str, Any]]:
    result = []
    for row in rows:
        copied = dict(row)
        for key in (
            "item_pick_rate",
            "item_win_rate",
            "without_item_win_rate",
            "status_pick_rate",
            "status_win_rate",
            "without_status_win_rate",
            "build_pick_rate",
            "build_win_rate",
            "without_build_win_rate",
            "win_rate_lift_vs_without",
        ):
            if copied.get(key) is not None:
                copied[key] = display_number(float(copied[key]), 3)
        result.append(copied)
    return result


def render_report(
    *,
    dataset: Dataset,
    filter_stats: Mapping[str, int],
    groups: Sequence[ScopeGroup],
    rows: Sequence[Mapping[str, Any]],
    status_rows: Sequence[Mapping[str, Any]],
    build_rows: Sequence[Mapping[str, Any]],
    theory_rows: Sequence[Mapping[str, Any]],
    row_stats: Mapping[str, Mapping[str, int]],
    args: argparse.Namespace,
    item_metadata_count: int,
) -> str:
    overall = _overall_rows(rows)
    overall_status = _overall_rows(status_rows)
    overall_builds = _overall_rows(build_rows)
    overall_theory = _overall_rows(theory_rows)
    display_min_games = max(args.min_games, args.report_min_games)
    positive = _display_rows(_rank_positive(overall, display_min_games, args.top))
    negative = _display_rows(_rank_negative(overall, display_min_games, args.top))
    common = _display_rows(_rank_common(overall, display_min_games, args.top))
    champion_examples = _display_rows(_rank_champion_examples(overall, display_min_games, args.top))
    status_positive = _display_rows(_rank_status_positive(overall_status, display_min_games, args.top))
    status_negative = _display_rows(_rank_status_negative(overall_status, display_min_games, args.top))
    status_common = _display_rows(_rank_status_common(overall_status, display_min_games, args.top))
    build_positive = _display_rows(_rank_build_positive(overall_builds, display_min_games, args.top))
    build_common = _display_rows(_rank_build_common(overall_builds, display_min_games, args.top))
    theory_common = _display_rows(_rank_theoretical(overall_theory, args.top))
    quality = {
        "input": dataset.quality.as_dict(),
        "filters": filter_stats,
        "groups": {
            group.scope + ":" + group.observed_tier: len(group.entries)
            for group in groups
        },
        "row_stats": row_stats,
        "item_metadata_records": item_metadata_count,
        "status_group_definitions": {
            group_id: {
                "name": STATUS_GROUP_NAMES[group_id],
                "stats_keys": list(keys),
            }
            for group_id, keys in STATUS_GROUP_SPECS.items()
            if not args.status_groups or group_id in args.status_groups
        },
    }
    unknown_item_observations = sum(
        int(stats.get("unknown_item_observations", 0))
        for stats in row_stats.values()
    )
    positive_columns = (
        ("champion_name", "チャンピオン"),
        ("role", "ロール"),
        ("item_name", "アイテム"),
        ("item_games", "所持試合"),
        ("without_item_games", "非所持試合"),
        ("item_pick_rate", "所持率"),
        ("item_win_rate", "所持時勝率"),
        ("without_item_win_rate", "非所持時勝率"),
        ("win_rate_lift_vs_without", "差"),
    )
    status_columns = (
        ("champion_name", "チャンピオン"),
        ("role", "ロール"),
        ("status_group_name", "ステータス群"),
        ("status_games", "該当試合"),
        ("without_status_games", "非該当試合"),
        ("status_pick_rate", "該当率"),
        ("status_win_rate", "該当時勝率"),
        ("without_status_win_rate", "非該当時勝率"),
        ("win_rate_lift_vs_without", "差"),
    )
    build_columns = (
        ("champion_name", "チャンピオン"),
        ("role", "ロール"),
        ("build_name", "ビルド中核"),
        ("build_games", "該当試合"),
        ("without_build_games", "非該当試合"),
        ("build_pick_rate", "採用率"),
        ("build_win_rate", "該当時勝率"),
        ("without_build_win_rate", "非該当時勝率"),
        ("win_rate_lift_vs_without", "差"),
    )
    theory_columns = (
        ("champion_name", "チャンピオン"),
        ("role", "ロール"),
        ("build_name", "仮説ビルド"),
        ("build_games", "実測試合"),
        ("theory_type", "根拠状態"),
        ("theory_reason", "推測根拠"),
    )
    lines = [
        "# 実試合データによるチャンピオン・アイテム相性分析",
        "",
        f"- 解析スクリプト：`{SCRIPT_NAME}`",
        f"- キュー：`{args.queue_id}`",
        f"- tier mode：`{args.tier_mode}`",
        f"- ペア掲載の最小ゲーム数：`{args.min_games}`",
        f"- Markdown表示の最小ゲーム数（所持・非所持の双方）：`{display_min_games}`",
        f"- ビルド中核サイズ：`{','.join(str(size) for size in args.build_sizes)}`（アイテム順は無視）",
        f"- ステータス群フィルター：`{','.join(sorted(args.status_groups)) if args.status_groups else '全て'}`",
        f"- 通常アイテムのみ：`{not args.include_utility}`（`--include-utility` 指定時は消耗品・視界・トリンケット等も含む）",
        f"- Data Dragon：`{args.data_dragon}`",
        f"- 入力ファイル数：{len(dataset.input_files)}",
        f"- 入力後のユニーク試合数：{len(dataset.matches)}",
        "",
        "> [!warning] 相性の意味",
        "> このレポートの「差」は、同じチャンピオン・正規化ロールで、通常スロット `item0`〜`item5` にそのアイテム・ビルド中核・ステータス群を持っていた試合と、持っていなかった試合の勝率差である。最終所持状態の記述的な関連であり、アイテムの因果効果、最適ビルド、推奨順序を示さない。",
        "",
        "## 集計方法",
        "",
        "- 同じ試合IDを共通ローダーで1回だけ数え、既定では完全試合だけを対象にした。",
        "- 同じアイテムが複数スロットに現れても、1参加者につき1所持として数えた。`item6` はトリンケット等の補助スロットなので除外した。",
        "- ステータス群はData Dragon `item.json` の `stats` に非ゼロ値があるアイテムの集合で、同じ参加者が同群のアイテムを複数持っていても1回と数えた。クリティカル率なら、`FlatCritChanceMod` を持つアイテムを1つ以上所持したかを判定する。",
        "- ステータス群とビルド中核には、指定Data Dragonで `maps[\"11\"]` が真のアイテムだけを使った。過去のアイテムIDが現行の別モード用IDへ再利用された場合の混入を抑えるためである。",
        "- ビルド中核は、同一参加者の最終アイテム集合から順序を無視した2個・3個の組み合わせを作ったもの。完成順、購入時刻、同時点の所持は表していない。",
        "- 基準勝率と非所持時勝率は、チャンピオンとロールごとに計算した。役割・パッチ・試合時間・プレイヤー・購入時点の違いは調整していない。",
        f"- CSV/JSONには所持試合数15以上の個別アイテム・ステータス群・ビルド中核を残し、Markdownの上位表は所持・非所持の双方が{display_min_games}ゲーム以上ある候補に限定した。",
        "",
        "## データ品質",
        "",
        "```json",
        json.dumps(quality, ensure_ascii=False, indent=2, sort_keys=True),
        "```",
        "",
        f"アイテム原典のメタデータ読込件数は {item_metadata_count} 件。Data Dragonタグに `Consumable`、`Trinket`、`Vision`、`Stealth`、`GoldPer` のいずれかを持つものは、既定では実戦ビルドの相性表から除外した。",
        f"現行Data Dragonで表示名・タグを解決できなかったアイテム所持観測は {unknown_item_observations} 件あり、該当行は `UNKNOWN(<id>)` として品質情報へ残る。過去パッチを含む集計では、アイテムIDの再利用や原典差に注意する。",
        "Data Dragonの表示名・タグは指定アーカイブから解決する。複数パッチを合算する場合、同じアイテムIDの効果や名称がパッチ間で変わっている可能性があるため、厳密な現行比較には `--patch` と対応するData Dragonを指定する。",
        "",
        f"## 観測上のプラス差（所持・非所持の双方が{display_min_games}ゲーム以上）",
        "",
        markdown_table(positive, positive_columns, limit=args.top),
        "",
        "所持時勝率から非所持時勝率を引いた値が大きい順。少なくとも試合時間、パッチ、勝敗後に完成したアイテムであることによる生存者バイアスを含むため、候補の発見用に限る。",
        "",
        f"## ステータス群のプラス差（該当・非該当の双方が{display_min_games}ゲーム以上）",
        "",
        markdown_table(status_positive, status_columns, limit=args.top),
        "",
        "ステータス群を持つアイテムを1つ以上持った参加者を該当とした。アイテム個別の効果量や合計値ではなく、同じステータスを持つアイテムの採用有無の相関である。",
        "",
        f"## ステータス群のマイナス差（該当・非該当の双方が{display_min_games}ゲーム以上）",
        "",
        markdown_table(status_negative, status_columns, limit=args.top),
        "",
        "差がマイナスでも、そのステータス群が弱いことを意味しない。不利な試合で対策アイテムを選ぶなどの選択バイアスを含む。",
        "",
        f"## 出場数が多いステータス群（該当・非該当の双方が{display_min_games}ゲーム以上）",
        "",
        markdown_table(status_common, status_columns, limit=args.top),
        "",
        f"## 観測上のビルド中核プラス差（該当・非該当の双方が{display_min_games}ゲーム以上）",
        "",
        markdown_table(build_positive, build_columns, limit=args.top),
        "",
        "ビルド中核の組み合わせをまとめて持った最終状態の差であり、推奨購入順や完成前の強さではない。",
        "",
        f"## 出場数が多いビルド中核（該当・非該当の双方が{display_min_games}ゲーム以上）",
        "",
        markdown_table(build_common, build_columns, limit=args.top),
        "",
        "",
        "## ステータスから導いた理論仮説ビルド",
        "",
        markdown_table(theory_common, theory_columns, limit=args.top),
        "",
        "ここは十分な実測件数がない、または同じ組み合わせが未観測の候補を、Data Dragonの`stats`上で共通するステータスから機械的に抽出した仮説である。ゲーム内効果、チャンピオンのスキル倍率、対面、パッチを検証していないため、推奨確定として扱わない。",
        "",
        f"## 観測上のマイナス差（所持・非所持の双方が{display_min_games}ゲーム以上）",
        "",
        markdown_table(negative, positive_columns, limit=args.top),
        "",
        "差がマイナスでも、アイテムが弱いことを意味しない。不利な試合で防御・対策アイテムを選ぶ、完成前に敗北する、役割や構成が偏るなどの逆方向の要因があり得る。",
        "",
        f"## 出場数が多い組み合わせ（所持・非所持の双方が{display_min_games}ゲーム以上）",
        "",
        markdown_table(common, positive_columns, limit=args.top),
        "",
        "出場数の多さは、一般的な選択であることを示すだけで、相性の良さや推奨を示さない。",
        "",
        f"## チャンピオン・ロールごとの代表的なプラス差（所持・非所持の双方が{display_min_games}ゲーム以上）",
        "",
        markdown_table(champion_examples, positive_columns, limit=args.top),
        "",
        "各チャンピオン・ロールから差が最大の1件だけを抜き出した一覧。全ペアは `champion-item-synergy.csv`、ステータス群は `champion-status-synergy.csv`、ビルド中核は `champion-build-synergy.csv` と `analysis.json` を参照する。チャンピオン別の解釈は `champions/` を参照する。",
        "",
        "## 未解決事項",
        "",
        "- Timelineデータがないため、アイテムの購入時刻、完成時刻、15分時点の有利不利は分析していない。",
        "- ステータス群は現行Data Dragonの`stats`フィールドだけを根拠にする。説明文の発動効果、固有効果、実際のゲーム内相互作用は分類していない。",
        "- 理論仮説は観測の代替ではなく、共通ステータスを持つ未観測・小標本の組み合わせを候補化したもの。チャンピオンごとの推奨は、実測候補と仮説候補を分けて読む必要がある。",
        "- `min-games` は表示安定化の閾値であり、統計的有意性、信頼区間、パッチ間の再現性を保証しない。",
        "- パッチ・観測ランク帯・試合時間・相手構成を揃えた条件付き分析と、外部のビルド統計との照合が必要である。",
        "",
    ]
    return "\n".join(lines)


def render_champion_report(
    *,
    champion_id: str,
    champion_name: str,
    item_rows: Sequence[Mapping[str, Any]],
    status_rows: Sequence[Mapping[str, Any]],
    build_rows: Sequence[Mapping[str, Any]],
    theory_rows: Sequence[Mapping[str, Any]],
    args: argparse.Namespace,
) -> str:
    """1チャンピオン分の実測候補と理論仮説を分離して記録する。"""
    display_min_games = max(args.min_games, args.report_min_games)
    roles = sorted(
        {
            str(row.get("role") or "UNKNOWN")
            for row in (*item_rows, *status_rows, *build_rows, *theory_rows)
        }
    )
    item_columns = (
        ("item_name", "個別アイテム"),
        ("item_games", "所持試合"),
        ("without_item_games", "非所持試合"),
        ("item_pick_rate", "所持率"),
        ("item_win_rate", "所持時勝率"),
        ("without_item_win_rate", "非所持時勝率"),
        ("win_rate_lift_vs_without", "差"),
    )
    status_columns = (
        ("status_group_name", "ステータス群"),
        ("status_games", "該当試合"),
        ("without_status_games", "非該当試合"),
        ("status_pick_rate", "該当率"),
        ("status_win_rate", "該当時勝率"),
        ("without_status_win_rate", "非該当時勝率"),
        ("win_rate_lift_vs_without", "差"),
    )
    build_columns = (
        ("build_name", "ビルド中核"),
        ("build_games", "該当試合"),
        ("without_build_games", "非該当試合"),
        ("build_pick_rate", "採用率"),
        ("build_win_rate", "該当時勝率"),
        ("without_build_win_rate", "非該当時勝率"),
        ("win_rate_lift_vs_without", "差"),
    )
    theory_columns = (
        ("build_name", "仮説ビルド"),
        ("build_games", "実測試合"),
        ("theory_type", "根拠状態"),
        ("theory_reason", "推測根拠"),
    )
    lines = [
        f"# {champion_name}（チャンピオンID: {champion_id}）ビルド分析",
        "",
        f"- 解析スクリプト：`{SCRIPT_NAME}`",
        f"- 実測候補の最小ゲーム数：`{args.min_games}`（表示時の双方分母：`{display_min_games}`）",
        f"- 対象ステータス群：`{','.join(sorted(args.status_groups)) if args.status_groups else '全て'}`",
        "",
        "> [!warning] 読み方",
        "> 「推奨候補」は、最終所持状態の実測相関が比較的安定した候補を意味する。因果効果、購入順、完成前の強さ、対面別の最適解ではない。「理論仮説」は実測件数が不足または未観測で、Data Dragonの共通ステータスだけから候補化したものなので、実測候補と混同しない。",
        "",
        "## 結論の要約",
        "",
        "ロールごとに、実測ビルド中核、個別アイテム、ステータス群、理論仮説の順で分けている。差は同じチャンピオン・ロールの非所持状態との差であり、複数パッチを合算している場合はパッチ差も含む。",
        "",
    ]
    for role in roles:
        role_items = [dict(row) for row in item_rows if row.get("role") == role]
        role_status = [dict(row) for row in status_rows if row.get("role") == role]
        role_builds = [dict(row) for row in build_rows if row.get("role") == role]
        role_theory = [dict(row) for row in theory_rows if row.get("role") == role]
        item_positive = _display_rows(_rank_positive(role_items, display_min_games, min(args.top, 10)))
        status_positive = _display_rows(_rank_status_positive(role_status, display_min_games, min(args.top, 10)))
        build_positive = _display_rows(_rank_build_positive(role_builds, display_min_games, min(args.top, 10)))
        build_common = _display_rows(_rank_build_common(role_builds, display_min_games, min(args.top, 10)))
        theory = _display_rows(_rank_theoretical(role_theory, min(args.top, 10)))
        lines.extend(
            [
                f"## ロール：{role}",
                "",
                "### 実測からの推奨候補",
                "",
                "#### ビルド中核",
                "",
                markdown_table(build_positive or build_common, build_columns, limit=min(args.top, 10)),
                "",
                "差が正のビルド中核を優先し、該当しない場合は出場数の多い中核を表示した。どちらも購入順を意味しない。",
                "",
                "#### 個別アイテム",
                "",
                markdown_table(item_positive, item_columns, limit=min(args.top, 10)),
                "",
                "個別アイテムの差は、ビルド全体の代わりにはならない。アイテムが完成するまでの脱落や対面に起因する選択バイアスを含む。",
                "",
                "#### ステータス群",
                "",
                markdown_table(status_positive, status_columns, limit=min(args.top, 10)),
                "",
                "ステータス群は該当アイテムを1つ以上持ったかで判定し、同じステータスのアイテムを複数持つことによる総量・閾値効果は推定していない。",
                "",
                "### 統計が不足する理論仮説",
                "",
                markdown_table(theory, theory_columns, limit=min(args.top, 10)),
                "",
                "仮説の根拠は表の「推測根拠」に限定される。共通ステータス以外のスキル相互作用、ダメージ計算、相手の防御、パッチごとの強さは別途検証が必要である。",
                "",
            ]
        )
    if not roles:
        lines.extend(["（最小ゲーム数を満たす分析対象がありません。）", ""])
    return "\n".join(lines)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", action="append", required=True, help="入力ファイルまたはディレクトリ。複数指定可")
    parser.add_argument("--output", default="reports/riot-champion-item-synergy", help="レポート出力先")
    parser.add_argument("--queue-id", type=int, default=420, help="対象キューID（既定: 420）")
    parser.add_argument("--tier-mode", choices=("all", "observed"), default="all", help="重複観測をまとめる all または観測帯別の observed")
    parser.add_argument("--tiers", help="観測ランク帯をカンマ区切りで限定")
    parser.add_argument("--patch", help="gameVersionの前方一致フィルター")
    parser.add_argument("--date-from", help="試合開始日の下限（UTC、YYYY-MM-DD）")
    parser.add_argument("--date-to", help="試合開始日の上限（UTC、YYYY-MM-DD）")
    parser.add_argument("--roles", help="対象ロールをカンマ区切りで限定")
    parser.add_argument("--champions", help="対象チャンピオンIDまたは表示名をカンマ区切りで限定")
    parser.add_argument("--status-groups", help="分析するステータス群をカンマ区切りで限定（例: critical_chance）")
    parser.add_argument("--build-sizes", default="2,3", help="ビルド中核のアイテム数（2または3、既定: 2,3）")
    parser.add_argument("--min-games", type=int, default=15, help="CSV/JSONへ掲載する最小所持ゲーム数（既定: 15）")
    parser.add_argument("--report-min-games", type=int, default=DEFAULT_REPORT_MIN_GAMES, help="Markdown上位表の所持・非所持双方の最小ゲーム数（既定: 30）")
    parser.add_argument("--top", type=int, default=30, help="Markdown上位表の件数（既定: 30）")
    parser.add_argument("--include-utility", action="store_true", help="消耗品・視界・トリンケット等を含める")
    parser.add_argument("--include-incomplete", action="store_true", help="不完全試合を算出可能な集計へ含める")
    parser.add_argument("--format", default="markdown,csv,json", help="markdown,csv,json の組み合わせ")
    parser.add_argument("--data-dragon", default=str(DEFAULT_DATA_DRAGON), help="Data Dragonアーカイブ")
    parser.add_argument("--overwrite", action="store_true", help="同一runディレクトリが存在する場合に上書きする")
    parser.add_argument("--dry-run", action="store_true", help="入力と条件だけ検証して出力しない")
    return parser


def create_run_dir(output_root: Path, overwrite: bool) -> Path:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    run_dir = output_root / f"run-{stamp}"
    if run_dir.exists() and not overwrite:
        raise RuntimeError(f"出力ディレクトリが存在します: {run_dir}。--overwrite を指定してください")
    run_dir.mkdir(parents=True, exist_ok=True)
    return run_dir


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        if args.min_games <= 0 or args.report_min_games <= 0 or args.top <= 0:
            raise ValueError("--min-games、--report-min-games、--top は正の値が必要です")
        date_from = parse_date(args.date_from, "--date-from")
        date_to = parse_date(args.date_to, "--date-to")
        if date_from and date_to and date_from > date_to:
            raise ValueError("--date-from は --date-to 以下である必要があります")
        formats = parse_formats(args.format)
        roles = parse_roles(args.roles)
        status_groups = parse_status_groups(args.status_groups)
        build_sizes = parse_build_sizes(args.build_sizes)
        args.status_groups = status_groups
        args.build_sizes = build_sizes
        tiers = normalize_tiers(args.tiers)
        inputs = [Path(value) for value in args.input]
        dataset = load_dataset(inputs)
        catalog = DataDragonCatalog(Path(args.data_dragon)).load()
        item_metadata = load_item_metadata(Path(args.data_dragon))
        champion_ids = resolve_champion_ids(args.champions, dataset, catalog)
        scopes, filter_stats = select_scopes(
            dataset.matches,
            queue_id=args.queue_id,
            tier_mode=args.tier_mode,
            tiers=tiers,
            patch=args.patch,
            date_from=date_from,
            date_to=date_to,
        )
        groups = scope_groups(scopes, args.tier_mode)
        filters = {
            "script": SCRIPT_NAME,
            "schema_version": SCHEMA_VERSION,
            "queue_id": args.queue_id,
            "tier_mode": args.tier_mode,
            "tiers": sorted(tiers),
            "patch": args.patch,
            "date_from": date_from,
            "date_to": date_to,
            "roles": sorted(roles),
            "champion_ids": sorted(champion_ids),
            "status_groups": sorted(status_groups),
            "build_sizes": list(build_sizes),
            "min_games": args.min_games,
            "report_min_games": args.report_min_games,
            "top": args.top,
            "include_utility": args.include_utility,
            "include_incomplete": args.include_incomplete,
            "selected_scopes": len(scopes),
            "selected_unique_matches": len({entry.match.match_id for entry in scopes}),
        }
        dry_summary = {
            "filters": filters,
            "input_files": len(dataset.input_files),
            "quality": dataset.quality.as_dict(),
            "groups": [
                {"scope": group.scope, "observed_tier": group.observed_tier, "matches": len(group.entries)}
                for group in groups
            ],
            "item_metadata_records": len(item_metadata),
            "status_group_definitions": {
                group_id: {
                    "name": STATUS_GROUP_NAMES[group_id],
                    "stats_keys": list(keys),
                }
                for group_id, keys in STATUS_GROUP_SPECS.items()
                if not status_groups or group_id in status_groups
            },
        }
        if args.dry_run:
            print(json.dumps(dry_summary, ensure_ascii=False, indent=2, sort_keys=True))
            return 0

        output_root = resolve_root_path(args.output)
        reject_raw_output(output_root)
        run_dir = create_run_dir(output_root, args.overwrite)
        all_rows: list[dict[str, Any]] = []
        all_status_rows: list[dict[str, Any]] = []
        all_build_rows: list[dict[str, Any]] = []
        all_theory_rows: list[dict[str, Any]] = []
        row_stats: dict[str, dict[str, int]] = {}
        for group in groups:
            group_rows, group_status_rows, group_build_rows, group_theory_rows, stats = build_rows(
                group,
                catalog=catalog,
                item_metadata=item_metadata,
                roles=roles,
                champion_ids=champion_ids,
                min_games=args.min_games,
                include_incomplete=args.include_incomplete,
                include_utility=args.include_utility,
                build_sizes=build_sizes,
                selected_status_groups=status_groups,
            )
            all_rows.extend(group_rows)
            all_status_rows.extend(group_status_rows)
            all_build_rows.extend(group_build_rows)
            all_theory_rows.extend(group_theory_rows)
            row_stats[f"{group.scope}:{group.observed_tier}"] = stats
        all_rows.sort(
            key=lambda row: (
                str(row.get("scope") or ""),
                str(row.get("observed_tier") or ""),
                str(row.get("champion_name") or ""),
                str(row.get("role") or ""),
                -int(row.get("item_games") or 0),
                str(row.get("item_name") or ""),
                int(row.get("item_id") or 0),
            )
        )
        all_status_rows.sort(
            key=lambda row: (
                str(row.get("scope") or ""),
                str(row.get("observed_tier") or ""),
                str(row.get("champion_name") or ""),
                str(row.get("role") or ""),
                -int(row.get("status_games") or 0),
                str(row.get("status_group_name") or ""),
            )
        )
        all_build_rows.sort(
            key=lambda row: (
                str(row.get("scope") or ""),
                str(row.get("observed_tier") or ""),
                str(row.get("champion_name") or ""),
                str(row.get("role") or ""),
                int(row.get("build_size") or 0),
                -int(row.get("build_games") or 0),
                str(row.get("build_name") or ""),
            )
        )
        all_theory_rows.sort(
            key=lambda row: (
                str(row.get("scope") or ""),
                str(row.get("observed_tier") or ""),
                str(row.get("champion_name") or ""),
                str(row.get("role") or ""),
                -len(row.get("shared_status_groups") or []),
                -int(row.get("build_games") or 0),
                str(row.get("build_name") or ""),
            )
        )
        generated_at = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
        analysis = {
            "schema_version": SCHEMA_VERSION,
            "generated_at": generated_at,
            "filters": filters,
            "results": all_rows,
            "status_group_results": all_status_rows,
            "build_results": all_build_rows,
            "theoretical_build_results": all_theory_rows,
        }
        quality = {
            "input": dataset.quality.as_dict(),
            "filters": filter_stats,
            "selected": dry_summary,
            "row_stats": row_stats,
            "item_metadata_records": len(item_metadata),
            "result_counts": {
                "champion_item_rows": len(all_rows),
                "champion_status_rows": len(all_status_rows),
                "champion_build_rows": len(all_build_rows),
                "theoretical_build_rows": len(all_theory_rows),
            },
        }
        manifest = {
            "schema_version": SCHEMA_VERSION,
            "script": SCRIPT_NAME,
            "generated_at": generated_at,
            "inputs": manifest_input_paths(dataset.input_files),
            "data_dragon": str(Path(args.data_dragon)),
            "arguments": filters,
            "outputs": [],
        }
        if "csv" in formats:
            rows_to_csv(run_dir / "champion-item-synergy.csv", all_rows, CSV_FIELDS)
            manifest["outputs"].append("champion-item-synergy.csv")
            rows_to_csv(run_dir / "champion-status-synergy.csv", all_status_rows, STATUS_CSV_FIELDS)
            manifest["outputs"].append("champion-status-synergy.csv")
            rows_to_csv(run_dir / "champion-build-synergy.csv", all_build_rows, BUILD_CSV_FIELDS)
            manifest["outputs"].append("champion-build-synergy.csv")
            rows_to_csv(run_dir / "theoretical-build-candidates.csv", all_theory_rows, THEORY_CSV_FIELDS)
            manifest["outputs"].append("theoretical-build-candidates.csv")
        if "json" in formats:
            json_write(run_dir / "analysis.json", analysis)
            manifest["outputs"].append("analysis.json")
        json_write(run_dir / "quality.json", quality)
        manifest["outputs"].append("quality.json")
        if "markdown" in formats:
            (run_dir / "report.md").write_text(
                render_report(
                    dataset=dataset,
                    filter_stats=filter_stats,
                    groups=groups,
                    rows=all_rows,
                    status_rows=all_status_rows,
                    build_rows=all_build_rows,
                    theory_rows=all_theory_rows,
                    row_stats=row_stats,
                    args=args,
                    item_metadata_count=len(item_metadata),
                ),
                encoding="utf-8",
            )
            manifest["outputs"].append("report.md")
            champion_root = run_dir / "champions"
            champion_root.mkdir(parents=True, exist_ok=True)
            champion_keys = sorted(
                {
                    str(row.get("champion_id") or "")
                    for row in (*_overall_rows(all_rows), *_overall_rows(all_status_rows), *_overall_rows(all_build_rows), *_overall_rows(all_theory_rows))
                    if row.get("champion_id") is not None
                },
                key=lambda value: (int(value) if value.isdigit() else 10**9, value),
            )
            champion_index: list[dict[str, str]] = []
            for champion_id in champion_keys:
                champion_source_rows = [
                    row
                    for row in (
                        *_overall_rows(all_rows),
                        *_overall_rows(all_status_rows),
                        *_overall_rows(all_build_rows),
                        *_overall_rows(all_theory_rows),
                    )
                    if str(row.get("champion_id") or "") == champion_id
                ]
                name_counts = Counter(str(row.get("champion_name") or champion_id) for row in champion_source_rows)
                champion_name = _name_from_counter(name_counts, champion_id)
                report_path = champion_root / f"champion-{champion_id}.md"
                report_path.write_text(
                    render_champion_report(
                        champion_id=champion_id,
                        champion_name=champion_name,
                        item_rows=[row for row in _overall_rows(all_rows) if str(row.get("champion_id") or "") == champion_id],
                        status_rows=[row for row in _overall_rows(all_status_rows) if str(row.get("champion_id") or "") == champion_id],
                        build_rows=[row for row in _overall_rows(all_build_rows) if str(row.get("champion_id") or "") == champion_id],
                        theory_rows=[row for row in _overall_rows(all_theory_rows) if str(row.get("champion_id") or "") == champion_id],
                        args=args,
                    ),
                    encoding="utf-8",
                )
                champion_index.append({"champion_id": champion_id, "champion_name": champion_name, "path": str(report_path.relative_to(run_dir))})
            json_write(champion_root / "index.json", {"champions": champion_index})
            manifest["outputs"].append("champions/")
        json_write(run_dir / "manifest.json", manifest)
        print(f"解析完了: {run_dir}")
        print(json.dumps({"matches": len(dataset.matches), "selected": len(scopes), "rows": len(all_rows), "outputs": manifest["outputs"]}, ensure_ascii=False))
        return 0
    except (OSError, RuntimeError, ValueError, KeyError) as error:
        print(f"エラー: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
