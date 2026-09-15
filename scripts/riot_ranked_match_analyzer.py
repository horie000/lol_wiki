#!/usr/bin/env python3
"""取得済みのRiot Match-v5データを集計し、再利用可能なレポートを生成する。"""

from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable, Mapping, Optional, Sequence

from riot_match_analysis import (
    DEFAULT_DATA_DRAGON,
    DataDragonCatalog,
    Dataset,
    ParticipantView,
    ScopeGroup,
    ScopedMatch,
    as_float,
    as_int,
    champion_label,
    display_number,
    extract_bans,
    json_write,
    load_dataset,
    markdown_table,
    mean,
    normalize_alias,
    normalize_role,
    normalize_tiers,
    parse_formats,
    participant_views,
    patch_prefix,
    quantile,
    ratio,
    rows_to_csv,
    safe_slug,
    scope_groups,
    select_scopes,
    utc_iso,
)


SCRIPT_NAME = "scripts/riot_ranked_match_analyzer.py"
SCHEMA_VERSION = 2


def parse_roles(value: Optional[str]) -> set[str]:
    if not value:
        return set()
    roles = {normalize_role(item) for item in value.split(",") if item.strip()}
    return {role for role in roles if role != "UNKNOWN"}


def parse_date(value: Optional[str], option: str) -> Optional[str]:
    if not value:
        return None
    try:
        return datetime.strptime(value, "%Y-%m-%d").date().isoformat()
    except ValueError as error:
        raise ValueError(f"{option} は YYYY-MM-DD 形式が必要です: {value}") from error


def resolve_root_path(value: str) -> Path:
    path = Path(value).expanduser()
    return path if path.is_absolute() else Path(__file__).resolve().parents[1] / path


def reject_raw_output(path: Path) -> None:
    root = Path(__file__).resolve().parents[1]
    raw_root = (root / "raw").resolve()
    resolved = path.resolve()
    if resolved == raw_root or raw_root in resolved.parents:
        raise ValueError("解析結果を raw/ 配下へ書き出すことはできません")


def resolve_champion_ids(
    values: Optional[str],
    dataset: Dataset,
    catalog: DataDragonCatalog,
) -> set[str]:
    if not values:
        return set()
    available: dict[str, set[str]] = defaultdict(set)
    for match in dataset.matches:
        for raw in match.participants:
            if not isinstance(raw, Mapping):
                continue
            champion_id = as_int(raw.get("championId"))
            if champion_id is None:
                continue
            champion_key = str(champion_id)
            available[champion_key].add(champion_key)
            available[normalize_alias(raw.get("championName"))].add(champion_key)
    resolved: set[str] = set()
    for value in values.split(","):
        token = value.strip()
        if not token:
            continue
        direct = str(as_int(token)) if as_int(token) is not None else ""
        candidates = set(catalog.champion_candidates(token))
        candidates.update(available.get(normalize_alias(token), set()))
        if direct:
            candidates.add(direct)
        if not candidates:
            raise ValueError(f"チャンピオンを解決できません: {token}")
        resolved.update(candidates)
    return resolved


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


def complete_entries(entries: Sequence[ScopedMatch], include_incomplete: bool) -> list[ScopedMatch]:
    if include_incomplete:
        return list(entries)
    return [entry for entry in entries if entry.match.is_complete()]


def group_by_patch(entries: Sequence[ScopedMatch]) -> dict[str, list[ScopedMatch]]:
    grouped: defaultdict[str, list[ScopedMatch]] = defaultdict(list)
    for entry in entries:
        grouped[patch_prefix(entry.match.game_version)].append(entry)
    return dict(sorted(grouped.items()))


def team_damage_totals(views: Sequence[ParticipantView]) -> dict[tuple[str, str], float]:
    totals: defaultdict[tuple[str, str], float] = defaultdict(float)
    for view in views:
        damage = as_float(view.raw.get("totalDamageDealtToChampions"))
        if damage is not None:
            totals[(view.match.match_id, view.team_id)] += damage
    return dict(totals)


def team_gold_totals(views: Sequence[ParticipantView]) -> dict[tuple[str, str], float]:
    totals: defaultdict[tuple[str, str], float] = defaultdict(float)
    for view in views:
        gold = as_float(view.raw.get("goldEarned"))
        if gold is not None and gold >= 0:
            totals[(view.match.match_id, view.team_id)] += gold
    return dict(totals)


def participant_metric(view: ParticipantView, key: str) -> Optional[float]:
    return as_float(view.raw.get(key))


def per_minute(view: ParticipantView, key: str) -> Optional[float]:
    value = participant_metric(view, key)
    duration = participant_metric(view, "timePlayed")
    return ratio(value or 0, duration / 60) if value is not None and duration and duration > 0 else None


def cs_per_minute(view: ParticipantView) -> Optional[float]:
    minions = participant_metric(view, "totalMinionsKilled")
    neutral = participant_metric(view, "neutralMinionsKilled")
    duration = participant_metric(view, "timePlayed")
    if minions is None or neutral is None or duration is None or duration <= 0:
        return None
    return (minions + neutral) / (duration / 60)


def kda(view: ParticipantView) -> Optional[float]:
    kills = participant_metric(view, "kills")
    assists = participant_metric(view, "assists")
    deaths = participant_metric(view, "deaths")
    if kills is None or assists is None or deaths is None:
        return None
    return (kills + assists) / max(deaths, 1)


def damage_share(view: ParticipantView, totals: Mapping[tuple[str, str], float]) -> Optional[float]:
    damage = participant_metric(view, "totalDamageDealtToChampions")
    total = totals.get((view.match.match_id, view.team_id), 0)
    return ratio(damage or 0, total) if damage is not None and total else None


def base_row(group: ScopeGroup, patch: str, role: str) -> dict[str, Any]:
    return {
        "scope": group.scope,
        "observed_tier": group.observed_tier,
        "patch": patch,
        "role": role,
    }


def champion_rows(
    group: ScopeGroup,
    entries: Sequence[ScopedMatch],
    *,
    catalog: DataDragonCatalog,
    roles: set[str],
    champion_ids: set[str],
    min_games: int,
    include_incomplete: bool,
) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for patch, patch_entries in group_by_patch(entries).items():
        eligible_entries = complete_entries(patch_entries, include_incomplete)
        all_views = [view for entry in eligible_entries for view in participant_views(entry)]
        filtered_views = [
            view
            for view in all_views
            if participant_matches_filters(view, roles=roles, champion_ids=champion_ids)
        ]
        role_filtered_views = [view for view in all_views if not roles or view.role in roles]
        damage_totals = team_damage_totals(all_views)
        ban_counts: defaultdict[int, int] = defaultdict(int)
        ban_matches: defaultdict[int, set[str]] = defaultdict(set)
        for entry in eligible_entries:
            for champion_id in extract_bans(entry.match):
                ban_counts[champion_id] += 1
                ban_matches[champion_id].add(entry.match.match_id)
        role_labels = ["ALL"] + sorted({view.role for view in role_filtered_views if view.role != "UNKNOWN"})
        for role_label in role_labels:
            selected = filtered_views if role_label == "ALL" else [view for view in filtered_views if view.role == role_label]
            denominator = (
                len(role_filtered_views)
                if role_label == "ALL"
                else sum(1 for view in role_filtered_views if view.role == role_label)
            )
            grouped: defaultdict[str, list[ParticipantView]] = defaultdict(list)
            for view in selected:
                grouped[str(view.champion_id) if view.champion_id is not None else normalize_alias(view.champion_name)].append(view)
            for champion_key, champion_views in grouped.items():
                if len(champion_views) < min_games:
                    continue
                first = champion_views[0]
                wins = sum(1 for view in champion_views if view.win is True)
                losses = sum(1 for view in champion_views if view.win is False)
                champion_id = first.champion_id
                rows.append(
                    {
                        **base_row(group, patch, role_label),
                        "champion_id": champion_id,
                        "champion_name": champion_label(first),
                        "games": len(champion_views),
                        "wins": wins,
                        "losses": losses,
                        "win_rate": ratio(wins, len(champion_views)),
                        "pick_count": len(champion_views),
                        "pick_rate": ratio(len(champion_views), denominator),
                        "pick_rate_denominator": denominator,
                        "avg_kda": mean(kda(view) for view in champion_views),
                        "avg_cs_per_min": mean(cs_per_minute(view) for view in champion_views),
                        "avg_gold_per_min": mean(per_minute(view, "goldEarned") for view in champion_views),
                        "avg_damage_share": mean(damage_share(view, damage_totals) for view in champion_views),
                        "avg_vision_score": mean(participant_metric(view, "visionScore") for view in champion_views),
                        "first_blood_rate": mean(
                            participant_metric(view, "firstBloodKill") for view in champion_views
                        ),
                        "first_tower_rate": mean(
                            participant_metric(view, "firstTowerKill") for view in champion_views
                        ),
                        "ban_count": ban_counts.get(champion_id or -1, 0),
                        "ban_match_count": len(ban_matches.get(champion_id or -1, set())),
                        "ban_rate": ratio(
                            len(ban_matches.get(champion_id or -1, set())),
                            len(eligible_entries),
                        ),
                        "min_games_applied": min_games,
                    }
                )
    return sorted(
        rows,
        key=lambda row: (
            -int(row.get("games") or 0),
            -(float(row.get("win_rate")) if row.get("win_rate") is not None else -1),
            str(row.get("champion_name") or ""),
            str(row.get("role") or ""),
        ),
    )


