---
title: "マスター・イー"
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
  - role-assassin
champion_id: "MasterYi"
champion_key: "11"
data_version: "16.18.1"
roles:
  - "Fighter"
  - "Assassin"
resource_type: "マナ"
image_path: "raw/assets/champions/MasterYi.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/MasterYi.png"
---

# マスター・イー

![[raw/assets/champions/MasterYi.png|128]]

## 基本情報

- **英字ID：** `MasterYi`
- **キー：** `11`
- **称号：** ウージューの剣客
- **データversion：** `16.18.1`

## 紹介

極限まで心身を鍛え上げたマスター・イーは、もはや心技一体の境地へと達している。武力に訴えるのはやむを得ぬ場合のみと己を律しながらも、その優雅で素早い太刀筋には刹那の迷いも見られない。アイオニアに伝わる武術、ウージュースタイルの現存する最後の伝承者の一人として、マスター・イーは洞察の七つのレンズを使い、その生涯をかけて、彼の部族が残した遺産を伝授するのにふさわしい弟子たちを探している。

## 分類

- **役割タグ：** `Fighter`、`Assassin`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 10 |
| `defense` | 4 |
| `magic` | 2 |
| `difficulty` | 4 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 640 |
| `hpperlevel` | 105 |
| `mp` | 251 |
| `mpperlevel` | 42 |
| `movespeed` | 355 |
| `armor` | 33 |
| `armorperlevel` | 5 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 175 |
| `hpregen` | 7.5 |
| `hpregenperlevel` | 0.65 |
| `mpregen` | 7.25 |
| `mpregenperlevel` | 0.45 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 65 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2.5 |
| `attackspeed` | 0.679 |

## アビリティ

- **パッシブ — ダブルストライク：** 通常攻撃を数回行うごとに、通常攻撃が2回連続攻撃になる。

- **Q — アルファストライク：** 目にもとまらぬ速さで複数の敵を斬り抜け、物理ダメージを与える。この間、マスター・イーは対象指定されない。このスキルの攻撃はクリティカルを発生させる場合もあり、モンスターには追加物理ダメージを与える。通常攻撃をするたびに、このスキルのクールダウンが短縮される。
- **W — 明鏡止水：** 精神を統一して体力を回復する。また効果時間中、受けるダメージを軽減する。さらに、詠唱中は毎秒「ダブルストライク」のスタックを獲得して、「ウージュースタイル」と「ハイランダー」の残り効果時間を一時停止する。
- **E — ウージュースタイル：** 通常攻撃が追加確定ダメージを与える。
- **R — ハイランダー：** 一時的に移動速度と攻撃速度が増加し、あらゆるスロウ効果を受けなくなる。発動中にチャンピオンに対するキルまたはアシストを達成すると「ハイランダー」の効果時間が延びる。またこのスキルは自動効果を持ち、チャンピオンに対するキルまたはアシストを達成すると、他のスキルのクールダウンが短縮されるようになる。

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.MasterYi` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/MasterYi.png)
