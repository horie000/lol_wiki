#!/usr/bin/env python3
"""チャンピオン別ビルド分析の短い要約をentityページへ同期する。"""

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

from riot_champion_item_synergy import STATUS_GROUP_NAMES


ROOT = Path(__file__).resolve().parents[1]
SCRIPT_NAME = "scripts/riot_champion_build_wiki_sync.py"
DEFAULT_ENTITY_ROOT = ROOT / "wiki/entities/champions"
DEFAULT_SOURCE_REF = "[[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis]]"
DEFAULT_SOURCE_BODY_LINK = (
    "[[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|"
    "Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]"
)
METHOD_LINK = (
    "[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|"
    "アイテム相性タグ分類の実試合再評価]]"
)
BLOCK_START = "<!-- champion-build-analysis:start -->"
BLOCK_END = "<!-- champion-build-analysis:end -->"
ROLE_ORDER = {"TOP": 0, "JUNGLE": 1, "MIDDLE": 2, "BOTTOM": 3, "UTILITY": 4, "UNKNOWN": 5}
SIGNAL_KEYWORDS: dict[str, tuple[str, ...]] = {
    "critical_chance": ("クリティカル",),
    "attack_damage": ("攻撃力", "通常攻撃"),
    "attack_speed": ("攻撃速度",),
    "ability_power": ("魔力",),
    "health": ("体力", "シールド"),
    "armor": ("物理防御",),
    "magic_resist": ("魔法防御",),
    "mana": ("マナ",),
    "health_regen": ("体力再生",),
    "movement_speed": ("移動速度",),
    "lifesteal": ("ライフスティール",),
}


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


def load_analysis(path: Path) -> dict[str, Any]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, Mapping):
        raise ValueError("analysis.json のルートはオブジェクトである必要があります")
    for key in ("results", "status_group_results", "build_results", "theoretical_build_results"):
        if not isinstance(payload.get(key), list):
            raise ValueError(f"analysis.json に配列 `{key}` がありません")
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
        champion_id = frontmatter_value(text, "champion_id")
        title = frontmatter_value(text, "title") or path.stem
        if champion_key is None:
            continue
        if champion_key in result:
            raise ValueError(f"champion_keyが重複しています: {champion_key}")
        result[champion_key] = {
            "path": path,
            "text": text,
            "title": title,
            "champion_id": champion_id or path.stem,
        }
    if not result:
        raise ValueError(f"チャンピオンentityを検出できません: {entity_root}")
    return result


def normalize_token(value: Any) -> str:
    return "".join(character for character in str(value or "").casefold() if character.isalnum())


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


def overall_rows(rows: Sequence[Any]) -> list[dict[str, Any]]:
    return [dict(row) for row in rows if isinstance(row, Mapping) and row.get("scope") == "overall"]


def group_analysis(payload: Mapping[str, Any]) -> dict[str, dict[str, list[dict[str, Any]]]]:
    grouped: dict[str, dict[str, list[dict[str, Any]]]] = {
        "items": defaultdict(list),
        "statuses": defaultdict(list),
        "builds": defaultdict(list),
        "theories": defaultdict(list),
    }
    sources = {
        "items": payload["results"],
        "statuses": payload["status_group_results"],
        "builds": payload["build_results"],
        "theories": payload["theoretical_build_results"],
    }
    for kind, rows in sources.items():
        for row in overall_rows(rows):
            champion_id = str(row.get("champion_id") or "")
            if champion_id:
                grouped[kind][champion_id].append(row)
    return grouped


def without_generated_block(text: str) -> str:
    start = text.find(BLOCK_START)
    end = text.find(BLOCK_END)
    if start < 0 and end < 0:
        return text
    if start < 0 or end < 0 or end < start:
        raise ValueError("チャンピオン分析ブロックの開始・終了マーカーが不整合です")
    return text[:start] + text[end + len(BLOCK_END) :]


def champion_signals(text: str) -> set[str]:
    source_text = without_generated_block(text)
    return {
        group_id
        for group_id, keywords in SIGNAL_KEYWORDS.items()
        if any(keyword in source_text for keyword in keywords)
    }


