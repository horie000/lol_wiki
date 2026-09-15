#!/usr/bin/env python3
"""取得済みRiot Match-v5データからロール別のチーム内ゴールド獲得シェアを集計する。"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable, Mapping, Optional, Sequence

from riot_match_analysis import (
    KNOWN_ROLES,
    ScopedMatch,
    as_float,
    json_write,
    load_dataset,
    normalize_tiers,
    participant_views,
    patch_prefix,
    quantile,
    ratio,
    rows_to_csv,
    select_scopes,
)


SCRIPT_NAME = "scripts/riot_role_gold_share.py"
SCHEMA_VERSION = 1
ROOT = Path(__file__).resolve().parents[1]
ROLE_LABELS = {
    "TOP": "トップ",
    "JUNGLE": "ジャングル",
    "MIDDLE": "ミッド",
    "BOTTOM": "ボット",
    "UTILITY": "サポート",
}
DURATION_BANDS = (
    ("under-20", "20分未満", 0.0, 20.0),
    ("20-25", "20〜25分未満", 20.0, 25.0),
    ("25-30", "25〜30分未満", 25.0, 30.0),
    ("30-35", "30〜35分未満", 30.0, 35.0),
    ("35-plus", "35分以上", 35.0, None),
)

OVERALL_FIELDS = (
    "role",
    "role_label",
    "matches",
    "team_observations",
    "avg_gold_share",
    "pooled_gold_share",
    "median_gold_share",
    "p10_gold_share",
    "p25_gold_share",
    "p75_gold_share",
    "p90_gold_share",
    "avg_gold_earned",
    "median_gold_earned",
    "avg_gold_per_minute",
    "winner_avg_gold_share",
    "loser_avg_gold_share",
    "winner_minus_loser_share",
    "median_paired_winner_minus_loser_share",
)
GROUP_FIELDS = (
    "group",
    "group_label",
    "role",
    "role_label",
    "matches",
    "team_observations",
    "avg_gold_share",
    "pooled_gold_share",
    "median_gold_share",
    "p10_gold_share",
    "p90_gold_share",
    "avg_gold_earned",
    "avg_gold_per_minute",
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
    return path if path.is_absolute() else ROOT / path


def reject_raw_output(path: Path) -> None:
    raw_root = (ROOT / "raw").resolve()
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


def selected_fingerprint(scopes: Sequence[ScopedMatch]) -> str:
    """選択試合のID・本体hash・観測帯から、個人情報を含まない再現確認用hashを作る。"""
    unique = {scoped.match.match_id: scoped.match for scoped in scopes}
    digest = hashlib.sha256()
    for match_id in sorted(unique):
        match = unique[match_id]
        row = {
            "match_id": match.match_id,
            "payload_hash": match.payload_hash,
            "observed_tiers": sorted(match.effective_tiers),
        }
        digest.update(json.dumps(row, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8"))
        digest.update(b"\n")
    return digest.hexdigest()


def duration_band(seconds: float) -> tuple[str, str]:
    minutes = seconds / 60.0
    for key, label, lower, upper in DURATION_BANDS:
        if minutes >= lower and (upper is None or minutes < upper):
            return key, label
    return "unknown", "不明"


def finite_positive(value: Any) -> Optional[float]:
    number = as_float(value)
    if number is None or number <= 0 or not math.isfinite(number):
        return None
    return number


def extract_match_observations(scoped: ScopedMatch) -> tuple[list[dict[str, Any]], Optional[str]]:
    match = scoped.match
    if not match.is_complete():
        return [], "incomplete_match"
    duration_seconds = finite_positive(match.info.get("gameDuration"))
    if duration_seconds is None:
        return [], "missing_or_nonpositive_duration"

    by_team: defaultdict[str, list[Any]] = defaultdict(list)
    for view in participant_views(scoped):
        by_team[view.team_id].append(view)
    if len(by_team) != 2 or any(len(views) != 5 for views in by_team.values()):
        return [], "invalid_team_composition"

    prepared: list[tuple[str, bool, list[tuple[Any, float]], float]] = []
    for team_id, views in sorted(by_team.items()):
        roles = [view.role for view in views]
        if len(set(roles)) != len(KNOWN_ROLES) or set(roles) != set(KNOWN_ROLES):
            return [], "invalid_role_composition"
        outcomes = {view.win for view in views}
        if len(outcomes) != 1 or None in outcomes:
            return [], "unresolved_team_outcome"
        role_gold: list[tuple[Any, float]] = []
        for view in views:
            gold = finite_positive(view.raw.get("goldEarned"))
            if gold is None:
                return [], "missing_or_nonpositive_gold"
            role_gold.append((view, gold))
        team_gold = sum(gold for _, gold in role_gold)
        if team_gold <= 0:
            return [], "missing_or_nonpositive_team_gold"
        prepared.append((team_id, outcomes.pop() is True, role_gold, team_gold))

    if sorted(win for _, win, _, _ in prepared) != [False, True]:
        return [], "invalid_match_outcome"

    band_key, band_label = duration_band(duration_seconds)
    result: list[dict[str, Any]] = []
    for team_id, win, role_gold, team_gold in prepared:
        for view, gold in role_gold:
            time_played = finite_positive(view.raw.get("timePlayed"))
            gold_per_minute = ratio(gold, time_played / 60.0) if time_played else None
            result.append(
                {
                    "match_id": match.match_id,
                    "team_id": team_id,
                    "role": view.role,
                    "win": win,
                    "gold_earned": gold,
                    "team_gold_earned": team_gold,
                    "gold_share": gold / team_gold,
                    "gold_per_minute": gold_per_minute,
                    "duration_seconds": duration_seconds,
                    "duration_band": band_key,
                    "duration_band_label": band_label,
                    "patch": patch_prefix(match.game_version),
                    "observed_tier": scoped.observed_tier,
                    "start_date": match.start_date,
                }
            )
    return result, None


def collect_observations(
    scopes: Sequence[ScopedMatch],
    *,
    record_quality: bool,
) -> tuple[list[dict[str, Any]], dict[str, int]]:
    records: list[dict[str, Any]] = []
    stats: Counter[str] = Counter()
    for scoped in scopes:
        match_records, reason = extract_match_observations(scoped)
        if reason:
            if record_quality:
                stats[reason] += 1
            continue
        records.extend(match_records)
        stats["analysis_scope_entries"] += 1
    stats["participant_observations"] = len(records)
    stats["team_observations"] = len(records) // len(KNOWN_ROLES)
    stats["analysis_unique_matches"] = len({record["match_id"] for record in records})
    return records, dict(sorted(stats.items()))


def average(values: Iterable[Optional[float]]) -> Optional[float]:
    numbers = [value for value in values if value is not None]
    return sum(numbers) / len(numbers) if numbers else None


def summarize_group(records: Sequence[Mapping[str, Any]]) -> dict[str, Any]:
    shares = [float(record["gold_share"]) for record in records]
    gold = [float(record["gold_earned"]) for record in records]
    team_gold = [float(record["team_gold_earned"]) for record in records]
    gold_per_minute = [
        float(record["gold_per_minute"])
        for record in records
        if record.get("gold_per_minute") is not None
    ]
    return {
        "matches": len({record["match_id"] for record in records}),
        "team_observations": len(records),
        "avg_gold_share": average(shares),
        "pooled_gold_share": ratio(sum(gold), sum(team_gold)),
        "median_gold_share": quantile(shares, 0.5),
        "p10_gold_share": quantile(shares, 0.1),
        "p25_gold_share": quantile(shares, 0.25),
        "p75_gold_share": quantile(shares, 0.75),
        "p90_gold_share": quantile(shares, 0.9),
        "avg_gold_earned": average(gold),
        "median_gold_earned": quantile(gold, 0.5),
        "avg_gold_per_minute": average(gold_per_minute),
        "gold_per_minute_observations": len(gold_per_minute),
    }


def overall_rows(records: Sequence[Mapping[str, Any]]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    by_match_role: defaultdict[tuple[str, str], dict[bool, float]] = defaultdict(dict)
    for record in records:
        by_match_role[(str(record["match_id"]), str(record["role"]))][bool(record["win"])] = float(record["gold_share"])

    for role in KNOWN_ROLES:
        selected = [record for record in records if record["role"] == role]
        winners = [record for record in selected if record["win"] is True]
        losers = [record for record in selected if record["win"] is False]
        paired_differences = [
            outcomes[True] - outcomes[False]
            for (match_id, paired_role), outcomes in by_match_role.items()
            if paired_role == role and set(outcomes) == {False, True}
        ]
        row = {
            "role": role,
            "role_label": ROLE_LABELS[role],
            **summarize_group(selected),
            "winner_avg_gold_share": average(float(record["gold_share"]) for record in winners),
            "loser_avg_gold_share": average(float(record["gold_share"]) for record in losers),
            "winner_minus_loser_share": average(paired_differences),
            "median_paired_winner_minus_loser_share": quantile(paired_differences, 0.5),
        }
        rows.append(row)
    return rows


def grouped_rows(
    records: Sequence[Mapping[str, Any]],
    *,
    group_field: str,
    label_field: str,
    group_order: Optional[Sequence[str]] = None,
) -> list[dict[str, Any]]:
    values = list(group_order or sorted({str(record[group_field]) for record in records}))
    rows: list[dict[str, Any]] = []
    for value in values:
        group_records = [record for record in records if str(record[group_field]) == value]
        if not group_records:
            continue
        label = str(group_records[0][label_field])
        for role in KNOWN_ROLES:
            selected = [record for record in group_records if record["role"] == role]
            if not selected:
                continue
            rows.append(
                {
                    "group": value,
                    "group_label": label,
                    "role": role,
                    "role_label": ROLE_LABELS[role],
                    **summarize_group(selected),
                }
            )
    return rows


def outcome_rows(records: Sequence[Mapping[str, Any]]) -> list[dict[str, Any]]:
    transformed = []
    for record in records:
        copy = dict(record)
        copy["outcome"] = "WIN" if record["win"] else "LOSS"
        copy["outcome_label"] = "勝利チーム" if record["win"] else "敗北チーム"
        transformed.append(copy)
    return grouped_rows(
        transformed,
        group_field="outcome",
        label_field="outcome_label",
        group_order=("WIN", "LOSS"),
    )


def pct(value: Any, digits: int = 2) -> str:
    number = as_float(value)
    return "" if number is None else f"{number * 100:.{digits}f}%"


def pp(value: Any, digits: int = 2) -> str:
    number = as_float(value)
    return "" if number is None else f"{number * 100:+.{digits}f}pp"


def integer(value: Any) -> str:
    number = as_float(value)
    return "" if number is None else f"{number:,.0f}"


def decimal(value: Any, digits: int = 1) -> str:
    number = as_float(value)
    return "" if number is None else f"{number:,.{digits}f}"


def markdown_table(headers: Sequence[str], rows: Sequence[Sequence[Any]], align: Optional[Sequence[str]] = None) -> str:
    alignment = list(align or ("---",) * len(headers))
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join(alignment) + " |",
    ]
    for row in rows:
        lines.append("| " + " | ".join(str(value).replace("|", "\\|") for value in row) + " |")
    return "\n".join(lines)


def pivot_group_rows(rows: Sequence[Mapping[str, Any]]) -> list[list[str]]:
    by_group: defaultdict[str, dict[str, Mapping[str, Any]]] = defaultdict(dict)
    labels: dict[str, str] = {}
    order: list[str] = []
    for row in rows:
        group = str(row["group"])
        if group not in labels:
            order.append(group)
            labels[group] = str(row["group_label"])
        by_group[group][str(row["role"])] = row
    result: list[list[str]] = []
    for group in order:
        role_rows = by_group[group]
        match_count = max(int(row["matches"]) for row in role_rows.values())
        result.append(
            [labels[group], f"{match_count:,}"]
            + [pct(role_rows[role]["avg_gold_share"]) for role in KNOWN_ROLES]
        )
    return result


def render_report(
    *,
    overall: Sequence[Mapping[str, Any]],
    outcomes: Sequence[Mapping[str, Any]],
    durations: Sequence[Mapping[str, Any]],
    tiers: Sequence[Mapping[str, Any]],
    input_quality: Mapping[str, int],
    analysis_quality: Mapping[str, int],
    filter_stats: Mapping[str, int],
    selected_matches: Sequence[ScopedMatch],
    includes_cache: bool,
) -> str:
    eligible_matches = int(analysis_quality.get("analysis_unique_matches", 0))
    dates = sorted({entry.match.start_date for entry in selected_matches if entry.match.start_date})
    patches = sorted({patch_prefix(entry.match.game_version) for entry in selected_matches})
    ranked = sorted(overall, key=lambda row: -float(row["avg_gold_share"]))
    highest = ranked[0]
    lowest = ranked[-1]
    outcome_change = sorted(overall, key=lambda row: float(row["winner_minus_loser_share"] or 0))
    most_negative = outcome_change[0]
    most_positive = outcome_change[-1]

    duration_lookup = {(str(row["group"]), str(row["role"])): row for row in durations}
    short_long = []
    for role in KNOWN_ROLES:
        short = duration_lookup.get(("under-20", role))
        long = duration_lookup.get(("35-plus", role))
        if short and long:
            short_long.append((role, float(long["avg_gold_share"]) - float(short["avg_gold_share"])))
    duration_increase = max(short_long, key=lambda item: item[1]) if short_long else ("", 0.0)
    duration_decrease = min(short_long, key=lambda item: item[1]) if short_long else ("", 0.0)

    overall_table = markdown_table(
        ("ロール", "チーム観測", "平均シェア", "中央値", "P10〜P90", "プール比", "平均獲得G", "平均G/分"),
        [
            (
                row["role_label"],
                f"{int(row['team_observations']):,}",
                pct(row["avg_gold_share"]),
                pct(row["median_gold_share"]),
                f"{pct(row['p10_gold_share'])}〜{pct(row['p90_gold_share'])}",
                pct(row["pooled_gold_share"]),
                integer(row["avg_gold_earned"]),
                decimal(row["avg_gold_per_minute"]),
            )
            for row in overall
        ],
        ("---", "---:", "---:", "---:", "---:", "---:", "---:", "---:"),
    )
    outcome_table = markdown_table(
        ("ロール", "勝利側", "敗北側", "勝利−敗北", "ペア差中央値"),
        [
            (
                row["role_label"],
                pct(row["winner_avg_gold_share"]),
                pct(row["loser_avg_gold_share"]),
                pp(row["winner_minus_loser_share"]),
                pp(row["median_paired_winner_minus_loser_share"]),
            )
            for row in overall
        ],
        ("---", "---:", "---:", "---:", "---:"),
    )
    duration_table = markdown_table(
        ("試合時間", "試合", *(ROLE_LABELS[role] for role in KNOWN_ROLES)),
        pivot_group_rows(durations),
        ("---", "---:", "---:", "---:", "---:", "---:", "---:"),
    )
    tier_table = markdown_table(
        ("観測ランク帯", "ユニーク試合", *(ROLE_LABELS[role] for role in KNOWN_ROLES)),
        pivot_group_rows(tiers),
        ("---", "---:", "---:", "---:", "---:", "---:", "---:"),
    )
    quality_table = markdown_table(
        ("項目", "件数"),
        (
            ("入力ファイル", f"{int(input_quality.get('input_files', 0)):,}"),
            ("入力レコード", f"{int(input_quality.get('input_records', 0)):,}"),
            ("重複レコード", f"{int(input_quality.get('duplicate_match', 0)):,}"),
            ("重複除去後のユニーク試合", f"{int(input_quality.get('unique_matches', 0)):,}"),
            ("キュー等の条件適用後", f"{int(filter_stats.get('selected_unique_matches', 0)):,}"),
            ("ロール・ゴールド集計対象", f"{eligible_matches:,}"),
            ("不完全試合の除外", f"{int(analysis_quality.get('incomplete_match', 0)):,}"),
            ("ロール構成不正の除外", f"{int(analysis_quality.get('invalid_role_composition', 0)):,}"),
            ("ゴールド欠損等の除外", f"{int(analysis_quality.get('missing_or_nonpositive_gold', 0)):,}"),
        ),
        ("---", "---:"),
    )

    input_description = (
        "`raw/sources/riot-ranked-matches/` の完成済み `matches.jsonl` 4本"
        if not includes_cache
        else "`raw/sources/riot-ranked-matches/`（収集キャッシュを含むローカルMatch-v5データ）"
    )
    unknown_tier_note = (
        "`UNKNOWN` は完成済み一覧に含まれないキャッシュ由来の試合を主に表す。"
        if any(str(row.get("group")) == "UNKNOWN" for row in tiers)
        else "今回の正規入力では `UNKNOWN` の観測帯はなかった。"
    )
    input_limit = (
        "- キャッシュを含む入力は、各ランク帯の完成済み1,000試合だけでなく収集時の候補試合も含む。完成済み一覧だけの再集計は別の感度分析となる。"
        if includes_cache
        else "- 完成済み一覧は各観測ランク帯1,000件を選んだ標本であり、帯内の全試合を無作為抽出したものではない。"
    )
    next_sensitivity = (
        "- 完成済み `matches.jsonl` だけの4ランク帯均等標本と、キャッシュを含む全候補標本を比較する。"
        if includes_cache
        else "- キャッシュを含む全候補標本との感度差を、同じ指標定義で継続確認する。"
    )

    lines = [
        "# ロール別ゴールド獲得シェア分析",
        "",
        "## 結論",
        "",
        f"チーム内の累積獲得ゴールドに占める割合は、{highest['role_label']}が平均{pct(highest['avg_gold_share'])}で最も高く、{lowest['role_label']}が{pct(lowest['avg_gold_share'])}で最も低かった。5ロールの平均シェアは各チーム内で合計100%になる。",
        f"勝利側と敗北側の差が最もプラスだったのは{most_positive['role_label']}（{pp(most_positive['winner_minus_loser_share'])}）、最もマイナスだったのは{most_negative['role_label']}（{pp(most_negative['winner_minus_loser_share'])}）だった。これは勝利の原因ではなく、試合終了時の資源配分と試合展開が同時に反映された記述差である。",
        f"20分未満から35分以上への変化では、{ROLE_LABELS.get(duration_increase[0], duration_increase[0])}が{pp(duration_increase[1])}、{ROLE_LABELS.get(duration_decrease[0], duration_decrease[0])}が{pp(duration_decrease[1])}だった。",
        "",
        "## 指標の定義",
        "",
        "ユーザー指定の「ゴールドの所持率」は、Match-v5の最終スコアにある `goldEarned` を用い、各参加者の累積獲得ゴールドを同じチーム5人の累積獲得ゴールド合計で割った「チーム内ゴールド獲得シェア」として操作的に定義した。`goldEarned` は未使用の現在ゴールドではなく、購入に使った分も含む累積値である。",
        "",
        "主結果の平均シェアは、各チームで割合を計算してからチーム観測を等しい重みで平均したマクロ平均である。「プール比」はロールの獲得ゴールド総和をチーム総ゴールド総和で割るため、ゴールド総量の多い試合をより重く扱う。",
        "",
        "## 解析条件",
        "",
        f"- 入力：{input_description}",
        f"- キュー：`420`、重複処理：試合ID単位、全体集計：`tier_mode=all`",
        f"- 集計対象：{eligible_matches:,}試合、{eligible_matches * 2:,}チーム、各ロール{eligible_matches * 2:,}観測",
        f"- 期間：{dates[0] if dates else '不明'}〜{dates[-1] if dates else '不明'}（UTC日付）、パッチ数：{len(patches)}",
        "- 適格条件：完全試合、2チーム各5人、各チームに5ロールが1人ずつ、正の `goldEarned` と試合時間、勝敗が解決可能",
        "",
        "## 全体集計",
        "",
        overall_table,
        "",
        "平均と中央値が近いため代表値は大きく乖離していないが、P10〜P90にはチャンピオン、試合展開、パッチ、プレイヤー構成の違いが含まれる。ロール間の順位はこの混合集計内の記述に限られる。",
        "",
        "## 勝敗別",
        "",
        outcome_table,
        "",
        "各試合で勝利チームと敗北チームを対応させた差である。勝利チームは総ゴールド自体も多い傾向があるため、ここで比較するのは絶対量ではなく、そのチーム内でどのロールへ比率的に配分されたかである。",
        "",
        "## 試合時間帯別",
        "",
        duration_table,
        "",
        "時間帯は `[0,20) / [20,25) / [25,30) / [30,35) / [35,∞)` 分で区切った。試合時間は試合展開と勝敗の後に確定するため、時間経過そのものの因果効果とは解釈しない。",
        "",
        "## 観測ランク帯別の感度確認",
        "",
        tier_table,
        "",
        f"観測ランク帯は収集時点で試合を発見したプレイヤーの所属帯であり、試合時点の10人全員のランクではない。同じ試合が複数帯に含まれ得るため、この表の試合数を合算してはならない。{unknown_tier_note}",
        "",
        "## データ品質",
        "",
        quality_table,
        "",
        "## 解釈上の限界",
        "",
        "- Match-v5の最終スコアだけを使うため、10分・15分時点など途中時点のシェアや、ゴールドを得た経路は分からない。",
        f"- 複数パッチ（今回{len(patches)}パッチ）、複数の観測ランク帯、チャンピオンとプレイヤーの構成を合算した未調整の記述統計である。",
        "- 勝敗別・時間帯別の差は、キル、オブジェクト、ファーム、構成、試合時間などの交絡を含み、特定ロールへゴールドを集める戦術の因果効果を示さない。",
        input_limit,
        "",
        "## 未解決事項",
        "",
        "- Timelineデータを収集し、固定時点のゴールドシェアと変化量をロール別に比較する。",
        "- パッチとチャンピオン構成を固定し、ロール差が再現するか確認する。",
        next_sensitivity,
        "",
    ]
    return "\n".join(lines)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", action="append", required=True, help="入力ファイルまたはディレクトリ。複数指定可")
    parser.add_argument("--output", default="reports/riot-role-gold-share", help="レポート出力先")
    parser.add_argument("--queue-id", type=int, default=420, help="対象キューID（既定: 420）")
    parser.add_argument("--tiers", help="観測ランク帯をカンマ区切りで限定")
    parser.add_argument("--patch", help="gameVersionの前方一致フィルター")
    parser.add_argument("--date-from", help="試合開始日の下限（UTC、YYYY-MM-DD）")
    parser.add_argument("--date-to", help="試合開始日の上限（UTC、YYYY-MM-DD）")
    parser.add_argument("--format", default="markdown,csv,json", help="markdown,csv,json の組み合わせ")
    parser.add_argument("--overwrite", action="store_true", help="同一runディレクトリが存在する場合に上書きする")
    parser.add_argument("--dry-run", action="store_true", help="入力、条件、適格試合数だけを検証して出力しない")
    return parser


def parse_formats(value: str) -> set[str]:
    formats = {item.strip().lower() for item in value.split(",") if item.strip()}
    invalid = formats - {"markdown", "csv", "json"}
    if invalid or not formats:
        raise ValueError(f"--format の不正な値: {', '.join(sorted(invalid or {'空'}))}")
    return formats


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        formats = parse_formats(args.format)
        tiers_filter = normalize_tiers(args.tiers)
        date_from = parse_date(args.date_from, "--date-from")
        date_to = parse_date(args.date_to, "--date-to")
        if date_from and date_to and date_from > date_to:
            raise ValueError("--date-from は --date-to 以下である必要があります")

        inputs = [Path(value) for value in args.input]
        dataset = load_dataset(inputs)
        selected, filter_stats = select_scopes(
            dataset.matches,
            queue_id=args.queue_id,
            tier_mode="all",
            tiers=tiers_filter,
            patch=args.patch,
            date_from=date_from,
            date_to=date_to,
        )
        observations, analysis_quality = collect_observations(selected, record_quality=True)
        fingerprint = selected_fingerprint(selected)
        includes_cache = any(".cache" in path.parts for path in (Path(value) for value in dataset.input_files))
        dry_summary = {
            "input_files": len(dataset.input_files),
            "input_records": dataset.quality.counts.get("input_records", 0),
            "unique_matches": len(dataset.matches),
            "selected_unique_matches": filter_stats.get("selected_unique_matches", 0),
            "eligible_matches": analysis_quality.get("analysis_unique_matches", 0),
            "team_observations": analysis_quality.get("team_observations", 0),
            "excluded": {
                key: value
                for key, value in analysis_quality.items()
                if key not in {"analysis_scope_entries", "analysis_unique_matches", "participant_observations", "team_observations"}
            },
            "queue_id": args.queue_id,
            "tier_mode": "all",
            "selected_fingerprint_sha256": fingerprint,
            "input_mode": "cache-inclusive" if includes_cache else "finalized-matches-jsonl",
        }
        if args.dry_run:
            print(json.dumps(dry_summary, ensure_ascii=False, indent=2, sort_keys=True))
            return 0
        if not observations:
            raise ValueError("条件を満たすロール別ゴールド観測がありません")

        observed_scopes, observed_filter_stats = select_scopes(
            dataset.matches,
            queue_id=args.queue_id,
            tier_mode="observed",
            tiers=tiers_filter,
            patch=args.patch,
            date_from=date_from,
            date_to=date_to,
        )
        observed_records, observed_quality = collect_observations(observed_scopes, record_quality=False)

        overall = overall_rows(observations)
        outcomes = outcome_rows(observations)
        durations = grouped_rows(
            observations,
            group_field="duration_band",
            label_field="duration_band_label",
            group_order=tuple(band[0] for band in DURATION_BANDS),
        )
        tier_order = ("IRON", "BRONZE", "SILVER", "GOLD", "UNKNOWN")
        tiers = grouped_rows(
            observed_records,
            group_field="observed_tier",
            label_field="observed_tier",
            group_order=tier_order + tuple(sorted({str(record["observed_tier"]) for record in observed_records} - set(tier_order))),
        )

        generated_at = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
        output_root = resolve_root_path(args.output)
        reject_raw_output(output_root)
        run_dir = create_run_dir(output_root, args.overwrite)
        filters = {
            "queue_id": args.queue_id,
            "tier_mode": "all",
            "tiers": sorted(tiers_filter),
            "patch": args.patch,
            "date_from": date_from,
            "date_to": date_to,
        }
        analysis = {
            "schema_version": SCHEMA_VERSION,
            "generated_at": generated_at,
            "definition": "participant.goldEarned / sum(team participants' goldEarned), averaged across eligible teams",
            "filters": filters,
            "selected_fingerprint_sha256": fingerprint,
            "input_mode": "cache-inclusive" if includes_cache else "finalized-matches-jsonl",
            "results": {
                "overall": overall,
                "by_outcome": outcomes,
                "by_duration": durations,
                "by_observed_tier": tiers,
            },
        }
        quality = {
            "input": {"counts": dict(sorted(dataset.quality.counts.items()))},
            "filters": filter_stats,
            "analysis": analysis_quality,
            "observed_tier_filters": observed_filter_stats,
            "observed_tier_analysis": observed_quality,
            "selected": dry_summary,
        }
        manifest = {
            "schema_version": SCHEMA_VERSION,
            "script": SCRIPT_NAME,
            "generated_at": generated_at,
            "inputs": [str(resolve_root_path(value)) for value in args.input],
            "input_file_count": len(dataset.input_files),
            "selected_fingerprint_sha256": fingerprint,
            "input_mode": "cache-inclusive" if includes_cache else "finalized-matches-jsonl",
            "arguments": filters,
            "outputs": [],
        }

        if "csv" in formats:
            rows_to_csv(run_dir / "role-gold-share.csv", overall, OVERALL_FIELDS)
            rows_to_csv(run_dir / "role-gold-share-by-outcome.csv", outcomes, GROUP_FIELDS)
            rows_to_csv(run_dir / "role-gold-share-by-duration.csv", durations, GROUP_FIELDS)
            rows_to_csv(run_dir / "role-gold-share-by-observed-tier.csv", tiers, GROUP_FIELDS)
            manifest["outputs"].extend(
                [
                    "role-gold-share.csv",
                    "role-gold-share-by-outcome.csv",
                    "role-gold-share-by-duration.csv",
                    "role-gold-share-by-observed-tier.csv",
                ]
            )
        if "json" in formats:
            json_write(run_dir / "analysis.json", analysis)
            manifest["outputs"].append("analysis.json")
        json_write(run_dir / "quality.json", quality)
        manifest["outputs"].append("quality.json")
        if "markdown" in formats:
            (run_dir / "report.md").write_text(
                render_report(
                    overall=overall,
                    outcomes=outcomes,
                    durations=durations,
                    tiers=tiers,
                    input_quality=dataset.quality.counts,
                    analysis_quality=analysis_quality,
                    filter_stats=filter_stats,
                    selected_matches=selected,
                    includes_cache=includes_cache,
                ),
                encoding="utf-8",
            )
            manifest["outputs"].append("report.md")
        json_write(run_dir / "manifest.json", manifest)
        print(f"解析完了: {run_dir}")
        print(json.dumps({"eligible_matches": dry_summary["eligible_matches"], "outputs": manifest["outputs"]}, ensure_ascii=False))
        return 0
    except (OSError, RuntimeError, ValueError, KeyError) as error:
        print(f"エラー: {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
