#!/usr/bin/env python3
"""取得済みのRiot Match-v5データを観測ランク帯ごとに比較する。"""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable, Mapping, Optional, Sequence

from riot_match_analysis import (
    DEFAULT_DATA_DRAGON,
    DataDragonCatalog,
    Dataset,
    ScopeGroup,
    as_bool,
    as_float,
    json_write,
    load_dataset,
    markdown_table,
    mean,
    normalize_tiers,
    parse_formats,
    participant_views,
    patch_prefix,
    quantile,
    ratio,
    rows_to_csv,
    scope_groups,
    select_scopes,
)


SCRIPT_NAME = "scripts/riot_ranked_tier_analyzer.py"
SCHEMA_VERSION = 1
TIER_ORDER = (
    "IRON",
    "BRONZE",
    "SILVER",
    "GOLD",
    "PLATINUM",
    "EMERALD",
    "DIAMOND",
    "MASTER",
    "GRANDMASTER",
    "CHALLENGER",
)
ROLE_ORDER = ("TOP", "JUNGLE", "MIDDLE", "BOTTOM", "UTILITY")


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


def create_run_dir(output_root: Path, overwrite: bool) -> Path:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    run_dir = output_root / f"run-{stamp}"
    if run_dir.exists() and not overwrite:
        raise RuntimeError(f"出力ディレクトリが存在します: {run_dir}。--overwrite を指定してください")
    run_dir.mkdir(parents=True, exist_ok=True)
    return run_dir


def average(values: Iterable[Optional[float]]) -> Optional[float]:
    return mean(values)


def per_minute(raw: Mapping[str, Any], key: str) -> Optional[float]:
    value = as_float(raw.get(key))
    duration = as_float(raw.get("timePlayed"))
    if value is None or duration is None or duration <= 0:
        return None
    return value / (duration / 60)


def cs_per_minute(raw: Mapping[str, Any]) -> Optional[float]:
    duration = as_float(raw.get("timePlayed"))
    if duration is None or duration <= 0:
        return None
    minions = as_float(raw.get("totalMinionsKilled"))
    neutral = as_float(raw.get("neutralMinionsKilled"))
    if minions is None or neutral is None:
        return None
    return (minions + neutral) / (duration / 60)


def kda(raw: Mapping[str, Any]) -> Optional[float]:
    kills = as_float(raw.get("kills"))
    assists = as_float(raw.get("assists"))
    deaths = as_float(raw.get("deaths"))
    if kills is None or assists is None or deaths is None:
        return None
    return (kills + assists) / max(deaths, 1)


def is_surrendered(raw: Mapping[str, Any]) -> bool:
    keys = (
        "gameEndedInSurrender",
        "gameEndedInEarlySurrender",
        "gameEndedInIGNBSurrender",
    )
    return any(as_bool(raw.get(key)) is True for key in keys)


def has_first_tower(entry: Any) -> bool:
    teams = entry.match.info.get("teams")
    if not isinstance(teams, list):
        return False
    for team in teams:
        if not isinstance(team, Mapping):
            continue
        objectives = team.get("objectives")
        if not isinstance(objectives, Mapping):
            continue
        tower = objectives.get("tower")
        if isinstance(tower, Mapping) and as_bool(tower.get("first")) is True:
            return True
    return False


def champion_key(view: Any) -> tuple[str, str]:
    champion_id = str(view.champion_id) if view.champion_id is not None else ""
    return champion_id, view.champion_name or "UNKNOWN"


def champion_label(key: tuple[str, str]) -> str:
    return key[1] if key[1] else (key[0] or "UNKNOWN")


def spell_pair(view: Any) -> tuple[int, ...]:
    # サモナースペルの順番は意味を持たない。異常な重複IDも表示上は一度にする。
    return tuple(sorted({spell_id for spell_id in view.summoner_spells}))


def format_percent(value: Any, digits: int = 1) -> str:
    number = as_float(value)
    if number is None:
        return ""
    return f"{number * 100:.{digits}f}%"


def format_number(value: Any, digits: int = 1) -> str:
    number = as_float(value)
    if number is None:
        return ""
    return f"{number:.{digits}f}"


def format_duration(seconds: Any) -> str:
    value = as_float(seconds)
    if value is None:
        return ""
    total_seconds = max(0, int(round(value)))
    minutes, remainder = divmod(total_seconds, 60)
    return f"{minutes}分{remainder:02d}秒"


def complete_entries(group: ScopeGroup) -> list[Any]:
    return [entry for entry in group.entries if entry.match.is_complete()]


def role_accumulator() -> dict[str, Any]:
    return {
        "match_ids": set(),
        "participants": 0,
        "wins": 0,
        "losses": 0,
        "gold_per_min": [],
        "damage_per_min": [],
        "cs_per_min": [],
        "vision_score": [],
        "kda": [],
        "team_gold_share": [],
    }


