#!/usr/bin/env python3
"""実測ルーンセットの上位候補をチャンピオンentityへ同期する。"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from typing import Any, Mapping, Optional, Sequence
from zoneinfo import ZoneInfo


ROOT = Path(__file__).resolve().parents[1]
SCRIPT_NAME = "scripts/riot_champion_rune_wiki_sync.py"
DEFAULT_ENTITY_ROOT = ROOT / "wiki/entities/champions"
DEFAULT_SOURCE_REF = "[[wiki/sources/src-2026-09-15-riot-ranked-match-champion-rune-selection]]"
DEFAULT_SOURCE_BODY_LINK = (
    "[[wiki/sources/src-2026-09-15-riot-ranked-match-champion-rune-selection|"
    "Riotランク戦試合データ：チャンピオン別ルーン選択]]"
)
METHOD_LINK = (
    "[[wiki/syntheses/champion-rune-selection-ranked-matches|"
    "実測チャンピオン別ルーン選択分析]]"
)
BLOCK_START = "<!-- champion-rune-set-analysis:start -->"
BLOCK_END = "<!-- champion-rune-set-analysis:end -->"
ROLE_ORDER = {"TOP": 0, "JUNGLE": 1, "MIDDLE": 2, "BOTTOM": 3, "UTILITY": 4, "UNKNOWN": 5}


def resolve_path(value: str) -> Path:
    path = Path(value).expanduser()
    return path.resolve() if path.is_absolute() else (ROOT / path).resolve()


def as_int(value: Any) -> Optional[int]:
    try:
        if value is None or value == "":
            return None
        return int(value)
    except (TypeError, ValueError):
        return None


def as_float(value: Any) -> Optional[float]:
    try:
        if value is None or value == "":
            return None
        return float(value)
    except (TypeError, ValueError):
        return None


def percent(value: Any) -> str:
    number = as_float(value)
    return "不明" if number is None else f"{number * 100:.1f}%"


def normalize_token(value: Any) -> str:
    return "".join(character for character in str(value or "").casefold() if character.isalnum())


def frontmatter_value(text: str, key: str) -> Optional[str]:
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---\n", 4)
    if end < 0:
        return None
    pattern = re.compile(rf"^{re.escape(key)}:\s*[\"']?([^\"'\n]+)[\"']?\s*$", re.MULTILINE)
    match = pattern.search(text[:end])
    return match.group(1).strip() if match else None


def entity_catalog(entity_root: Path) -> dict[str, dict[str, Any]]:
    result: dict[str, dict[str, Any]] = {}
    for path in sorted(entity_root.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        champion_key = frontmatter_value(text, "champion_key")
        if champion_key is None:
            continue
        if champion_key in result:
            raise ValueError(f"champion_keyが重複しています: {champion_key}")
        result[champion_key] = {
            "path": path,
            "text": text,
            "title": frontmatter_value(text, "title") or path.stem,
            "champion_id": frontmatter_value(text, "champion_id") or path.stem,
        }
    if not result:
        raise ValueError(f"チャンピオンentityを検出できません: {entity_root}")
    return result


def select_entity_keys(
    catalog: Mapping[str, Mapping[str, Any]], selector: Optional[str]
) -> list[str]:
    if not selector:
        return sorted(catalog, key=lambda value: (int(value) if value.isdigit() else 10**9, value))
    aliases: defaultdict[str, set[str]] = defaultdict(set)
    for champion_key, entry in catalog.items():
        path = entry["path"]
        for value in (champion_key, entry.get("champion_id"), entry.get("title"), path.stem):
            aliases[normalize_token(value)].add(champion_key)
    selected: set[str] = set()
    for raw_value in selector.split(","):
        token = normalize_token(raw_value)
        matches = aliases.get(token, set())
        if not matches:
            raise ValueError(f"チャンピオンentityを解決できません: {raw_value.strip()}")
        if len(matches) > 1:
            raise ValueError(f"チャンピオン指定が曖昧です: {raw_value.strip()}")
        selected.update(matches)
    return sorted(selected, key=lambda value: (int(value) if value.isdigit() else 10**9, value))


def load_analysis(path: Path) -> dict[str, Any]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, Mapping):
        raise ValueError("analysis.json のルートはオブジェクトである必要があります")
    results = payload.get("results")
    if not isinstance(results, Mapping):
        raise ValueError("analysis.json に results がありません")
    if not isinstance(results.get("rune_sets"), list):
        raise ValueError("analysis.json に results.rune_sets がありません。新しい解析を実行してください")
    if not isinstance(results.get("champions"), list):
        raise ValueError("analysis.json に results.champions がありません")
    if not isinstance(payload.get("filters"), Mapping):
        raise ValueError("analysis.json に filters がありません")
    return dict(payload)


def analysis_updated_date(payload: Mapping[str, Any]) -> str:
    raw_value = str(payload.get("generated_at") or "").strip()
    if not raw_value:
        raise ValueError("analysis.json に generated_at がありません")
    try:
        generated_at = datetime.fromisoformat(raw_value.replace("Z", "+00:00"))
    except ValueError as error:
        raise ValueError("analysis.json の generated_at を日時として解釈できません") from error
    if generated_at.tzinfo is None:
        generated_at = generated_at.replace(tzinfo=ZoneInfo("UTC"))
    return generated_at.astimezone(ZoneInfo("Asia/Tokyo")).date().isoformat()


def id_tuple(value: Any) -> tuple[int, ...]:
    if isinstance(value, str):
        values: Any = [item for item in value.split(",") if item != ""]
    elif isinstance(value, (list, tuple)):
        values = value
    else:
        return ()
    return tuple(as_int(item) or 0 for item in values)


def rune_set_key(row: Mapping[str, Any]) -> tuple[Any, ...]:
    return (
        str(row.get("primary_style_id") or ""),
        str(row.get("primary_keystone_id") or ""),
        id_tuple(row.get("primary_rune_ids")),
        str(row.get("secondary_style_id") or ""),
        id_tuple(row.get("secondary_rune_ids")),
        id_tuple(row.get("shard_ids")),
    )


def overall_rows(rows: Any) -> list[dict[str, Any]]:
    if not isinstance(rows, list):
        return []
    return [
        dict(row)
        for row in rows
        if isinstance(row, Mapping)
        and row.get("scope") == "overall"
        and row.get("observed_tier") in {"ALL", "MIXED"}
        and str(row.get("patch") or "") != "ALL"
    ]


def aggregate_analysis(payload: Mapping[str, Any]) -> dict[str, dict[str, Any]]:
    """パッチ別行を重複なく全パッチ・チャンピオン・ロールへ集約する。"""

    results = payload["results"]
    champion_by_patch: dict[tuple[str, str, str], dict[str, Any]] = {}
    for row in overall_rows(results.get("champions")):
        champion_id = str(row.get("champion_id") or "")
        role = str(row.get("role") or "")
        patch = str(row.get("patch") or "")
        if not champion_id or not role or not patch:
            continue
        champion_by_patch.setdefault(
            (champion_id, role, patch),
            {
                "champion_id": row.get("champion_id"),
                "champion_name": row.get("champion_name"),
                "role": role,
                "champion_games": as_int(row.get("games")) or 0,
                "champion_wins": as_int(row.get("wins")) or 0,
                "champion_losses": as_int(row.get("losses")) or 0,
            },
        )

    set_totals: dict[tuple[Any, ...], dict[str, Any]] = {}
    for row in overall_rows(results.get("rune_sets")):
        champion_id = str(row.get("champion_id") or "")
        role = str(row.get("role") or "")
        patch = str(row.get("patch") or "")
        if not champion_id or not role or not patch or role == "ALL":
            continue
        champion_by_patch.setdefault(
            (champion_id, role, patch),
            {
                "champion_id": row.get("champion_id"),
                "champion_name": row.get("champion_name"),
                "role": role,
                "champion_games": as_int(row.get("champion_games")) or 0,
                "champion_wins": as_int(row.get("champion_wins")) or 0,
                "champion_losses": as_int(row.get("champion_losses")) or 0,
            },
        )
        key = (champion_id, role, rune_set_key(row))
        current = set_totals.get(key)
        if current is None:
            current = dict(row)
            current["games"] = 0
            current["wins"] = 0
            current["losses"] = 0
            set_totals[key] = current
        current["games"] += as_int(row.get("games")) or 0
        current["wins"] += as_int(row.get("wins")) or 0
        current["losses"] += as_int(row.get("losses")) or 0

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

    result: defaultdict[str, dict[str, Any]] = defaultdict(dict)
    for (champion_id, role, _key), row in set_totals.items():
        champion = champion_totals.get((champion_id, role))
        if champion is None:
            continue
        row["champion_games"] = champion["champion_games"]
        row["champion_wins"] = champion["champion_wins"]
        row["champion_losses"] = champion["champion_losses"]
        row["champion_win_rate"] = (
            champion["champion_wins"] / champion["champion_games"]
            if champion["champion_games"]
            else None
        )
        row["win_rate"] = row["wins"] / row["games"] if row["games"] else None
        row["pick_rate"] = row["games"] / champion["champion_games"] if champion["champion_games"] else None
        row["pick_rate_denominator"] = champion["champion_games"]
        result[champion_id].setdefault(
            role,
            {
                "champion_id": champion.get("champion_id", row.get("champion_id")),
                "champion_name": champion.get("champion_name", row.get("champion_name")),
                "role": role,
                "champion_games": champion["champion_games"],
                "champion_wins": champion["champion_wins"],
                "champion_losses": champion["champion_losses"],
                "sets": [],
            },
        )["sets"].append(row)

    for champion_id, roles in result.items():
        for role, data in roles.items():
            data["sets"].sort(
                key=lambda row: (
                    -int(row.get("games") or 0),
                    -(float(row.get("win_rate")) if row.get("win_rate") is not None else -1),
                    str(row.get("primary_keystone_name") or ""),
                    str(row.get("secondary_style_name") or ""),
                    str(rune_set_key(row)),
                )
            )
    return {champion_id: dict(roles) for champion_id, roles in result.items()}


def without_generated_block(text: str) -> str:
    start = text.find(BLOCK_START)
    end = text.find(BLOCK_END)
    if start < 0 and end < 0:
        return text
    if start < 0 or end < 0 or end < start:
        raise ValueError("ルーンセット分析ブロックの開始・終了マーカーが不整合です")
    return text[:start] + text[end + len(BLOCK_END) :]


def replace_or_insert_block(text: str, block: str) -> str:
    start = text.find(BLOCK_START)
    end = text.find(BLOCK_END)
    if start >= 0 or end >= 0:
        if start < 0 or end < 0 or end < start:
            raise ValueError("ルーンセット分析ブロックの開始・終了マーカーが不整合です")
        end += len(BLOCK_END)
        return text[:start].rstrip() + "\n\n" + block + "\n\n" + text[end:].lstrip()
    for heading in ("## 関連ページ", "## 出典"):
        marker = "\n" + heading + "\n"
        position = text.find(marker)
        if position >= 0:
            return text[:position].rstrip() + "\n\n" + block + "\n" + text[position:]
    return text.rstrip() + "\n\n" + block + "\n"


def ensure_source_and_updated(text: str, source_ref: str, updated: str) -> str:
    if not text.startswith("---\n"):
        raise ValueError("YAMLフロントマターがありません")
    end = text.find("\n---\n", 4)
    if end < 0:
        raise ValueError("YAMLフロントマターの終端がありません")
    front_lines = text[4:end].splitlines()
    updated_found = False
    for index, line in enumerate(front_lines):
        if line.startswith("updated:"):
            existing = line.split(":", 1)[1].strip()
            front_lines[index] = f"updated: {max(existing, updated)}"
            updated_found = True
            break
    if not updated_found:
        raise ValueError("YAMLフロントマターにupdatedがありません")
    source_line = f'  - "{source_ref}"'
    if source_ref not in "\n".join(front_lines):
        try:
            source_index = next(index for index, line in enumerate(front_lines) if line == "sources:")
        except StopIteration as error:
            raise ValueError("YAMLフロントマターにsourcesがありません") from error
        insert_at = source_index + 1
        while insert_at < len(front_lines) and front_lines[insert_at].startswith("  - "):
            insert_at += 1
        front_lines.insert(insert_at, source_line)
    return "---\n" + "\n".join(front_lines) + text[end:]


def report_link(analysis_path: Path, label: str = "ルーンセットの詳細レポート") -> str:
    report_path = analysis_path.parent / "report.md"
    if not report_path.exists():
        return ""
    try:
        relative = report_path.relative_to(ROOT).with_suffix("")
    except ValueError:
        return ""
    return f"[[{relative.as_posix()}|{label}]]"


def list_values(row: Mapping[str, Any], names_field: str, ids_field: str) -> list[str]:
    names = row.get(names_field)
    if isinstance(names, list) and names:
        return [str(value) for value in names]
    if isinstance(names, str) and names:
        return [value for value in names.split(",") if value]
    return [f"ID {value}" for value in id_tuple(row.get(ids_field))]


def rune_set_label(row: Mapping[str, Any]) -> str:
    primary_runes = "・".join(list_values(row, "primary_rune_names", "primary_rune_ids")) or "不明"
    secondary_runes = "・".join(list_values(row, "secondary_rune_names", "secondary_rune_ids")) or "不明"
    shards = "・".join(list_values(row, "shard_names", "shard_ids")) or "不明"
    primary_style = str(row.get("primary_style_name") or f"ID {row.get('primary_style_id') or '不明'}")
    secondary_style = str(row.get("secondary_style_name") or f"ID {row.get('secondary_style_id') or '不明'}")
    keystone = str(row.get("primary_keystone_name") or f"ID {row.get('primary_keystone_id') or '不明'}")
    return (
        f"主系{primary_style}：{keystone}／{primary_runes}；"
        f"副系{secondary_style}：{secondary_runes}；シャード{shards}"
    )


def render_block(
    *,
    champion_key: str,
    title: str,
    analysis_path: Path,
    payload: Mapping[str, Any],
    grouped: Mapping[str, Mapping[str, Any]],
    role_min_games: int,
    max_sets: int,
    source_ref: str,
) -> str:
    filters = payload.get("filters", {}) if isinstance(payload.get("filters"), Mapping) else {}
    roles = grouped.get(champion_key, {})
    role_candidates = [
        data
        for role, data in roles.items()
        if role not in {"ALL", "UNKNOWN"} and int(data.get("champion_games") or 0) >= role_min_games
    ]
    role_candidates.sort(
        key=lambda data: (
            -int(data.get("champion_games") or 0),
            ROLE_ORDER.get(str(data.get("role") or "UNKNOWN"), 99),
            str(data.get("role") or ""),
        )
    )
    selected_role = role_candidates[0] if role_candidates else None
    generated_at = str(payload.get("generated_at") or "不明")
    generated_date = generated_at[:10] if len(generated_at) >= 10 else generated_at
    selected_matches = as_int(filters.get("selected_unique_matches")) or as_int(filters.get("selected_scopes"))
    queue_id = filters.get("queue_id", "不明")
    snapshot_parts = [f"{generated_date}生成", f"キュー{queue_id}"]
    if selected_matches is not None:
        snapshot_parts.append(f"ユニーク試合{selected_matches:,}件")
    detail = report_link(analysis_path)
    if detail:
        snapshot_parts.append(detail)
    source_link = DEFAULT_SOURCE_BODY_LINK if source_ref == DEFAULT_SOURCE_REF else source_ref
    lines = [
        BLOCK_START,
        "## よく選ばれるルーンセット（実測）",
        "",
        "- **スナップショット：** " + "、".join(snapshot_parts) + "。",
        "- **根拠と方法：** "
        + source_link
        + f"、{METHOD_LINK}。",
        "- **読み方：** 主系・キーストーン・主系3枠・副系2枠・3シャードが完全一致する組み合わせを、同じチャンピオン・正規化ロールの参加者を分母に集計した。選択時勝率は記述統計であり、因果効果や推奨を示さない。",
        "",
    ]
    if selected_role is None:
        available = sorted(
            roles.values(),
            key=lambda data: (
                -int(data.get("champion_games") or 0),
                ROLE_ORDER.get(str(data.get("role") or "UNKNOWN"), 99),
            ),
        )
        if available:
            top = available[0]
            lines.extend(
                [
                    f"- **対象ロール：** 最大の観測ロールは{top.get('role') or 'UNKNOWN'}（{int(top.get('champion_games') or 0):,}試合）だが、掲載基準{role_min_games}試合を満たさない。",
                    "- **結果：** 分母不足のため、上位ルーンセットを掲載しない。",
                    "",
                ]
            )
        else:
            lines.extend(["- **結果：** このスナップショットに分析可能な完全ルーンセットがない。", ""])
    else:
        role = str(selected_role.get("role") or "UNKNOWN")
        games = int(selected_role.get("champion_games") or 0)
        wins = int(selected_role.get("champion_wins") or 0)
        sets = list(selected_role.get("sets") or [])[:max_sets]
        lines.extend(
            [
                f"### {role}（対象{games:,}試合、全体勝率{percent(wins / games if games else None)}）",
                "",
                "| 順位 | 完全ルーンセット | 選択数 | 選択率 | 選択時勝率 |",
                "| ---: | --- | ---: | ---: | ---: |",
            ]
        )
        for index, row in enumerate(sets, start=1):
            lines.append(
                f"| {index} | {rune_set_label(row)} | {int(row.get('games') or 0):,}/{games:,} | {percent(row.get('pick_rate'))} | {percent(row.get('win_rate'))} |"
            )
        if not sets:
            lines.append(f"| — | n={role_min_games}以上の完全ルーンセットなし | — | — | — |")
        elif len(sets) < max_sets:
            lines.append(f"\n- **注記：** 最小ゲーム数条件を満たす完全セットは{len(sets)}件で、{max_sets}件に満たない。")
        lines.extend(
            [
                "",
                "- **選定ロール：** チャンピオン・ロール別の完全試合数が最も多いロールを1つ選んだ。別ロールや全候補は詳細レポートで確認できる。",
                "- **シャード表示：** Data Dragonで表示名を解決できない場合は`UNKNOWN(<ID>)`としてIDを保持する。",
                "",
            ]
        )
    lines.extend(["- **出典：** " + source_link + f"、{METHOD_LINK}。", BLOCK_END])
    return "\n".join(lines)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--analysis", required=True, help="riot_ranked_match_analyzer.py が生成した analysis.json")
    parser.add_argument("--entity-root", default=str(DEFAULT_ENTITY_ROOT), help="チャンピオンentityディレクトリ")
    parser.add_argument("--champions", help="同期対象のchampion_key、英字ID、タイトル、ファイル名をカンマ区切りで限定")
    parser.add_argument("--role-min-games", type=int, default=15, help="entityへロールを掲載する最小試合数（既定: 15）")
    parser.add_argument("--max-sets", type=int, default=3, help="ロールごとのルーンセット掲載数（既定: 3）")
    parser.add_argument("--source-ref", default=DEFAULT_SOURCE_REF, help="entityのsourcesへ追加する原典要約Wikilink")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--dry-run", action="store_true", help="差分件数だけ確認し、書き込まない（既定）")
    mode.add_argument("--write", action="store_true", help="生成ブロックとsourcesをentityへ同期する")
    mode.add_argument("--check", action="store_true", help="entityが期待内容と一致するか検証する")
    return parser


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        if args.role_min_games <= 0 or args.max_sets <= 0:
            raise ValueError("--role-min-games と --max-sets は正の整数が必要です")
        analysis_path = resolve_path(args.analysis)
        entity_root = resolve_path(args.entity_root)
        payload = load_analysis(analysis_path)
        catalog = entity_catalog(entity_root)
        selected_keys = select_entity_keys(catalog, args.champions)
        grouped = aggregate_analysis(payload)
        updated = analysis_updated_date(payload)
        changes: list[tuple[Path, str]] = []
        for champion_key in selected_keys:
            entry = catalog[champion_key]
            path = entry["path"]
            original = entry["text"]
            block = render_block(
                champion_key=champion_key,
                title=str(entry["title"]),
                analysis_path=analysis_path,
                payload=payload,
                grouped=grouped,
                role_min_games=args.role_min_games,
                max_sets=args.max_sets,
                source_ref=args.source_ref,
            )
            expected = ensure_source_and_updated(
                replace_or_insert_block(original, block), args.source_ref, updated
            )
            if expected != original:
                changes.append((path, expected))
        summary = {
            "script": SCRIPT_NAME,
            "mode": "write" if args.write else "check" if args.check else "dry-run",
            "analysis": str(analysis_path),
            "entities_detected": len(catalog),
            "entities_selected": len(selected_keys),
            "entities_changed": len(changes),
            "champions_with_rune_set_rows": len(grouped),
            "role_min_games": args.role_min_games,
            "max_sets": args.max_sets,
        }
        if args.check:
            print(json.dumps(summary, ensure_ascii=False, indent=2, sort_keys=True))
            if changes:
                print("不一致: " + ", ".join(str(path.relative_to(ROOT)) for path, _ in changes[:20]), file=sys.stderr)
                return 1
            return 0
        if args.write:
            for path, expected in changes:
                path.write_text(expected, encoding="utf-8")
        print(json.dumps(summary, ensure_ascii=False, indent=2, sort_keys=True))
        return 0
    except (OSError, ValueError, json.JSONDecodeError) as error:
        print(f"エラー: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
