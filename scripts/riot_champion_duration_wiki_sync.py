#!/usr/bin/env python3
"""試合時間帯別の実測結果をチャンピオンentityへ同期する。"""

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
SCRIPT_NAME = "scripts/riot_champion_duration_wiki_sync.py"
DEFAULT_ENTITY_ROOT = ROOT / "wiki/entities/champions"
DEFAULT_SOURCE_REF = "[[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]"
SYNTHESIS_REF = "[[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]]"
BLOCK_START = "<!-- power-spike-match:start -->"
BLOCK_END = "<!-- power-spike-match:end -->"


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
    match = re.search(rf"^{re.escape(key)}:\s*[\"']?([^\"'\n]+)[\"']?\s*$", text[:end], flags=re.MULTILINE)
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


def analysis_updated_date(payload: Mapping[str, Any]) -> str:
    raw_value = str(payload.get("generated_at") or "").strip()
    if not raw_value:
        raise ValueError("analysis.jsonにgenerated_atがありません")
    try:
        generated_at = datetime.fromisoformat(raw_value.replace("Z", "+00:00"))
    except ValueError as error:
        raise ValueError("analysis.jsonのgenerated_atを日時として解釈できません") from error
    if generated_at.tzinfo is None:
        generated_at = generated_at.replace(tzinfo=ZoneInfo("UTC"))
    return generated_at.astimezone(ZoneInfo("Asia/Tokyo")).date().isoformat()


def load_analysis(path: Path) -> tuple[dict[str, Any], dict[str, Any]]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, Mapping):
        raise ValueError("champion-duration-winrate.jsonのルートはオブジェクトである必要があります")
    rows = payload.get("rows")
    method = payload.get("method")
    duration = payload.get("duration")
    if not isinstance(rows, list) or not isinstance(method, Mapping) or not isinstance(duration, Mapping):
        raise ValueError("時間帯別分析にmethod、duration、rowsが必要です")
    bins = method.get("bins")
    if not isinstance(bins, list) or not bins:
        raise ValueError("時間帯別分析にmethod.binsが必要です")
    labels: list[str] = []
    for index, raw_bin in enumerate(bins):
        if not isinstance(raw_bin, Mapping) or not str(raw_bin.get("label") or ""):
            raise ValueError(f"method.bins[{index}]のlabelがありません")
        labels.append(str(raw_bin["label"]))
    normalized_rows: dict[str, dict[str, Any]] = {}
    for index, raw_row in enumerate(rows):
        if not isinstance(raw_row, Mapping):
            raise ValueError(f"rows[{index}]がオブジェクトではありません")
        row = dict(raw_row)
        champion_id = str(row.get("champion_id") or "")
        if not champion_id:
            raise ValueError(f"rows[{index}]にchampion_idがありません")
        if champion_id in normalized_rows:
            raise ValueError(f"rowsにchampion_idが重複しています: {champion_id}")
        if as_int(row.get("overall_games")) is None or as_float(row.get("overall_win_rate")) is None:
            raise ValueError(f"rows[{index}]にoverall_gamesまたはoverall_win_rateがありません")
        if not isinstance(row.get("bins"), Mapping):
            raise ValueError(f"rows[{index}]にbinsがありません")
        for label in labels:
            bin_row = row["bins"].get(label)
            if not isinstance(bin_row, Mapping):
                raise ValueError(f"rows[{index}].binsに{label}がありません")
            if as_int(bin_row.get("games")) is None or as_float(bin_row.get("win_rate")) is None:
                raise ValueError(f"rows[{index}].bins.{label}にgamesまたはwin_rateがありません")
        normalized_rows[champion_id] = row
    metadata_path = path.parent / "analysis.json"
    report_path = path.parent / "report.md"
    if not metadata_path.exists() or not report_path.exists():
        raise ValueError(f"時間帯別分析にanalysis.jsonとreport.mdが必要です: {path.parent}")
    metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
    if not isinstance(metadata, Mapping):
        raise ValueError(f"analysis.jsonのルートがオブジェクトではありません: {metadata_path}")
    analysis_updated_date(metadata)
    return {"payload": dict(payload), "rows": normalized_rows, "labels": labels}, dict(metadata)


