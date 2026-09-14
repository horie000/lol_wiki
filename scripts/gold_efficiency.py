#!/usr/bin/env python3
"""Data Dragon アイテムのゴールド効率を算定・検証する。

現行の基準値は、2026年公開のレッド＆ふぉー「アイテムの金銭効率
ランキング：ファイター編」に掲載された単価表を採用する。記事が扱って
いない自動効果・発動効果は原則として理論価格に含めず、直接数値化できる
基礎ステータスだけを合算する。

固定通常攻撃時追加ダメージの単価は、現行記事に基準値がないため、補助的に
FirstBloodStats の記事から 25 gold/unit を引き継ぐ。この混合は明示的な
近似であり、記事間で異なる単価を単一のゲーム内真値として扱うものではない。

Usage:
    python3 scripts/gold_efficiency.py --write
    python3 scripts/gold_efficiency.py --check
    python3 scripts/gold_efficiency.py --ranking
"""

from __future__ import annotations

import argparse
import html
import json
import re
import sys
import tarfile
from dataclasses import dataclass, field
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
from pathlib import Path
from typing import Iterable, Mapping


ROOT = Path(__file__).resolve().parents[1]
ARCHIVE_PATH = ROOT / "raw" / "sources" / "dragontail-16.18.1.tgz"
ITEM_MEMBER = "16.18.1/data/ja_JP/item.json"
ITEM_DIR = ROOT / "wiki" / "entities" / "items"
METHOD_URL = "https://red-ff-gamenews.com/lol-item-ft-ce/"
METHOD_WIKILINK = "[[wiki/sources/src-2026-02-28-red-ff-item-gold-efficiency|アイテムの金銭効率ランキング：ファイター編【LoL】]]"
LEGACY_METHOD_URL = "https://firstbloodstats.com/archives/158"
LEGACY_METHOD_WIKILINK = "[[wiki/sources/src-2017-11-26-firstbloodstats-gold-efficiency|アイテムのゴールド効率について改めてまとめた]]"
START_MARKER = "<!-- gold-efficiency:start -->"
END_MARKER = "<!-- gold-efficiency:end -->"

Q2 = Decimal("0.01")
HUNDRED = Decimal("100")


# レッド＆ふぉー記事の基準表にある gold/stat。割合系は「1%」単位で保持する。
GOLD_PER_STAT: dict[str, Decimal] = {
    "attack_damage": Decimal("35"),
    "ability_power": Decimal("20"),
    "armor": Decimal("20"),
    "magic_resist": Decimal("20"),
    "health": Decimal("2.67"),
    "mana": Decimal("1"),
    "health_regen_percent": Decimal("3"),
    "mana_regen_percent": Decimal("4"),
    "crit_chance_percent": Decimal("40"),
    "attack_speed_percent": Decimal("25"),
    "flat_move_speed": Decimal("12"),
    "life_steal_percent": Decimal("53.57"),
    "lethality": Decimal("30"),
    "armor_penetration_percent": Decimal("41.67"),
    "magic_penetration_percent": Decimal("46.15"),
    "magic_penetration": Decimal("46.67"),
    # レッド＆ふぉー記事に追加ダメージの単価がないため、旧原典を補助使用。
    "on_hit_damage": Decimal("25"),
    "ability_haste": Decimal("50"),
    "percent_move_speed": Decimal("62.5"),
    "heal_shield_percent": Decimal("50"),
    "tenacity_percent": Decimal("10.33"),
}