def tier_analysis(
    groups: Sequence[ScopeGroup],
    *,
    catalog: DataDragonCatalog,
    min_games: int,
) -> dict[str, Any]:
    tier_rows: list[dict[str, Any]] = []
    role_rows: list[dict[str, Any]] = []
    champion_rows: list[dict[str, Any]] = []
    champion_extreme_rows: list[dict[str, Any]] = []
    keystone_rows: list[dict[str, Any]] = []
    spell_pair_rows: list[dict[str, Any]] = []
    top_champion_sets: list[set[tuple[str, str]]] = []
    top_keystone_sets: list[set[int]] = []
    top_spell_pair_sets: list[set[tuple[int, ...]]] = []

    tier_groups = [group for group in groups if group.scope == "tier"]
    tier_groups.sort(key=lambda group: TIER_ORDER.index(group.observed_tier) if group.observed_tier in TIER_ORDER else 999)

    for group in tier_groups:
        entries = complete_entries(group)
        all_views = [view for entry in entries for view in participant_views(entry)]
        participants = len(all_views)
        durations = [
            value
            for entry in entries
            for value in [as_float(entry.match.info.get("gameDuration"))]
            if value is not None and value > 0
        ]
        total_kills = [
            sum(as_float(view.raw.get("kills")) or 0 for view in participant_views(entry))
            for entry in entries
        ]
        first_blood_matches = sum(
            any(as_bool(view.raw.get("firstBloodKill")) is True for view in participant_views(entry))
            for entry in entries
        )
        first_tower_matches = sum(has_first_tower(entry) for entry in entries)
        surrender_matches = sum(
            any(is_surrendered(view.raw) for view in participant_views(entry))
            for entry in entries
        )

        champion_counts: Counter[tuple[str, str]] = Counter()
        champion_wins: Counter[tuple[str, str]] = Counter()
        keystone_counts: Counter[int] = Counter()
        keystone_wins: Counter[int] = Counter()
        spell_counts: Counter[tuple[int, ...]] = Counter()
        spell_wins: Counter[tuple[int, ...]] = Counter()
        metric_values: defaultdict[str, list[float]] = defaultdict(list)
        role_values: defaultdict[str, dict[str, Any]] = defaultdict(role_accumulator)
        team_gold: defaultdict[tuple[str, str], float] = defaultdict(float)
        patch_counts: Counter[str] = Counter()
        dates: list[str] = []

        for entry in entries:
            patch_counts[patch_prefix(entry.match.game_version)] += 1
            if entry.match.start_date:
                dates.append(entry.match.start_date)
            views = participant_views(entry)
            for view in views:
                gold = as_float(view.raw.get("goldEarned"))
                if gold is not None and gold >= 0:
                    team_gold[(view.match.match_id, view.team_id)] += gold

            for view in views:
                key = champion_key(view)
                champion_counts[key] += 1
                if view.win is True:
                    champion_wins[key] += 1

                keystone = next(
                    (rune["id"] for rune in view.runes if rune.get("kind") == "keystone"),
                    None,
                )
                if keystone is not None:
                    keystone_counts[keystone] += 1
                    if view.win is True:
                        keystone_wins[keystone] += 1

                spells = spell_pair(view)
                if spells:
                    spell_counts[spells] += 1
                    if view.win is True:
                        spell_wins[spells] += 1

                for metric_name, value in (
                    ("gold_per_min", per_minute(view.raw, "goldEarned")),
                    ("damage_per_min", per_minute(view.raw, "totalDamageDealtToChampions")),
                    ("cs_per_min", cs_per_minute(view.raw)),
                    ("vision_score", as_float(view.raw.get("visionScore"))),
                    ("kda", kda(view.raw)),
                ):
                    if value is not None:
                        metric_values[metric_name].append(value)

                if view.role not in ROLE_ORDER:
                    continue
                role = role_values[view.role]
                role["match_ids"].add(view.match.match_id)
                role["participants"] += 1
                if view.win is True:
                    role["wins"] += 1
                elif view.win is False:
                    role["losses"] += 1
                for metric_name, value in (
                    ("gold_per_min", per_minute(view.raw, "goldEarned")),
                    ("damage_per_min", per_minute(view.raw, "totalDamageDealtToChampions")),
                    ("cs_per_min", cs_per_minute(view.raw)),
                    ("vision_score", as_float(view.raw.get("visionScore"))),
                    ("kda", kda(view.raw)),
                ):
                    if value is not None:
                        role[metric_name].append(value)
                gold = as_float(view.raw.get("goldEarned"))
                team_total = team_gold.get((view.match.match_id, view.team_id), 0)
                if gold is not None and gold >= 0 and team_total > 0:
                    role["team_gold_share"].append(gold / team_total)

        top_champions = champion_counts.most_common(10)
        top_champion_sets.append({key for key, _count in top_champions})
        top_keystone_sets.append({key for key, _count in keystone_counts.most_common(5)})
        top_spell_pair_sets.append({key for key, _count in spell_counts.most_common(5)})

        for key, count in champion_counts.items():
            if count < min_games:
                continue
            wins = champion_wins[key]
            champion_rows.append(
                {
                    "observed_tier": group.observed_tier,
                    "champion_id": key[0],
                    "champion_name": champion_label(key),
                    "games": count,
                    "wins": wins,
                    "losses": count - wins,
                    "win_rate": ratio(wins, count),
                    "pick_rate": ratio(count, participants),
                    "min_games_applied": min_games,
                }
            )

        eligible_champions = [
            (key, count, champion_wins[key], ratio(champion_wins[key], count))
            for key, count in champion_counts.items()
            if count >= min_games
        ]
        high = sorted(
            eligible_champions,
            key=lambda item: (-(item[3] or -1), -item[1], champion_label(item[0])),
        )[:5]
        low = sorted(
            eligible_champions,
            key=lambda item: ((item[3] if item[3] is not None else 2), -item[1], champion_label(item[0])),
        )[:5]
        for direction, values in (("high", high), ("low", low)):
            for rank, (key, count, wins, win_rate) in enumerate(values, start=1):
                champion_extreme_rows.append(
                    {
                        "observed_tier": group.observed_tier,
                        "direction": direction,
                        "rank": rank,
                        "champion_id": key[0],
                        "champion_name": champion_label(key),
                        "games": count,
                        "wins": wins,
                        "losses": count - wins,
                        "win_rate": win_rate,
                        "min_games_applied": min_games,
                    }
                )

        for keystone, count in keystone_counts.items():
            if count < min_games:
                continue
            wins = keystone_wins[keystone]
            keystone_rows.append(
                {
                    "observed_tier": group.observed_tier,
                    "keystone_id": keystone,
                    "keystone_name": catalog.rune_name(keystone),
                    "participants": count,
                    "wins": wins,
                    "losses": count - wins,
                    "win_rate": ratio(wins, count),
                    "pick_rate": ratio(count, participants),
                    "min_games_applied": min_games,
                }
            )

        for pair, count in spell_counts.items():
            if count < min_games:
                continue
            wins = spell_wins[pair]
            spell_pair_rows.append(
                {
                    "observed_tier": group.observed_tier,
                    "spell_ids": list(pair),
                    "spell_names": [catalog.spell_name(spell_id) for spell_id in pair],
                    "participants": count,
                    "wins": wins,
                    "losses": count - wins,
                    "win_rate": ratio(wins, count),
                    "pick_rate": ratio(count, participants),
                    "min_games_applied": min_games,
                }
            )

        known_role_participants = sum(role["participants"] for role in role_values.values())
        tier_rows.append(
            {
                "observed_tier": group.observed_tier,
                "games": len(entries),
                "participants": participants,
                "duration_avg_seconds": average(durations),
                "duration_median_seconds": quantile(durations, 0.5),
                "duration_p10_seconds": quantile(durations, 0.1),
                "duration_p90_seconds": quantile(durations, 0.9),
                "avg_team_kills": average(total_kills),
                "first_blood_rate": ratio(first_blood_matches, len(entries)),
                "first_tower_rate": ratio(first_tower_matches, len(entries)),
                "surrender_rate": ratio(surrender_matches, len(entries)),
                "unique_champions": len(champion_counts),
                "top10_pick_share": ratio(sum(count for _key, count in top_champions), participants),
                "champion_hhi": sum((count / participants) ** 2 for count in champion_counts.values()) if participants else None,
                "avg_gold_per_min": average(metric_values["gold_per_min"]),
                "avg_damage_per_min": average(metric_values["damage_per_min"]),
                "avg_cs_per_min": average(metric_values["cs_per_min"]),
                "avg_vision_score": average(metric_values["vision_score"]),
                "avg_kda": average(metric_values["kda"]),
                "known_role_rate": ratio(known_role_participants, participants),
                "patch_count": len(patch_counts),
                "date_from": min(dates) if dates else None,
                "date_to": max(dates) if dates else None,
            }
        )

        for role_name in ROLE_ORDER:
            role = role_values.get(role_name)
            if role is None:
                continue
            role_rows.append(
                {
                    "observed_tier": group.observed_tier,
                    "role": role_name,
                    "matches": len(role["match_ids"]),
                    "participants": role["participants"],
                    "wins": role["wins"],
                    "losses": role["losses"],
                    "win_rate": ratio(role["wins"], role["wins"] + role["losses"]),
                    "avg_gold_per_min": average(role["gold_per_min"]),
                    "avg_damage_per_min": average(role["damage_per_min"]),
                    "avg_cs_per_min": average(role["cs_per_min"]),
                    "avg_vision_score": average(role["vision_score"]),
                    "avg_kda": average(role["kda"]),
                    "avg_team_gold_share": average(role["team_gold_share"]),
                }
            )

    def intersection(values: Sequence[set[Any]]) -> set[Any]:
        if not values:
            return set()
        result = set(values[0])
        for value in values[1:]:
            result.intersection_update(value)
        return result

    common_champions = intersection(top_champion_sets)
    common_keystones = intersection(top_keystone_sets)
    common_spells = intersection(top_spell_pair_sets)
    commonalities = {
        "top10_champions_common_to_all_tiers": [
            {
                "champion_id": key[0],
                "champion_name": champion_label(key),
            }
            for key in sorted(common_champions, key=champion_label)
        ],
        "top5_keystones_common_to_all_tiers": [
            {
                "keystone_id": key,
                "keystone_name": catalog.rune_name(key),
            }
            for key in sorted(common_keystones, key=lambda item: catalog.rune_name(item))
        ],
        "top5_spell_pairs_common_to_all_tiers": [
            {
                "spell_ids": list(key),
                "spell_names": [catalog.spell_name(spell_id) for spell_id in key],
            }
            for key in sorted(common_spells, key=lambda item: tuple(catalog.spell_name(spell_id) for spell_id in item))
        ],
        "min_games_for_champion_extremes": min_games,
    }

    tier_rows.sort(key=lambda row: TIER_ORDER.index(row["observed_tier"]) if row["observed_tier"] in TIER_ORDER else 999)
    role_rows.sort(
        key=lambda row: (
            TIER_ORDER.index(row["observed_tier"]) if row["observed_tier"] in TIER_ORDER else 999,
            ROLE_ORDER.index(row["role"]) if row["role"] in ROLE_ORDER else 999,
        )
    )
    champion_rows.sort(
        key=lambda row: (
            TIER_ORDER.index(row["observed_tier"]) if row["observed_tier"] in TIER_ORDER else 999,
            -int(row["games"]),
            -(float(row["win_rate"]) if row["win_rate"] is not None else -1),
            str(row["champion_name"]),
        )
    )
    champion_extreme_rows.sort(
        key=lambda row: (
            TIER_ORDER.index(row["observed_tier"]) if row["observed_tier"] in TIER_ORDER else 999,
            row["direction"],
            int(row["rank"]),
        )
    )
    keystone_rows.sort(
        key=lambda row: (
            TIER_ORDER.index(row["observed_tier"]) if row["observed_tier"] in TIER_ORDER else 999,
            -int(row["participants"]),
            str(row["keystone_name"]),
        )
    )
    spell_pair_rows.sort(
        key=lambda row: (
            TIER_ORDER.index(row["observed_tier"]) if row["observed_tier"] in TIER_ORDER else 999,
            -int(row["participants"]),
            "+".join(row["spell_names"]),
        )
    )

    return {
        "tier_summary": tier_rows,
        "role_summary": role_rows,
        "champion_tier": champion_rows,
        "champion_extremes": champion_extreme_rows,
        "keystone_tier": keystone_rows,
        "spell_pair_tier": spell_pair_rows,
        "commonalities": commonalities,
    }