def item_rows(
    group: ScopeGroup,
    entries: Sequence[ScopedMatch],
    *,
    catalog: DataDragonCatalog,
    roles: set[str],
    champion_ids: set[str],
    min_games: int,
    include_incomplete: bool,
) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for patch, patch_entries in group_by_patch(entries).items():
        eligible_entries = complete_entries(patch_entries, include_incomplete)
        all_views = [view for entry in eligible_entries for view in participant_views(entry)]
        filtered = [view for view in all_views if participant_matches_filters(view, roles=roles, champion_ids=champion_ids)]
        role_filtered = [view for view in all_views if not roles or view.role in roles]
        role_labels = ["ALL"] + sorted({view.role for view in role_filtered if view.role != "UNKNOWN"})
        for role_label in role_labels:
            selected = filtered if role_label == "ALL" else [view for view in filtered if view.role == role_label]
            denominator = len(role_filtered) if role_label == "ALL" else sum(1 for view in role_filtered if view.role == role_label)
            grouped: defaultdict[int, list[tuple[ParticipantView, int]]] = defaultdict(list)
            for view in selected:
                seen: dict[int, int] = {}
                for item_id, slot in view.items:
                    seen[item_id] = min(slot, seen.get(item_id, slot))
                for item_id, slot in seen.items():
                    grouped[item_id].append((view, slot))
            for item_id, holders in grouped.items():
                if len(holders) < min_games:
                    continue
                wins = sum(1 for view, _ in holders if view.win is True)
                rows.append(
                    {
                        **base_row(group, patch, role_label),
                        "item_id": item_id,
                        "item_name": catalog.item_name(item_id),
                        "games": len(holders),
                        "wins": wins,
                        "losses": sum(1 for view, _ in holders if view.win is False),
                        "win_rate": ratio(wins, len(holders)),
                        "holder_count": len(holders),
                        "pick_rate": ratio(len(holders), denominator),
                        "pick_rate_denominator": denominator,
                        "avg_final_slot": mean(float(slot) for _, slot in holders),
                        "min_games_applied": min_games,
                    }
                )
    return sort_aggregate(rows, "item_name")


def rune_rows(
    group: ScopeGroup,
    entries: Sequence[ScopedMatch],
    *,
    catalog: DataDragonCatalog,
    roles: set[str],
    champion_ids: set[str],
    min_games: int,
    include_incomplete: bool,
) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for patch, patch_entries in group_by_patch(entries).items():
        eligible_entries = complete_entries(patch_entries, include_incomplete)
        selected_views = [
            view
            for entry in eligible_entries
            for view in participant_views(entry)
            if participant_matches_filters(view, roles=roles, champion_ids=champion_ids)
        ]
        role_views = [
            view
            for entry in eligible_entries
            for view in participant_views(entry)
            if not roles or view.role in roles
        ]
        role_labels = ["ALL"] + sorted({view.role for view in role_views if view.role != "UNKNOWN"})
        for role_label in role_labels:
            selected = selected_views if role_label == "ALL" else [view for view in selected_views if view.role == role_label]
            denominator = len(role_views) if role_label == "ALL" else sum(1 for view in role_views if view.role == role_label)
            grouped: defaultdict[tuple[str, int], list[ParticipantView]] = defaultdict(list)
            for view in selected:
                seen: set[tuple[str, int]] = set()
                for rune in view.runes:
                    rune_id = as_int(rune.get("id"))
                    kind = str(rune.get("kind") or "rune")
                    if rune_id is not None and (kind, rune_id) not in seen:
                        grouped[(kind, rune_id)].append(view)
                        seen.add((kind, rune_id))
            for (kind, rune_id), holders in grouped.items():
                if len(holders) < min_games:
                    continue
                wins = sum(1 for view in holders if view.win is True)
                rows.append(
                    {
                        **base_row(group, patch, role_label),
                        "rune_kind": kind,
                        "rune_id": rune_id,
                        "rune_name": catalog.rune_name(rune_id),
                        "games": len(holders),
                        "wins": wins,
                        "losses": sum(1 for view in holders if view.win is False),
                        "win_rate": ratio(wins, len(holders)),
                        "pick_rate": ratio(len(holders), denominator),
                        "pick_rate_denominator": denominator,
                        "min_games_applied": min_games,
                    }
                )
    return sort_aggregate(rows, "rune_name")


