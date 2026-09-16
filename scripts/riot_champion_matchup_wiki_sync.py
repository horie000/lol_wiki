#!/usr/bin/env python3
"""実測の味方コンボ・同ロール対面を集計し、チャンピオンentityへ同期する。"""

from __future__ import annotations

import argparse
import csv
import json
import math
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Optional, Sequence
from zoneinfo import ZoneInfo

from riot_match_analysis import (
    as_int,
    json_write,
    load_dataset,
    participant_views,
    patch_prefix,
    ratio,
    rows_to_csv,
    select_scopes,
)


ROOT = Path(__file__).resolve().parents[1]
SCRIPT_NAME = "scripts/riot_champion_matchup_wiki_sync.py"
SCHEMA_VERSION = 2
DEFAULT_SELECTION_LIMIT = 3
DEFAULT_ENTITY_ROOT = ROOT / "wiki/entities/champions"
DEFAULT_OUTPUT_ROOT = ROOT / "reports/riot-champion-matchups"
SOURCE_REF = "[[wiki/sources/src-2026-09-15-riot-ranked-match-champion-matchups]]"
SYNTHESIS_REF = "[[wiki/syntheses/champion-combo-counter-ranked-matches|実測コンボ・カウンターピック分析]]"
START_MARKER = "<!-- champion-matchup-analysis:start -->"
END_MARKER = "<!-- champion-matchup-analysis:end -->"
Z95 = 1.959963984540054


def resolve_path(value: str | Path) -> Path:
    path = Path(value).expanduser()
    return path if path.is_absolute() else ROOT / path


def parse_frontmatter_value(text: str, key: str) -> Optional[str]:
    match = re.search(rf"^{re.escape(key)}:\s*(.+?)\s*$", text, flags=re.MULTILINE)
    if not match:
        return None
    value = match.group(1).strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {'"', "'"}:
        value = value[1:-1]
    return value


def entity_catalog(entity_root: Path) -> dict[str, dict[str, str | Path]]:
    result: dict[str, dict[str, str | Path]] = {}
    for path in sorted(entity_root.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        champion_key = parse_frontmatter_value(text, "champion_key")
        champion_id = parse_frontmatter_value(text, "champion_id")
        title = parse_frontmatter_value(text, "title") or path.stem
        if not champion_key or not champion_id:
            continue
        if champion_key in result:
            raise ValueError(f"champion_keyが重複しています: {champion_key}")
        result[champion_key] = {
            "path": path,
            "champion_id": champion_id,
            "title": title,
            "slug": path.stem,
        }
    if not result:
        raise ValueError(f"チャンピオンentityを検出できません: {entity_root}")
    return result


def load_analysis_snapshot(path: Path) -> dict[str, Any]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, Mapping):
        raise ValueError(f"analysis.jsonのルートがオブジェクトではありません: {path}")
    rows = payload.get("candidates")
    target_games = payload.get("target_games_by_role")
    target_names = payload.get("target_names")
    if not isinstance(rows, list) or not isinstance(target_games, Mapping) or not isinstance(target_names, Mapping):
        raise ValueError("analysis.jsonにcandidates、target_games_by_role、target_namesが必要です")
    quality_path = path.parent / "quality.json"
    if not quality_path.exists():
        raise ValueError(f"analysis.jsonに対応するquality.jsonがありません: {quality_path}")
    quality = json.loads(quality_path.read_text(encoding="utf-8"))
    if not isinstance(quality, Mapping) or not isinstance(quality.get("summary"), Mapping):
        raise ValueError(f"quality.jsonにsummaryがありません: {quality_path}")
    summary = dict(quality["summary"])
    target_counts: Counter[tuple[str, str]] = Counter()
    for raw_key, raw_count in target_games.items():
        target_id, separator, role = str(raw_key).partition(":")
        if not separator or not target_id or not role:
            raise ValueError(f"target_games_by_roleのキーが不正です: {raw_key}")
        target_counts[(target_id, role)] = int(raw_count)
    run_rel = str(summary.get("run_dir") or path.parent.relative_to(ROOT).as_posix())
    required_summary = ("complete_matches", "input_files", "input_records", "unique_matches")
    missing = [key for key in required_summary if key not in summary]
    if missing:
        raise ValueError(f"quality.jsonのsummaryに必要な値がありません: {', '.join(missing)}")
    return {
        "analysis": payload,
        "quality": quality,
        "rows": [dict(row) for row in rows if isinstance(row, Mapping)],
        "target_counts": target_counts,
        "target_names": {str(key): str(value) for key, value in target_names.items()},
        "summary": summary,
        "run_rel": run_rel,
        "generated_at": str(payload.get("generated_at") or ""),
    }