STAT_LABELS: dict[str, str] = {
    "attack_damage": "攻撃力",
    "ability_power": "魔力",
    "armor": "物理防御",
    "magic_resist": "魔法防御",
    "health": "体力",
    "mana": "マナ",
    "health_regen_percent": "体力自動回復",
    "mana_regen_percent": "マナ自動回復",
    "crit_chance_percent": "クリティカル率",
    "attack_speed_percent": "攻撃速度",
    "flat_move_speed": "移動速度",
    "life_steal_percent": "ライフスティール",
    "lethality": "脅威",
    "armor_penetration_percent": "物理防御貫通",
    "magic_penetration_percent": "魔法防御貫通",
    "magic_penetration": "魔法防御貫通",
    "on_hit_damage": "固定通常攻撃時追加ダメージ",
    "ability_haste": "スキルヘイスト",
    "percent_move_speed": "割合移動速度",
    "heal_shield_percent": "回復効果・シールド量",
    "tenacity_percent": "行動妨害耐性",
}

DIRECT_FIELD_SPECS: dict[str, str] = {
    "攻撃力": "attack_damage",
    "魔力": "ability_power",
    "体力": "health",
    "マナ": "mana",
    "物理防御": "armor",
    "魔法防御": "magic_resist",
    "攻撃速度": "attack_speed_percent",
    "クリティカル率": "crit_chance_percent",
    "ライフスティール": "life_steal_percent",
    "脅威": "lethality",
    "スキルヘイスト": "ability_haste",
    "基本体力自動回復": "health_regen_percent",
    "体力自動回復": "health_regen_percent",
    "基本マナ自動回復": "mana_regen_percent",
    "マナ自動回復": "mana_regen_percent",
    "体力回復量とシールド量": "heal_shield_percent",
    "回復効果およびシールド量": "heal_shield_percent",
    "回復量およびシールド量": "heal_shield_percent",
    "行動妨害耐性": "tenacity_percent",
}

RAW_FIELD_SPECS: dict[str, tuple[str, bool]] = {
    "FlatPhysicalDamageMod": ("attack_damage", False),
    "FlatMagicDamageMod": ("ability_power", False),
    "FlatHPPoolMod": ("health", False),
    "FlatMPPoolMod": ("mana", False),
    "FlatArmorMod": ("armor", False),
    "FlatSpellBlockMod": ("magic_resist", False),
    "PercentAttackSpeedMod": ("attack_speed_percent", True),
    "FlatCritChanceMod": ("crit_chance_percent", True),
    "FlatMovementSpeedMod": ("flat_move_speed", False),
    "PercentMovementSpeedMod": ("percent_move_speed", True),
    "PercentLifeStealMod": ("life_steal_percent", True),
}

UNPRICED_DIRECT_LABELS: dict[str, str] = {
    "クリティカルダメージ": "クリティカルダメージ",
    "オムニヴァンプ": "オムニヴァンプ",
    "スペルヴァンプ": "スペルヴァンプ",
}


@dataclass(frozen=True)
class ParsedStat:
    label: str
    value: Decimal
    is_percent: bool
    source: str


@dataclass(frozen=True)
class Contribution:
    key: str
    value: Decimal
    source_label: str

    @property
    def gold(self) -> Decimal:
        return self.value * GOLD_PER_STAT[self.key]


@dataclass
class ItemCalculation:
    item_id: str
    name: str
    price: Decimal
    purchasable: bool
    in_store: bool
    contributions: list[Contribution] = field(default_factory=list)
    unsupported: list[str] = field(default_factory=list)

    @property
    def theoretical_price(self) -> Decimal:
        return sum((c.gold for c in self.contributions), Decimal("0"))

    @property
    def efficiency(self) -> Decimal | None:
        if self.price <= 0:
            return None
        return self.theoretical_price * HUNDRED / self.price


def decimal_from_text(value: str) -> Decimal | None:
    cleaned = value.strip().replace(",", "")
    match = re.fullmatch(r"[-+]?\d+(?:\.\d+)?%?", cleaned)
    if not match:
        return None
    try:
        return Decimal(cleaned.rstrip("%"))
    except InvalidOperation:
        return None


def fmt_decimal(value: Decimal, places: int = 2) -> str:
    quantized = value.quantize(Q2 if places == 2 else Decimal("1"), rounding=ROUND_HALF_UP)
    if places == 0:
        return f"{quantized:,.0f}"
    return f"{quantized:,.2f}"