def champion_rune_rows(
    group: ScopeGroup,
    entries: Sequence[ScopedMatch],
    *,
    catalog: DataDragonCatalog,
    roles: set[str],
    champion_ids: set[str],
    min_games: int,
    include_incomplete: bool,
) -> list[dict[str, Any]]:
    """チャンピオン・ロールごとのルーン選択率と関連勝率を集計する。"""

    rows: list[dict[str, Any]] = []
    role_order = {"ALL": 0, "TOP": 1, "JUNGLE": 2, "MIDDLE": 3, "BOTTOM": 4, "UTILITY": 5, "UNKNOWN": 6}
    kind_order = {"keystone": 0, "rune": 1, "shard": 2}
    for patch, patch_entries in group_by_patch(entries).items():
        eligible_entries = complete_entries(patch_entries, include_incomplete)
        all_views = [view for entry in eligible_entries for view in participant_views(entry)]
        filtered_views = [
            view
            for view in all_views
            if participant_matches_filters(view, roles=roles, champion_ids=champion_ids)
        ]
        role_labels = ["ALL"] + sorted(
            {view.role for view in filtered_views if view.role != "UNKNOWN"},
            key=lambda role: (role_order.get(role, 99), role),
        )
        for role_label in role_labels:
            selected = filtered_views if role_label == "ALL" else [
                view for view in filtered_views if view.role == role_label
            ]
            grouped: defaultdict[tuple[str, str], list[ParticipantView]] = defaultdict(list)
            for view in selected:
                champion_key = str(view.champion_id or normalize_alias(view.champion_name))
                grouped[(champion_key, champion_label(view))].append(view)
            for (champion_key, champion_name), champion_views in grouped.items():
                if len(champion_views) < min_games:
                    continue
                champion_wins = sum(1 for view in champion_views if view.win is True)
                rune_holders: defaultdict[tuple[str, int, Optional[int]], list[ParticipantView]] = defaultdict(list)
                for view in champion_views:
                    seen: set[tuple[str, int, Optional[int]]] = set()
                    for rune in view.runes:
                        rune_id = as_int(rune.get("id"))
                        if rune_id is None:
                            continue
                        kind = str(rune.get("kind") or "rune")
                        style_id = as_int(rune.get("style_id"))
                        key = (kind, rune_id, style_id)
                        if key not in seen:
                            rune_holders[key].append(view)
                            seen.add(key)
                for (kind, rune_id, style_id), holders in rune_holders.items():
                    if len(holders) < min_games:
                        continue
                    wins = sum(1 for view in holders if view.win is True)
                    rows.append(
                        {
                            **base_row(group, patch, role_label),
                            "champion_id": int(champion_key) if champion_key.isdigit() else champion_key,
                            "champion_name": champion_name,
                            "champion_games": len(champion_views),
                            "champion_wins": champion_wins,
                            "champion_losses": sum(1 for view in champion_views if view.win is False),
                            "champion_win_rate": ratio(champion_wins, len(champion_views)),
                            "rune_kind": kind,
                            "rune_id": rune_id,
                            "rune_name": catalog.rune_name(rune_id),
                            "rune_style_id": style_id,
                            "rune_style_name": catalog.rune_style_name(style_id) if style_id is not None else "",
                            "games": len(holders),
                            "wins": wins,
                            "losses": sum(1 for view in holders if view.win is False),
                            "win_rate": ratio(wins, len(holders)),
                            "pick_rate": ratio(len(holders), len(champion_views)),
                            "pick_rate_denominator": len(champion_views),
                            "min_games_applied": min_games,
                        }
                    )
    return sorted(
        rows,
        key=lambda row: (
            -int(row.get("champion_games") or 0),
            role_order.get(str(row.get("role") or ""), 99),
            str(row.get("champion_name") or ""),
            kind_order.get(str(row.get("rune_kind") or ""), 99),
            -int(row.get("games") or 0),
            str(row.get("rune_name") or ""),
            int(row.get("rune_id") or 0),
        ),
    )


def spell_rows(
    group: ScopeGroup,
    entries: Sequence[ScopedMatch],
    *,
    catalog: DataDragonCatalog,
    roles: set[str],
    champion_ids: set[str],
    min_games: int,
    include_incomplete: bool,
) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for patch, patch_entries in group_by_patch(entries).items():
        eligible_entries = complete_entries(patch_entries, include_incomplete)
        selected_views = [
            view
            for entry in eligible_entries
            for view in participant_views(entry)
            if participant_matches_filters(view, roles=roles, champion_ids=champion_ids)
        ]
        role_views = [
            view
            for entry in eligible_entries
            for view in participant_views(entry)
            if not roles or view.role in roles
        ]
        role_labels = ["ALL"] + sorted({view.role for view in role_views if view.role != "UNKNOWN"})
        for role_label in role_labels:
            selected = selected_views if role_label == "ALL" else [view for view in selected_views if view.role == role_label]
            denominator = len(role_views) if role_label == "ALL" else sum(1 for view in role_views if view.role == role_label)
            grouped: defaultdict[int, list[ParticipantView]] = defaultdict(list)
            for view in selected:
                for spell_id in set(view.summoner_spells):
                    grouped[spell_id].append(view)
            for spell_id, holders in grouped.items():
                if len(holders) < min_games:
                    continue
                wins = sum(1 for view in holders if view.win is True)
                rows.append(
                    {
                        **base_row(group, patch, role_label),
                        "spell_id": spell_id,
                        "spell_name": catalog.spell_name(spell_id),
                        "games": len(holders),
                        "wins": wins,
                        "losses": sum(1 for view in holders if view.win is False),
                        "win_rate": ratio(wins, len(holders)),
                        "pick_rate": ratio(len(holders), denominator),
                        "pick_rate_denominator": denominator,
                        "min_games_applied": min_games,
                    }
                )
    return sort_aggregate(rows, "spell_name")


def performance_rows(
    group: ScopeGroup,
    entries: Sequence[ScopedMatch],
    *,
    roles: set[str],
    champion_ids: set[str],
    min_games: int,
    include_incomplete: bool,
) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for patch, patch_entries in group_by_patch(entries).items():
        eligible_entries = complete_entries(patch_entries, include_incomplete)
        all_views = [view for entry in eligible_entries for view in participant_views(entry)]
        totals = team_damage_totals(all_views)
        filtered = [view for view in all_views if participant_matches_filters(view, roles=roles, champion_ids=champion_ids)]
        grouped: defaultdict[tuple[str, str], list[ParticipantView]] = defaultdict(list)
        for view in filtered:
            grouped[(str(view.champion_id or normalize_alias(view.champion_name)), view.role)].append(view)
        for (_, role), selected in grouped.items():
            if len(selected) < min_games:
                continue
            first = selected[0]
            rows.append(
                {
                    **base_row(group, patch, role),
                    "champion_id": first.champion_id,
                    "champion_name": champion_label(first),
                    "participants": len(selected),
                    "avg_kda": mean(kda(view) for view in selected),
                    "avg_cs_per_min": mean(cs_per_minute(view) for view in selected),
                    "avg_gold_per_min": mean(per_minute(view, "goldEarned") for view in selected),
                    "avg_damage_per_min": mean(per_minute(view, "totalDamageDealtToChampions") for view in selected),
                    "avg_damage_share": mean(damage_share(view, totals) for view in selected),
                    "avg_vision_score": mean(participant_metric(view, "visionScore") for view in selected),
                    "avg_wards_placed": mean(participant_metric(view, "wardsPlaced") for view in selected),
                    "avg_wards_killed": mean(participant_metric(view, "wardsKilled") for view in selected),
                    "min_games_applied": min_games,
                }
            )
    return sorted(rows, key=lambda row: (-int(row.get("participants") or 0), str(row.get("champion_name") or "")))


