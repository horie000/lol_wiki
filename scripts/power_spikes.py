#!/usr/bin/env python3
"""チャンピオン個別ページのパワースパイク分類を生成・検証する。

分類はData Dragon v16.18.1の基礎ステータスと能力説明だけを使う再現可能な
ヒューリスティックである。役割タグ（`Marksman` を含む）は終盤判定に使わない。
実戦の勝率や厳密なダメージ計算を表すものではない。スキルの基礎ダメージを全
チャンピオンで一貫して比較できる定義は原典に含まれないため、この分類の序盤
シグナルは基礎ステータスに限定する。

Usage:
    python3 scripts/power_spikes.py --write
    python3 scripts/power_spikes.py --check
"""

from __future__ import annotations

import argparse
import json
import math
import re
import statistics
import sys
import tarfile
from collections import Counter
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Mapping


ROOT = Path(__file__).resolve().parents[1]
CHAMPION_SOURCE = ROOT / "raw" / "sources" / "champion.json.md"
ARCHIVE_PATH = ROOT / "raw" / "sources" / "dragontail-16.18.1.tgz"
CHAMPION_DIR = ROOT / "wiki" / "entities" / "champions"
DETAIL_MEMBER = "16.18.1/data/ja_JP/champion/{champion_id}.json"
METHOD_LINK = "[[wiki/syntheses/champion-power-spikes-v16-18-1|パワースパイク分類 v16.18.1]]"
START_MARKER = "<!-- power-spike:start -->"
END_MARKER = "<!-- power-spike:end -->"
EARLY_FIELDS = ("hp", "armor", "attackdamage", "movespeed")
EARLY_FRACTION = 0.15

# 能力説明が、蓄積による恒常的・段階的な成長を明示するチャンピオン。
# 各トークンはData Dragonの日本語説明に存在することを実行時に検証する。
GROWTH_SIGNALS: dict[str, tuple[tuple[str, ...], str]] = {
    "AurelionSol": (("星屑", "恒久的に強化"), "「星屑」のスタックが各スキルを恒久的に強化する。"),
    "Bard": (("チャイム", "範囲攻撃"), "一定数のチャイムでミィプの通常攻撃が範囲攻撃・スロウへ強化される。"),
    "Belveth": (("攻撃速度のスタックを恒久的に獲得",), "キルまたはアシストで攻撃速度のスタックを恒久的に獲得する。"),
    "Chogath": (("最大体力が増加",), "「捕食」で敵を倒すと巨大化し、最大体力が増加する。"),
    "Garen": (("物理防御と魔法防御が増加",), "敵ユニットを倒すたびに物理防御と魔法防御が増加する。"),
    "Kindred": (("通常スキルを恒常的に強化", "通常攻撃の射程も強化"), "獲物を狩ることで通常スキルと通常攻撃射程を恒常的に強化する。"),
    "Nasus": (("ダメージが恒久的に",), "「サイフォンストライク」で敵を倒すたびにダメージが恒久的に増加する。"),
    "Rengar": (("トロフィーを獲得し、増加攻撃力を獲得",), "チャンピオン撃破時のトロフィーで増加攻撃力を獲得する。"),
    "Senna": (("攻撃力、射程距離、クリティカル率が増加",), "「霧」の吸収で攻撃力・射程距離・クリティカル率が増加する。"),
    "Shyvana": (("スケールメイル", "防御力が向上"), "キルまたはアシストで「スケールメイル」のスタックを得て防御力が向上する。"),
    "Sion": (("最大体力が増加",), "敵ユニットをキルするたびに最大体力が増加する。"),
    "Smolder": (("スタック数に応じて通常スキルのダメージが増加",), "「駆けだしドラゴン」のスタック数に応じて通常スキルのダメージが増加する。"),
    "Sona": (("恒久的に通常スキルヘイストを獲得",), "条件達成ごとに恒久的に通常スキルヘイストを獲得する。"),
    "Swain": (("最大体力を恒久的に上昇",), "「魂のかけら」で最大体力を恒久的に上昇させる。"),
    "Syndra": (("怒りの破片", "スキルをアップグレード"), "レベル上昇・敵へのダメージで「怒りの破片」を集め、スキルをアップグレードできる。"),
    "Thresh": (("物理防御と魔力を永続的に獲得",), "近くで倒れた敵の魂から物理防御と魔力を永続的に獲得する。"),
    "Veigar": (("魔力は永続的に増加",), "キル・アシスト・スキル命中で魔力が永続的に増加する。"),
    "Viktor": (("ヘクス フラグメント", "恒久的に強化"), "「ヘクス フラグメント」100個ごとにスキルを恒久的に強化する。"),
}

