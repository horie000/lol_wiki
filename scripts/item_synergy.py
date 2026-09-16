#!/usr/bin/env python3
"""アイテムを相性のよいチャンピオン系統へ分類し、タグを同期する。

Data Dragon のアイテムレコードには、特定のチャンピオン名やビルド勝率の
データはない。そのため、このスクリプトは原典の ``tags``、数値ステータス、
説明文に現れる効果シグナルから、チャンピオンの役割・戦闘特性に対応する
候補タグを再現可能な規則で付与する。タグは exact build recommendation
ではなく、Obsidian の検索・絞り込み用の分類である。

Usage:
    python3 scripts/item_synergy.py --write
    python3 scripts/item_synergy.py --check
    python3 scripts/item_synergy.py --summary
"""

from __future__ import annotations

import argparse
import html
import json
import re
import sys
import tarfile
from collections import Counter
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Mapping


ROOT = Path(__file__).resolve().parents[1]
ARCHIVE_PATH = ROOT / "raw" / "sources" / "dragontail-16.18.1.tgz"
ITEM_MEMBER = "16.18.1/data/ja_JP/item.json"
ITEM_DIR = ROOT / "wiki" / "entities" / "items"
TAG_PREFIX = "champion-synergy-"

# 表示順を固定すると、ページ差分とレビューが安定する。
ROLE_ORDER = (
    "marksman",
    "fighter",
    "assassin",
    "mage",
    "tank",
    "support",
    "jungler",
    "utility",
)

RELEVANT_TAGS = {
    "AbilityHaste",
    "Active",
    "Armor",
    "ArmorPenetration",
    "AttackSpeed",
    "Aura",
    "Consumable",
    "CooldownReduction",
    "CriticalStrike",
    "Damage",
    "GoldPer",
    "Health",
    "HealthRegen",
    "Jungle",
    "Lane",
    "LifeSteal",
    "MagicPenetration",
    "MagicResist",
    "Mana",
    "ManaRegen",
    "NonbootsMovement",
    "OnHit",
    "Shield",
    "Slow",
    "SpellBlock",
    "SpellDamage",
    "SpellVamp",
    "Stealth",
    "Tenacity",
    "Trinket",
    "Vision",
}


@dataclass(frozen=True)
class Classification:
    item_id: str
    tags: tuple[str, ...]
    scores: tuple[tuple[str, int], ...]


def strip_tags(value: str) -> str:
    return html.unescape(re.sub(r"<[^>]+>", "", value or ""))


def load_items() -> dict[str, Mapping[str, object]]:
    if not ARCHIVE_PATH.exists():
        raise FileNotFoundError(f"原典アーカイブがありません: {ARCHIVE_PATH}")
    with tarfile.open(ARCHIVE_PATH, mode="r:gz") as archive:
        member = archive.getmember(ITEM_MEMBER)
        extracted = archive.extractfile(member)
        if extracted is None:
            raise RuntimeError(f"アイテム原典を開けません: {ITEM_MEMBER}")
        payload = json.load(extracted)
    data = payload.get("data")
    if not isinstance(data, dict):
        raise ValueError("item.json の data がオブジェクトではありません")
    return {str(item_id): item for item_id, item in data.items() if isinstance(item, Mapping)}


def normalized_stats(item: Mapping[str, object]) -> dict[str, float]:
    raw_stats = item.get("stats")
    if not isinstance(raw_stats, Mapping):
        return {}
    result: dict[str, float] = {}
    for key, value in raw_stats.items():
        if isinstance(value, (int, float)) and value != 0:
            result[str(key)] = float(value)
    return result


def meaningful_item(item: Mapping[str, object], raw_tags: set[str], stats: Mapping[str, float]) -> bool:
    """説明・ステータス・既知タグのいずれかがある実質的なレコードか判定する。"""

    description = strip_tags(str(item.get("description") or "")).strip()
    plaintext = strip_tags(str(item.get("plaintext") or "")).strip()
    if description or plaintext or stats:
        return True
    return bool(raw_tags & RELEVANT_TAGS)