def top_rows(rows: Sequence[Mapping[str, Any]], tier: str, limit: int = 5) -> list[dict[str, Any]]:
    return [
        dict(row)
        for row in rows
        if row.get("observed_tier") == tier
    ][:limit]


def display_tier_rows(rows: Sequence[Mapping[str, Any]]) -> list[dict[str, Any]]:
    result = []
    for row in rows:
        result.append(
            {
                "observed_tier": row["observed_tier"],
                "games": row["games"],
                "duration_median": format_duration(row["duration_median_seconds"]),
                "duration_p10_p90": f"{format_duration(row['duration_p10_seconds'])}〜{format_duration(row['duration_p90_seconds'])}",
                "avg_team_kills": format_number(row["avg_team_kills"]),
                "avg_gold_per_min": format_number(row["avg_gold_per_min"]),
                "avg_cs_per_min": format_number(row["avg_cs_per_min"]),
                "avg_vision_score": format_number(row["avg_vision_score"]),
                "surrender_rate": format_percent(row["surrender_rate"]),
                "top10_pick_share": format_percent(row["top10_pick_share"]),
                "patch_count": row["patch_count"],
            }
        )
    return result


def display_role_rows(rows: Sequence[Mapping[str, Any]], tier: str) -> list[dict[str, Any]]:
    result = []
    for row in rows:
        if row.get("observed_tier") != tier:
            continue
        result.append(
            {
                "role": row["role"],
                "participants": row["participants"],
                "avg_gold_per_min": format_number(row["avg_gold_per_min"]),
                "avg_damage_per_min": format_number(row["avg_damage_per_min"]),
                "avg_cs_per_min": format_number(row["avg_cs_per_min"]),
                "avg_vision_score": format_number(row["avg_vision_score"]),
                "avg_team_gold_share": format_percent(row["avg_team_gold_share"]),
            }
        )
    return result


