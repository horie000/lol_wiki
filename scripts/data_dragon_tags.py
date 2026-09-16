#!/usr/bin/env python3
"""Data Dragon 由来の個別ページへ ``data-dragon`` タグを同期する。

チャンピオン、アイテム、ルーン、サモナースペルの個別ページは、表示用に
別データセットを統合している場合でも、大元のレコードが Data Dragon 配布
アーカイブである。このスクリプトは各エンティティのフロントマターに共通
タグを付与し、後からページを再生成しても由来を検索できる状態を検証する。

Usage:
    python3 scripts/data_dragon_tags.py --write
    python3 scripts/data_dragon_tags.py --check
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ENTITY_ROOT = ROOT / "wiki" / "entities"
ENTITY_DIRS = ("champions", "items", "runes", "spells")
TAG = "data-dragon"
SOURCE_TOKEN = "src-2026-09-14-dragontail-16-18-1"


def page_paths() -> list[Path]:
    paths: list[Path] = []
    for directory in ENTITY_DIRS:
        paths.extend(sorted((ENTITY_ROOT / directory).glob("*.md")))
    if not paths:
        raise ValueError("Data Dragon 個別ページが見つかりません")
    return paths


def tags_match(page: str) -> re.Match[str]:
    match = re.search(r"^tags:\n(?P<body>(?:  - .*\n)+)", page, flags=re.MULTILINE)
    if match is None:
        raise ValueError("tags フロントマターがありません")
    return match


def current_tags(page: str) -> list[str]:
    match = tags_match(page)
    return re.findall(r"^  - (.+)$", match.group("body"), flags=re.MULTILINE)


def replace_tags(page: str) -> str:
    match = tags_match(page)
    tags = current_tags(page)
    if TAG in tags:
        return page
    tags.append(TAG)
    replacement = "tags:\n" + "\n".join(f"  - {tag}" for tag in tags) + "\n"
    return page[: match.start()] + replacement + page[match.end() :]


def with_updated_date(page: str) -> str:
    return re.sub(
        r"^updated: .*?$",
        f"updated: {date.today().isoformat()}",
        page,
        count=1,
        flags=re.MULTILINE,
    )


def check_pages(paths: list[Path]) -> tuple[list[Path], Counter[str]]:
    errors: list[Path] = []
    counts: Counter[str] = Counter()
    for path in paths:
        page = path.read_text(encoding="utf-8")
        tags = current_tags(page)
        relative_dir = path.parent.name
        counts[relative_dir] += 1
        if tags.count(TAG) != 1 or SOURCE_TOKEN not in page:
            errors.append(path)
    return errors, counts


def write_pages(paths: list[Path]) -> int:
    changed = 0
    for path in paths:
        original = path.read_text(encoding="utf-8")
        tagged = replace_tags(original)
        if tagged == original:
            continue
        updated = with_updated_date(tagged)
        if updated != original:
            path.write_text(updated, encoding="utf-8")
            changed += 1
    return changed


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--write", action="store_true", help="data-dragon タグを付与する")
    mode.add_argument("--check", action="store_true", help="タグとData Dragon出典を検証する")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        paths = page_paths()
        if args.write:
            print(f"updated Data Dragon entity pages: {write_pages(paths)}")
            return 0
        errors, counts = check_pages(paths)
        if errors:
            for path in errors:
                print(f"Data Dragonタグまたは出典が不一致: {path.relative_to(ROOT)}", file=sys.stderr)
            return 1
        print(f"data-dragon check passed: {len(paths)} pages")
        for directory in ENTITY_DIRS:
            print(f"{directory}: {counts[directory]}")
        return 0
    except (OSError, ValueError) as error:
        print(f"data-dragon tag error: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