def add(scores: Counter[str], role: str, points: int) -> None:
    if points > 0:
        scores[role] += points


def classify_item(item_id: str, item: Mapping[str, object]) -> Classification:
    raw_tags = {str(tag) for tag in item.get("tags", []) if isinstance(tag, str)}
    stats = normalized_stats(item)
    description = strip_tags(str(item.get("description") or ""))
    scores: Counter[str] = Counter()

    # マップ専用・内部用レコードには、役割を無理に推測しない。
    if not meaningful_item(item, raw_tags, stats):
        return Classification(item_id, (f"{TAG_PREFIX}utility",), (("utility", 1),))
    # 内部用のランダム／プレースホルダー項目は、タグに列挙された全能力を
    # 実際に付与する通常アイテムではないため、汎用用途へ寄せる。
    if not stats and ("？" in description or len(raw_tags) >= 10):
        return Classification(item_id, (f"{TAG_PREFIX}utility",), (("utility", 1),))

    # Jungle のみで効果を持たない初期アイテムや、ポーション・トリンケットは
    # 戦闘系タグではなく、ジャングラー／汎用用途として扱う。
    jungle_only = "Jungle" in raw_tags and not stats and not (
        raw_tags & {"Damage", "SpellDamage", "CriticalStrike", "AttackSpeed", "OnHit"}
    )
    if jungle_only:
        # ジャングル用初期装備の LifeSteal / SpellVamp はチャンピオンの
        # 恒常的なビルド特性ではなく、モンスター狩り用の原典タグである。
        # そのため通常の物理・魔法スコアへ流さない。
        jungle_roles = ["jungler"]
        if raw_tags & {"Consumable", "Trinket", "Stealth", "Vision"}:
            jungle_roles.append("utility")
        tags = tuple(f"{TAG_PREFIX}{role}" for role in jungle_roles)
        return Classification(item_id, tags, tuple((role, 4) for role in jungle_roles))

    # 物理攻撃・通常攻撃系。
    if "CriticalStrike" in raw_tags or "FlatCritChanceMod" in stats:
        add(scores, "marksman", 3)
        add(scores, "fighter", 1)
    if "AttackSpeed" in raw_tags or "PercentAttackSpeedMod" in stats:
        add(scores, "marksman", 2)
        add(scores, "fighter", 1)
    if "LifeSteal" in raw_tags:
        add(scores, "marksman", 3)
        add(scores, "fighter", 2)
    if "OnHit" in raw_tags:
        add(scores, "marksman", 3)
        add(scores, "fighter", 2)
    if "Damage" in raw_tags or "FlatPhysicalDamageMod" in stats:
        add(scores, "fighter", 2)
    if "ArmorPenetration" in raw_tags:
        add(scores, "assassin", 3)
        add(scores, "fighter", 1)

    # 魔法・スキル系。
    if "SpellDamage" in raw_tags or "FlatMagicDamageMod" in stats:
        add(scores, "mage", 3)
    if "MagicPenetration" in raw_tags:
        add(scores, "mage", 3)
        add(scores, "assassin", 1)
    if "SpellVamp" in raw_tags and ("SpellDamage" in raw_tags or "FlatMagicDamageMod" in stats):
        add(scores, "mage", 1)
    if "Mana" in raw_tags and ("SpellDamage" in raw_tags or "FlatMagicDamageMod" in stats):
        add(scores, "mage", 2)
    if "AbilityHaste" in raw_tags or "CooldownReduction" in raw_tags:
        if "SpellDamage" in raw_tags or "FlatMagicDamageMod" in stats:
            add(scores, "mage", 1)
        if "Damage" in raw_tags or "FlatPhysicalDamageMod" in stats:
            add(scores, "fighter", 1)

    # 耐久・前衛系。
    if "Health" in raw_tags or "FlatHPPoolMod" in stats:
        # 体力だけを持つレーン開始アイテムは前衛候補とするが、魔力＋体力の
        # メイジや、支援用体力アイテムを自動的にタンク扱いしない。
        if not (
            ("SpellDamage" in raw_tags or "FlatMagicDamageMod" in stats)
            and not (raw_tags & {"Armor", "SpellBlock", "MagicResist", "Tenacity"})
        ):
            add(scores, "tank", 2)
        if "Damage" in raw_tags or "FlatPhysicalDamageMod" in stats:
            add(scores, "fighter", 2)
    if raw_tags & {"Armor", "SpellBlock", "MagicResist", "Tenacity"}:
        add(scores, "tank", 2)
        if "Damage" in raw_tags or "FlatPhysicalDamageMod" in stats:
            add(scores, "fighter", 1)
    if "Slow" in raw_tags:
        if "Damage" in raw_tags or "FlatPhysicalDamageMod" in stats:
            add(scores, "fighter", 1)
        if "SpellDamage" in raw_tags or "FlatMagicDamageMod" in stats:
            add(scores, "mage", 1)

    # 味方支援・視界・収入系。ManaRegen 単独だけではサポートと断定しない。
    if "GoldPer" in raw_tags:
        add(scores, "support", 3)
    elif "Aura" in raw_tags:
        # Sunfire 等の自己オーラはサポート専用ではないため、味方効果の
        # テキストが見つかった場合に後段で加点する。
        add(scores, "support", 1)
    elif "Vision" in raw_tags:
        add(scores, "support", 2)
    elif "ManaRegen" in raw_tags and not (
        raw_tags & {"Damage", "SpellDamage", "Armor", "SpellBlock", "MagicResist"}
    ):
        add(scores, "support", 1)
    if re.search(r"味方|味方1体|回復効果|シールドを付与|味方の", description):
        add(scores, "support", 3)
    if "Aura" in raw_tags and raw_tags & {"Health", "Armor", "SpellBlock", "MagicResist"}:
        add(scores, "tank", 1)

    # 消耗品・視界装備は、他の役割シグナルがあっても汎用タグを併記する。
    if raw_tags & {"Consumable", "Trinket", "Stealth", "Vision"}:
        add(scores, "utility", 3)

    # Jungle は原典で明示されたポジション情報なので、他の役割タグと併記する。
    if "Jungle" in raw_tags and not jungle_only:
        add(scores, "jungler", 4)

    if not scores:
        add(scores, "utility", 1)

    max_score = max(scores.values())
    # 最高点から1点以内の役割を併記する。3点以上の役割が一つもない場合は
    # 最上位だけを採用し、弱い偶然のシグナルによる過剰タグ付けを防ぐ。
    selected = {
        role for role, score in scores.items() if score >= 3 and score >= max_score - 1
    }
    if not selected:
        selected = {max(scores, key=lambda role: (scores[role], -ROLE_ORDER.index(role)))}
    # 原典が Jungle を明示しているレコードは、他の役割スコアが高くても
    # ジャングラー向け候補であることを失わないよう必ずタグへ残す。
    if "Jungle" in raw_tags:
        selected.add("jungler")
    ordered_roles = tuple(role for role in ROLE_ORDER if role in selected)
    tags = tuple(f"{TAG_PREFIX}{role}" for role in ordered_roles)
    return Classification(item_id, tags, tuple(sorted(scores.items())))