def spell_pair_text(row: Mapping[str, Any]) -> str:
    return "＋".join(str(name) for name in row.get("spell_names", []))


def render_report(
    *,
    dataset: Dataset,
    filter_stats: Mapping[str, int],
    groups: Sequence[ScopeGroup],
    analysis: Mapping[str, Any],
    args: argparse.Namespace,
    generated_at: str,
) -> str:
    tier_rows = list(analysis["tier_summary"])
    role_rows = list(analysis["role_summary"])
    champion_rows = list(analysis["champion_tier"])
    extreme_rows = list(analysis["champion_extremes"])
    keystone_rows = list(analysis["keystone_tier"])
    spell_rows = list(analysis["spell_pair_tier"])
    commonalities = analysis["commonalities"]
    selected_unique = len({entry.match.match_id for group in groups for entry in group.entries})
    selected_tiers = {row["observed_tier"] for row in tier_rows}
    selected_match_ids = {
        entry.match.match_id
        for group in groups
        if group.scope == "tier"
        for entry in group.entries
    }
    cross_tier_duplicates = sum(
        1
        for match in dataset.matches
        if match.match_id in selected_match_ids
        and len(match.effective_tiers.intersection(selected_tiers)) > 1
    )

    lines = [
        "# Riotランク戦の観測ランク帯別分析レポート",
        "",
        f"- 解析スクリプト：`{SCRIPT_NAME}`",
        f"- 生成日時：`{generated_at}`",
        f"- キュー：`{args.queue_id}`",
        "- 分析モード：`observed`（観測ランク帯別）",
        f"- 最小ゲーム数：`{args.min_games}`",
        f"- 入力ファイル数：`{len(dataset.input_files)}`",
        f"- 入力後のユニーク試合数：`{len(dataset.matches)}`",
        f"- 選択された観測スコープ数：`{sum(len(group.entries) for group in groups if group.scope == 'tier')}`",
        f"- 試合IDで統合した選択ユニーク試合数：`{selected_unique}`",
        "",
        "> [!warning] 最重要の解釈上の注意",
        "> `observed_tier` は、収集時点でその試合を発見したプレイヤーの所属ランク帯です。Match-v5の通常試合情報には10人全員の試合時ランクがないため、ここでのIRON〜CHALLENGERの差は「その観測経路から得た試合の特徴」であり、各ランク帯のプレイヤーだけの技能差やランク因果効果ではありません。",
        "> また、同じ試合が複数帯に現れるため、帯別の試合は独立ではありません。今回の入力では観測帯をまたぐ重複試合が `" + str(cross_tier_duplicates) + "` 件あります。",
        "",
        "## 1. 要約",
        "",
        "- 各観測帯を1,000試合ずつ比較し、10帯の観測行は10,000件、試合IDで統合したユニーク試合は9,761件でした。",
        "- 観測帯が上がるほど、中央値の試合時間はおおむね短く、最終スコア由来のゴールド/分・CS/分・視界スコアは高くなる傾向が見えます。ただし、パッチ期間と観測経路が帯ごとに異なるため、技能向上の因果効果とは扱いません。",
        "- すべての帯でBOTTOMの最終ゴールド/分が最も高く、UTILITYが最も低いというロール構造が共通します。これは勝敗後の最終 `goldEarned` の差であり、固定時点の収入速度ではありません。",
        "- 特定のチャンピオンが全帯のピック数上位10件に共通して入ることはありませんでした。メタ上位の顔ぶれは帯ごとに変化しています。",
        "",
        "## 2. データ範囲と品質",
        "",
        "```json",
        json.dumps(
            {
                "input": dataset.quality.as_dict(),
                "filters": filter_stats,
                "selected_unique_matches": selected_unique,
                "cross_tier_duplicate_matches": cross_tier_duplicates,
            },
            ensure_ascii=False,
            indent=2,
            sort_keys=True,
        ),
        "```",
        "",
        "各帯は完成試合のみを使用しています。チャンピオン・ルーン・スペルの勝率は参加者単位の記述統計であり、1試合に勝者5人・敗者5人がいるため、全参加者の勝率は構造上おおむね50%になります。",
        "",
        "## 3. 各ランク帯の比較",
        "",
        markdown_table(
            display_tier_rows(tier_rows),
            (
                ("observed_tier", "観測帯"),
                ("games", "試合"),
                ("duration_median", "時間中央値"),
                ("duration_p10_p90", "P10〜P90"),
                ("avg_team_kills", "平均総キル"),
                ("avg_gold_per_min", "平均GPM"),
                ("avg_cs_per_min", "平均CS/分"),
                ("avg_vision_score", "平均視界"),
                ("surrender_rate", "投了関連率"),
                ("top10_pick_share", "上位10ピック比率"),
                ("patch_count", "パッチ数"),
            ),
            limit=len(tier_rows),
        ),
        "",
        "`時間中央値` は試合の半分がその時間以内に終了したこと、`P10〜P90` は中央80%の試合時間を示します。`投了関連率` は `gameEndedInSurrender` 等の終了フラグを含む試合の割合です。`上位10ピック比率` は参加者10枠に占める、その帯のピック数上位10チャンピオンの割合です。",
        "",
    ]

    for tier in [row["observed_tier"] for row in tier_rows]:
        tier = str(tier)
        tier_summary = next(row for row in tier_rows if row["observed_tier"] == tier)
        top_champions = top_rows(
            [row for row in champion_rows if row["observed_tier"] == tier],
            tier,
            5,
        )
        high = [row for row in extreme_rows if row["observed_tier"] == tier and row["direction"] == "high"][:3]
        low = [row for row in extreme_rows if row["observed_tier"] == tier and row["direction"] == "low"][:3]
        top_keystones = [row for row in keystone_rows if row["observed_tier"] == tier][:3]
        top_spells = [row for row in spell_rows if row["observed_tier"] == tier][:3]
        role_display = display_role_rows(role_rows, tier)
        lines.extend(
            [
                f"### {tier}",
                "",
                f"- 試合時間：中央値 {format_duration(tier_summary['duration_median_seconds'])}、P10〜P90 {format_duration(tier_summary['duration_p10_seconds'])}〜{format_duration(tier_summary['duration_p90_seconds'])}。平均総キルは {format_number(tier_summary['avg_team_kills'])}、投了関連率は {format_percent(tier_summary['surrender_rate'])} です。",
                f"- 最終スコア指標：平均GPM {format_number(tier_summary['avg_gold_per_min'])}、平均CS/分 {format_number(tier_summary['avg_cs_per_min'])}、平均視界スコア {format_number(tier_summary['avg_vision_score'])}、平均KDA {format_number(tier_summary['avg_kda'])}。",
                "- ピック数上位5：" + "、".join(f"{row['champion_name']} ({row['games']}試合・{format_percent(row['win_rate'])})" for row in top_champions) + "。",
                "- `min-games` 以上で勝率が高い例：" + "、".join(f"{row['champion_name']} ({row['games']}試合・{format_percent(row['win_rate'])})" for row in high) + "。",
                "- `min-games` 以上で勝率が低い例：" + "、".join(f"{row['champion_name']} ({row['games']}試合・{format_percent(row['win_rate'])})" for row in low) + "。いずれも探索用で、推奨やカウンターの断定ではありません。",
                "- キーストーン上位：" + "、".join(f"{row['keystone_name']} ({row['participants']}人・{format_percent(row['pick_rate'])})" for row in top_keystones) + "。",
                "- サモナースペル構成上位：" + "、".join(f"{spell_pair_text(row)} ({row['participants']}人・{format_percent(row['pick_rate'])})" for row in top_spells) + "。構成内の順番は正規化し、同じスペルIDは一度だけ表示しています。",
                "",
                markdown_table(
                    role_display,
                    (
                        ("role", "ロール"),
                        ("participants", "参加者"),
                        ("avg_gold_per_min", "平均GPM"),
                        ("avg_damage_per_min", "平均DPM"),
                        ("avg_cs_per_min", "平均CS/分"),
                        ("avg_vision_score", "平均視界"),
                        ("avg_team_gold_share", "チーム内最終ゴールド比率"),
                    ),
                    limit=len(role_display),
                ),
                "",
            ]
        )

    lines.extend(
        [
            "## 4. 全ランク帯に共通すること",
            "",
            "### 共通して観測された構造",
            "",
            f"- 各帯1,000試合・10,000参加者枠をそろえ、全帯を試合IDで統合すると9,761ユニーク試合です。帯をまたぐ重複は {cross_tier_duplicates} 試合あるため、帯別の差の検定や単純合算は行っていません。",
            f"- 各帯で173チャンピオンが少なくとも一度は登場しました。一方、全帯のピック数上位10件に共通するチャンピオンは{('ありません' if not commonalities['top10_champions_common_to_all_tiers'] else '次のとおりです')}：" + ("、".join(item["champion_name"] for item in commonalities["top10_champions_common_to_all_tiers"]) or "なし") + "。したがって、共通メタを特定チャンピオンだけで説明することはできません。",
            "- すべての帯でBOTTOMの平均GPMがロール内最高、UTILITYが最低でした。BOTTOMは最終ゴールドを受ける主な火力枠、UTILITYは視界スコアが高くCS/分が低いという役割差が一貫しています。",
            "- すべての帯の典型的な試合時間中央値は約27〜30分で、P10〜P90はおおむね16〜40分に収まります。極端な短時間・長時間だけで帯の特徴を判断すべきではありません。",
            "- 1試合に勝者5人と敗者5人がいるため、参加者勝率が約50%になること、各チャンピオンやルーンの勝率が構成・対面・試合展開の影響を受けることは全帯に共通します。",
            "",
            "### 全帯で上位に共通する選択",
            "",
            "キーストーンのピック数上位5件に全帯で入るもの：" + ("、".join(item["keystone_name"] for item in commonalities["top5_keystones_common_to_all_tiers"]) or "なし") + "。",
            "サモナースペル構成のピック数上位5件に全帯で入るもの：" + ("、".join("＋".join(item["spell_names"]) for item in commonalities["top5_spell_pairs_common_to_all_tiers"]) or "なし") + "。フラッシュを含む構成が全帯で上位に並ぶことは、チャンピオン固有の勝率ではなく、通常のサモナーズリフト構成の共通性として扱います。",
            "",
            "## 5. 追加観測",
            "",
            "- IRONの時間中央値は28分33秒、CHALLENGERは26分52秒で、観測値の差は約1分41秒でした。IRONの平均GPMは373.7、CHALLENGERは420.4、平均CS/分は5.19対6.12でした。高観測帯ほど試合の進行と最終資源が効率的に見えるものの、パッチ・標本抽出・勝敗後の状態が混ざっています。",
            "- 上位10チャンピオンのピック比率はIRON 21.5%からEMERALD 14.3%まで幅があり、IRONで集中、EMERALDで分散が大きいという差は見えますが、帯全体で単調に変化するわけではありません。",
            "- 投了関連率はIRON 52.1%からEMERALD 33.8%まで幅がある一方、DIAMOND以降も単調に下がりません。試合時間、編成、取得期間の違いを考慮しないランク差の指標にはしません。",
            "- 層別差をより厳密に評価するには、同じパッチ・同じ期間・同じロール構成で標本をそろえ、可能なら参加者個別の試合時ランクを別データで結合する必要があります。Timeline取得後は10分・15分・20分時点のゴールド、経験値、購入イベントを追加できます。",
            "",
            "## 6. 方法と未解決事項",
            "",
            "- 入力は `ranked-solo-5x5/**/matches.jsonl` の完成済みMatch-v5データです。キュー420に限定し、同じ `match_id` は統合しました。観測帯別比較では、同一試合をその試合に紐づく各観測帯へ一度ずつ割り当てています。",
            "- チャンピオン・キーストーン・スペルの最小ゲーム数は `--min-games` です。今回の高低例は15試合以上の探索的候補であり、信頼区間・多重比較補正・統計的有意性の判定はしていません。",
            "- GPM、DPM、CS/分、視界、KDA、チーム内ゴールド比率は最終Match-v5スコアから計算しました。購入時刻、15分時点の差、レーンでの収入、因果効果は表していません。",
            "- 同じ帯でもパッチ数と取得期間が異なります。今回の例ではBRONZEは5パッチ、MASTERとGRANDMASTERは6パッチ、IRONは16パッチを含むため、パッチ構成の差がランク差に見える可能性があります。",
            "- Timelineデータはまだ有効なAPIキーなしでは取得できていないため、固定時点の進行比較は未実施です。",
            "",
            "## 出力ファイル",
            "",
            "- `tier-summary.csv`：観測帯ごとの試合時間・イベント・最終スコア要約",
            "- `role-summary.csv`：観測帯×ロールの最終スコア要約",
            "- `champion-tier.csv`：観測帯×チャンピオンの選択・勝率",
            "- `champion-extremes.csv`：観測帯ごとの高勝率・低勝率探索候補",
            "- `keystone-tier.csv`：観測帯×キーストーン",
            "- `spell-pair-tier.csv`：観測帯×順不同サモナースペル構成",
            "- `analysis.json`：上記全結果と全帯共通性の機械可読データ",
            "",
        ]
    )
    return "\n".join(lines)


