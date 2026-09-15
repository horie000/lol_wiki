#!/usr/bin/env python3
"""指定チャンピオンの味方組み合わせと相手別勝率を抽出する。"""

from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Mapping, Optional, Sequence

from riot_match_analysis import (
    DEFAULT_DATA_DRAGON,
    DataDragonCatalog,
    Dataset,
    ParticipantView,
    ScopeGroup,
    ScopedMatch,
    as_int,
    champion_label,
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
    safe_slug,
    scope_groups,
    select_scopes,
)


SCRIPT_NAME = "scripts/riot_champion_query.py"
SCHEMA_VERSION = 1
CSV_FIELDS = (
    "scope", "observed_tier", "patch", "patches", "target_champion_id", "target_champion_name", "target_role",
    "related_champion_id", "related_champion_name", "related_role", "opponent_scope", "same_role_match",
    "games", "wins", "losses", "target_win_rate", "pick_rate", "pick_rate_denominator", "min_games_applied", "rank",
)


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


def resolve_target(
    value: str,
    dataset: Dataset,
    catalog: DataDragonCatalog,
) -> tuple[str, str]:
    candidates: dict[str, set[str]] = defaultdict(set)
    for match in dataset.matches:
        for raw in match.participants:
            if not isinstance(raw, Mapping):
                continue
            champion_id = as_int(raw.get("championId"))
            if champion_id is None:
                continue
            key = str(champion_id)
            candidates[key].add(str(raw.get("championName") or key))
            candidates[normalize_alias(raw.get("championName"))].add(key)
    direct = as_int(value)
    resolved = set(catalog.champion_candidates(value))
    if direct is not None:
        resolved.add(str(direct))
    resolved.update(candidates.get(normalize_alias(value), set()))
    resolved = {candidate for candidate in resolved if candidate.isdigit()}
    if not resolved:
        raise ValueError(f"チャンピオンを解決できません: {value}")
    if len(resolved) > 1:
        labels = sorted({name for champion_id in resolved for name in candidates.get(champion_id, set())})
        raise ValueError(f"チャンピオン名が曖昧です: {value} -> {', '.join(sorted(resolved))} ({', '.join(labels)})")
    champion_id = next(iter(resolved))
    names = candidates.get(champion_id, set())
    champion_name = sorted(names)[0] if names else value
    return champion_id, champion_name


def create_run_dir(output_root: Path, champion_id: str, champion_name: str) -> Path:
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    run_dir = output_root / f"run-{stamp}-{safe_slug(champion_name or champion_id)}"
    if run_dir.exists():
        raise RuntimeError(f"出力ディレクトリが存在します: {run_dir}")
    run_dir.mkdir(parents=True, exist_ok=True)
    return run_dir


def complete_entries(entries: Sequence[ScopedMatch], include_incomplete: bool) -> list[ScopedMatch]:
    if include_incomplete:
        return list(entries)
    return [entry for entry in entries if entry.match.is_complete()]


def group_by_patch(entries: Sequence[ScopedMatch]) -> dict[str, list[ScopedMatch]]:
    grouped: defaultdict[str, list[ScopedMatch]] = defaultdict(list)
    for entry in entries:
        grouped[patch_prefix(entry.match.game_version)].append(entry)
    return dict(sorted(grouped.items()))