def wilson_interval(wins: int, games: int) -> tuple[Optional[float], Optional[float]]:
    if games <= 0:
        return None, None
    p = wins / games
    z2 = Z95 * Z95
    denominator = 1 + z2 / games
    center = (p + z2 / (2 * games)) / denominator
    margin = Z95 * math.sqrt((p * (1 - p) / games) + (z2 / (4 * games * games))) / denominator
    return max(0.0, center - margin), min(1.0, center + margin)


def row_key(target: Any, related: Any, relation: str) -> tuple[str, str, str, str, str, str]:
    target_id = str(target.champion_id or "")
    target_name = str(target.champion_name or target_id)
    related_id = str(related.champion_id or "")
    related_name = str(related.champion_name or related_id)
    return (target_id, target_name, target.role, related_id, related_name, related.role)


def aggregate_candidates(scopes: Sequence[Any], min_games: int) -> tuple[list[dict[str, Any]], Counter[tuple[str, str]], dict[str, str]]:
    ally_values: defaultdict[tuple[str, str, str, str, str, str], list[bool]] = defaultdict(list)
    opponent_values: defaultdict[tuple[str, str, str, str, str, str], list[bool]] = defaultdict(list)
    target_counts: Counter[tuple[str, str]] = Counter()
    target_names: dict[str, str] = {}
    patches: set[str] = set()
    complete_matches = 0
    for scoped in scopes:
        if not scoped.match.is_complete():
            continue
        complete_matches += 1
        patches.add(patch_prefix(scoped.match.game_version))
        views = participant_views(scoped)
        for target in views:
            if target.champion_id is None or target.role == "UNKNOWN" or target.win is None:
                continue
            target_id = str(target.champion_id)
            target_names[target_id] = target.champion_name
            target_counts[(target_id, target.role)] += 1
            for related in views:
                if related.participant_id == target.participant_id or related.champion_id is None:
                    continue
                if related.team_id == target.team_id:
                    ally_values[row_key(target, related, "ally")].append(target.win is True)
                elif related.role == target.role:
                    opponent_values[row_key(target, related, "opponent")].append(target.win is True)

    rows: list[dict[str, Any]] = []
    for relation, values in (("ally", ally_values), ("opponent", opponent_values)):
        for key, outcomes in values.items():
            if len(outcomes) < min_games:
                continue
            target_id, target_name, target_role, related_id, related_name, related_role = key
            wins = sum(outcomes)
            lower, upper = wilson_interval(wins, len(outcomes))
            rows.append(
                {
                    "scope": "overall",
                    "observed_tier": "MIXED",
                    "patch": "ALL",
                    "patch_count": len(patches),
                    "target_champion_id": target_id,
                    "target_champion_name": target_name,
                    "target_role": target_role,
                    "related_champion_id": related_id,
                    "related_champion_name": related_name,
                    "related_role": related_role,
                    "relation": relation,
                    "opponent_scope": "same-role" if relation == "opponent" else "",
                    "same_role_match": relation == "opponent",
                    "games": len(outcomes),
                    "wins": wins,
                    "losses": len(outcomes) - wins,
                    "target_win_rate": ratio(wins, len(outcomes)),
                    "pick_rate": ratio(len(outcomes), target_counts[(target_id, target_role)]),
                    "pick_rate_denominator": target_counts[(target_id, target_role)],
                    "min_games_applied": min_games,
                    "wilson_lower_95": lower,
                    "wilson_upper_95": upper,
                    "patches": sorted(patches),
                }
            )
    return rows, target_counts, target_names