def percent(value: Any) -> str:
    number = as_float(value)
    return "不明" if number is None else f"{number * 100:.1f}%"


def points(value: Any) -> str:
    number = as_float(value)
    return "不明" if number is None else f"{number * 100:+.1f}pt"


def build_entry(row: Mapping[str, Any]) -> str:
    return (
        f"{row.get('build_name', 'UNKNOWN')}（該当n={as_int(row.get('build_games')) or 0}、"
        f"{percent(row.get('build_win_rate'))} / 非該当{percent(row.get('without_build_win_rate'))}、"
        f"差{points(row.get('win_rate_lift_vs_without'))}）"
    )


def status_entry(row: Mapping[str, Any]) -> str:
    return (
        f"{row.get('status_group_name', row.get('status_group_id', 'UNKNOWN'))}"
        f"（該当n={as_int(row.get('status_games')) or 0}、"
        f"{percent(row.get('status_win_rate'))} / 非該当{percent(row.get('without_status_win_rate'))}、"
        f"差{points(row.get('win_rate_lift_vs_without'))}）"
    )


def theory_entry(row: Mapping[str, Any], signals: set[str], minimum_games: int) -> str:
    games = as_int(row.get("build_games")) or 0
    state = "未観測" if games == 0 else f"n={games}（{minimum_games}未満）"
    shared = [str(value) for value in row.get("shared_status_groups", [])]
    shared_labels = [STATUS_GROUP_NAMES.get(value, value) for value in shared]
    direct_labels = [STATUS_GROUP_NAMES.get(value, value) for value in shared if value in signals]
    reason = "共通stats: " + "・".join(shared_labels)
    if direct_labels:
        reason += "／チャンピオン原典にも言及: " + "・".join(direct_labels)
    else:
        reason += "／スキル相互作用は未検証"
    return f"{row.get('build_name', 'UNKNOWN')}（{state}；{reason}）"


def rows_for_role(rows: Sequence[Mapping[str, Any]], role: str) -> list[dict[str, Any]]:
    return [dict(row) for row in rows if str(row.get("role") or "UNKNOWN") == role]


def rank_builds(
    rows: Sequence[Mapping[str, Any]], minimum_games: int, limit: int
) -> list[dict[str, Any]]:
    selected = [
        dict(row)
        for row in rows
        if (as_int(row.get("build_games")) or 0) >= minimum_games
        and (as_int(row.get("without_build_games")) or 0) >= minimum_games
        and (as_float(row.get("win_rate_lift_vs_without")) or 0) > 0
    ]
    selected.sort(
        key=lambda row: (
            -(as_float(row.get("win_rate_lift_vs_without")) or 0),
            -(as_int(row.get("build_games")) or 0),
            str(row.get("build_name") or ""),
        )
    )
    return selected[:limit]


def rank_statuses(
    rows: Sequence[Mapping[str, Any]], minimum_games: int, limit: int
) -> list[dict[str, Any]]:
    selected = [
        dict(row)
        for row in rows
        if (as_int(row.get("status_games")) or 0) >= minimum_games
        and (as_int(row.get("without_status_games")) or 0) >= minimum_games
        and (as_float(row.get("win_rate_lift_vs_without")) or 0) > 0
    ]
    selected.sort(
        key=lambda row: (
            -(as_float(row.get("win_rate_lift_vs_without")) or 0),
            -(as_int(row.get("status_games")) or 0),
            str(row.get("status_group_name") or ""),
        )
    )
    return selected[:limit]


def rank_theories(
    rows: Sequence[Mapping[str, Any]], signals: set[str], limit: int
) -> list[dict[str, Any]]:
    selected = [dict(row) for row in rows]
    selected.sort(
        key=lambda row: (
            -len(set(str(value) for value in row.get("shared_status_groups", [])).intersection(signals)),
            -len(row.get("shared_status_groups", [])),
            -(as_int(row.get("build_games")) or 0),
            int(row.get("build_size") or 0),
            str(row.get("build_name") or ""),
        )
    )
    return selected[:limit]