def role_gold_rows(
    group: ScopeGroup,
    entries: Sequence[ScopedMatch],
    *,
    roles: set[str],
    champion_ids: set[str],
    min_games: int,
    include_incomplete: bool,
) -> list[dict[str, Any]]:
    """ロール別の最終ゴールド獲得速度とチーム内配分を集計する。"""

    rows: list[dict[str, Any]] = []

    def summarize(patch: str, selected: Sequence[ParticipantView], all_views: Sequence[ParticipantView]) -> dict[str, Any]:
        gold_values = [
            gold
            for view in selected
            for gold in [as_float(view.raw.get("goldEarned"))]
            if gold is not None and gold >= 0
        ]
        gold_per_minute = [
            value
            for view in selected
            for value in [per_minute(view, "goldEarned")]
            if value is not None
        ]
        gold_duration_pairs = [
            (gold, duration / 60)
            for view in selected
            for gold, duration in [
                (as_float(view.raw.get("goldEarned")), as_float(view.raw.get("timePlayed")))
            ]
            if gold is not None and gold >= 0 and duration is not None and duration > 0
        ]
        team_totals = team_gold_totals(all_views)
        team_gold_shares = [
            gold / team_total
            for view in selected
            for gold, team_total in [
                (as_float(view.raw.get("goldEarned")), team_totals.get((view.match.match_id, view.team_id), 0))
            ]
            if gold is not None and gold >= 0 and team_total > 0
        ]
        wins = sum(1 for view in selected if view.win is True)
        losses = sum(1 for view in selected if view.win is False)
        total_gold = sum(gold for gold, _ in gold_duration_pairs)
        total_minutes = sum(minutes for _, minutes in gold_duration_pairs)
        return {
            **base_row(group, patch, "ALL"),
            "role": role,
            "matches": len({view.match.match_id for view in selected}),
            "participants": len(selected),
            "wins": wins,
            "losses": losses,
            "win_rate": ratio(wins, wins + losses),
            "valid_gold_participants": len(gold_values),
            "missing_gold_participants": len(selected) - len(gold_values),
            "gold_coverage_rate": ratio(len(gold_values), len(selected)),
            "total_gold": total_gold,
            "total_time_minutes": total_minutes,
            "weighted_gold_per_min": ratio(total_gold, total_minutes),
            "avg_gold_per_min": mean(gold_per_minute),
            "median_gold_per_min": quantile(gold_per_minute, 0.5),
            "p10_gold_per_min": quantile(gold_per_minute, 0.1),
            "p90_gold_per_min": quantile(gold_per_minute, 0.9),
            "team_gold_share_participants": len(team_gold_shares),
            "avg_team_gold_share": mean(team_gold_shares),
            "min_games_applied": min_games,
        }

    patch_groups = list(group_by_patch(entries).items())
    if entries:
        patch_groups.insert(0, ("ALL", list(entries)))
    for patch, patch_entries in patch_groups:
        eligible_entries = complete_entries(patch_entries, include_incomplete)
        all_views = [view for entry in eligible_entries for view in participant_views(entry)]
        filtered = [
            view
            for view in all_views
            if participant_matches_filters(view, roles=roles, champion_ids=champion_ids)
        ]
        role_labels = ["ALL"] + sorted({view.role for view in filtered if view.role != "ALL"})
        for role in role_labels:
            selected = filtered if role == "ALL" else [view for view in filtered if view.role == role]
            if len(selected) < min_games:
                continue
            rows.append(summarize(patch, selected, all_views))
    role_order = {"ALL": 0, "TOP": 1, "JUNGLE": 2, "MIDDLE": 3, "BOTTOM": 4, "UTILITY": 5, "UNKNOWN": 6}
    return sorted(
        rows,
        key=lambda row: (
            0 if row.get("patch") == "ALL" else 1,
            role_order.get(str(row.get("role")), 99),
            str(row.get("role") or ""),
            -int(row.get("participants") or 0),
        ),
    )


def duration_rows(
    group: ScopeGroup,
    entries: Sequence[ScopedMatch],
    *,
    include_incomplete: bool,
) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []

    def summary(patch: str, values: Sequence[float]) -> dict[str, Any]:
        from riot_match_analysis import quantile

        return {
            "scope": group.scope,
            "observed_tier": group.observed_tier,
            "patch": patch,
            "games": len(values),
            "avg_duration_seconds": sum(values) / len(values),
            "median_duration_seconds": quantile(values, 0.5),
            "p10_duration_seconds": quantile(values, 0.1),
            "p25_duration_seconds": quantile(values, 0.25),
            "p75_duration_seconds": quantile(values, 0.75),
            "p90_duration_seconds": quantile(values, 0.9),
            "min_duration_seconds": min(values),
            "max_duration_seconds": max(values),
        }

    for patch, patch_entries in group_by_patch(entries).items():
        eligible = complete_entries(patch_entries, include_incomplete)
        seconds = [as_float(entry.match.info.get("gameDuration")) for entry in eligible]
        values = sorted(value for value in seconds if value is not None and value > 0)
        if not values:
            continue
        rows.append(summary(patch, values))

    all_values = sorted(
        value
        for entry in complete_entries(entries, include_incomplete)
        for value in [as_float(entry.match.info.get("gameDuration"))]
        if value is not None and value > 0
    )
    if all_values:
        rows.insert(0, summary("ALL", all_values))
    return rows


def sort_aggregate(rows: Sequence[Mapping[str, Any]], label_key: str) -> list[dict[str, Any]]:
    return sorted(
        (dict(row) for row in rows),
        key=lambda row: (
            -int(row.get("games") or row.get("participants") or 0),
            -(float(row.get("win_rate")) if row.get("win_rate") is not None else -1),
            str(row.get(label_key) or ""),
        ),
    )


def matchup_rows(
    group: ScopeGroup,
    entries: Sequence[ScopedMatch],
    *,
    roles: set[str],
    champion_ids: set[str],
    min_games: int,
    include_incomplete: bool,
) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for patch, patch_entries in group_by_patch(entries).items():
        eligible_entries = complete_entries(patch_entries, include_incomplete)
        ally_counts: defaultdict[tuple[str, str, str, str], list[bool]] = defaultdict(list)
        opponent_counts: defaultdict[tuple[str, str, str, str, bool], list[bool]] = defaultdict(list)
        for entry in eligible_entries:
            views = participant_views(entry)
            for target in views:
                if not participant_matches_filters(target, roles=roles, champion_ids=champion_ids):
                    continue
                for related in views:
                    if related.participant_id == target.participant_id:
                        continue
                    if related.team_id == target.team_id:
                        target_key = (str(target.champion_id or normalize_alias(target.champion_name)), champion_label(target))
                        related_key = (str(related.champion_id or normalize_alias(related.champion_name)), champion_label(related))
                        # 味方ペアは順不同の組み合わせとして集計し、
                        # A-B と B-A を別行にしない。
                        if target_key >= related_key:
                            continue
                        key = (
                            target_key[0],
                            target_key[1],
                            related_key[0],
                            related_key[1],
                        )
                        ally_counts[key].append(target.win is True)
                    elif related.role == target.role and target.role != "UNKNOWN":
                        key = (
                            str(target.champion_id or normalize_alias(target.champion_name)),
                            champion_label(target),
                            str(related.champion_id or normalize_alias(related.champion_name)),
                            champion_label(related),
                            True,
                        )
                        opponent_counts[key].append(target.win is True)
        for key, outcomes in ally_counts.items():
            if len(outcomes) < min_games:
                continue
            target_id, target_name, related_id, related_name = key
            wins = sum(outcomes)
            rows.append(
                {
                    **base_row(group, patch, "ALL"),
                    "relation": "ally",
                    "target_champion_id": target_id,
                    "target_champion_name": target_name,
                    "related_champion_id": related_id,
                    "related_champion_name": related_name,
                    "games": len(outcomes),
                    "wins": wins,
                    "losses": len(outcomes) - wins,
                    "win_rate": ratio(wins, len(outcomes)),
                    "min_games_applied": min_games,
                }
            )
        for key, outcomes in opponent_counts.items():
            if len(outcomes) < min_games:
                continue
            target_id, target_name, related_id, related_name, same_role = key
            wins = sum(outcomes)
            rows.append(
                {
                    **base_row(group, patch, "ALL"),
                    "relation": "opponent",
                    "target_champion_id": target_id,
                    "target_champion_name": target_name,
                    "related_champion_id": related_id,
                    "related_champion_name": related_name,
                    "games": len(outcomes),
                    "wins": wins,
                    "losses": len(outcomes) - wins,
                    "win_rate": ratio(wins, len(outcomes)),
                    "same_role_match": same_role,
                    "min_games_applied": min_games,
                }
            )
    return sort_aggregate(rows, "related_champion_name")