def page_paths_by_item_id() -> dict[str, Path]:
    paths: dict[str, Path] = {}
    for path in sorted(ITEM_DIR.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        match = re.search(r'^item_id: "([^"]+)"$', text, flags=re.MULTILINE)
        if match is None:
            raise ValueError(f"item_id がありません: {path.relative_to(ROOT)}")
        item_id = match.group(1)
        if item_id in paths:
            raise ValueError(f"item_id が重複しています: {item_id}")
        paths[item_id] = path
    return paths


def replace_tags(page: str, synergy_tags: tuple[str, ...]) -> str:
    """既存タグを保ち、分類タグだけを入れ替える。"""

    match = re.search(r"^tags:\n(?P<body>(?:  - .*\n)+)", page, flags=re.MULTILINE)
    if match is None:
        raise ValueError("tags フロントマターがありません")
    existing = re.findall(r"^  - (.+)$", match.group("body"), flags=re.MULTILINE)
    base_tags = [tag for tag in existing if not tag.startswith(TAG_PREFIX)]
    lines = ["tags:"] + [f"  - {tag}" for tag in (*base_tags, *synergy_tags)]
    replacement = "\n".join(lines) + "\n"
    return page[: match.start()] + replacement + page[match.end() :]


def with_updated_date(page: str) -> str:
    return re.sub(
        r"^updated: .*?$",
        f"updated: {date.today().isoformat()}",
        page,
        count=1,
        flags=re.MULTILINE,
    )


def expected_pages() -> list[tuple[Path, Classification]]:
    items = load_items()
    paths = page_paths_by_item_id()
    if set(paths) != set(items):
        missing_pages = sorted(set(items) - set(paths))
        extra_pages = sorted(set(paths) - set(items))
        raise ValueError(f"原典とページの対応が不一致です: missing={missing_pages}, extra={extra_pages}")
    return [
        (paths[item_id], classify_item(item_id, items[item_id]))
        for item_id in sorted(items)
    ]


def current_synergy_tags(page: str) -> tuple[str, ...]:
    match = re.search(r"^tags:\n(?P<body>(?:  - .*\n)+)", page, flags=re.MULTILINE)
    if match is None:
        raise ValueError("tags フロントマターがありません")
    return tuple(
        tag
        for tag in re.findall(r"^  - (.+)$", match.group("body"), flags=re.MULTILINE)
        if tag.startswith(TAG_PREFIX)
    )


def check_pages(pages: list[tuple[Path, Classification]]) -> tuple[int, Counter[str]]:
    errors = 0
    counts: Counter[str] = Counter()
    for path, classification in pages:
        actual = current_synergy_tags(path.read_text(encoding="utf-8"))
        counts.update(actual)
        if actual != classification.tags:
            print(
                f"分類タグ不一致: {path.relative_to(ROOT)} "
                f"expected={list(classification.tags)} actual={list(actual)}",
                file=sys.stderr,
            )
            errors += 1
    return errors, counts


def write_pages(pages: list[tuple[Path, Classification]]) -> int:
    changed = 0
    for path, classification in pages:
        original = path.read_text(encoding="utf-8")
        tagged = replace_tags(original, classification.tags)
        if tagged == original:
            continue
        updated = with_updated_date(tagged)
        if updated != original:
            path.write_text(updated, encoding="utf-8")
            changed += 1
    return changed


def print_summary(pages: list[tuple[Path, Classification]]) -> None:
    counts: Counter[str] = Counter()
    for _, classification in pages:
        counts.update(classification.tags)
    print(f"item pages: {len(pages)}")
    for role in ROLE_ORDER:
        print(f"{TAG_PREFIX}{role}: {counts[f'{TAG_PREFIX}{role}']}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--write", action="store_true", help="分類タグを個別ページへ書き込む")
    mode.add_argument("--check", action="store_true", help="分類タグの同期状態を検証する")
    mode.add_argument("--summary", action="store_true", help="分類タグの件数を表示する")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        pages = expected_pages()
        if args.write:
            print(f"updated item pages: {write_pages(pages)}")
            print_summary(pages)
            return 0
        if args.summary:
            print_summary(pages)
            return 0
        errors, counts = check_pages(pages)
        if errors:
            print(f"item synergy check failed: {errors} page(s)", file=sys.stderr)
            return 1
        print(f"item synergy check passed: {len(pages)} pages")
        for role in ROLE_ORDER:
            print(f"{TAG_PREFIX}{role}: {counts[f'{TAG_PREFIX}{role}']}")
        return 0
    except (OSError, ValueError, KeyError, RuntimeError) as error:
        print(f"item synergy error: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
