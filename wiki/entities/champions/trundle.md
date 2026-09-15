---
title: "トランドル"
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
  - role-fighter
  - role-tank
  - data-dragon
champion_id: "Trundle"
champion_key: "48"
data_version: "16.18.1"
roles:
  - "Fighter"
  - "Tank"
resource_type: "マナ"
image_path: "raw/assets/champions/Trundle.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Trundle.png"
---

# トランドル

![[raw/assets/champions/Trundle.png|128]]

## 基本情報

- **英字ID：** `Trundle`
- **キー：** `48`
- **称号：** トロールキング
- **データversion：** `16.18.1`

## 紹介

トランドルは巨大な図体をした底意地の悪いトロールであり、どんな相手でも力で抑えつけて従わせる──それはフレヨルド自体も例外ではない。縄張り意識が異常に強く、うかつにも領土に足を踏み入れる者があれば、追いかけて真なる氷の巨大な棍棒を取り出し、敵を骨の髄まで凍えさせてギザギザの氷片で打ち貫き、凍土を犠牲者の血で染めて高笑いをあげている。

## 分類

- **役割タグ：** `Fighter`、`Tank`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 7 |
| `defense` | 6 |
| `magic` | 2 |
| `difficulty` | 5 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 650 |
| `hpperlevel` | 110 |
| `mp` | 340 |
| `mpperlevel` | 45 |
| `movespeed` | 350 |
| `armor` | 37 |
| `armorperlevel` | 4.5 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 175 |
| `hpregen` | 6 |
| `hpregenperlevel` | 0.75 |
| `mpregen` | 7.5 |
| `mpregenperlevel` | 0.6 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 68 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2.9 |
| `attackspeed` | 0.67 |

## アビリティ

- **パッシブ — 王への貢物：** 近くにいる敵ユニットの体力がゼロになると、自身の体力が回復する。回復量は、倒れたユニットの最大体力に比例する。

- **Q — 咬み付き：** 敵に咬み付いてダメージを与える。咬み付かれた対象は一瞬スロウ状態となり、攻撃力が低下する。この攻撃でトランドルの攻撃力が上昇し、対象の攻撃力をその半分低下させる。
- **W — 凍てつく大地：** 指定範囲を自身の領土にする。範囲内にいる間はトランドルの攻撃速度と移動速度が増加し、あらゆる体力回復効果が増加する。
- **E — 氷冷の柱：** 指定地点に氷の柱を出現させて通行不能にし、近接する敵ユニット全員をスロウ効果を付与する。
- **R — 暴虐なる搾取：** 発動と同時に対象の体力、物理防御、魔法防御の一部を吸収する。 その後4秒かけて、さらに同量の体力、物理防御、魔法防御を吸収する。

<!-- power-spike:start -->
## パワースパイク

- **区分：** 序盤
- **判定：** [[wiki/syntheses/champion-power-spikes-v16-18-1|パワースパイク分類 v16.18.1]] に基づく原典ベースの推論。
- **根拠：**
  - 基礎ステータス指数（体力・物理防御・攻撃力・移動速度を標準化して合算）が173件中1位（上位15%）。体力650、物理防御37、攻撃力68、移動速度350。
- **限界：** スキル基礎ダメージ・係数・アイテム完成時刻を全チャンピオンで統一比較できる原典値がないため、実戦の強さや購入優先度を断定しない。

<!-- power-spike:end -->

<!-- power-spike-match:start -->
## 試合時間別の観測

- **観測分類：** 中盤寄り
- **対象試合：** 137試合、全体勝率 56.2%
- **時間帯別勝率：** 〜20分 35.0%（n=20）、20〜25分 84.6%（n=26）、25〜30分 55.9%（n=34）、30〜35分 53.1%（n=32）、35分〜 48.0%（n=25）
- **最高帯：** 20〜25分（判定差 36.6ポイント）
- **判定根拠：** 中間帯が最高、端点との差 36.6%
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Trundle` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Trundle.png)