def relation_rows(
    group: ScopeGroup,
    entries: Sequence[ScopedMatch],
    *,
    target_id: str,
    target_name: str,
    target_role: Optional[str],
    opponent_scope: str,
    min_games: int,
    include_incomplete: bool,
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    allies: list[dict[str, Any]] = []
    opponents: list[dict[str, Any]] = []
    eligible_entries = complete_entries(entries, include_incomplete)
    patches = sorted({patch_prefix(entry.match.game_version) for entry in eligible_entries})
    patch_label = patches[0] if len(patches) == 1 else "ALL"
    target_counts: defaultdict[str, int] = defaultdict(int)
    ally_values: defaultdict[tuple[str, str, str, str, str], list[bool]] = defaultdict(list)
    opponent_values: defaultdict[tuple[str, str, str, str, str, bool], list[bool]] = defaultdict(list)
    for entry in eligible_entries:
        views = participant_views(entry)
        targets = [
            view
            for view in views
            if str(view.champion_id or "") == target_id and (target_role is None or view.role == target_role)
        ]
        for target in targets:
            target_counts[target.role] += 1
            for related in views:
                if related.participant_id == target.participant_id:
                    continue
                related_id = str(related.champion_id or normalize_alias(related.champion_name))
                related_name = champion_label(related)
                target_key = (target.role, related_id, related_name, related.role, target.role)
                if related.team_id == target.team_id:
                    ally_values[target_key].append(target.win is True)
                else:
                    same_role = target.role != "UNKNOWN" and related.role == target.role
                    if opponent_scope == "same-role" and not same_role:
                        continue
                    opponent_key = (target.role, related_id, related_name, related.role, target.role, same_role)
                    opponent_values[opponent_key].append(target.win is True)
    for key, outcomes in ally_values.items():
        if len(outcomes) < min_games:
            continue
        role, related_id, related_name, related_role, _ = key
        wins = sum(outcomes)
        denominator = target_counts[role]
        allies.append(
            {
                "scope": group.scope,
                "observed_tier": group.observed_tier,
                "patch": patch_label,
                "patches": patches,
                "target_champion_id": target_id,
                "target_champion_name": target_name,
                "target_role": role,
                "related_champion_id": related_id,
                "related_champion_name": related_name,
                "related_role": related_role,
                "opponent_scope": "",
                "same_role_match": "",
                "games": len(outcomes),
                "wins": wins,
                "losses": len(outcomes) - wins,
                "target_win_rate": ratio(wins, len(outcomes)),
                "pick_rate": ratio(len(outcomes), denominator),
                "pick_rate_denominator": denominator,
                "min_games_applied": min_games,
            }
        )
    for key, outcomes in opponent_values.items():
        if len(outcomes) < min_games:
            continue
        role, related_id, related_name, related_role, _, same_role = key
        wins = sum(outcomes)
        denominator = target_counts[role]
        opponents.append(
            {
                "scope": group.scope,
                "observed_tier": group.observed_tier,
                "patch": patch_label,
                "patches": patches,
                "target_champion_id": target_id,
                "target_champion_name": target_name,
                "target_role": role,
                "related_champion_id": related_id,
                "related_champion_name": related_name,
                "related_role": related_role,
                "opponent_scope": opponent_scope,
                "same_role_match": same_role,
                "games": len(outcomes),
                "wins": wins,
                "losses": len(outcomes) - wins,
                "target_win_rate": ratio(wins, len(outcomes)),
                "pick_rate": ratio(len(outcomes), denominator),
                "pick_rate_denominator": denominator,
                "min_games_applied": min_games,
            }
        )
    return allies, opponents


def rank_rows(rows: Sequence[Mapping[str, Any]], *, ascending: bool, limit: int) -> list[dict[str, Any]]:
    partitions: defaultdict[tuple[str, str, str], list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        copied = dict(row)
        key = (str(copied.get("scope") or ""), str(copied.get("observed_tier") or ""), str(copied.get("target_role") or ""))
        partitions[key].append(copied)
    selected: list[dict[str, Any]] = []
    for key in sorted(partitions, key=lambda value: (0 if value[0] == "overall" else 1, value[1], value[2])):
        partition = partitions[key]
        ordered = sorted(
            partition,
            key=lambda row: (
                float(row.get("target_win_rate")) if row.get("target_win_rate") is not None else (float("inf") if ascending else float("-inf")),
                -int(row.get("games") or 0),
                str(row.get("related_champion_name") or ""),
            ),
            reverse=False,
        )
        if not ascending:
            ordered = sorted(
                partition,
                key=lambda row: (
                    -(float(row.get("target_win_rate")) if row.get("target_win_rate") is not None else float("inf")),
                    -int(row.get("games") or 0),
                    str(row.get("related_champion_name") or ""),
                ),
            )
        for index, row in enumerate(ordered[:limit], start=1):
            row["rank"] = index
            selected.append(row)
    return selected


def render_report(
    *,
    target_name: str,
    target_id: str,
    query: Mapping[str, Any],
    allies: Sequence[Mapping[str, Any]],
    opponents: Sequence[Mapping[str, Any]],
    quality: Mapping[str, Any],
) -> str:
    lines = [
        f"# {target_name}（{target_id}）チャンピオン指定クエリ",
        "",
        f"- スクリプト：`{SCRIPT_NAME}`",
        f"- 最小ゲーム数：`{query['min_games']}`",
        f"- 対面範囲：`{query['opponent_scope']}`",
        "",
        "> [!warning] 解釈上の注意",
        "> 勝率は対象チャンピオン側の観測勝率であり、味方組み合わせの因果効果や相手チャンピオンの確定的なカウンターを意味しない。観測ランク帯、パッチ、サンプル数を確認すること。",
        "",
        "## 味方組み合わせ：対象側勝率の高い順",
        "",
        markdown_table(
            allies,
            (("rank", "順位"), ("related_champion_name", "味方"), ("target_role", "対象ロール"), ("games", "試合"), ("target_win_rate", "対象側勝率"), ("pick_rate", "組み合わせ率")),
        ),
        "",
        "## 相手別：対象側勝率の低い順",
        "",
        markdown_table(
            opponents,
            (("rank", "順位"), ("related_champion_name", "相手"), ("target_role", "対象ロール"), ("related_role", "相手ロール"), ("games", "試合"), ("target_win_rate", "対象側勝率")),
        ),
        "",
        "## クエリ条件",
        "",
        "```json",
        json.dumps(query, ensure_ascii=False, indent=2, sort_keys=True),
        "```",
        "",
        "## データ品質",
        "",
        "```json",
        json.dumps(quality, ensure_ascii=False, indent=2, sort_keys=True),
        "```",
        "",
    ]
    return "\n".join(lines)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", action="append", required=True, help="入力ファイルまたはディレクトリ。複数指定可")
    parser.add_argument("--champion", required=True, help="対象チャンピオンのIDまたは日本語・英語表示名")
    parser.add_argument("--mode", default="ally-pairs,opponents", help="ally-pairs、opponents の組み合わせ")
    parser.add_argument("--opponent-scope", choices=("same-role", "all-enemy"), default="same-role")
    parser.add_argument("--role", help="対象チャンピオンのロールを限定")
    parser.add_argument("--queue-id", type=int, default=420, help="対象キューID（既定: 420）")
    parser.add_argument("--tier-mode", choices=("all", "observed"), default="observed")
    parser.add_argument("--tiers", help="観測ランク帯をカンマ区切りで限定")
    parser.add_argument("--patch", help="gameVersionの前方一致フィルター")
    parser.add_argument("--date-from", help="試合開始日の下限（UTC、YYYY-MM-DD）")
    parser.add_argument("--date-to", help="試合開始日の上限（UTC、YYYY-MM-DD）")
    parser.add_argument("--min-games", type=int, default=15, help="ランキングへ掲載する最小試合数（既定: 15）")
    parser.add_argument("--top", type=int, default=20, help="味方組み合わせの上位件数（既定: 20）")
    parser.add_argument("--bottom", type=int, default=20, help="相手別の下位件数（既定: 20）")
    parser.add_argument("--include-incomplete", action="store_true", help="不完全試合を含める")
    parser.add_argument("--format", default="markdown,csv,json", help="markdown,csv,json の組み合わせ")
    parser.add_argument("--data-dragon", default=str(DEFAULT_DATA_DRAGON), help="Data Dragonアーカイブ")
    parser.add_argument("--output", default="reports/riot-champion-query", help="クエリ出力先")
    parser.add_argument("--dry-run", action="store_true", help="入力と条件だけ検証して出力しない")
    return parser


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        if args.min_games <= 0 or args.top <= 0 or args.bottom <= 0:
            raise ValueError("--min-games、--top、--bottom は正の値が必要です")
        modes = {mode.strip() for mode in args.mode.split(",") if mode.strip()}
        if not modes or not modes.issubset({"ally-pairs", "opponents"}):
            raise ValueError("--mode は ally-pairs と opponents の組み合わせが必要です")
        target_role = normalize_role(args.role) if args.role else None
        if target_role == "UNKNOWN":
            raise ValueError(f"不明なロールです: {args.role}")
        date_from = parse_date(args.date_from, "--date-from")
        date_to = parse_date(args.date_to, "--date-to")
        if date_from and date_to and date_from > date_to:
            raise ValueError("--date-from は --date-to 以下である必要があります")
        formats = parse_formats(args.format)
        dataset = load_dataset([Path(value) for value in args.input])
        catalog = DataDragonCatalog(Path(args.data_dragon)).load()
        target_id, target_name = resolve_target(args.champion, dataset, catalog)
        scopes, filter_stats = select_scopes(
            dataset.matches,
            queue_id=args.queue_id,
            tier_mode=args.tier_mode,
            tiers=normalize_tiers(args.tiers),
            patch=args.patch,
            date_from=date_from,
            date_to=date_to,
        )
        groups = scope_groups(scopes, args.tier_mode)
        query = {
            "script": SCRIPT_NAME,
            "schema_version": SCHEMA_VERSION,
            "champion_id": target_id,
            "champion_name": target_name,
            "mode": sorted(modes),
            "opponent_scope": args.opponent_scope,
            "role": target_role,
            "queue_id": args.queue_id,
            "tier_mode": args.tier_mode,
            "tiers": sorted(normalize_tiers(args.tiers)),
            "patch": args.patch,
            "date_from": date_from,
            "date_to": date_to,
            "min_games": args.min_games,
            "top": args.top,
            "bottom": args.bottom,
            "include_incomplete": args.include_incomplete,
            "selected_scopes": len(scopes),
            "selected_unique_matches": len({entry.match.match_id for entry in scopes}),
        }
        if args.dry_run:
            print(json.dumps({"query": query, "input_files": len(dataset.input_files), "quality": dataset.quality.as_dict()}, ensure_ascii=False, indent=2, sort_keys=True))
            return 0
        all_allies: list[dict[str, Any]] = []
        all_opponents: list[dict[str, Any]] = []
        for group in groups:
            allies, opponents = relation_rows(
                group,
                group.entries,
                target_id=target_id,
                target_name=target_name,
                target_role=target_role,
                opponent_scope=args.opponent_scope,
                min_games=args.min_games,
                include_incomplete=args.include_incomplete,
            )
            all_allies.extend(allies)
            all_opponents.extend(opponents)
        selected_allies = rank_rows(all_allies, ascending=False, limit=args.top) if "ally-pairs" in modes else []
        selected_opponents = rank_rows(all_opponents, ascending=True, limit=args.bottom) if "opponents" in modes else []
        query["result_counts"] = {"ally_pairs": len(selected_allies), "opponents": len(selected_opponents)}
        quality = {
            "input": dataset.quality.as_dict(),
            "filters": filter_stats,
            "selected": query,
            "result_candidates": {"ally_pairs": len(all_allies), "opponents": len(all_opponents)},
        }
        output_root = resolve_root_path(args.output)
        reject_raw_output(output_root)
        run_dir = create_run_dir(output_root, target_id, target_name)
        payload = {
            "schema_version": SCHEMA_VERSION,
            "generated_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
            "query": query,
            "results": {"ally_pairs": selected_allies, "opponents": selected_opponents},
        }
        outputs: list[str] = []
        if "csv" in formats:
            if "ally-pairs" in modes:
                rows_to_csv(run_dir / "ally-pairs.csv", selected_allies, CSV_FIELDS)
                outputs.append("ally-pairs.csv")
            if "opponents" in modes:
                rows_to_csv(run_dir / "opponents.csv", selected_opponents, CSV_FIELDS)
                outputs.append("opponents.csv")
        json_write(run_dir / "quality.json", quality)
        outputs.append("quality.json")
        if "markdown" in formats:
            (run_dir / "report.md").write_text(
                render_report(
                    target_name=target_name,
                    target_id=target_id,
                    query=query,
                    allies=selected_allies,
                    opponents=selected_opponents,
                    quality=quality,
                ),
                encoding="utf-8",
            )
            outputs.append("report.md")
        outputs.insert(0, "query.json")
        query["outputs"] = outputs
        json_write(run_dir / "query.json", payload)
        print(f"クエリ完了: {run_dir}")
        print(json.dumps({"target": target_name, "ally_pairs": len(selected_allies), "opponents": len(selected_opponents), "outputs": outputs}, ensure_ascii=False))
        return 0
    except (OSError, RuntimeError, ValueError, KeyError) as error:
        print(f"エラー: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