def fmt_quantity(value: Decimal, is_percent: bool = False) -> str:
    if value == value.to_integral_value():
        result = f"{value:,.0f}"
    else:
        result = f"{value:,.2f}".rstrip("0").rstrip(".")
    return f"{result}%" if is_percent else result


def strip_tags(value: str) -> str:
    return html.unescape(re.sub(r"<[^>]+>", "", value))


def normalize_label(value: str) -> str:
    return re.sub(r"[\s　]", "", value).strip()


def extract_stats(description: str) -> list[ParsedStat]:
    match = re.search(r"<stats>(.*?)</stats>", description, flags=re.IGNORECASE | re.DOTALL)
    if not match:
        return []

    result: list[ParsedStat] = []
    for segment in re.split(r"<br\s*/?>", match.group(1), flags=re.IGNORECASE):
        attention = re.search(r"<attention>(.*?)</attention>", segment, flags=re.IGNORECASE | re.DOTALL)
        if not attention:
            continue
        value_text = strip_tags(attention.group(1)).strip()
        value = decimal_from_text(value_text)
        if value is None or value == 0:
            continue
        label = normalize_label(strip_tags(segment[: attention.start()]))
        if not label:
            continue
        result.append(
            ParsedStat(
                label=label,
                value=value,
                is_percent="%" in value_text,
                source=strip_tags(segment).strip(),
            )
        )
    return result


def raw_stats(item: Mapping[str, object]) -> Iterable[ParsedStat]:
    stats = item.get("stats")
    if not isinstance(stats, Mapping):
        return []

    parsed: list[ParsedStat] = []
    for field_name, (key, is_ratio) in RAW_FIELD_SPECS.items():
        raw_value = stats.get(field_name, 0)
        if not isinstance(raw_value, (int, float)) or raw_value == 0:
            continue
        value = Decimal(str(raw_value))
        if is_ratio:
            value *= HUNDRED
        parsed.append(
            ParsedStat(
                label=STAT_LABELS[key],
                value=value,
                is_percent=is_ratio,
                source=field_name,
            )
        )
    return parsed


def parse_fixed_on_hit(description: str) -> Decimal:
    """記事のリカーブ ボウ例に合わせ、無条件の固定通常攻撃時ダメージだけ拾う。"""

    plain = strip_tags(description)
    total = Decimal("0")
    pattern = re.compile(r"通常攻撃が\s*(\d+(?:\.\d+)?)の追加(?:物理|魔法)ダメージ")
    for match in pattern.finditer(plain):
        prefix = plain[max(0, match.start() - 12) : match.start()]
        # エネルギー充填などの条件付き通常攻撃は基礎ステータスに含めない。
        if prefix.endswith("状態の") or prefix.endswith("次の"):
            continue
        value = decimal_from_text(match.group(1))
        if value is not None:
            total += value
    return total


def add_unsupported(items: list[str], value: str) -> None:
    value = value.strip()
    if value and value not in items:
        items.append(value)


