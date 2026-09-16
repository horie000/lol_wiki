#!/usr/bin/env python3
"""最新の派生レポートをentityへ同期してからWikiのLintを実行する。"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from collections.abc import Callable, Mapping
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional


ROOT = Path(__file__).resolve().parents[1]

STATIC_CHECKERS = (
    ROOT / "scripts" / "data_dragon_tags.py",
    ROOT / "scripts" / "gold_efficiency.py",
    ROOT / "scripts" / "item_synergy.py",
    ROOT / "scripts" / "power_spikes.py",
)

STATIC_WRITERS = (
    ROOT / "scripts" / "gold_efficiency.py",
    ROOT / "scripts" / "item_synergy.py",
    ROOT / "scripts" / "power_spikes.py",
)


@dataclass(frozen=True)
class ReportSpec:
    label: str
    root: Path
    input_name: str
    sync_script: Path
    required_outputs: tuple[str, ...]
    validator: Callable[[Mapping[str, Any], Path], bool]


@dataclass(frozen=True)
class CompletedRun:
    spec: ReportSpec
    run_dir: Path
    input_path: Path
    generated_at: datetime


def parse_timestamp(value: Any) -> Optional[datetime]:
    raw_value = str(value or "").strip()
    if not raw_value:
        return None
    try:
        parsed = datetime.fromisoformat(raw_value.replace("Z", "+00:00"))
    except ValueError:
        return None
    if parsed.tzinfo is None:
        parsed = parsed.replace(tzinfo=timezone.utc)
    return parsed.astimezone(timezone.utc)


def read_json(path: Path) -> Mapping[str, Any]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, Mapping):
        raise ValueError(f"JSONのルートがオブジェクトではありません: {path}")
    return payload


def declared_output_exists(run_dir: Path, output: Any) -> bool:
    if not isinstance(output, str) or not output:
        return False
    relative = Path(output.rstrip("/"))
    if relative.is_absolute() or ".." in relative.parts:
        return False
    target = run_dir / relative
    return target.is_dir() if output.endswith("/") else target.exists()


def has_list(value: Any, key: str) -> bool:
    return isinstance(value, Mapping) and isinstance(value.get(key), list)


def valid_duration_report(_: Mapping[str, Any], run_dir: Path) -> bool:
    try:
        payload = read_json(run_dir / "champion-duration-winrate.json")
    except (OSError, ValueError, json.JSONDecodeError):
        return False
    return (
        isinstance(payload.get("method"), Mapping)
        and isinstance(payload.get("duration"), Mapping)
        and isinstance(payload.get("rows"), list)
        and bool(payload.get("rows"))
    )


def valid_build_report(payload: Mapping[str, Any], _: Path) -> bool:
    return all(
        has_list(payload, key)
        for key in ("results", "status_group_results", "build_results", "theoretical_build_results")
    )


def valid_matchup_report(payload: Mapping[str, Any], _: Path) -> bool:
    return (
        has_list(payload, "candidates")
        and isinstance(payload.get("target_games_by_role"), Mapping)
        and isinstance(payload.get("target_names"), Mapping)
    )


def valid_rune_report(payload: Mapping[str, Any], _: Path) -> bool:
    results = payload.get("results")
    return (
        isinstance(results, Mapping)
        and isinstance(results.get("rune_sets"), list)
        and isinstance(results.get("champions"), list)
        and isinstance(payload.get("filters"), Mapping)
    )


def valid_tier_report(payload: Mapping[str, Any], _: Path) -> bool:
    results = payload.get("results")
    filters = payload.get("filters")
    return (
        isinstance(results, Mapping)
        and isinstance(results.get("champion_tier"), list)
        and isinstance(results.get("champion_extremes"), list)
        and isinstance(filters, Mapping)
        and str(filters.get("tier_mode") or "").lower() == "observed"
    )


REPORT_SPECS = (
    ReportSpec(
        label="試合時間帯・パワースパイク",
        root=ROOT / "reports" / "riot-ranked-match-analysis",
        input_name="champion-duration-winrate.json",
        sync_script=ROOT / "scripts" / "riot_champion_duration_wiki_sync.py",
        required_outputs=("analysis.json", "quality.json", "report.md", "champion-duration-winrate.json"),
        validator=valid_duration_report,
    ),
    ReportSpec(
        label="チャンピオン別ビルド",
        root=ROOT / "reports" / "riot-champion-item-synergy",
        input_name="analysis.json",
        sync_script=ROOT / "scripts" / "riot_champion_build_wiki_sync.py",
        required_outputs=("analysis.json", "quality.json", "report.md", "champions/"),
        validator=valid_build_report,
    ),
    ReportSpec(
        label="コンボ・カウンターピック",
        root=ROOT / "reports" / "riot-champion-matchups",
        input_name="analysis.json",
        sync_script=ROOT / "scripts" / "riot_champion_matchup_wiki_sync.py",
        required_outputs=("analysis.json", "quality.json", "report.md", "champions/"),
        validator=valid_matchup_report,
    ),
    ReportSpec(
        label="チャンピオン別ルーン",
        root=ROOT / "reports" / "riot-ranked-match-analysis",
        input_name="analysis.json",
        sync_script=ROOT / "scripts" / "riot_champion_rune_wiki_sync.py",
        required_outputs=("analysis.json", "quality.json", "report.md"),
        validator=valid_rune_report,
    ),
    ReportSpec(
        label="観測ランク帯別チャンピオン候補",
        root=ROOT / "reports" / "riot-ranked-tier-analysis",
        input_name="analysis.json",
        sync_script=ROOT / "scripts" / "riot_champion_tier_wiki_sync.py",
        required_outputs=("analysis.json", "quality.json", "report.md"),
        validator=valid_tier_report,
    ),
)


def relative_path(path: Path) -> str:
    try:
        return path.relative_to(ROOT).as_posix()
    except ValueError:
        return str(path)


def latest_completed_run(spec: ReportSpec) -> Optional[CompletedRun]:
    candidates: list[CompletedRun] = []
    if not spec.root.exists():
        return None
    for run_dir in spec.root.glob("run-*"):
        if not run_dir.is_dir():
            continue
        manifest_path = run_dir / "manifest.json"
        input_path = run_dir / spec.input_name
        if not manifest_path.exists() or not input_path.exists():
            continue
        try:
            manifest = read_json(manifest_path)
            payload = read_json(run_dir / "analysis.json")
            outputs = manifest.get("outputs")
            if not isinstance(outputs, list) or not all(
                declared_output_exists(run_dir, output) for output in outputs
            ):
                continue
            if not all((run_dir / required.rstrip("/")).exists() for required in spec.required_outputs):
                continue
            generated_at = parse_timestamp(manifest.get("generated_at"))
            if generated_at is None or not spec.validator(payload, run_dir):
                continue
        except (OSError, ValueError, json.JSONDecodeError):
            continue
        candidates.append(
            CompletedRun(
                spec=spec,
                run_dir=run_dir,
                input_path=input_path,
                generated_at=generated_at,
            )
        )
    return max(candidates, key=lambda run: (run.generated_at, run.run_dir.name), default=None)


def run_command(label: str, script: Path, arguments: list[str]) -> int:
    command = [sys.executable, str(script), *arguments]
    print(f"[lint] {label}", flush=True)
    result = subprocess.run(command, cwd=ROOT)
    return result.returncode


def run_report_command(run: CompletedRun, mode: str) -> int:
    return run_command(
        f"{run.spec.label}: {mode} ({relative_path(run.input_path)})",
        run.spec.sync_script,
        ["--analysis", str(run.input_path), mode],
    )


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--check-only",
        action="store_true",
        help="entityや生成物を更新せず、最新レポートに対する期待内容だけを検証する",
    )
    return parser


def main(argv: Optional[list[str]] = None) -> int:
    args = build_parser().parse_args(argv)
    runs: list[CompletedRun] = []
    for spec in REPORT_SPECS:
        run = latest_completed_run(spec)
        if run is None:
            print(f"[lint] {spec.label}: 完了済みレポートなし（同期をスキップ）", flush=True)
            continue
        runs.append(run)
        print(
            f"[lint] {spec.label}: 最新 {relative_path(run.run_dir)} "
            f"（generated_at={run.generated_at.isoformat()}）",
            flush=True,
        )

    if not args.check_only:
        for run in runs:
            result = run_report_command(run, "--dry-run")
            if result:
                return result
        for generator in STATIC_WRITERS:
            result = run_command(f"派生entity生成: {relative_path(generator)} --write", generator, ["--write"])
            if result:
                return result
        for run in runs:
            result = run_report_command(run, "--write")
            if result:
                return result

    for checker in STATIC_CHECKERS:
        result = run_command(f"派生entity検証: {relative_path(checker)} --check", checker, ["--check"])
        if result:
            return result
    for run in runs:
        result = run_report_command(run, "--check")
        if result:
            return result
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