def aggregate(
    groups: Sequence[ScopeGroup],
    *,
    catalog: DataDragonCatalog,
    roles: set[str],
    champion_ids: set[str],
    min_games: int,
    include_incomplete: bool,
    include_matchups: bool,
) -> dict[str, list[dict[str, Any]]]:
    result: dict[str, list[dict[str, Any]]] = {
        "champions": [],
        "items": [],
        "runes": [],
        "champion_runes": [],
        "spells": [],
        "performance": [],
        "role_gold": [],
        "duration": [],
        "matchups": [],
    }
    for group in groups:
        result["champions"].extend(
            champion_rows(
                group,
                group.entries,
                catalog=catalog,
                roles=roles,
                champion_ids=champion_ids,
                min_games=min_games,
                include_incomplete=include_incomplete,
            )
        )
        result["items"].extend(
            item_rows(
                group,
                group.entries,
                catalog=catalog,
                roles=roles,
                champion_ids=champion_ids,
                min_games=min_games,
                include_incomplete=include_incomplete,
            )
        )
        result["runes"].extend(
            rune_rows(
                group,
                group.entries,
                catalog=catalog,
                roles=roles,
                champion_ids=champion_ids,
                min_games=min_games,
                include_incomplete=include_incomplete,
            )
        )
        result["champion_runes"].extend(
            champion_rune_rows(
                group,
                group.entries,
                catalog=catalog,
                roles=roles,
                champion_ids=champion_ids,
                min_games=min_games,
                include_incomplete=include_incomplete,
            )
        )
        result["spells"].extend(
            spell_rows(
                group,
                group.entries,
                catalog=catalog,
                roles=roles,
                champion_ids=champion_ids,
                min_games=min_games,
                include_incomplete=include_incomplete,
            )
        )
        result["performance"].extend(
            performance_rows(
                group,
                group.entries,
                roles=roles,
                champion_ids=champion_ids,
                min_games=min_games,
                include_incomplete=include_incomplete,
            )
        )
        result["role_gold"].extend(
            role_gold_rows(
                group,
                group.entries,
                roles=roles,
                champion_ids=champion_ids,
                min_games=min_games,
                include_incomplete=include_incomplete,
            )
        )
        result["duration"].extend(duration_rows(group, group.entries, include_incomplete=include_incomplete))
        if include_matchups:
            result["matchups"].extend(
                matchup_rows(
                    group,
                    group.entries,
                    roles=roles,
                    champion_ids=champion_ids,
                    min_games=min_games,
                    include_incomplete=include_incomplete,
                )
            )
    return result


CSV_FIELDS = {
    "champions": (
        "scope", "observed_tier", "patch", "role", "champion_id", "champion_name", "games", "wins", "losses",
        "win_rate", "pick_count", "pick_rate", "pick_rate_denominator", "avg_kda", "avg_cs_per_min",
        "avg_gold_per_min", "avg_damage_share", "avg_vision_score", "first_blood_rate", "first_tower_rate",
        "ban_count", "ban_match_count", "ban_rate", "min_games_applied",
    ),
    "items": (
        "scope", "observed_tier", "patch", "role", "item_id", "item_name", "games", "wins", "losses",
        "win_rate", "holder_count", "pick_rate", "pick_rate_denominator", "avg_final_slot", "min_games_applied",
    ),
    "runes": (
        "scope", "observed_tier", "patch", "role", "rune_kind", "rune_id", "rune_name", "games", "wins",
        "losses", "win_rate", "pick_rate", "pick_rate_denominator", "min_games_applied",
    ),
    "champion_runes": (
        "scope", "observed_tier", "patch", "role", "champion_id", "champion_name", "champion_games",
        "champion_wins", "champion_losses", "champion_win_rate", "rune_kind", "rune_id", "rune_name",
        "rune_style_id", "rune_style_name", "games", "wins", "losses", "win_rate", "pick_rate",
        "pick_rate_denominator", "min_games_applied",
    ),
    "spells": (
        "scope", "observed_tier", "patch", "role", "spell_id", "spell_name", "games", "wins", "losses",
        "win_rate", "pick_rate", "pick_rate_denominator", "min_games_applied",
    ),
    "performance": (
        "scope", "observed_tier", "patch", "role", "champion_id", "champion_name", "participants", "avg_kda",
        "avg_cs_per_min", "avg_gold_per_min", "avg_damage_per_min", "avg_damage_share", "avg_vision_score",
        "avg_wards_placed", "avg_wards_killed", "min_games_applied",
    ),
    "role_gold": (
        "scope", "observed_tier", "patch", "role", "matches", "participants", "wins", "losses", "win_rate",
        "valid_gold_participants", "missing_gold_participants", "gold_coverage_rate", "total_gold",
        "total_time_minutes", "weighted_gold_per_min", "avg_gold_per_min", "median_gold_per_min",
        "p10_gold_per_min", "p90_gold_per_min", "team_gold_share_participants", "avg_team_gold_share",
        "min_games_applied",
    ),
    "duration": (
        "scope", "observed_tier", "patch", "games", "avg_duration_seconds", "median_duration_seconds",
        "p10_duration_seconds", "p25_duration_seconds", "p75_duration_seconds", "p90_duration_seconds",
        "min_duration_seconds", "max_duration_seconds",
    ),
    "matchups": (
        "scope", "observed_tier", "patch", "role", "relation", "target_champion_id", "target_champion_name",
        "related_champion_id", "related_champion_name", "games", "wins", "losses", "win_rate",
        "same_role_match", "min_games_applied",
    ),
}


def report_overall_rows(rows: Sequence[Mapping[str, Any]]) -> list[dict[str, Any]]:
    return [
        dict(row)
        for row in rows
        if row.get("scope") == "overall"
        and row.get("observed_tier") in {"ALL", "MIXED"}
        and row.get("role", "ALL") == "ALL"
    ]


def aggregate_report_rows(
    rows: Sequence[Mapping[str, Any]],
    key_fields: Sequence[str],
    label_field: str,
) -> list[dict[str, Any]]:
    grouped: dict[tuple[Any, ...], dict[str, Any]] = {}
    for row in report_overall_rows(rows):
        key = tuple(row.get(field) for field in key_fields)
        current = grouped.get(key)
        if current is None:
            current = dict(row)
            current["games"] = 0
            current["wins"] = 0
            current["losses"] = 0
            current["pick_rate_denominator"] = 0
            grouped[key] = current
        current["games"] += int(row.get("games") or 0)
        current["wins"] += int(row.get("wins") or 0)
        current["losses"] += int(row.get("losses") or 0)
        current["pick_rate_denominator"] += int(row.get("pick_rate_denominator") or 0)

    result: list[dict[str, Any]] = []
    for row in grouped.values():
        row["patch"] = "ALL"
        row["observed_tier"] = "ALL"
        row["win_rate"] = ratio(row["wins"], row["games"])
        row["pick_rate"] = ratio(row["games"], row["pick_rate_denominator"])
        result.append(row)
    return sorted(
        result,
        key=lambda row: (
            -int(row.get("games") or 0),
            -(float(row.get("win_rate")) if row.get("win_rate") is not None else -1),
            str(row.get(label_field) or ""),
        ),
    )


def report_matchup_rows(
    rows: Sequence[Mapping[str, Any]],
    relation: str,
) -> list[dict[str, Any]]:
    candidates = [
        row
        for row in rows
        if row.get("scope") == "overall"
        and row.get("observed_tier") == "ALL"
        and row.get("relation") == relation
    ]
    grouped: dict[tuple[Any, ...], dict[str, Any]] = {}
    for row in candidates:
        target_key = (str(row.get("target_champion_id") or ""), str(row.get("target_champion_name") or ""))
        related_key = (str(row.get("related_champion_id") or ""), str(row.get("related_champion_name") or ""))
        if relation == "ally":
            pair = tuple(sorted((target_key, related_key)))
            # ally_counts contains the same team pair once from each direction;
            # keep one direction per patch before aggregating across patches.
            if target_key != pair[0]:
                continue
            key = pair
        else:
            key = (target_key, related_key)
        current = grouped.get(key)
        if current is None:
            current = {
                "games": 0,
                "wins": 0,
                "losses": 0,
                "patches": set(),
                "target_champion_name": target_key[1],
                "related_champion_name": related_key[1],
            }
            if relation == "ally":
                current["champion_a_name"] = pair[0][1]
                current["champion_b_name"] = pair[1][1]
            grouped[key] = current
        current["games"] += int(row.get("games") or 0)
        current["wins"] += int(row.get("wins") or 0)
        current["losses"] += int(row.get("losses") or 0)
        current["patches"].add(str(row.get("patch") or "UNKNOWN"))

    result: list[dict[str, Any]] = []
    for row in grouped.values():
        row["relation"] = relation
        row["win_rate"] = ratio(row["wins"], row["games"])
        row["patch_count"] = len(row["patches"])
        del row["patches"]
        result.append(row)
    if relation == "ally":
        return sorted(
            result,
            key=lambda row: (
                -(float(row.get("win_rate")) if row.get("win_rate") is not None else -1),
                -int(row.get("games") or 0),
                str(row.get("champion_a_name") or ""),
                str(row.get("champion_b_name") or ""),
            ),
        )
    return sorted(
        result,
        key=lambda row: (
            float(row.get("win_rate")) if row.get("win_rate") is not None else 2,
            -int(row.get("games") or 0),
            str(row.get("target_champion_name") or ""),
            str(row.get("related_champion_name") or ""),
        ),
    )