def select_candidates(
    rows: Sequence[Mapping[str, Any]],
    target_counts: Counter[tuple[str, str]],
    sufficient_games: int,
    selection_limit: int = DEFAULT_SELECTION_LIMIT,
) -> dict[str, dict[str, list[dict[str, Any]]]]:
    grouped: defaultdict[tuple[str, str, str], list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        key = (str(row["target_champion_id"]), str(row["target_role"]), str(row["relation"]))
        grouped[key].append(dict(row))
    selected: defaultdict[str, dict[str, list[dict[str, Any]]]] = defaultdict(lambda: {"ally": [], "opponent": []})
    targets = sorted({key[0] for key in target_counts})
    for target_id in targets:
        roles = sorted(
            {role for candidate_id, role in target_counts if candidate_id == target_id},
            key=lambda role: (-target_counts[(target_id, role)], role),
        )
        for role in roles[:2]:
            for relation in ("ally", "opponent"):
                candidates = grouped.get((target_id, role, relation), [])
                if not candidates:
                    continue
                sufficient = [row for row in candidates if int(row["games"]) >= sufficient_games]
                pool = sufficient or candidates
                if relation == "ally":
                    ordered = sorted(
                        pool,
                        key=lambda row: (
                            -(float(row["wilson_lower_95"]) if row["wilson_lower_95"] is not None else -1),
                            -(float(row["target_win_rate"]) if row["target_win_rate"] is not None else -1),
                            -int(row["games"]),
                            str(row["related_champion_name"]),
                        ),
                    )
                else:
                    ordered = sorted(
                        pool,
                        key=lambda row: (
                            float(row["wilson_upper_95"]) if row["wilson_upper_95"] is not None else 2,
                            float(row["target_win_rate"]) if row["target_win_rate"] is not None else 2,
                            -int(row["games"]),
                            str(row["related_champion_name"]),
                        ),
                    )
                for candidate in ordered[:selection_limit]:
                    chosen = dict(candidate)
                    chosen["sufficient_sample"] = int(chosen["games"]) >= sufficient_games
                    chosen["selection_score"] = (
                        chosen["wilson_lower_95"] if relation == "ally" else chosen["wilson_upper_95"]
                    )
                    selected[target_id][relation].append(chosen)
    return dict(selected)


def percent(value: Any) -> str:
    try:
        return f"{float(value) * 100:.1f}%"
    except (TypeError, ValueError):
        return "不明"


def link_for_champion(
    champion_id: str,
    champion_name: str,
    catalog: Mapping[str, Mapping[str, str | Path]],
) -> str:
    entry = catalog.get(str(champion_id))
    if entry is None:
        return champion_name
    path = Path(entry["path"]).relative_to(ROOT).with_suffix("").as_posix()
    return f"[[{path}|{entry['title']}（{champion_name}）]]"


def sample_note(row: Mapping[str, Any], sufficient_games: int) -> str:
    games = int(row["games"])
    if games < sufficient_games:
        return f"サンプル不足（n={games}、十分性の目安{sufficient_games}未満）"
    return f"n={games}（十分性の目安を満たす）"


def build_entity_block(
    *,
    champion_id: str,
    target_counts: Counter[tuple[str, str]],
    selected: Mapping[str, Mapping[str, list[dict[str, Any]]]],
    entity_catalog_data: Mapping[str, Mapping[str, str | Path]],
    run_rel: str,
    complete_matches: int,
    input_files: int,
    input_records: int,
    unique_matches: int,
    min_games: int,
    sufficient_games: int,
    selection_limit: int,
) -> str:
    lines = [
        START_MARKER,
        "## 実測コンボ・カウンターピック",
        "",
        f"- **スナップショット：** キュー420、`tier-mode=all`、完全試合{complete_matches:,}件（入力{input_files:,}ファイル・{input_records:,}レコード、重複統合後{unique_matches:,}試合）。",
        f"- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n={min_games}以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<{sufficient_games}はサンプル不足として扱う。",
        f"- **読み方：** [[{run_rel}/champions/champion-{champion_id}|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。",
        "",
    ]
    roles = sorted(
        {role for target, role in target_counts if target == champion_id},
        key=lambda role: (-target_counts[(champion_id, role)], role),
    )[:2]
    if not roles:
        lines.append(f"- **結果：** 対象ロールの参加者数を確認できず、n={min_games}以上の実測候補を掲載できない。サンプル不足のため判断保留。")
    for role in roles:
        lines.extend([f"### {role}（対象n={target_counts[(champion_id, role)]:,}）", ""])
        ally_rows = [
            row for row in selected.get(champion_id, {}).get("ally", []) if row["target_role"] == role
        ]
        opponent_rows = [
            row for row in selected.get(champion_id, {}).get("opponent", []) if row["target_role"] == role
        ]
        ally_rows.sort(
            key=lambda row: (
                -(float(row["target_win_rate"]) if row["target_win_rate"] is not None else -1),
                -int(row["games"]),
                str(row["related_champion_name"]),
            )
        )
        opponent_rows.sort(
            key=lambda row: (
                float(row["target_win_rate"]) if row["target_win_rate"] is not None else 2,
                -int(row["games"]),
                str(row["related_champion_name"]),
            )
        )
        if not ally_rows:
            lines.append(
                f"- **高勝率コンボ候補（最大{selection_limit}件）：** n={min_games}以上の味方組み合わせなし。サンプル不足のため判断保留。"
            )
        else:
            lines.append(f"- **高勝率コンボ候補（最大{selection_limit}件）：**")
            for ally in ally_rows:
                lines.append(
                    f"  - {link_for_champion(str(ally['related_champion_id']), str(ally['related_champion_name']), entity_catalog_data)} — 対象側勝率{percent(ally['target_win_rate'])}（{ally['wins']}/{ally['games']}）、{sample_note(ally, sufficient_games)}。"
                )
        if not opponent_rows:
            lines.append(
                f"- **低勝率カウンターピック候補（最大{selection_limit}件）：** n={min_games}以上の同ロール対面なし。サンプル不足のため判断保留。"
            )
        else:
            lines.append(f"- **低勝率カウンターピック候補（最大{selection_limit}件）：**")
            for opponent in opponent_rows:
                lines.append(
                    f"  - {link_for_champion(str(opponent['related_champion_id']), str(opponent['related_champion_name']), entity_catalog_data)} — 対象側勝率{percent(opponent['target_win_rate'])}（{opponent['wins']}/{opponent['games']}）、{sample_note(opponent, sufficient_games)}。"
                )
        lines.append("")
    lines.extend(
        [
            "> [!warning] 実測値の限界",
            "> 味方ペアは同一試合・同一チームで同時に出場した組み合わせ、対面はMatch-v5の最終ロールから推定した同ロール候補である。パッチ、観測ランク帯、プレイヤー、試合展開、構成の交絡を調整していない。とくにサンプル不足の行は探索的な参考値に留める。",
            f"- **出典：** {SOURCE_REF}、{SYNTHESIS_REF}",
            END_MARKER,
            "",
        ]
    )
    return "\n".join(lines)


def add_source_and_block(text: str, block: str, updated: str = "2026-09-15") -> str:
    first = text.find("---")
    second = text.find("---", first + 3) if first >= 0 else -1
    if first < 0 or second < 0:
        raise ValueError("frontmatterがありません")
    frontmatter = text[first + 3 : second]
    if SOURCE_REF not in frontmatter:
        lines = frontmatter.splitlines()
        tag_index = next((index for index, line in enumerate(lines) if line.startswith("tags:")), len(lines))
        lines.insert(tag_index, f'  - "{SOURCE_REF}"')
        frontmatter = "\n".join(lines) + "\n"
    updated_match = re.search(r"^updated:\s*(.*?)\s*$", frontmatter, flags=re.MULTILINE)
    if updated_match:
        effective_updated = max(updated_match.group(1), updated)
        frontmatter = re.sub(
            r"^updated:.*$",
            f"updated: {effective_updated}",
            frontmatter,
            count=1,
            flags=re.MULTILINE,
        )
    text = text[: first + 3] + frontmatter + text[second:]
    normalized_block = block.rstrip() + "\n\n"
    if START_MARKER in text:
        start = text.index(START_MARKER)
        end_marker = text.index(END_MARKER, start) + len(END_MARKER)
        return text[:start] + normalized_block + text[end_marker:].lstrip("\n")
    anchor = "## 関連ページ"
    if anchor in text:
        index = text.index(anchor)
        return text[:index] + normalized_block + text[index:]
    source_anchor = "## 出典"
    if source_anchor in text:
        index = text.index(source_anchor)
        return text[:index] + normalized_block + text[index:]
    return text.rstrip() + "\n\n" + normalized_block


def analysis_updated_date(generated_at: str) -> str:
    try:
        parsed = datetime.fromisoformat(generated_at.replace("Z", "+00:00"))
    except ValueError as error:
        raise ValueError("analysis.jsonのgenerated_atを日時として解釈できません") from error
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=ZoneInfo("UTC"))
    return parsed.astimezone(ZoneInfo("Asia/Tokyo")).date().isoformat()