def report_wikilink(analysis_path: Path) -> str:
    report_path = analysis_path.parent / "report.md"
    if not report_path.exists():
        return ""
    report_rel = report_path.relative_to(ROOT).with_suffix("").as_posix()
    return f"[[{report_rel}|詳細レポート]]"


def render_block(
    *,
    row: Optional[Mapping[str, Any]],
    labels: Sequence[str],
    analysis_path: Path,
    metadata: Mapping[str, Any],
    payload: Mapping[str, Any],
    source_ref: str,
) -> str:
    generated_date = analysis_updated_date(metadata)
    method = payload.get("method")
    duration = payload.get("duration")
    queue_id = method.get("queue_id", "不明") if isinstance(method, Mapping) else "不明"
    games = as_int(duration.get("games")) if isinstance(duration, Mapping) else None
    snapshot = f"{generated_date}生成、キュー{queue_id}"
    if games is not None:
        snapshot += f"、完全試合{games:,}件"
    report_link = report_wikilink(analysis_path)
    if report_link:
        snapshot += f"、{report_link}"

    lines = [
        BLOCK_START,
        "## 試合時間別の観測",
        "",
    ]
    if row is None:
        lines.extend(
            [
                f"- **スナップショット：** {snapshot}。",
                "- **観測分類：** データなし",
                "- **対象試合：** データなし",
                "- **時間帯別勝率：** データなし",
                "- **最高帯：** データなし",
                "- **判定根拠：** 対象チャンピオンの行が分析結果にありません。",
            ]
        )
    else:
        overall_games = as_int(row.get("overall_games"))
        overall_rate = percent(row.get("overall_win_rate"))
        bin_values = []
        for label in labels:
            bin_row = row["bins"][label]
            bin_values.append(f"{label} {percent(bin_row.get('win_rate'))}（n={as_int(bin_row.get('games')):,}）")
        peak_bin = str(row.get("peak_bin") or "データなし")
        gap = as_float(row.get("gap_pp"))
        gap_text = "不明" if gap is None else f"{gap:.1f}ポイント"
        lines.extend(
            [
                f"- **スナップショット：** {snapshot}。",
                f"- **観測分類：** {row.get('classification') or '不明'}",
                f"- **対象試合：** {overall_games:,}試合、全体勝率 {overall_rate}",
                f"- **時間帯別勝率：** {'、'.join(bin_values)}",
                f"- **最高帯：** {peak_bin}（判定差 {gap_text}）",
                f"- **判定根拠：** {row.get('classification_reason') or '分析結果の判定根拠なし'}。",
            ]
        )
    lines.extend(
        [
            f"- **解釈上の限界：** {SYNTHESIS_REF} に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。",
            f"- **出典：** {source_ref}",
            "",
            BLOCK_END,
            "",
        ]
    )
    return "\n".join(lines)


def replace_or_insert_block(text: str, block: str) -> str:
    start = text.find(BLOCK_START)
    end = text.find(BLOCK_END)
    if start >= 0 or end >= 0:
        if start < 0 or end < 0 or end < start:
            raise ValueError("試合時間別観測ブロックの開始・終了マーカーが不整合です")
        end += len(BLOCK_END)
        return text[:start].rstrip() + "\n\n" + block.rstrip() + "\n\n" + text[end:].lstrip()
    for heading in ("## 関連ページ", "## 出典"):
        marker = "\n" + heading + "\n"
        position = text.find(marker)
        if position >= 0:
            return text[:position].rstrip() + "\n\n" + block.rstrip() + "\n" + text[position:]
    return text.rstrip() + "\n\n" + block.rstrip() + "\n"


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