def format_duration(seconds: Any) -> str:
    value = as_float(seconds)
    if value is None:
        return ""
    total_seconds = max(0, int(round(value)))
    minutes, remainder = divmod(total_seconds, 60)
    return f"{minutes}分{remainder:02d}秒"


def report_duration_rows(rows: Sequence[Mapping[str, Any]]) -> list[dict[str, Any]]:
    filtered = [
        dict(row)
        for row in rows
        if row.get("scope") == "overall" and row.get("observed_tier") in {"ALL", "MIXED"}
    ]
    all_rows = [row for row in filtered if row.get("patch") == "ALL"]
    patch_rows = sorted(
        [row for row in filtered if row.get("patch") != "ALL"],
        key=lambda row: (-int(row.get("games") or 0), str(row.get("patch") or "")),
    )
    selected = all_rows[:1] + patch_rows[:9]
    for row in selected:
        row["avg_duration"] = format_duration(row.get("avg_duration_seconds"))
        row["median_duration"] = format_duration(row.get("median_duration_seconds"))
        row["p10_duration"] = format_duration(row.get("p10_duration_seconds"))
        row["p90_duration"] = format_duration(row.get("p90_duration_seconds"))
    return selected


ROLE_LABELS = {
    "ALL": "全ロール",
    "TOP": "TOP",
    "JUNGLE": "JUNGLE",
    "MIDDLE": "MIDDLE",
    "BOTTOM": "BOTTOM",
    "UTILITY": "UTILITY",
    "UNKNOWN": "UNKNOWN（未分類）",
}


def format_percent(value: Any, digits: int = 1) -> str:
    number = as_float(value)
    if number is None:
        return ""
    return f"{number * 100:.{digits}f}%"


def report_role_gold_rows(rows: Sequence[Mapping[str, Any]]) -> list[dict[str, Any]]:
    selected = [
        dict(row)
        for row in rows
        if row.get("scope") == "overall"
        and row.get("observed_tier") in {"ALL", "MIXED"}
        and row.get("patch") == "ALL"
        and row.get("role") in ROLE_LABELS
    ]
    role_order = {"ALL": 0, "TOP": 1, "JUNGLE": 2, "MIDDLE": 3, "BOTTOM": 4, "UTILITY": 5, "UNKNOWN": 6}
    for row in selected:
        row["role_label"] = ROLE_LABELS[str(row.get("role"))]
        row["avg_gold_per_min_display"] = display_number(row.get("avg_gold_per_min"), 1)
        row["median_gold_per_min_display"] = display_number(row.get("median_gold_per_min"), 1)
        row["weighted_gold_per_min_display"] = display_number(row.get("weighted_gold_per_min"), 1)
        row["avg_team_gold_share_display"] = format_percent(row.get("avg_team_gold_share"))
        row["win_rate_display"] = format_percent(row.get("win_rate"))
        row["gold_coverage_display"] = format_percent(row.get("gold_coverage_rate"))
    return sorted(selected, key=lambda row: role_order.get(str(row.get("role")), 99))


def report_champion_rune_rows(rows: Sequence[Mapping[str, Any]]) -> list[dict[str, Any]]:
    """観測数の多いチャンピオン・ロールのルーン選択例を抽出する。"""
    candidates = [
        dict(row)
        for row in rows
        if row.get("scope") == "overall"
        and row.get("observed_tier") in {"ALL", "MIXED"}
        and row.get("role") not in {None, "ALL"}
    ]
    # champion_rune_rows はパッチごとの行を返すため、レポートの代表値は
    # パッチをまたいで合算する。チャンピオン分母は同じパッチの重複行を
    # 一度だけ数え、ルーンの分子・分母はルーンごとに加算する。
    champion_by_patch: dict[tuple[str, str, str], dict[str, Any]] = {}
    rune_totals: dict[tuple[str, str, str, str, str, str], dict[str, Any]] = {}
    for row in candidates:
        champion_key = (
            str(row.get("champion_id") or ""),
            str(row.get("role") or ""),
            str(row.get("patch") or ""),
        )
        champion_by_patch.setdefault(champion_key, {
            "champion_id": row.get("champion_id"),
            "champion_name": row.get("champion_name"),
            "role": row.get("role"),
            "champion_games": int(row.get("champion_games") or 0),
            "champion_wins": int(row.get("champion_wins") or 0),
            "champion_losses": int(row.get("champion_losses") or 0),
        })
        rune_key = (
            champion_key[0],
            champion_key[1],
            str(row.get("rune_kind") or ""),
            str(row.get("rune_id") or ""),
            str(row.get("rune_style_id") or ""),
            str(row.get("rune_name") or ""),
        )
        current = rune_totals.get(rune_key)
        if current is None:
            current = dict(row)
            current["games"] = 0
            current["wins"] = 0
            current["losses"] = 0
            rune_totals[rune_key] = current
        current["games"] += int(row.get("games") or 0)
        current["wins"] += int(row.get("wins") or 0)
        current["losses"] += int(row.get("losses") or 0)

    champion_totals: dict[tuple[str, str], dict[str, Any]] = {}
    for (champion_id, role, _patch), row in champion_by_patch.items():
        key = (champion_id, role)
        current = champion_totals.get(key)
        if current is None:
            current = dict(row)
            current["champion_games"] = 0
            current["champion_wins"] = 0
            current["champion_losses"] = 0
            champion_totals[key] = current
        current["champion_games"] += row["champion_games"]
        current["champion_wins"] += row["champion_wins"]
        current["champion_losses"] += row["champion_losses"]

    aggregated: list[dict[str, Any]] = []
    for (champion_id, role, _kind, _rune_id, _style_id, _rune_name), row in rune_totals.items():
        champion = champion_totals[(champion_id, role)]
        row["patch"] = "ALL"
        row["champion_games"] = champion["champion_games"]
        row["champion_wins"] = champion["champion_wins"]
        row["champion_losses"] = champion["champion_losses"]
        row["champion_win_rate"] = ratio(champion["champion_wins"], champion["champion_games"])
        row["win_rate"] = ratio(row["wins"], row["games"])
        row["pick_rate"] = ratio(row["games"], row["champion_games"])
        row["pick_rate_denominator"] = row["champion_games"]
        aggregated.append(row)

    partitions: defaultdict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)
    for row in aggregated:
        partitions[(str(row.get("champion_id") or ""), str(row.get("role") or ""))].append(row)
    top_partitions = sorted(
        partitions.items(),
        key=lambda item: (
            -int(max((row.get("champion_games") or 0 for row in item[1]), default=0)),
            str(item[1][0].get("champion_name") or ""),
            str(item[0][1]),
        ),
    )[:20]
    kind_order = {"keystone": 0, "rune": 1, "shard": 2}
    selected: list[dict[str, Any]] = []
    for _, partition in top_partitions:
        for kind in ("keystone", "rune", "shard"):
            selected.extend(
                sorted(
                    (row for row in partition if row.get("rune_kind") == kind),
                    key=lambda row: (
                        -(float(row.get("pick_rate")) if row.get("pick_rate") is not None else -1),
                        -int(row.get("games") or 0),
                        str(row.get("rune_name") or ""),
                    ),
                )[:2]
            )
    return sorted(
        selected,
        key=lambda row: (
            -int(row.get("champion_games") or 0),
            str(row.get("champion_name") or ""),
            str(row.get("role") or ""),
            kind_order.get(str(row.get("rune_kind") or ""), 99),
            -(float(row.get("pick_rate")) if row.get("pick_rate") is not None else -1),
        ),
    )