def sync_entity_blocks(
    *,
    entities: Mapping[str, Mapping[str, str | Path]],
    rows: Sequence[Mapping[str, Any]],
    target_counts: Counter[tuple[str, str]],
    selected: Mapping[str, Mapping[str, list[dict[str, Any]]]],
    run_rel: str,
    complete_matches: int,
    input_files: int,
    input_records: int,
    unique_matches: int,
    min_games: int,
    sufficient_games: int,
    selection_limit: int,
    updated: str = "2026-09-15",
    write: bool = True,
) -> list[tuple[Path, str]]:
    changes: list[tuple[Path, str]] = []
    for target_id, entity in entities.items():
        block = build_entity_block(
            champion_id=target_id,
            target_counts=target_counts,
            selected=selected,
            entity_catalog_data=entities,
            run_rel=run_rel,
            complete_matches=complete_matches,
            input_files=input_files,
            input_records=input_records,
            unique_matches=unique_matches,
            min_games=min_games,
            sufficient_games=sufficient_games,
            selection_limit=selection_limit,
        )
        path = Path(entity["path"])
        original = path.read_text(encoding="utf-8")
        expected = add_source_and_block(original, block, updated=updated)
        if expected != original:
            changes.append((path, expected))
    if write:
        for path, expected in changes:
            path.write_text(expected, encoding="utf-8")
    return changes