# アイテムで得るステータスまたはアイテム自体との明示的な連動を持つチャンピオン。
ITEM_SCALING_SIGNALS: dict[str, tuple[tuple[str, ...], str]] = {
    "Akali": (("増加攻撃力と魔力に応じたダメージ",), "Qが増加攻撃力と魔力に応じたダメージを与える。"),
    "DrMundo": (("最大体力に応じて増加する、増加攻撃力",), "Eの自動効果で最大体力に応じた増加攻撃力を得る。"),
    "Kaisa": (("アイテム購入によって", "スキルがアップグレード"), "アイテム購入により通常スキルがアップグレードされる。"),
    "Ornn": (("追加物理防御と追加魔法防御", "名匠アイテム"), "追加物理防御・追加魔法防御の獲得量が増え、名匠アイテムを作れる。"),
    "Pyke": (("増加最大体力を得ることはできず、代わりに増加攻撃力を得る",), "増加最大体力を得られない代わりに増加攻撃力へ変換する。"),
    "Ryze": (("増加したマナに応じて追加ダメージ", "魔力に応じて最大マナ"), "増加マナでスキルダメージが増え、魔力で最大マナも増加する。"),
    "Vladimir": (("増加体力を30得るたび魔力が1増加", "魔力1につき体力が1.6増加"), "増加体力と魔力を相互に増加させる。"),
    "Yasuo": (("クリティカル率が増加", "通常攻撃扱い"), "パッシブでクリティカル率が増加し、Qは通常攻撃扱いである。"),
    "Yone": (("クリティカル率が増加", "攻撃速度が増加すると"), "パッシブでクリティカル率が増加し、攻撃速度はWのクールダウンと詠唱時間に影響する。"),
}


@dataclass(frozen=True)
class Classification:
    champion_id: str
    phases: tuple[str, ...]
    reasons: tuple[str, ...]
    base_stat_rank: int | None
    base_stat_score: float | None


def strip_tags(value: str) -> str:
    return re.sub(r"<[^>]+>", "", value).replace("\u00a0", " ")


def load_base_champions() -> dict[str, Mapping[str, object]]:
    payload = json.loads(CHAMPION_SOURCE.read_text(encoding="utf-8"))
    data = payload.get("data")
    if not isinstance(data, dict):
        raise ValueError("champion.json.md の data がオブジェクトではありません")
    return data


def load_detail_texts(champion_ids: set[str]) -> dict[str, str]:
    if not ARCHIVE_PATH.exists():
        raise FileNotFoundError(f"原典アーカイブがありません: {ARCHIVE_PATH}")
    detail_texts: dict[str, str] = {}
    with tarfile.open(ARCHIVE_PATH, mode="r:gz") as archive:
        for champion_id in champion_ids:
            member = archive.getmember(DETAIL_MEMBER.format(champion_id=champion_id))
            extracted = archive.extractfile(member)
            if extracted is None:
                raise RuntimeError(f"詳細レコードを開けません: {member.name}")
            payload = json.load(extracted)
            data = payload.get("data", {}).get(champion_id)
            if not isinstance(data, Mapping):
                raise ValueError(f"詳細レコードがありません: {champion_id}")
            values = [str(data.get("passive", {}).get("description") or "")]
            for spell in data.get("spells", []):
                if isinstance(spell, Mapping):
                    values.extend((str(spell.get("description") or ""), str(spell.get("tooltip") or "")))
            detail_texts[champion_id] = strip_tags(" ".join(values))
    return detail_texts