def render_report(
    *,
    dataset: Dataset,
    filter_stats: Mapping[str, int],
    groups: Sequence[ScopeGroup],
    analysis: Mapping[str, Sequence[Mapping[str, Any]]],
    args: argparse.Namespace,
) -> str:
    quality = dataset.quality.as_dict()
    champion_report = aggregate_report_rows(analysis["champions"], ("champion_id",), "champion_name")
    rune_report = aggregate_report_rows(analysis["runes"], ("rune_kind", "rune_id"), "rune_name")
    champion_rune_report = report_champion_rune_rows(analysis["champion_runes"])
    spell_report = aggregate_report_rows(analysis["spells"], ("spell_id",), "spell_name")
    role_gold_report = report_role_gold_rows(analysis["role_gold"])
    duration_report = report_duration_rows(analysis["duration"])
    ally_report = report_matchup_rows(analysis["matchups"], "ally") if args.include_matchups else []
    opponent_report = report_matchup_rows(analysis["matchups"], "opponent") if args.include_matchups else []
    unknown_shard_ids = sorted(
        str(row.get("rune_id"))
        for row in rune_report
        if row.get("rune_kind") == "shard" and str(row.get("rune_name") or "").startswith("UNKNOWN(")
    )
    lines = [
        "# Riotランク戦試合結果解析レポート",
        "",
        f"- 解析スクリプト：`{SCRIPT_NAME}`",
        f"- キュー：`{args.queue_id}`",
        f"- tier mode：`{args.tier_mode}`",
        f"- 最小ゲーム数：`{args.min_games}`",
        f"- 入力ファイル数：{len(dataset.input_files)}",
        f"- 入力後のユニーク試合数：{len({entry.match.match_id for group in groups for entry in group.entries})}",
        "",
        "> [!warning] 解釈上の注意",
        "> 観測ランク帯は収集時点のプレイヤー所属帯であり、試合時点の全参加者のランクを表さない。勝率、ゴールド/分、アイテム所持率、味方組み合わせ、対面の値は記述統計であり、因果効果や推奨を意味しない。",
        "",
        "## データ品質",
        "",
        "```json",
        json.dumps({"input": quality, "filters": filter_stats}, ensure_ascii=False, indent=2, sort_keys=True),
        "```",
        "",
        "## チャンピオン上位（全パッチ合算・ゲーム数順）",
        "",
        markdown_table(
            champion_report,
            (("champion_name", "チャンピオン"), ("role", "ロール"), ("games", "試合"), ("win_rate", "勝率"), ("pick_rate", "ピック率")),
        ),
        "",
        "## ルーン上位（選択数順）",
        "",
        markdown_table(
            rune_report,
            (("rune_name", "ルーン"), ("rune_kind", "種類"), ("rune_id", "ID"), ("games", "選択試合"), ("win_rate", "勝率")),
        ),
        "",
        "## チャンピオン別ルーン選択（観測数の多い上位例）",
        "",
        "同じチャンピオン・正規化ロールの参加者を分母に、各ルーンを選択した参加者の割合を集計しています。以下は観測数の多い20チャンピオン・ロールからの上位例で、全行は `champion-rune-summary.csv` と `analysis.json` に保存しています。",
        "",
        markdown_table(
            champion_rune_report,
            (
                ("champion_name", "チャンピオン"),
                ("role", "ロール"),
                ("rune_kind", "種類"),
                ("rune_name", "ルーン"),
                ("rune_style_name", "ルーン系統"),
                ("games", "選択数"),
                ("champion_games", "チャンピオン試合"),
                ("pick_rate", "選択率"),
                ("win_rate", "選択時勝率"),
                ("champion_win_rate", "チャンピオン勝率"),
            ),
            limit=40,
        ),
        "",
        "選択時勝率とチャンピオン全体の勝率の差は未調整の記述統計であり、ルーンの因果効果や推奨を示しません。シャードは1参加者が3つ選ぶため、種類内の選択率を合計して100%にはなりません。",
        "",
        "## ルーン表示名の注意",
        "",
        "Data Dragon v16.18.1 の `runesReforged.json` はルーンツリー内の選択ルーンを収録していますが、Match-v5 の `perks.statPerks` に含まれるステータスシャードの表示名辞書は収録していません。",
        "そのため、`rune_kind=shard` の `UNKNOWN(<ID>)` は試合データの欠損ではなく、ローカルData Dragonで表示名を解決できないIDです。ID・件数は `rune-summary.csv` と `analysis.json` に残しています。",
        f"今回確認された未知のステータスシャードID：{', '.join(unknown_shard_ids) if unknown_shard_ids else 'なし'}。",
        "",
        "## サモナースペル上位（選択数順）",
        "",
        markdown_table(
            spell_report,
            (("spell_name", "スペル"), ("spell_id", "ID"), ("games", "選択試合"), ("win_rate", "勝率"), ("pick_rate", "選択率")),
        ),
        "",
        "## 試合時間",
        "",
        "この表の1行は、`overall`（全体）・`observed_tier=ALL/MIXED`（観測帯を分けない）で、`パッチ=ALL` は全パッチ合算、その他はパッチ別の集計です。時間の単位は分・秒です。",
        "`中央値` は試合の半分がこの時間以内に終了したことを示します。`P10` は短い方から10%地点、`P90` は90%地点で、P10〜P90の間が中央80%の試合時間です。`試合` はその統計の分母です。",
        "具体例として、`パッチ=ALL` の行では、中央値を典型的な試合時間、P10〜P90を極端に短い・長い試合を除いた範囲として読みます。これはチャンピオンのパワースパイク、勝ちやすい時間帯、試合時間の因果要因を示すものではありません。",
        "",
        markdown_table(
            duration_report,
            (("patch", "パッチ"), ("games", "試合"), ("avg_duration", "平均"), ("median_duration", "中央値"), ("p10_duration", "P10"), ("p90_duration", "P90")),
        ),
        "",
        "## ロール別ゴールド獲得率",
        "",
        "ゴールド獲得率は、Match-v5の最終 `goldEarned` を `timePlayed`（分）で割ったゴールド/分です。平均は参加者ごとの値を同じ重みで平均し、加重平均は全ゴールドを全参加者時間で割っています。チーム内比率は、同じ試合・チームの最終ゴールド合計に占める参加者の比率です。",
        "いずれも試合終了時点の集計であり、15分時点のゴールド差、獲得の傾き、購入時刻、レーンでの実際の収入を表しません。",
        "",
        markdown_table(
            role_gold_report,
            (
                ("role_label", "ロール"),
                ("participants", "参加者"),
                ("matches", "試合"),
                ("avg_gold_per_min_display", "平均GPM"),
                ("median_gold_per_min_display", "中央値GPM"),
                ("weighted_gold_per_min_display", "加重GPM"),
                ("avg_team_gold_share_display", "チーム内比率"),
                ("win_rate_display", "勝率"),
                ("gold_coverage_display", "Gold有効率"),
            ),
        ),
    ]
    if args.include_matchups:
        lines.extend(
            [
                "",
                "## 味方になると強い組み合わせ",
                "",
                markdown_table(
                    ally_report,
                    (("champion_a_name", "味方A"), ("champion_b_name", "味方B"), ("games", "試合"), ("win_rate", "チーム勝率"), ("patch_count", "パッチ数")),
                ),
                "",
                "同じチーム内の組み合わせを順不同でまとめ、チーム勝率の高い順に並べています。これは味方シナジーの観測値であり、推奨編成や因果効果を意味しません。",
                "",
                "## カウンターピック候補（対象側勝率が低い順）",
                "",
                markdown_table(
                    opponent_report,
                    (("target_champion_name", "対象"), ("related_champion_name", "相手候補"), ("games", "試合"), ("win_rate", "対象側勝率"), ("patch_count", "パッチ数")),
                ),
                "",
                "同じ正規化ロールの相手候補だけを対象に、対象チャンピオン側の勝率が低い順に並べています。「カウンター」と断定せず、サンプル数・パッチ・観測ランク帯の違いを含む記述統計として読んでください。",
            ]
        )
    lines.extend(["", "## 未解決事項", "", "- Timelineデータがないため、購入時刻や15分時点の差分は分析していない。", "- 最小ゲーム数は表示安定化のための閾値であり、統計的有意性を示さない。", ""])
    return "\n".join(lines)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", action="append", required=True, help="入力ファイルまたはディレクトリ。複数指定可")
    parser.add_argument("--output", default="reports/riot-ranked-match-analysis", help="レポート出力先")
    parser.add_argument("--queue-id", type=int, default=420, help="対象キューID（既定: 420）")
    parser.add_argument("--tier-mode", choices=("all", "observed"), default="observed")
    parser.add_argument("--tiers", help="観測ランク帯をカンマ区切りで限定")
    parser.add_argument("--patch", help="gameVersionの前方一致フィルター")
    parser.add_argument("--date-from", help="試合開始日の下限（UTC、YYYY-MM-DD）")
    parser.add_argument("--date-to", help="試合開始日の上限（UTC、YYYY-MM-DD）")
    parser.add_argument("--roles", help="対象ロールをカンマ区切りで限定")
    parser.add_argument("--champions", help="対象チャンピオンIDまたは表示名をカンマ区切りで限定")
    parser.add_argument("--min-games", type=int, default=15, help="集計表へ掲載する最小ゲーム数（既定: 15）")
    parser.add_argument("--include-incomplete", action="store_true", help="不完全試合を算出可能な集計へ含める")
    parser.add_argument("--include-matchups", action="store_true", help="味方ペア・同ロール対面を生成する")
    parser.add_argument("--format", default="markdown,csv,json", help="markdown,csv,json の組み合わせ")
    parser.add_argument("--data-dragon", default=str(DEFAULT_DATA_DRAGON), help="Data Dragonアーカイブ")
    parser.add_argument("--overwrite", action="store_true", help="同一runディレクトリが存在する場合に上書きする")
    parser.add_argument("--dry-run", action="store_true", help="入力と条件だけ検証して出力しない")
    return parser