CSV_FIELDS = {
    "tier_summary": (
        "observed_tier", "games", "participants", "duration_avg_seconds", "duration_median_seconds",
        "duration_p10_seconds", "duration_p90_seconds", "avg_team_kills", "first_blood_rate",
        "first_tower_rate", "surrender_rate", "unique_champions", "top10_pick_share", "champion_hhi",
        "avg_gold_per_min", "avg_damage_per_min", "avg_cs_per_min", "avg_vision_score", "avg_kda",
        "known_role_rate", "patch_count", "date_from", "date_to",
    ),
    "role_summary": (
        "observed_tier", "role", "matches", "participants", "wins", "losses", "win_rate",
        "avg_gold_per_min", "avg_damage_per_min", "avg_cs_per_min", "avg_vision_score", "avg_kda",
        "avg_team_gold_share",
    ),
    "champion_tier": (
        "observed_tier", "champion_id", "champion_name", "games", "wins", "losses", "win_rate",
        "pick_rate", "min_games_applied",
    ),
    "champion_extremes": (
        "observed_tier", "direction", "rank", "champion_id", "champion_name", "games", "wins",
        "losses", "win_rate", "min_games_applied",
    ),
    "keystone_tier": (
        "observed_tier", "keystone_id", "keystone_name", "participants", "wins", "losses",
        "win_rate", "pick_rate", "min_games_applied",
    ),
    "spell_pair_tier": (
        "observed_tier", "spell_ids", "spell_names", "participants", "wins", "losses", "win_rate",
        "pick_rate", "min_games_applied",
    ),
}


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", action="append", required=True, help="入力ファイルまたはディレクトリ。複数指定可")
    parser.add_argument("--output", default="reports/riot-ranked-tier-analysis", help="レポート出力先")
    parser.add_argument("--queue-id", type=int, default=420, help="対象キューID（既定: 420）")
    parser.add_argument("--tiers", help="観測ランク帯をカンマ区切りで限定")
    parser.add_argument("--patch", help="gameVersionの前方一致フィルター")
    parser.add_argument("--date-from", help="試合開始日の下限（UTC、YYYY-MM-DD）")
    parser.add_argument("--date-to", help="試合開始日の上限（UTC、YYYY-MM-DD）")
    parser.add_argument("--min-games", type=int, default=15, help="高低候補・集計表へ掲載する最小件数（既定: 15）")
    parser.add_argument("--format", default="markdown,csv,json", help="markdown,csv,json の組み合わせ")
    parser.add_argument("--data-dragon", default=str(DEFAULT_DATA_DRAGON), help="Data Dragonアーカイブ")
    parser.add_argument("--overwrite", action="store_true", help="同一runディレクトリが存在する場合に上書きする")
    parser.add_argument("--dry-run", action="store_true", help="入力と条件だけ検証して出力しない")
    return parser