def validate_signals(detail_texts: Mapping[str, str]) -> None:
    for signal_group in (GROWTH_SIGNALS, ITEM_SCALING_SIGNALS):
        for champion_id, (tokens, _) in signal_group.items():
            text = detail_texts.get(champion_id, "")
            missing = [token for token in tokens if token not in text]
            if missing:
                raise ValueError(
                    f"パワースパイク根拠が原典と一致しません: {champion_id}: {', '.join(missing)}"
                )


def base_stat_ranks(champions: Mapping[str, Mapping[str, object]]) -> tuple[dict[str, int], dict[str, float], set[str]]:
    records = list(champions.values())
    values: dict[str, list[float]] = {field: [] for field in EARLY_FIELDS}
    for champion in records:
        stats = champion.get("stats")
        if not isinstance(stats, Mapping):
            raise ValueError(f"stats がありません: {champion.get('id')}")
        for field in EARLY_FIELDS:
            value = stats.get(field)
            if not isinstance(value, (int, float)):
                raise ValueError(f"{champion.get('id')} の {field} が数値ではありません")
            values[field].append(float(value))

    means = {field: statistics.mean(values[field]) for field in EARLY_FIELDS}
    deviations = {field: statistics.pstdev(values[field]) for field in EARLY_FIELDS}
    scores: dict[str, float] = {}
    for champion in records:
        champion_id = str(champion["id"])
        stats = champion["stats"]
        scores[champion_id] = sum(
            (float(stats[field]) - means[field]) / deviations[field] for field in EARLY_FIELDS
        )

    ordered = sorted(records, key=lambda champion: (-scores[str(champion["id"])], str(champion["id"])))
    ranks = {str(champion["id"]): index for index, champion in enumerate(ordered, start=1)}
    cutoff = math.ceil(len(ordered) * EARLY_FRACTION)
    early_ids = {str(champion["id"]) for champion in ordered[:cutoff]}
    return ranks, scores, early_ids


def format_number(value: int | float) -> str:
    return f"{value:g}"


def classify_champions(champions: Mapping[str, Mapping[str, object]]) -> dict[str, Classification]:
    champion_ids = set(champions)
    required_ids = set(GROWTH_SIGNALS) | set(ITEM_SCALING_SIGNALS)
    missing_ids = required_ids - champion_ids
    if missing_ids:
        raise ValueError(f"原典にない判定対象があります: {', '.join(sorted(missing_ids))}")
    detail_texts = load_detail_texts(required_ids)
    validate_signals(detail_texts)
    ranks, scores, early_ids = base_stat_ranks(champions)

    result: dict[str, Classification] = {}
    for champion_id, champion in champions.items():
        stats = champion["stats"]
        phases: list[str] = []
        reasons: list[str] = []
        if champion_id in early_ids:
            phases.append("序盤")
            reasons.append(
                "基礎ステータス指数（体力・物理防御・攻撃力・移動速度を標準化して合算）が"
                f"173件中{ranks[champion_id]}位（上位15%）。"
                f"体力{format_number(stats['hp'])}、物理防御{format_number(stats['armor'])}、"
                f"攻撃力{format_number(stats['attackdamage'])}、移動速度{format_number(stats['movespeed'])}。"
            )

        late_reasons: list[str] = []
        if champion_id in GROWTH_SIGNALS:
            late_reasons.append(GROWTH_SIGNALS[champion_id][1])
        if champion_id in ITEM_SCALING_SIGNALS:
            late_reasons.append(ITEM_SCALING_SIGNALS[champion_id][1])
        if late_reasons:
            phases.append("終盤")
            reasons.extend(late_reasons)

        if not phases:
            phases.append("中盤")
            reasons.append(
                "本分類で採用した序盤の基礎ステータス上位15%と、終盤の能力の蓄積成長・"
                "明示的なステータス連動のいずれにも当たらないため、中盤を暫定指定する。"
            )

        result[champion_id] = Classification(
            champion_id=champion_id,
            phases=tuple(phases),
            reasons=tuple(reasons),
            base_stat_rank=ranks[champion_id] if champion_id in early_ids else None,
            base_stat_score=scores[champion_id] if champion_id in early_ids else None,
        )
    return result