def calculate_item(item_id: str, item: Mapping[str, object]) -> ItemCalculation:
    name = str(item.get("name") or f"ID {item_id}")
    gold = item.get("gold") if isinstance(item.get("gold"), Mapping) else {}
    price_raw = gold.get("total", 0) if isinstance(gold, Mapping) else 0
    price = Decimal(str(price_raw or 0))
    purchasable = bool(gold.get("purchasable", False)) if isinstance(gold, Mapping) else False
    # Data Dragon は通常レコードで `inStore` を省略する。省略を非表示と
    # 誤認せず、明示的な false のときだけショップ非表示として扱う。
    in_store = item.get("inStore") is not False
    calculation = ItemCalculation(
        item_id=item_id,
        name=name,
        price=price,
        purchasable=purchasable,
        in_store=in_store,
    )

    parsed = extract_stats(str(item.get("description") or ""))
    parsed_labels: set[str] = set()
    contributions: dict[str, Contribution] = {}

    for stat in parsed:
        parsed_labels.add(stat.label)
        normalized = normalize_label(stat.label)
        key = DIRECT_FIELD_SPECS.get(normalized)
        if normalized == "移動速度":
            key = "percent_move_speed" if stat.is_percent else "flat_move_speed"
        if normalized == "魔法防御貫通":
            key = "magic_penetration_percent" if stat.is_percent else "magic_penetration"
        if normalized == "物理防御貫通":
            key = "armor_penetration_percent" if stat.is_percent else None

        if key in GOLD_PER_STAT:
            contributions[key] = Contribution(key=key, value=stat.value, source_label=stat.label)
        else:
            unpriced_label = UNPRICED_DIRECT_LABELS.get(normalized)
            if unpriced_label:
                add_unsupported(calculation.unsupported, f"{unpriced_label} {fmt_quantity(stat.value, stat.is_percent)}")
            elif normalized == "物理防御貫通":
                add_unsupported(calculation.unsupported, f"物理防御貫通（割合単価は記事に記載なし） {fmt_quantity(stat.value, stat.is_percent)}")
            elif normalized not in DIRECT_FIELD_SPECS and normalized not in {"移動速度", "魔法防御貫通"}:
                add_unsupported(calculation.unsupported, f"{stat.label} {fmt_quantity(stat.value, stat.is_percent)}")

    # description の <stats> が欠落している特殊レコードを raw stats で補う。
    for stat in raw_stats(item):
        key = next((k for k, label in STAT_LABELS.items() if label == stat.label), None)
        if key and key not in contributions and stat.label not in parsed_labels:
            contributions[key] = Contribution(key=key, value=stat.value, source_label=stat.label)

    fixed_on_hit = parse_fixed_on_hit(str(item.get("description") or ""))
    if fixed_on_hit:
        contributions["on_hit_damage"] = Contribution(
            key="on_hit_damage",
            value=fixed_on_hit,
            source_label="固定通常攻撃時追加ダメージ",
        )

    description = str(item.get("description") or "")
    if re.search(r"<(?:passive|active|OnHit|onHit)>", description, flags=re.IGNORECASE):
        add_unsupported(calculation.unsupported, "自動効果・発動効果（記事の一般式では原則除外）")
    if "クリティカルダメージ" in description and not any("クリティカルダメージ" in x for x in calculation.unsupported):
        # <stats> で値を拾った場合も、単価がないことを明示する。
        match = re.search(r"クリティカルダメージ<attention>(.*?)</attention>", description)
        if match:
            value = strip_tags(match.group(1))
            add_unsupported(calculation.unsupported, f"クリティカルダメージ {value}")

    calculation.contributions = list(contributions.values())
    return calculation


def load_items() -> dict[str, Mapping[str, object]]:
    if not ARCHIVE_PATH.exists():
        raise FileNotFoundError(f"原典アーカイブがありません: {ARCHIVE_PATH}")
    with tarfile.open(ARCHIVE_PATH, mode="r:gz") as archive:
        member = archive.getmember(ITEM_MEMBER)
        extracted = archive.extractfile(member)
        if extracted is None:
            raise RuntimeError(f"アーカイブ内のアイテムデータを開けません: {ITEM_MEMBER}")
        payload = json.load(extracted)
    data = payload.get("data")
    if not isinstance(data, dict):
        raise ValueError("item.json の data がオブジェクトではありません")
    return data