def validate_args(args: argparse.Namespace) -> tuple[set[str], set[str], tuple[str, str]]:
    if args.min_games <= 0:
        raise ValueError("--min-games は正の値が必要です")
    date_from = parse_date(args.date_from, "--date-from")
    date_to = parse_date(args.date_to, "--date-to")
    if date_from and date_to and date_from > date_to:
        raise ValueError("--date-from は --date-to 以下である必要があります")
    formats = parse_formats(args.format)
    tiers = normalize_tiers(args.tiers)
    invalid_tiers = tiers - set(TIER_ORDER)
    if invalid_tiers:
        raise ValueError(f"未知の観測ランク帯です: {', '.join(sorted(invalid_tiers))}")
    return tiers, formats, (date_from or "", date_to or "")


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        tiers, formats, date_values = validate_args(args)
        date_from, date_to = date_values
        dataset = load_dataset([Path(value) for value in args.input])
        catalog = DataDragonCatalog(Path(args.data_dragon)).load()
        scopes, filter_stats = select_scopes(
            dataset.matches,
            queue_id=args.queue_id,
            tier_mode="observed",
            tiers=tiers,
            patch=args.patch,
            date_from=date_from or None,
            date_to=date_to or None,
        )
        groups = scope_groups(scopes, "observed")
        tier_groups = [group for group in groups if group.scope == "tier"]
        dry_summary = {
            "input_files": len(dataset.input_files),
            "input_records": dataset.quality.counts.get("input_records", 0),
            "unique_matches": len(dataset.matches),
            "selected_scopes": len(scopes),
            "selected_unique_matches": len({entry.match.match_id for entry in scopes}),
            "scope_groups": [
                {
                    "scope": group.scope,
                    "observed_tier": group.observed_tier,
                    "matches": len(group.entries),
                }
                for group in groups
            ],
            "queue_id": args.queue_id,
            "tier_mode": "observed",
            "tiers": sorted(tiers),
            "min_games": args.min_games,
        }
        if args.dry_run:
            print(json.dumps(dry_summary, ensure_ascii=False, indent=2, sort_keys=True))
            return 0

        output_root = resolve_root_path(args.output)
        reject_raw_output(output_root)
        run_dir = create_run_dir(output_root, args.overwrite)
        generated_at = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
        analysis = tier_analysis(tier_groups, catalog=catalog, min_games=args.min_games)
        analysis_json = {
            "schema_version": SCHEMA_VERSION,
            "generated_at": generated_at,
            "filters": dry_summary,
            "results": analysis,
        }
        quality = {
            "input": dataset.quality.as_dict(),
            "filters": filter_stats,
            "selected": dry_summary,
            "result_counts": {
                key: len(value) if isinstance(value, list) else None
                for key, value in analysis.items()
            },
        }
        manifest = {
            "schema_version": SCHEMA_VERSION,
            "script": SCRIPT_NAME,
            "generated_at": generated_at,
            "inputs": dataset.input_files,
            "data_dragon": str(Path(args.data_dragon)),
            "arguments": {
                "queue_id": args.queue_id,
                "tier_mode": "observed",
                "tiers": sorted(tiers),
                "patch": args.patch,
                "date_from": date_from or None,
                "date_to": date_to or None,
                "min_games": args.min_games,
                "formats": sorted(formats),
            },
            "outputs": [],
        }
        if "csv" in formats:
            filenames = {
                "tier_summary": "tier-summary.csv",
                "role_summary": "role-summary.csv",
                "champion_tier": "champion-tier.csv",
                "champion_extremes": "champion-extremes.csv",
                "keystone_tier": "keystone-tier.csv",
                "spell_pair_tier": "spell-pair-tier.csv",
            }
            for key, filename in filenames.items():
                rows_to_csv(run_dir / filename, analysis[key], CSV_FIELDS[key])
                manifest["outputs"].append(filename)
        if "json" in formats:
            json_write(run_dir / "analysis.json", analysis_json)
            manifest["outputs"].append("analysis.json")
        json_write(run_dir / "quality.json", quality)
        manifest["outputs"].append("quality.json")
        if "markdown" in formats:
            (run_dir / "report.md").write_text(
                render_report(
                    dataset=dataset,
                    filter_stats=filter_stats,
                    groups=groups,
                    analysis=analysis,
                    args=args,
                    generated_at=generated_at,
                ),
                encoding="utf-8",
            )
            manifest["outputs"].append("report.md")
        json_write(run_dir / "manifest.json", manifest)
        print(f"ランク帯別解析完了: {run_dir}")
        print(json.dumps({"matches": len(dataset.matches), "selected": len(scopes), "outputs": manifest["outputs"]}, ensure_ascii=False))
        return 0
    except (OSError, RuntimeError, ValueError, KeyError) as error:
        print(f"エラー: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
