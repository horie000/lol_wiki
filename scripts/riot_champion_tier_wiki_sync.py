#!/usr/bin/env python3
"""観測ランク帯別チャンピオン候補をチャンピオンentityへ同期する。"""

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
SCRIPT_NAME = "scripts/riot_champion_tier_wiki_sync.py"
DEFAULT_ENTITY_ROOT = ROOT / "wiki/entities/champions"
DEFAULT_SOURCE_REF = "[[wiki/sources/src-2026-09-16-riot-ranked-match-tier-analysis]]"
DEFAULT_SOURCE_BODY_LINK = (
    "[[wiki/sources/src-2026-09-16-riot-ranked-match-tier-analysis|"
    "Riotランク戦試合データ：観測ランク帯別特徴]]"
)
SYNTHESIS_REF = "[[wiki/syntheses/ranked-tier-characteristics|ランク帯別の試合特徴と全帯共通傾向]]"
START_MARKER = "<!-- champion-tier-analysis:start -->"
END_MARKER = "<!-- champion-tier-analysis:end -->"
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


def resolve_path(value: str | Path) -> Path:
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


def parse_frontmatter_value(text: str, key: str) -> Optional[str]:
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---\n", 4)
    if end < 0:
        return None
    match = re.search(rf"^{re.escape(key)}:\s*(.+?)\s*$", text[4:end], flags=re.MULTILINE)
    if not match:
        return None
    value = match.group(1).strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"\"", "'"}:
        value = value[1:-1]
    return value