def csv_fields() -> tuple[str, ...]:
    return (
        "target_champion_id", "target_champion_name", "target_role", "relation",
        "related_champion_id", "related_champion_name", "related_role", "games", "wins",
        "losses", "target_win_rate", "pick_rate", "pick_rate_denominator", "wilson_lower_95",
        "wilson_upper_95", "patch_count", "sufficient_sample", "selection_score",
    )


def render_detail(
    champion_id: str,
    champion_name: str,
    rows: Sequence[Mapping[str, Any]],
    selected: Mapping[str, Mapping[str, list[dict[str, Any]]]],
    target_counts: Counter[tuple[str, str]],
    sufficient_games: int,
) -> str:
    lines = [
        f"# {champion_name}（{champion_id}）実測コンボ・カウンターピック",
        "",
        f"- 集計候補：{len(rows)}件（味方コンボ・同ロール対面、最小n以上）。",
        f"- n≥{sufficient_games}を十分性の目安とし、下回る選定結果にはサンプル不足を付記した。",
        "",
        "## 選定結果",
        "",
        "| ロール | 種別 | 相手・味方 | 試合 | 対象側勝率 | 95% Wilson区間 | 判定 |",
        "| --- | --- | --- | ---: | ---: | ---: | --- |",
    ]
    selected_rows: list[Mapping[str, Any]] = []
    selected_data = selected.get(champion_id, {})
    selected_rows.extend(selected_data.get("ally", []))
    selected_rows.extend(selected_data.get("opponent", []))
    selected_rows.sort(key=lambda row: (str(row["target_role"]), str(row["relation"])))
    for row in selected_rows:
        interval = f"{percent(row['wilson_lower_95'])}–{percent(row['wilson_upper_95'])}"
        label = "コンボ" if row["relation"] == "ally" else "カウンター候補"
        status = f"n≥{sufficient_games}" if row.get("sufficient_sample") else f"サンプル不足（n<{sufficient_games}）"
        lines.append(
            f"| {row['target_role']} | {label} | {row['related_champion_name']} | {row['games']} | {percent(row['target_win_rate'])} | {interval} | {status} |"
        )
    if not selected_rows:
        lines.append("| — | — | 15試合以上の候補なし | — | — | — | サンプル不足 |")
    lines.extend(["", "## ロール別参加者数", "", "| ロール | 対象試合 |", "| --- | ---: |"])
    for role, count in sorted(target_counts.items(), key=lambda item: (-item[1], item[0])):
        if role[0] == champion_id:
            lines.append(f"| {role[1]} | {count} |")
    lines.extend(
        [
            "",
            "## 候補全体（対象側勝率順）",
            "",
            "| ロール | 種別 | 関連チャンピオン | 試合 | 勝率 |",
            "| --- | --- | --- | ---: | ---: |",
        ]
    )
    ordered = sorted(
        rows,
        key=lambda row: (
            str(row["target_role"]),
            0 if row["relation"] == "ally" else 1,
            -(float(row["target_win_rate"]) if row["target_win_rate"] is not None else -1)
            if row["relation"] == "ally"
            else (float(row["target_win_rate"]) if row["target_win_rate"] is not None else 2),
            -int(row["games"]),
        ),
    )
    for row in ordered[:40]:
        label = "コンボ" if row["relation"] == "ally" else "対面"
        lines.append(
            f"| {row['target_role']} | {label} | {row['related_champion_name']} | {row['games']} | {percent(row['target_win_rate'])} |"
        )
    if not rows:
        lines.append("| — | — | 15試合以上の候補なし | — | — |")
    lines.extend(
        [
            "",
            "> [!warning] 解釈上の注意",
            "> これは最終スコアから正規化ロールと同時出場を復元した記述統計であり、実際のレーン対面、因果効果、推奨編成を保証しない。",
            "",
        ]
    )
    return "\n".join(lines)


