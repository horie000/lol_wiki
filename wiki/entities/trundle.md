---
title: "トランドル"
type: entity
status: active
created: 2026-09-14
updated: 2026-09-14
sources:
  - "[[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]]"
  - "[[wiki/sources/src-2026-09-14-dragontail-16-18-1]]"
tags:
  - champion
  - role-fighter
  - role-tank
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

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Trundle` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Trundle.png)