def sync_entities(
    *,
    catalog: Mapping[str, Mapping[str, Any]],
    rows: Mapping[str, Mapping[str, Any]],
    labels: Sequence[str],
    analysis_path: Path,
    metadata: Mapping[str, Any],
    payload: Mapping[str, Any],
    source_ref: str,
    selected_keys: Sequence[str],
    write: bool,
) -> list[tuple[Path, str]]:
    updated = analysis_updated_date(metadata)
    changes: list[tuple[Path, str]] = []
    for champion_key in selected_keys:
        entry = catalog[champion_key]
        block = render_block(
            row=rows.get(champion_key),
            labels=labels,
            analysis_path=analysis_path,
            metadata=metadata,
            payload=payload,
            source_ref=source_ref,
        )
        path = Path(entry["path"])
        original = path.read_text(encoding="utf-8")
        expected = ensure_source_and_updated(replace_or_insert_block(original, block), source_ref, updated)
        if expected != original:
            changes.append((path, expected))
    if write:
        for path, expected in changes:
            path.write_text(expected, encoding="utf-8")
    return changes


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--analysis", required=True, help="champion-duration-winrate.json")
    parser.add_argument("--entity-root", default=str(DEFAULT_ENTITY_ROOT), help="チャンピオンentityディレクトリ")
    parser.add_argument("--champions", help="同期対象のchampion_key、英字ID、タイトル、ファイル名をカンマ区切りで限定")
    parser.add_argument("--source-ref", default=DEFAULT_SOURCE_REF, help="entityのsourcesへ追加する原典要約Wikilink")
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--dry-run", action="store_true", help="差分件数だけ確認し、書き込まない（既定）")
    mode.add_argument("--write", action="store_true", help="生成ブロックとsourcesをentityへ同期する")
    mode.add_argument("--check", action="store_true", help="entityが期待内容と一致するか検証する")
    return parser


def main(argv: Optional[Sequence[str]] = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        analysis_path = resolve_path(args.analysis)
        entity_root = resolve_path(args.entity_root)
        loaded, metadata = load_analysis(analysis_path)
        payload = loaded["payload"]
        rows = loaded["rows"]
        labels = loaded["labels"]
        catalog = entity_catalog(entity_root)
        missing_ids = sorted(set(rows) - set(catalog))
        if missing_ids:
            raise ValueError("分析結果に対応するchampion entityがありません: " + ", ".join(missing_ids))
        if args.champions:
            selected_keys = select_entity_keys(catalog, args.champions)
        else:
            stale_keys = {key for key, entry in catalog.items() if BLOCK_START in str(entry["text"])}
            selected_keys = sorted(
                set(rows) | stale_keys,
                key=lambda value: (int(value) if value.isdigit() else 10**9, value),
            )
        changes = sync_entities(
            catalog=catalog,
            rows=rows,
            labels=labels,
            analysis_path=analysis_path,
            metadata=metadata,
            payload=payload,
            source_ref=args.source_ref,
            selected_keys=selected_keys,
            write=args.write,
        )
        duration = payload.get("duration")
        summary = {
            "script": SCRIPT_NAME,
            "mode": "write" if args.write else "check" if args.check else "dry-run",
            "analysis": str(analysis_path.relative_to(ROOT)),
            "entities_detected": len(catalog),
            "entities_selected": len(selected_keys),
            "analysis_rows": len(rows),
            "entities_changed": len(changes),
            "generated_at": metadata.get("generated_at"),
            "games": as_int(duration.get("games")) if isinstance(duration, Mapping) else None,
            "bin_count": len(labels),
        }
        print(json.dumps(summary, ensure_ascii=False, indent=2, sort_keys=True))
        if args.check and changes:
            print(
                "不一致: " + ", ".join(str(path.relative_to(ROOT)) for path, _ in changes[:20]),
                file=sys.stderr,
            )
            return 1
        return 0
    except (OSError, ValueError, json.JSONDecodeError) as error:
        print(f"エラー: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