def render_report(
    rows: Sequence[Mapping[str, Any]],
    selected: Mapping[str, Mapping[str, list[dict[str, Any]]]],
    entity_data: Mapping[str, Mapping[str, str | Path]],
    target_counts: Counter[tuple[str, str]],
    quality: Mapping[str, Any],
    run_rel: str,
    sufficient_games: int,
    selection_limit: int,
) -> str:
    lines = [
        "# 実測チャンピオン・コンボ／カウンターピック分析",
        "",
        f"- スクリプト：`{SCRIPT_NAME}`（内部で共通ローダーと `riot_champion_query.py` と同じ正規化を利用）",
        "- キュー：`420`、tier mode：`all`、対面範囲：同じ正規化ロール",
        "- 最小ゲーム数：`15`、十分性の目安：`30`",
        "",
        "> [!warning] 解釈上の注意",
        "> 勝率は対象チャンピオン側の観測値であり、味方シナジーの因果効果や確定的なカウンターを意味しない。候補の選定では、コンボは95% Wilson区間の下限、対面は上限を用いて小標本の極端値を抑えた。",
        "",
        "## 集計品質",
        "",
        "```json",
        json.dumps(quality, ensure_ascii=False, indent=2, sort_keys=True),
        "```",
        "",
        "## Entityへの選定結果",
        "",
        "| チャンピオン | ロール | 種別 | 関連チャンピオン | 試合 | 対象側勝率 | 判定 |",
        "| --- | --- | --- | --- | ---: | ---: | --- |",
    ]
    selected_rows: list[dict[str, Any]] = []
    for target_id, data in selected.items():
        for relation in ("ally", "opponent"):
            selected_rows.extend(data.get(relation, []))
    selected_rows.sort(key=lambda row: (str(row["target_champion_name"]), str(row["target_role"]), str(row["relation"])))
    for row in selected_rows:
        target_link = link_for_champion(str(row["target_champion_id"]), str(row["target_champion_name"]), entity_data)
        related_link = link_for_champion(str(row["related_champion_id"]), str(row["related_champion_name"]), entity_data)
        kind = "コンボ" if row["relation"] == "ally" else "カウンター候補"
        status = f"n≥{sufficient_games}" if row.get("sufficient_sample") else f"サンプル不足（n<{sufficient_games}）"
        lines.append(
            f"| {target_link} | {row['target_role']} | {kind} | {related_link} | {row['games']} | {percent(row['target_win_rate'])} | {status} |"
        )
    lines.extend(
        [
            "",
            "## 使い方",
            "",
            f"各チャンピオンの候補全体は `/{run_rel}/champions/` に保存し、entityページにはロールごとに高勝率コンボと低勝率カウンターピックを最大{selection_limit}件ずつ記載した。n<30の選定結果はentityにもサンプル不足と明記した。",
            "",
            "## 出典",
            "",
            f"- {SOURCE_REF}",
            f"- {SYNTHESIS_REF}",
            "",
        ]
    )
    return "\n".join(lines)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    input_group = parser.add_mutually_exclusive_group(required=True)
    input_group.add_argument("--input", action="append", help="JSON/JSONLまたは探索ディレクトリ")
    input_group.add_argument("--analysis", help="既存のmatchup analysis.jsonを使ってentityだけを同期")
    parser.add_argument("--output", default=str(DEFAULT_OUTPUT_ROOT), help="レポート出力先")
    parser.add_argument("--entity-root", default=str(DEFAULT_ENTITY_ROOT), help="チャンピオンentityディレクトリ")
    parser.add_argument("--queue-id", type=int, default=420)
    parser.add_argument("--min-games", type=int, default=15)
    parser.add_argument("--sufficient-games", type=int, default=30)
    parser.add_argument("--selection-limit", type=int, default=DEFAULT_SELECTION_LIMIT, help="各ロール・種別のentity掲載件数")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--dry-run", action="store_true", help="入力と件数だけ検証し、書き込まない")
    mode.add_argument("--write", action="store_true", help="レポートまたはentity生成ブロックを書き込む")
    mode.add_argument("--check", action="store_true", help="entityが期待内容と一致するか検証する")
    return parser