def validate_args(args: argparse.Namespace) -> tuple[set[str], set[str], set[str], tuple[str, str]]:
    if args.min_games <= 0:
        raise ValueError("--min-games は正の値が必要です")
    date_from = parse_date(args.date_from, "--date-from")
    date_to = parse_date(args.date_to, "--date-to")
    if date_from and date_to and date_from > date_to:
        raise ValueError("--date-from は --date-to 以下である必要があります")
    return normalize_tiers(args.tiers), parse_roles(args.roles), parse_formats(args.format), (date_from or "", date_to or "")


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
        tiers, roles, formats, date_values = validate_args(args)
        date_from, date_to = tuple(date_values)
        inputs = [Path(value) for value in args.input]
        dataset = load_dataset(inputs)
        catalog = DataDragonCatalog(Path(args.data_dragon)).load()
        champion_ids = resolve_champion_ids(args.champions, dataset, catalog)
        scopes, filter_stats = select_scopes(
            dataset.matches,
            queue_id=args.queue_id,
            tier_mode=args.tier_mode,
            tiers=tiers,
            patch=args.patch,
            date_from=date_from or None,
            date_to=date_to or None,
        )
        groups = scope_groups(scopes, args.tier_mode)
        dry_summary = {
            "input_files": len(dataset.input_files),
            "input_records": dataset.quality.counts.get("input_records", 0),
            "unique_matches": len(dataset.matches),
            "selected_scopes": len(scopes),
            "scope_groups": [{"scope": group.scope, "observed_tier": group.observed_tier, "matches": len(group.entries)} for group in groups],
            "queue_id": args.queue_id,
            "tier_mode": args.tier_mode,
            "min_games": args.min_games,
            "champion_filter_ids": sorted(champion_ids),
        }
        if args.dry_run:
            print(json.dumps(dry_summary, ensure_ascii=False, indent=2, sort_keys=True))
            return 0
        output_root = resolve_root_path(args.output)
        reject_raw_output(output_root)
        run_dir = create_run_dir(output_root, args.overwrite)
        analysis = aggregate(
            groups,
            catalog=catalog,
            roles=roles,
            champion_ids=champion_ids,
            min_games=args.min_games,
            include_incomplete=args.include_incomplete,
            include_matchups=args.include_matchups,
        )
        analysis_json = {
            "schema_version": SCHEMA_VERSION,
            "generated_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
            "filters": dry_summary,
            "results": analysis,
        }
        quality = {
            "input": dataset.quality.as_dict(),
            "filters": filter_stats,
            "selected": dry_summary,
            "include_incomplete": args.include_incomplete,
            "result_counts": {key: len(value) for key, value in analysis.items()},
        }
        manifest = {
            "schema_version": SCHEMA_VERSION,
            "script": SCRIPT_NAME,
            "generated_at": analysis_json["generated_at"],
            "inputs": dataset.input_files,
            "data_dragon": str(Path(args.data_dragon)),
            "arguments": {
                "queue_id": args.queue_id,
                "tier_mode": args.tier_mode,
                "tiers": sorted(tiers),
                "patch": args.patch,
                "date_from": date_from or None,
                "date_to": date_to or None,
                "roles": sorted(roles),
                "champion_ids": sorted(champion_ids),
                "min_games": args.min_games,
                "include_incomplete": args.include_incomplete,
                "include_matchups": args.include_matchups,
                "formats": sorted(formats),
            },
            "outputs": [],
        }
        if "csv" in formats:
            for key, rows in analysis.items():
                if key == "matchups" and not args.include_matchups:
                    continue
                filename = {
                    "champions": "champion-summary.csv",
                    "items": "item-summary.csv",
                    "runes": "rune-summary.csv",
                    "champion_runes": "champion-rune-summary.csv",
                    "spells": "summoner-spell-summary.csv",
                    "performance": "performance-summary.csv",
                    "role_gold": "role-gold.csv",
                    "duration": "duration-summary.csv",
                    "matchups": "matchup-summary.csv",
                }[key]
                rows_to_csv(run_dir / filename, rows, CSV_FIELDS[key])
                manifest["outputs"].append(filename)
        if "json" in formats:
            json_write(run_dir / "analysis.json", analysis_json)
            manifest["outputs"].append("analysis.json")
        json_write(run_dir / "quality.json", quality)
        manifest["outputs"].append("quality.json")
        if "markdown" in formats:
            (run_dir / "report.md").write_text(
                render_report(dataset=dataset, filter_stats=filter_stats, groups=groups, analysis=analysis, args=args),
                encoding="utf-8",
            )
            manifest["outputs"].append("report.md")
        json_write(run_dir / "manifest.json", manifest)
        print(f"解析完了: {run_dir}")
        print(json.dumps({"matches": len(dataset.matches), "selected": len(scopes), "outputs": manifest["outputs"]}, ensure_ascii=False))
        return 0
    except (OSError, RuntimeError, ValueError, KeyError) as error:
        print(f"エラー: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