def role_game_counts(*row_groups: Sequence[Mapping[str, Any]]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for rows in row_groups:
        for row in rows:
            role = str(row.get("role") or "UNKNOWN")
            counts[role] = max(counts.get(role, 0), as_int(row.get("champion_games")) or 0)
    return counts


def detail_wikilink(analysis_path: Path, champion_key: str, title: str) -> Optional[str]:
    detail_path = analysis_path.parent / "champions" / f"champion-{champion_key}.md"
    if not detail_path.exists():
        return None
    try:
        relative = detail_path.relative_to(ROOT).with_suffix("")
    except ValueError:
        return None
    return f"[[{relative.as_posix()}|{title}の詳細レポート]]"


def render_block(
    *,
    champion_key: str,
    title: str,
    entity_text: str,
    analysis_path: Path,
    payload: Mapping[str, Any],
    grouped: Mapping[str, Mapping[str, list[dict[str, Any]]]],
    role_min_games: int,
    comparison_min_games: int,
    max_roles: int,
    max_builds: int,
    max_statuses: int,
    max_theories: int,
    source_ref: str,
) -> str:
    items = grouped["items"].get(champion_key, [])
    statuses = grouped["statuses"].get(champion_key, [])
    builds = grouped["builds"].get(champion_key, [])
    theories = grouped["theories"].get(champion_key, [])
    counts = role_game_counts(items, statuses, builds, theories)
    roles = [role for role, games in counts.items() if games >= role_min_games]
    roles.sort(key=lambda role: (-counts[role], ROLE_ORDER.get(role, 99), role))
    roles = roles[:max_roles]
    signals = champion_signals(entity_text)
    filters = payload.get("filters", {}) if isinstance(payload.get("filters"), Mapping) else {}
    generated_at = str(payload.get("generated_at") or "不明")
    generated_date = generated_at[:10] if len(generated_at) >= 10 else generated_at
    selected_matches = as_int(filters.get("selected_unique_matches"))
    queue_id = filters.get("queue_id", "不明")
    detail = detail_wikilink(analysis_path, champion_key, title)
    snapshot_parts = [f"{generated_date}生成", f"キュー{queue_id}"]
    if selected_matches is not None:
        snapshot_parts.append(f"ユニーク試合{selected_matches:,}件")
    if detail:
        snapshot_parts.append(detail)
    lines = [
        BLOCK_START,
        "## 実試合ビルド分析",
        "",
        "- **スナップショット：** " + "、".join(snapshot_parts) + "。",
        "- **根拠と方法：** "
        + (DEFAULT_SOURCE_BODY_LINK if source_ref == DEFAULT_SOURCE_REF else source_ref)
        + f"、{METHOD_LINK}。",
        "- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。",
        "",
    ]
    if not roles:
        if counts:
            role, games = sorted(
                counts.items(), key=lambda item: (-item[1], ROLE_ORDER.get(item[0], 99), item[0])
            )[0]
            lines.extend(
                [
                    f"- **分母不足：** 最大の観測ロールは{role}の{games}試合で、entity掲載基準{role_min_games}試合を満たさない。",
                    "",
                ]
            )
        else:
            lines.extend(["- **分母不足：** このスナップショットに分析可能な観測がない。", ""])
    for role in roles:
        role_builds = rank_builds(rows_for_role(builds, role), comparison_min_games, max_builds)
        role_statuses = rank_statuses(rows_for_role(statuses, role), comparison_min_games, max_statuses)
        role_theories = rank_theories(rows_for_role(theories, role), signals, max_theories)
        build_text = "；".join(build_entry(row) for row in role_builds)
        status_text = "；".join(status_entry(row) for row in role_statuses)
        theory_text = "；".join(
            theory_entry(row, signals, as_int(filters.get("min_games")) or 15)
            for row in role_theories
        )
        lines.extend(
            [
                f"### {role}（{counts[role]:,}試合）",
                "",
                "- **実測ビルド候補：** "
                + (build_text or f"該当・非該当が各{comparison_min_games}試合以上で正の差を持つ候補なし。"),
                "- **ステータス傾向：** "
                + (status_text or f"該当・非該当が各{comparison_min_games}試合以上で正の差を持つ群なし。"),
                "- **理論仮説：** " + (theory_text or "共通statsから抽出できる未観測・小標本候補なし。"),
                "",
            ]
        )
    lines.append(BLOCK_END)
    return "\n".join(lines)


def replace_or_insert_block(text: str, block: str) -> str:
    start = text.find(BLOCK_START)
    end = text.find(BLOCK_END)
    if start >= 0 or end >= 0:
        if start < 0 or end < 0 or end < start:
            raise ValueError("チャンピオン分析ブロックの開始・終了マーカーが不整合です")
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
            front_lines[index] = f"updated: {updated}"
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


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--analysis", required=True, help="riot_champion_item_synergy.py が生成した analysis.json")
    parser.add_argument("--entity-root", default=str(DEFAULT_ENTITY_ROOT), help="チャンピオンentityディレクトリ")
    parser.add_argument("--champions", help="同期対象のchampion_key、英字ID、タイトル、ファイル名をカンマ区切りで限定")
    parser.add_argument("--role-min-games", type=int, default=30, help="entityへロールを掲載する最小試合数（既定: 30）")
    parser.add_argument("--comparison-min-games", type=int, help="実測候補の該当・非該当双方の最小試合数。省略時はanalysisのreport_min_games")
    parser.add_argument("--max-roles", type=int, default=2, help="entityへ掲載する最大ロール数（既定: 2）")
    parser.add_argument("--max-builds", type=int, default=2, help="ロールごとの実測ビルド候補数（既定: 2）")
    parser.add_argument("--max-statuses", type=int, default=2, help="ロールごとのステータス群数（既定: 2）")
    parser.add_argument("--max-theories", type=int, default=2, help="ロールごとの理論仮説数（既定: 2）")
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
        numeric_values = (
            args.role_min_games,
            args.max_roles,
            args.max_builds,
            args.max_statuses,
            args.max_theories,
        )
        if any(value <= 0 for value in numeric_values):
            raise ValueError("件数・上限オプションは正の整数が必要です")
        analysis_path = resolve_path(args.analysis)
        entity_root = resolve_path(args.entity_root)
        payload = load_analysis(analysis_path)
        filters = payload.get("filters", {}) if isinstance(payload.get("filters"), Mapping) else {}
        comparison_min_games = args.comparison_min_games or as_int(filters.get("report_min_games")) or 30
        if comparison_min_games <= 0:
            raise ValueError("--comparison-min-games は正の整数が必要です")
        catalog = entity_catalog(entity_root)
        selected_keys = select_entity_keys(catalog, args.champions)
        grouped = group_analysis(payload)
        updated = analysis_updated_date(payload)
        changes: list[tuple[Path, str]] = []
        missing_detail: list[str] = []
        for champion_key in selected_keys:
            entry = catalog[champion_key]
            path = entry["path"]
            original = entry["text"]
            block = render_block(
                champion_key=champion_key,
                title=str(entry["title"]),
                entity_text=original,
                analysis_path=analysis_path,
                payload=payload,
                grouped=grouped,
                role_min_games=args.role_min_games,
                comparison_min_games=comparison_min_games,
                max_roles=args.max_roles,
                max_builds=args.max_builds,
                max_statuses=args.max_statuses,
                max_theories=args.max_theories,
                source_ref=args.source_ref,
            )
            if detail_wikilink(analysis_path, champion_key, str(entry["title"])) is None:
                missing_detail.append(champion_key)
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
            "missing_detail_reports": len(missing_detail),
            "role_min_games": args.role_min_games,
            "comparison_min_games": comparison_min_games,
            "max_roles": args.max_roles,
            "max_builds": args.max_builds,
            "max_statuses": args.max_statuses,
            "max_theories": args.max_theories,
        }
        if missing_detail:
            summary["missing_detail_examples"] = missing_detail[:10]
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