def main(argv: Optional[Sequence[str]] = None) -> int:
    args = build_parser().parse_args(argv)
    if args.min_games <= 0 or args.sufficient_games < args.min_games or args.selection_limit <= 0:
        raise ValueError("--sufficient-games は --min-games 以上の正数が必要です")
    if not args.dry_run and not args.write and not args.check:
        raise ValueError("--dry-run、--write、または--checkを指定してください")
    if args.check and not args.analysis:
        raise ValueError("--checkは--analysisと組み合わせて指定してください")

    entity_root = resolve_path(args.entity_root)
    entities = entity_catalog(entity_root)
    if args.analysis:
        snapshot = load_analysis_snapshot(resolve_path(args.analysis))
        rows = snapshot["rows"]
        target_counts = snapshot["target_counts"]
        selected = select_candidates(rows, target_counts, args.sufficient_games, args.selection_limit)
        source_summary = snapshot["summary"]
        updated_date = analysis_updated_date(snapshot["generated_at"])
        changes = sync_entity_blocks(
            entities=entities,
            rows=rows,
            target_counts=target_counts,
            selected=selected,
            run_rel=snapshot["run_rel"],
            complete_matches=int(source_summary["complete_matches"]),
            input_files=int(source_summary["input_files"]),
            input_records=int(source_summary["input_records"]),
            unique_matches=int(source_summary["unique_matches"]),
            min_games=args.min_games,
            sufficient_games=args.sufficient_games,
            selection_limit=args.selection_limit,
            updated=updated_date,
            write=args.write,
        )
        summary = {
            "mode": "analysis_sync",
            "analysis": str(resolve_path(args.analysis).relative_to(ROOT)),
            "script": SCRIPT_NAME,
            "schema_version": SCHEMA_VERSION,
            "entity_count": len(entities),
            "target_champion_count": len(snapshot["target_names"]),
            "candidate_rows": len(rows),
            "selected_rows": sum(
                len(data.get(relation, [])) for data in selected.values() for relation in ("ally", "opponent")
            ),
            "min_games": args.min_games,
            "sufficient_games": args.sufficient_games,
            "selection_limit": args.selection_limit,
            "complete_matches": int(source_summary["complete_matches"]),
            "input_files": int(source_summary["input_files"]),
            "input_records": int(source_summary["input_records"]),
            "unique_matches": int(source_summary["unique_matches"]),
            "run_dir": snapshot["run_rel"],
            "entities_changed": len(changes),
        }
        print(json.dumps(summary, ensure_ascii=False, indent=2, sort_keys=True))
        if args.check and changes:
            print(
                "不一致: " + ", ".join(str(path.relative_to(ROOT)) for path, _ in changes[:20]),
                file=sys.stderr,
            )
            return 1
        return 0

    dataset = load_dataset([resolve_path(value) for value in args.input or []])
    scopes, filter_stats = select_scopes(
        dataset.matches,
        queue_id=args.queue_id,
        tier_mode="all",
        tiers=set(),
        patch=None,
        date_from=None,
        date_to=None,
    )
    rows, target_counts, target_names = aggregate_candidates(scopes, args.min_games)
    selected = select_candidates(rows, target_counts, args.sufficient_games, args.selection_limit)
    complete_matches = sum(1 for scoped in scopes if scoped.match.is_complete())
    candidate_counts = Counter((str(row["relation"]), bool(row.get("games", 0) >= args.sufficient_games)) for row in rows)
    summary = {
        "script": SCRIPT_NAME,
        "schema_version": SCHEMA_VERSION,
        "input_files": len(dataset.input_files),
        "input_records": dataset.quality.counts.get("input_records", 0),
        "unique_matches": dataset.quality.counts.get("unique_matches", 0),
        "complete_matches": complete_matches,
        "selected_unique_matches": len({scoped.match.match_id for scoped in scopes}),
        "entity_count": len(entities),
        "target_champion_count": len(target_names),
        "candidate_rows": len(rows),
        "candidate_counts": {f"{relation}:{'sufficient' if sufficient else 'insufficient'}": count for (relation, sufficient), count in sorted(candidate_counts.items())},
        "selected_rows": sum(len(data.get(relation, [])) for data in selected.values() for relation in ("ally", "opponent")),
        "min_games": args.min_games,
        "sufficient_games": args.sufficient_games,
        "selection_limit": args.selection_limit,
        "quality": dataset.quality.as_dict(),
        "filters": filter_stats,
    }
    if args.dry_run:
        print(json.dumps(summary, ensure_ascii=False, indent=2, sort_keys=True))
        return 0
    if args.check:
        raise ValueError("raw入力の集計結果に対する--checkは利用できません。--analysisを指定してください")

    output_root = resolve_path(args.output)
    output_root.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    run_dir = output_root / f"run-{stamp}"
    if run_dir.exists():
        raise ValueError(f"出力ディレクトリが存在します: {run_dir}")
    run_dir.mkdir(parents=True)
    run_rel = run_dir.relative_to(ROOT).as_posix()

    for target_id, entity in entities.items():
        champion_rows = [row for row in rows if str(row["target_champion_id"]) == target_id]
        detail = render_detail(
            target_id,
            str(entity["title"]),
            champion_rows,
            selected,
            target_counts,
            args.sufficient_games,
        )
        detail_dir = run_dir / "champions"
        detail_dir.mkdir(exist_ok=True)
        (detail_dir / f"champion-{target_id}.md").write_text(detail, encoding="utf-8")
    sync_entity_blocks(
        entities=entities,
        rows=rows,
        target_counts=target_counts,
        selected=selected,
        run_rel=run_rel,
        complete_matches=complete_matches,
        input_files=len(dataset.input_files),
        input_records=dataset.quality.counts.get("input_records", 0),
        unique_matches=dataset.quality.counts.get("unique_matches", 0),
        min_games=args.min_games,
        sufficient_games=args.sufficient_games,
        selection_limit=args.selection_limit,
    )

    flattened_selected = []
    for data in selected.values():
        flattened_selected.extend(data.get("ally", []))
        flattened_selected.extend(data.get("opponent", []))
    rows_to_csv(run_dir / "combo-counter.csv", rows, csv_fields())
    rows_to_csv(run_dir / "selected.csv", flattened_selected, csv_fields())
    quality = {
        "input": dataset.quality.as_dict(),
        "filters": filter_stats,
        "summary": summary,
        "sample_thresholds": {
            "report_min_games": args.min_games,
            "sufficient_games": args.sufficient_games,
            "selection_limit": args.selection_limit,
        },
    }
    summary["run_dir"] = run_rel
    summary["outputs"] = [
        "analysis.json", "combo-counter.csv", "selected.csv", "quality.json", "manifest.json", "report.md", "champions/",
    ]
    analysis = {
        "schema_version": SCHEMA_VERSION,
        "generated_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
        "script": SCRIPT_NAME,
        "filters": {
            "queue_id": args.queue_id,
            "tier_mode": "all",
            "min_games": args.min_games,
            "sufficient_games": args.sufficient_games,
            "selection_limit": args.selection_limit,
        },
        "target_games_by_role": {f"{target_id}:{role}": count for (target_id, role), count in sorted(target_counts.items())},
        "target_names": dict(sorted(target_names.items())),
        "candidates": rows,
        "selected": selected,
    }
    manifest = {
        "schema_version": SCHEMA_VERSION,
        "script": SCRIPT_NAME,
        "generated_at": analysis["generated_at"],
        "inputs": [str(value) for value in args.input],
        "arguments": {
            "queue_id": args.queue_id,
            "tier_mode": "all",
            "min_games": args.min_games,
            "sufficient_games": args.sufficient_games,
            "selection_limit": args.selection_limit,
            "entity_root": str(entity_root.relative_to(ROOT)),
        },
        "outputs": summary["outputs"],
    }
    json_write(run_dir / "analysis.json", analysis)
    json_write(run_dir / "quality.json", quality)
    json_write(run_dir / "manifest.json", manifest)
    (run_dir / "report.md").write_text(
        render_report(rows, selected, entities, target_counts, quality, run_rel, args.sufficient_games, args.selection_limit),
        encoding="utf-8",
    )
    print(json.dumps(summary, ensure_ascii=False, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, RuntimeError, ValueError, KeyError) as error:
        print(f"エラー: {error}", file=sys.stderr)
        raise SystemExit(2)