def build_section(calculation: ItemCalculation) -> str:
    lines = [START_MARKER, "## ゴールド効率", ""]
    purchase_note = []
    if not calculation.purchasable:
        purchase_note.append("購入不可")
    if not calculation.in_store:
        purchase_note.append("ショップ非表示")
    note = f"（{'・'.join(purchase_note)}）" if purchase_note else ""

    if calculation.price <= 0:
        lines.extend(
            [
                f"- **実購入価格：** 設定なし{note}",
                f"- **理論価格：** {fmt_decimal(calculation.theoretical_price)}ゴールド",
                "- **ゴールド効率：** 算出不可（実購入価格が0）",
            ]
        )
    else:
        efficiency = calculation.efficiency
        lines.extend(
            [
                f"- **実購入価格：** {fmt_decimal(calculation.price, places=0)}ゴールド{note}",
                f"- **理論価格：** {fmt_decimal(calculation.theoretical_price)}ゴールド",
                f"- **ゴールド効率：** {fmt_decimal(efficiency)}%",
            ]
        )

    if calculation.contributions:
        rendered = []
        for contribution in calculation.contributions:
            label = STAT_LABELS[contribution.key]
            suffix = "%" if contribution.key.endswith("_percent") or contribution.key in {"attack_speed_percent", "crit_chance_percent", "life_steal_percent", "percent_move_speed", "health_regen_percent", "mana_regen_percent", "heal_shield_percent"} else ""
            rendered.append(f"{label} {fmt_quantity(contribution.value)}{suffix}（{fmt_decimal(contribution.gold)}ゴールド）")
        lines.append(f"- **計算対象：** {'、'.join(rendered)}")
    else:
        lines.append("- **計算対象：** なし")

    if calculation.unsupported:
        lines.append(f"- **算定対象外：** {'、'.join(calculation.unsupported)}")
    else:
        lines.append("- **算定対象外：** なし")
    lines.extend(
        [
            "- **算定式：** `理論価格 ÷ 実購入価格 × 100`",
            f"- **算定根拠：** {METHOD_WIKILINK}（[原典URL]({METHOD_URL})）",
        ]
    )
    if any(contribution.key == "on_hit_damage" for contribution in calculation.contributions):
        lines.append(
            f"- **補助根拠：** 固定通常攻撃時追加ダメージのみ {LEGACY_METHOD_WIKILINK}（[原典URL]({LEGACY_METHOD_URL})）の25 gold/statを適用。"
        )
    lines.extend(
        [
            "- **注記：** 行動妨害耐性、割合物理防御貫通、割合・固定魔法防御貫通、ライフスティール、割合移動速度などは現行記事の単価を適用。効果・発動効果は、固定通常攻撃時追加ダメージなど数値化できる一部を除き含めない。",
            "",
            END_MARKER,
        ]
    )
    return "\n".join(lines)


def replace_section(page: str, section: str) -> str:
    block_pattern = re.compile(
        re.escape(START_MARKER) + r".*?" + re.escape(END_MARKER) + r"\n?",
        flags=re.DOTALL,
    )
    if block_pattern.search(page):
        return block_pattern.sub(section + "\n", page, count=1)

    for heading in ("\n## 範囲と不確実性\n", "\n## 出典\n"):
        if heading in page:
            return page.replace(heading, "\n" + section + "\n" + heading, 1)
    return page.rstrip() + "\n\n" + section + "\n"


def expected_pages(items: Mapping[str, Mapping[str, object]]) -> list[tuple[Path, ItemCalculation]]:
    result = []
    for item_id, item in sorted(items.items(), key=lambda pair: int(pair[0]) if pair[0].isdigit() else pair[0]):
        result.append((ITEM_DIR / f"item-{item_id}.md", calculate_item(item_id, item)))
    return result


def write_pages(pages: list[tuple[Path, ItemCalculation]]) -> int:
    changed = 0
    for path, calculation in pages:
        if not path.exists():
            raise FileNotFoundError(f"アイテムページがありません: {path}")
        original = path.read_text(encoding="utf-8")
        updated = replace_section(original, build_section(calculation))
        if updated != original:
            path.write_text(updated, encoding="utf-8")
            changed += 1
    return changed