def entity_catalog(entity_root: Path) -> dict[str, dict[str, Any]]:
    result: dict[str, dict[str, Any]] = {}
    for path in sorted(entity_root.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        champion_key = parse_frontmatter_value(text, "champion_key")
        if champion_key is None:
            continue
        if champion_key in result:
            raise ValueError(f"champion_keyが重複しています: {champion_key}")
        result[champion_key] = {
            "path": path,
            "text": text,
            "title": parse_frontmatter_value(text, "title") or path.stem,
            "champion_id": parse_frontmatter_value(text, "champion_id") or path.stem,
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


def load_analysis(path: Path) -> dict[str, Any]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, Mapping):
        raise ValueError("analysis.jsonのルートはオブジェクトである必要があります")
    results = payload.get("results")
    if not isinstance(results, Mapping):
        raise ValueError("analysis.jsonにresultsがありません")
    for key in ("champion_tier", "champion_extremes"):
        if not isinstance(results.get(key), list):
            raise ValueError(f"analysis.jsonにresults.{key}がありません")
    filters = payload.get("filters")
    if not isinstance(filters, Mapping):
        raise ValueError("analysis.jsonにfiltersがありません")
    if str(filters.get("tier_mode") or "").lower() != "observed":
        raise ValueError("チャンピオンentity同期にはtier_mode=observedのanalysis.jsonが必要です")
    min_games = as_int(filters.get("min_games"))
    if min_games is None or min_games <= 0:
        raise ValueError("analysis.jsonのfilters.min_gamesが正の整数ではありません")
    generated_at = str(payload.get("generated_at") or "").strip()
    if not generated_at:
        raise ValueError("analysis.jsonにgenerated_atがありません")
    report_path = path.parent / "report.md"
    if not report_path.exists():
        raise ValueError(f"analysis.jsonに対応するreport.mdがありません: {report_path}")
    return dict(payload)


def analysis_updated_date(payload: Mapping[str, Any]) -> str:
    raw_value = str(payload.get("generated_at") or "").strip()
    try:
        generated_at = datetime.fromisoformat(raw_value.replace("Z", "+00:00"))
    except ValueError as error:
        raise ValueError("analysis.jsonのgenerated_atを日時として解釈できません") from error
    if generated_at.tzinfo is None:
        generated_at = generated_at.replace(tzinfo=ZoneInfo("UTC"))
    return generated_at.astimezone(ZoneInfo("Asia/Tokyo")).date().isoformat()


def validate_row(row: Any, kind: str, index: int) -> dict[str, Any]:
    if not isinstance(row, Mapping):
        raise ValueError(f"results.{kind}[{index}]がオブジェクトではありません")
    normalized = dict(row)
    tier = str(normalized.get("observed_tier") or "")
    if tier not in TIER_ORDER:
        raise ValueError(f"results.{kind}[{index}]のobserved_tierが不正です: {tier}")
    champion_id = str(normalized.get("champion_id") or "")
    if not champion_id:
        raise ValueError(f"results.{kind}[{index}]にchampion_idがありません")
    for field in ("games", "wins", "losses"):
        if as_int(normalized.get(field)) is None:
            raise ValueError(f"results.{kind}[{index}]に{field}がありません")
    if as_float(normalized.get("win_rate")) is None:
        raise ValueError(f"results.{kind}[{index}]にwin_rateがありません")
    if kind == "champion_tier" and as_float(normalized.get("pick_rate")) is None:
        raise ValueError(f"results.{kind}[{index}]にpick_rateがありません")
    if kind == "champion_extremes" and str(normalized.get("direction") or "") not in {"high", "low"}:
        raise ValueError(f"results.{kind}[{index}]のdirectionが不正です")
    return normalized


def sort_rate(value: Any, fallback: float) -> float:
    number = as_float(value)
    return fallback if number is None else number


def select_rows(
    rows: Sequence[Mapping[str, Any]],
    *,
    limit: int,
    min_games: int,
    kind: str,
    direction: Optional[str] = None,
) -> tuple[dict[str, list[dict[str, Any]]], int]:
    grouped: defaultdict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        if direction is not None and str(row.get("direction") or "") != direction:
            continue
        if (as_int(row.get("games")) or 0) < min_games:
            continue
        grouped[str(row["observed_tier"])].append(dict(row))

    selected: dict[str, list[dict[str, Any]]] = {}
    duplicate_ids_skipped = 0
    for tier in TIER_ORDER:
        tier_rows = grouped.get(tier, [])
        if kind == "champion_tier":
            tier_rows.sort(
                key=lambda row: (
                    -(as_int(row.get("games")) or 0),
                    -(as_float(row.get("win_rate")) or -1),
                    str(row.get("champion_name") or ""),
                    str(row.get("champion_id") or ""),
                )
            )
        else:
            tier_rows.sort(
                key=lambda row: (
                    as_int(row.get("rank")) or 10**9,
                    -sort_rate(row.get("win_rate"), -1) if direction == "high" else sort_rate(row.get("win_rate"), 2),
                    -(as_int(row.get("games")) or 0),
                    str(row.get("champion_name") or ""),
                    str(row.get("champion_id") or ""),
                )
            )
        seen: set[str] = set()
        chosen: list[dict[str, Any]] = []
        for row in tier_rows:
            champion_id = str(row.get("champion_id") or "")
            if champion_id in seen:
                duplicate_ids_skipped += 1
                continue
            seen.add(champion_id)
            row["selected_rank"] = len(chosen) + 1
            chosen.append(row)
            if len(chosen) >= limit:
                break
        if chosen:
            selected[tier] = chosen
    return selected, duplicate_ids_skipped


def candidate_data(payload: Mapping[str, Any], limit: int) -> tuple[dict[str, dict[str, list[dict[str, Any]]]], dict[str, int]]:
    results = payload["results"]
    filters = payload["filters"]
    min_games = as_int(filters.get("min_games")) or 0
    champion_rows = [
        validate_row(row, "champion_tier", index)
        for index, row in enumerate(results["champion_tier"])
    ]
    extreme_rows = [
        validate_row(row, "champion_extremes", index)
        for index, row in enumerate(results["champion_extremes"])
    ]
    top_by_tier, top_duplicates = select_rows(
        champion_rows, limit=limit, min_games=min_games, kind="champion_tier"
    )
    high_by_tier, high_duplicates = select_rows(
        extreme_rows, limit=limit, min_games=min_games, kind="champion_extremes", direction="high"
    )
    low_by_tier, low_duplicates = select_rows(
        extreme_rows, limit=limit, min_games=min_games, kind="champion_extremes", direction="low"
    )
    by_champion: defaultdict[str, dict[str, list[dict[str, Any]]]] = defaultdict(
        lambda: {"top": [], "high": [], "low": []}
    )
    for category, grouped in (("top", top_by_tier), ("high", high_by_tier), ("low", low_by_tier)):
        for tier, rows in grouped.items():
            for row in rows:
                by_champion[str(row["champion_id"])][category].append(row)
    counts = {
        "top_rows": sum(len(rows) for rows in top_by_tier.values()),
        "high_rows": sum(len(rows) for rows in high_by_tier.values()),
        "low_rows": sum(len(rows) for rows in low_by_tier.values()),
        "duplicate_ids_skipped": top_duplicates + high_duplicates + low_duplicates,
    }
    return dict(by_champion), counts


def report_wikilink(analysis_path: Path) -> str:
    report_path = analysis_path.parent / "report.md"
    try:
        relative = report_path.relative_to(ROOT).with_suffix("")
    except ValueError as error:
        raise ValueError("解析レポートはVault内に置かれている必要があります") from error
    return f"[[{relative.as_posix()}|ランク帯別詳細レポート]]"


def format_integer(value: Any) -> str:
    number = as_int(value)
    return "不明" if number is None else f"{number:,}"


def format_percent(value: Any) -> str:
    number = as_float(value)
    return "不明" if number is None else f"{number * 100:.1f}%"


def format_record(row: Mapping[str, Any], *, include_pick_rate: bool) -> str:
    wins = format_integer(row.get("wins"))
    losses = format_integer(row.get("losses"))
    if include_pick_rate:
        return (
            f"| {row['observed_tier']} | {format_integer(row.get('selected_rank'))} | "
            f"{format_integer(row.get('games'))} | {format_percent(row.get('pick_rate'))} | "
            f"{wins}勝/{losses}敗 | {format_percent(row.get('win_rate'))} |"
        )
    return (
        f"| {row['observed_tier']} | {format_integer(row.get('selected_rank'))} | "
        f"{format_integer(row.get('games'))} | {wins}勝/{losses}敗 | {format_percent(row.get('win_rate'))} |"
    )


def render_block(
    *,
    data: Mapping[str, Sequence[Mapping[str, Any]]],
    analysis_path: Path,
    payload: Mapping[str, Any],
    selection_limit: int,
    source_ref: str,
) -> str:
    filters = payload["filters"]
    min_games = as_int(filters.get("min_games")) or 0
    generated_at = str(payload.get("generated_at") or "不明")
    generated_date = generated_at[:10] if len(generated_at) >= 10 else generated_at
    queue_id = filters.get("queue_id", "不明")
    tier_counts: dict[str, int] = {}
    scope_groups = filters.get("scope_groups")
    if isinstance(scope_groups, list):
        for scope in scope_groups:
            if not isinstance(scope, Mapping) or scope.get("scope") != "tier":
                continue
            tier = str(scope.get("observed_tier") or "")
            matches = as_int(scope.get("matches"))
            if tier in TIER_ORDER and matches is not None:
                tier_counts[tier] = matches
    snapshot = [f"{generated_date}生成", f"キュー{queue_id}", f"観測{len(tier_counts) or len(set(row.get('observed_tier') for rows in data.values() for row in rows))}帯"]
    if tier_counts and len(set(tier_counts.values())) == 1:
        snapshot.append(f"各{next(iter(tier_counts.values())):,}試合")
    selected_unique = as_int(filters.get("selected_unique_matches"))
    if selected_unique is not None:
        snapshot.append(f"統合後{selected_unique:,}試合")
    snapshot.append(f"min-games {min_games}")
    source_link = DEFAULT_SOURCE_BODY_LINK if source_ref == DEFAULT_SOURCE_REF else source_ref
    top_rows = list(data.get("top", []))
    high_rows = list(data.get("high", []))
    low_rows = list(data.get("low", []))
    lines = [
        START_MARKER,
        "## 観測ランク帯別チャンピオン候補",
        "",
        "- **スナップショット：** " + "、".join(snapshot) + f"、{report_wikilink(analysis_path)}。",
        "- **根拠：** " + source_link + f"、{SYNTHESIS_REF}。",
        "- **読み方：** `observed_tier` はその試合を発見したプレイヤーの収集時点の所属帯であり、10人全員の試合時ランクではない。以下は各帯の上位選択と、min-games以上で機械的に抽出した高低勝率の探索候補で、推奨・因果効果・有意差を示さない。",
        "",
    ]
    if top_rows:
        lines.extend(
            [
                f"### ピック数上位{selection_limit}に入った帯",
                "",
                "| 観測帯 | 帯内順位 | 試合数 | ピック率 | 勝敗 | 勝率 |",
                "| --- | ---: | ---: | ---: | --- | ---: |",
            ]
        )
        lines.extend(format_record(row, include_pick_rate=True) for row in top_rows)
        lines.append("")
    if high_rows:
        lines.extend(
            [
                f"### 高勝率候補（上位{selection_limit}）",
                "",
                "| 観測帯 | 候補順位 | 試合数 | 勝敗 | 勝率 |",
                "| --- | ---: | ---: | --- | ---: |",
            ]
        )
        lines.extend(format_record(row, include_pick_rate=False) for row in high_rows)
        lines.append("")
    if low_rows:
        lines.extend(
            [
                f"### 低勝率候補（下位{selection_limit}）",
                "",
                "| 観測帯 | 候補順位 | 試合数 | 勝敗 | 勝率 |",
                "| --- | ---: | ---: | --- | ---: |",
            ]
        )
        lines.extend(format_record(row, include_pick_rate=False) for row in low_rows)
        lines.append("")
    if not top_rows and not high_rows and not low_rows:
        lines.extend(["- **該当なし：** このスナップショットの選定候補には含まれない。", ""])
    lines.extend([END_MARKER])
    return "\n".join(lines)


def replace_or_insert_block(text: str, block: str) -> str:
    start = text.find(START_MARKER)
    end = text.find(END_MARKER)
    if start >= 0 or end >= 0:
        if start < 0 or end < 0 or end < start:
            raise ValueError("観測ランク帯別候補ブロックの開始・終了マーカーが不整合です")
        end += len(END_MARKER)
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


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--analysis", required=True, help="riot_ranked_tier_analyzer.pyが生成したanalysis.json")
    parser.add_argument("--entity-root", default=str(DEFAULT_ENTITY_ROOT), help="チャンピオンentityディレクトリ")
    parser.add_argument("--champions", help="同期対象のchampion_key、英字ID、タイトル、ファイル名をカンマ区切りで限定")
    parser.add_argument("--selection-limit", type=int, default=5, help="各帯・各分類の掲載上限（既定: 5）")
    parser.add_argument("--source-ref", default=DEFAULT_SOURCE_REF, help="entityのsourcesへ追加する原典要約Wikilink")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--dry-run", action="store_true", help="差分件数だけ確認し、書き込まない（既定）")
    mode.add_argument("--write", action="store_true", help="生成ブロックとsourcesをentityへ同期する")
    mode.add_argument("--check", action="store_true", help="entityが期待内容と一致するか検証する")
    return parser


def main(argv: Optional[Sequence[str]] = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        if args.selection_limit <= 0:
            raise ValueError("--selection-limitは正の整数が必要です")
        analysis_path = resolve_path(args.analysis)
        entity_root = resolve_path(args.entity_root)
        payload = load_analysis(analysis_path)
        catalog = entity_catalog(entity_root)
        data, row_counts = candidate_data(payload, args.selection_limit)
        candidate_ids = set(data)
        missing_entity_ids = sorted(candidate_ids - set(catalog))
        if missing_entity_ids:
            raise ValueError("候補に対応するchampion entityがありません: " + ", ".join(missing_entity_ids))
        if args.champions:
            selected_keys = select_entity_keys(catalog, args.champions)
        else:
            stale_keys = {key for key, entry in catalog.items() if START_MARKER in str(entry["text"])}
            selected_keys = sorted(
                candidate_ids | stale_keys,
                key=lambda value: (int(value) if value.isdigit() else 10**9, value),
            )
        updated = analysis_updated_date(payload)
        changes: list[tuple[Path, str]] = []
        for champion_key in selected_keys:
            entry = catalog[champion_key]
            original = str(entry["text"])
            block = render_block(
                data=data.get(champion_key, {"top": [], "high": [], "low": []}),
                analysis_path=analysis_path,
                payload=payload,
                selection_limit=args.selection_limit,
                source_ref=args.source_ref,
            )
            expected = ensure_source_and_updated(
                replace_or_insert_block(original, block), args.source_ref, updated
            )
            if expected != original:
                changes.append((entry["path"], expected))
        summary = {
            "script": SCRIPT_NAME,
            "mode": "write" if args.write else "check" if args.check else "dry-run",
            "analysis": str(analysis_path),
            "entities_detected": len(catalog),
            "candidate_champions": len(candidate_ids),
            "entities_selected": len(selected_keys),
            "entities_changed": len(changes),
            "selection_limit": args.selection_limit,
            "min_games": as_int(payload["filters"].get("min_games")),
            "queue_id": payload["filters"].get("queue_id"),
            **row_counts,
        }
        if args.check:
            print(json.dumps(summary, ensure_ascii=False, indent=2, sort_keys=True))
            if changes:
                print(
                    "不一致: " + ", ".join(str(path.relative_to(ROOT)) for path, _ in changes[:20]),
                    file=sys.stderr,
                )
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
