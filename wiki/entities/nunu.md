---
title: "ヌヌ＆ウィルンプ"
type: entity
status: active
created: 2026-09-14
updated: 2026-09-14
sources:
  - "[[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]]"
  - "[[wiki/sources/src-2026-09-14-dragontail-16-18-1]]"
tags:
  - champion
  - role-tank
  - role-mage
champion_id: "Nunu"
champion_key: "20"
data_version: "16.18.1"
roles:
  - "Tank"
  - "Mage"
resource_type: "マナ"
image_path: "raw/assets/champions/Nunu.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Nunu.png"
---

# ヌヌ＆ウィルンプ

![[raw/assets/champions/Nunu.png|128]]

## 基本情報

- **英字ID：** `Nunu`
- **キー：** `20`
- **称号：** 少年とイエティ
- **データversion：** `16.18.1`

## 紹介

昔々あるところに、恐ろしい怪物を倒して英雄になりたいと願う少年がいた。しかし怪物の正体を知ってみれば、それは魔力を持った独りぼっちのイエティで、彼はただ友達が欲しいだけだった。古き力によって結ばれ、雪玉遊びの楽しさを共に分かち合ったヌヌとウィルンプは、フレヨルド各地を冒険してまわっている。そしていつかどこかで、ヌヌの母親を見つけ出すことを願っている。彼女を救い出すことができれば、本物の英雄になれるかもしれないのだ…

## 分類

- **役割タグ：** `Tank`、`Mage`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 4 |
| `defense` | 6 |
| `magic` | 7 |
| `difficulty` | 4 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 610 |
| `hpperlevel` | 90 |
| `mp` | 280 |
| `mpperlevel` | 42 |
| `movespeed` | 345 |
| `armor` | 29 |
| `armorperlevel` | 4.2 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 125 |
| `hpregen` | 5 |
| `hpregenperlevel` | 0.8 |
| `mpregen` | 7 |
| `mpregenperlevel` | 0.5 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 61 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2.25 |
| `attackspeed` | 0.625 |

## アビリティ

- **パッシブ — フレヨルドの呼び声：** ヌヌがウィルンプと近くにいる味方1体の攻撃速度と移動速度を増加させる。さらに、ウィルンプの通常攻撃が対象の周囲にいる敵にもダメージを与えるようになる。

- **Q — 丸かじり：** ウィルンプがミニオンかモンスター、または敵チャンピオンにかぶりつき、ダメージを与えて自身の体力を回復する。
- **W — 超特大の雪玉！：** ウィルンプが雪玉をつくって転がす。雪玉を転がす間、雪玉のサイズとスピードが増加していく。雪玉は敵にダメージを与えてノックアップする。
- **E — 雪玉連射：** ヌヌが雪玉を複数投げて敵にダメージを与える。その後、雪玉が当たったチャンピオンと大型モンスターにウィルンプがスネア効果を与える。
- **R — アブソリュート・ゼロ：** ヌヌとウィルンプが一定範囲内に強力な猛吹雪をつくりだして敵にスロウ効果を与え、詠唱完了時に大ダメージを与える。

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Nunu` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Nunu.png)
