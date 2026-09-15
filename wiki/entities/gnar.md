---
title: "ナー"
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
champion_id: "Gnar"
champion_key: "150"
data_version: "16.18.1"
roles:
  - "Fighter"
  - "Tank"
resource_type: "怒り"
image_path: "raw/assets/champions/Gnar.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Gnar.png"
---

# ナー

![[raw/assets/champions/Gnar.png|128]]

## 基本情報

- **英字ID：** `Gnar`
- **キー：** `150`
- **称号：** ミッシングリンク
- **データversion：** `16.18.1`

## 紹介

ナーは原始時代のヨードルで、おどけて悪ふざけをしていたかと思えば、あっという間にそれが幼児の怒りとなって爆発し、巨大な破壊の野獣に変身する。真なる氷に何千年間も閉じ込められていた彼にとって、一変した世界は見たこともないような不思議でいっぱいだ。彼は自分の骨牙のブーメランであろうが近くにあった建物であろうが、手当たり次第に敵に向かって投げつけては危険な状況を楽しんでいる。

## 分類

- **役割タグ：** `Fighter`、`Tank`
- **リソース種別：** 怒り

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 6 |
| `defense` | 5 |
| `magic` | 5 |
| `difficulty` | 8 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 540 |
| `hpperlevel` | 79 |
| `mp` | 100 |
| `mpperlevel` | 0 |
| `movespeed` | 335 |
| `armor` | 32 |
| `armorperlevel` | 3.7 |
| `spellblock` | 30 |
| `spellblockperlevel` | 1.3 |
| `attackrange` | 175 |
| `hpregen` | 4.5 |
| `hpregenperlevel` | 1.25 |
| `mpregen` | 0 |
| `mpregenperlevel` | 0 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 60 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 6 |
| `attackspeed` | 0.625 |

## アビリティ

- **パッシブ — ぷんすこ：** ナーは戦闘中に「怒り」が溜まっていく。「怒り」が最大の状態でスキルを使用するとメガナーに変身し、ステータスとスキルが変化する。

- **Q — ブーメラン/ぽいっ：** ナーが投げるブーメランは、命中した敵にダメージとスロウ効果を与える。戻ってきたブーメランをキャッチすると、クールダウンが短縮される。 メガナーは、ブーメランのかわりに岩石を投げる。敵に命中するとその場に落下して、付近の敵すべてにダメージとスロウ効果を与える。落ちた岩石を拾うとクールダウンが短縮される。
- **W — ごきげん/こてんぱん：** ナーが通常攻撃とスキルで相手にマークをつけるようになる。マークがたまった敵を攻撃するとナーは興奮し、追加ダメージを与えて移動速度が増加する。 メガナーは興奮を通りこし、怒りが爆発する。片腕を目の前におもいきり振り下ろし、範囲内の敵ユニットにダメージを与えてスタン効果を付与する。
- **E — ぴょんぴょん/ドーン！：** ナーがジャンプする。ユニットの上に着地すると、頭の上をはねてさらに遠くまでジャンプする。 メガナーは体が大きすぎて弾まない。そのかわり、着地するときに体をたたきつけて衝撃波をうみだし、周囲の敵にダメージを与える。着地地点にいる敵にはスロウ効果を与える。
- **R — ナー！：** メガナーが周りのモノを根こそぎ指定方向へ投げ、命中した敵にダメージとスロウ効果を与える。投げられた敵が壁にぶつかるとスタン状態になり、追加ダメージを受ける。

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Gnar` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Gnar.png)