def build_section(classification: Classification) -> str:
    lines = [START_MARKER, "## パワースパイク", ""]
    lines.append(f"- **区分：** {'、'.join(classification.phases)}")
    lines.append(f"- **判定：** {METHOD_LINK} に基づく原典ベースの推論。")
    lines.append("- **根拠：**")
    lines.extend(f"  - {reason}" for reason in classification.reasons)
    lines.append(
        "- **限界：** スキル基礎ダメージ・係数・アイテム完成時刻を全チャンピオンで統一比較できる原典値がないため、"
        "実戦の強さや購入優先度を断定しない。"
    )
    lines.extend(("", END_MARKER))
    return "\n".join(lines)


def replace_section(page: str, section: str) -> str:
    pattern = re.compile(re.escape(START_MARKER) + r".*?" + re.escape(END_MARKER) + r"\n?", re.DOTALL)
    if pattern.search(page):
        return pattern.sub(section + "\n", page, count=1)
    for heading in ("\n## 関連ページ\n", "\n## 出典\n"):
        if heading in page:
            return page.replace(heading, "\n" + section + "\n" + heading, 1)
    return page.rstrip() + "\n\n" + section + "\n"


def page_paths_by_champion_id() -> dict[str, Path]:
    paths: dict[str, Path] = {}
    for path in sorted(CHAMPION_DIR.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        match = re.search(r'^champion_id: "([^"]+)"$', text, flags=re.MULTILINE)
        if match is None:
            raise ValueError(f"champion_id がありません: {path.relative_to(ROOT)}")
        champion_id = match.group(1)
        if champion_id in paths:
            raise ValueError(f"champion_id が重複しています: {champion_id}")
        paths[champion_id] = path
    return paths


def with_updated_date(page: str) -> str:
    return re.sub(r"^updated: .*?$", f"updated: {date.today().isoformat()}", page, count=1, flags=re.MULTILINE)


def expected_pages() -> list[tuple[Path, Classification]]:
    champions = load_base_champions()
    classifications = classify_champions(champions)
    paths = page_paths_by_champion_id()
    if set(paths) != set(champions):
        missing_pages = sorted(set(champions) - set(paths))
        extra_pages = sorted(set(paths) - set(champions))
        raise ValueError(f"原典とページの対応が不一致です: missing={missing_pages}, extra={extra_pages}")
    return [(paths[champion_id], classifications[champion_id]) for champion_id in sorted(champions)]


def write_pages(pages: list[tuple[Path, Classification]]) -> int:
    changed = 0
    for path, classification in pages:
        original = path.read_text(encoding="utf-8")
        updated = replace_section(original, build_section(classification))
        if updated != original:
            path.write_text(with_updated_date(updated), encoding="utf-8")
            changed += 1
    return changed


def check_pages(pages: list[tuple[Path, Classification]]) -> int:
    errors: list[str] = []
    for path, classification in pages:
        page = path.read_text(encoding="utf-8")
        match = re.search(re.escape(START_MARKER) + r".*?" + re.escape(END_MARKER) + r"\n?", page, re.DOTALL)
        expected = build_section(classification) + "\n"
        if match is None:
            errors.append(f"パワースパイクブロックがありません: {path.relative_to(ROOT)}")
        elif match.group(0) != expected:
            errors.append(f"パワースパイクが古いか不一致です: {path.relative_to(ROOT)}")
    if errors:
        for error in errors[:30]:
            print(f"ERROR: {error}", file=sys.stderr)
        if len(errors) > 30:
            print(f"ERROR: ほか {len(errors) - 30} 件", file=sys.stderr)
        return 1
    counts = Counter(phase for _, classification in pages for phase in classification.phases)
    print(
        "power-spikes: "
        f"{len(pages)} 件のチャンピオンページを検証しました。"
        f" 序盤={counts['序盤']}、中盤={counts['中盤']}、終盤={counts['終盤']}"
    )
    return 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--write", action="store_true", help="全チャンピオンページのパワースパイクを生成・更新する")
    mode.add_argument("--check", action="store_true", help="全チャンピオンページのパワースパイクを検証する（既定）")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    pages = expected_pages()
    if args.write:
        changed = write_pages(pages)
        print(f"power-spikes: {len(pages)} 件を分類し、{changed} 件を更新しました。")
        return 0
    return check_pages(pages)


if __name__ == "__main__":
    raise SystemExit(main())
