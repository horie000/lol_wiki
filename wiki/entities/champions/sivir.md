---
title: "シヴィア"
type: entity
status: active
created: 2026-09-14
updated: 2026-09-15
sources:
  - "[[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]]"
  - "[[wiki/sources/src-2026-09-14-dragontail-16-18-1]]"
  - "[[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]"
tags:
  - champion
  - role-marksman
  - data-dragon
champion_id: "Sivir"
champion_key: "15"
data_version: "16.18.1"
roles:
  - "Marksman"
resource_type: "マナ"
image_path: "raw/assets/champions/Sivir.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Sivir.png"
---

# シヴィア

![[raw/assets/champions/Sivir.png|128]]

## 基本情報

- **英字ID：** `Sivir`
- **キー：** `15`
- **称号：** 戦場の女王
- **データversion：** `16.18.1`

## 紹介

シヴィアは、金のためならどのような仕事でも引き受ける。傭兵の一団を率いる彼女は血も涙もない名将としてその名をあまねく轟かせ、砂漠では彼女に仕事を依頼する者たちが後を絶たない。シヴィアは宝石を鏤めたクロスブレードを自在に操り、金に糸目をつけない雇い主たちのために無数の戦いを制してきた。何事をも恐れぬ覚悟と底無しの野望を抱き、シヴィアはたとえ如何なる危険が待ち受けていようとも、砂に埋もれたシュリーマの墓から揚々と財宝を掘り起こす。そこには莫大な見返りが眠っているのだ。しかしシュリーマの骨の髄を揺るがす太古...

## 分類

- **役割タグ：** `Marksman`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 9 |
| `defense` | 3 |
| `magic` | 1 |
| `difficulty` | 4 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 600 |
| `hpperlevel` | 104 |
| `mp` | 340 |
| `mpperlevel` | 45 |
| `movespeed` | 335 |
| `armor` | 30 |
| `armorperlevel` | 4 |
| `spellblock` | 33 |
| `spellblockperlevel` | 1.1 |
| `attackrange` | 500 |
| `hpregen` | 3.25 |
| `hpregenperlevel` | 0.55 |
| `mpregen` | 6 |
| `mpregenperlevel` | 0.8 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 60 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 1.6 |
| `attackspeed` | 0.625 |

## アビリティ

- **パッシブ — 戦駆け：** 敵チャンピオンを攻撃すると移動速度が短時間増加する。

- **Q — ブーメランブレード：** クロスブレードをブーメランのように投げ、往復のそれぞれで命中した敵ユニットすべてにダメージを与える。
- **W — 跳刃：** 次の数回の通常攻撃は攻撃速度が増加し、対象の周囲に跳ね返るようになる。跳ね返った攻撃は与えるダメージが低下する。
- **E — スペルシールド：** 魔法のバリアを張り、一度だけ敵のスキル攻撃やその付随効果をブロックする。スキルをブロックすると体力が回復して、少しの間だけ移動速度が増加する。
- **R — 戦姫の号令：** 発動するとシヴィアの号令により、自身と味方の移動速度を一定時間増加させる。また、自身は通常攻撃するたびに、スキルのクールダウンを短縮できる。

<!-- power-spike:start -->
## パワースパイク

- **区分：** 中盤
- **判定：** [[wiki/syntheses/champion-power-spikes-v16-18-1|パワースパイク分類 v16.18.1]] に基づく原典ベースの推論。
- **根拠：**
  - 本分類で採用した序盤の基礎ステータス上位15%と、終盤の能力の蓄積成長・明示的なステータス連動のいずれにも当たらないため、中盤を暫定指定する。
- **限界：** スキル基礎ダメージ・係数・アイテム完成時刻を全チャンピオンで統一比較できる原典値がないため、実戦の強さや購入優先度を断定しない。

<!-- power-spike:end -->

<!-- power-spike-match:start -->
## 試合時間別の観測

- **観測分類：** 中盤寄り
- **対象試合：** 261試合、全体勝率 51.3%
- **時間帯別勝率：** 〜20分 43.8%（n=32）、20〜25分 57.1%（n=28）、25〜30分 51.4%（n=74）、30〜35分 55.9%（n=59）、35分〜 48.5%（n=68）
- **最高帯：** 20〜25分（判定差 8.6ポイント）
- **判定根拠：** 中間帯が最高、端点との差 8.6%
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Sivir` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Sivir.png)