def check_pages(pages: list[tuple[Path, ItemCalculation]]) -> int:
    errors: list[str] = []
    for path, calculation in pages:
        if not path.exists():
            errors.append(f"アイテムページがありません: {path.relative_to(ROOT)}")
            continue
        expected = build_section(calculation) + "\n"
        actual_page = path.read_text(encoding="utf-8")
        match = re.search(
            re.escape(START_MARKER) + r".*?" + re.escape(END_MARKER) + r"\n?",
            actual_page,
            flags=re.DOTALL,
        )
        if match is None:
            errors.append(f"ゴールド効率ブロックがありません: {path.relative_to(ROOT)}")
        elif match.group(0) != expected:
            errors.append(f"ゴールド効率が古いか不一致です: {path.relative_to(ROOT)}")

    if errors:
        for error in errors[:30]:
            print(f"ERROR: {error}", file=sys.stderr)
        if len(errors) > 30:
            print(f"ERROR: ほか {len(errors) - 30} 件", file=sys.stderr)
        return 1
    print(f"gold-efficiency: {len(pages)} 件のアイテムページを検証しました。")
    return 0


def standard_sr_ranking(items: Mapping[str, Mapping[str, object]]) -> list[ItemCalculation]:
    """サモナーズリフトで購入できるアイテムを効率順に返す。

    同名かつ説明文も同一のレコードは、重複として最小IDを採用する。これにより、
    同じジャングル・コンパニオン等がランキングを複数
    占有しないようにする。
    """

    representatives: dict[tuple[str, str], ItemCalculation] = {}
    for item_id, item in items.items():
        calculation = calculate_item(item_id, item)
        maps = item.get("maps")
        on_summoners_rift = isinstance(maps, Mapping) and maps.get("11") is True
        if (
            not on_summoners_rift
            or not calculation.purchasable
            or not calculation.in_store
            or calculation.price <= 0
            or calculation.efficiency is None
        ):
            continue

        key = (calculation.name, strip_tags(str(item.get("description") or "")))
        existing = representatives.get(key)
        if existing is None or int(calculation.item_id) < int(existing.item_id):
            representatives[key] = calculation

    return sorted(
        representatives.values(),
        key=lambda calculation: (calculation.efficiency or Decimal("0"), int(calculation.item_id)),
    )


def print_ranking(items: Mapping[str, Mapping[str, object]], limit: int = 10) -> int:
    """再利用しやすい上位・下位のゴールド効率をTSV形式で出力する。"""

    ranking = standard_sr_ranking(items)
    print(
        "gold-efficiency-ranking: "
        f"サモナーズリフトで購入可能・ショップ表示・価格ありの重複除外後 {len(ranking)} 件"
    )
    for label, entries in (("LOW", ranking[:limit]), ("HIGH", list(reversed(ranking[-limit:])))):
        print(label)
        print("item_id\tname\tprice\ttheoretical_price\tefficiency")
        for calculation in entries:
            print(
                "\t".join(
                    (
                        calculation.item_id,
                        calculation.name,
                        fmt_decimal(calculation.price, places=0),
                        fmt_decimal(calculation.theoretical_price),
                        fmt_decimal(calculation.efficiency or Decimal("0")),
                    )
                )
            )
    return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--write", action="store_true", help="全アイテムページの算定ブロックを生成・更新する")
    mode.add_argument("--check", action="store_true", help="全アイテムページの算定ブロックを検証する（既定）")
    mode.add_argument("--ranking", action="store_true", help="サモナーズリフト向けの上位・下位10件を表示する")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    items = load_items()
    if args.ranking:
        return print_ranking(items)

    pages = expected_pages(items)
    if args.write:
        changed = write_pages(pages)
        print(f"gold-efficiency: {len(pages)} 件を算定し、{changed} 件を更新しました。")
        return 0
    return check_pages(pages)


if __name__ == "__main__":
    raise SystemExit(main())
