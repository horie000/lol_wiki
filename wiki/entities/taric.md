---
title: "タリック"
type: entity
status: active
created: 2026-09-14
updated: 2026-09-14
sources:
  - "[[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]]"
  - "[[wiki/sources/src-2026-09-14-dragontail-16-18-1]]"
tags:
  - champion
  - role-support
  - role-tank
champion_id: "Taric"
champion_key: "44"
data_version: "16.18.1"
roles:
  - "Support"
  - "Tank"
resource_type: "マナ"
image_path: "raw/assets/champions/Taric.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Taric.png"
---

# タリック

![[raw/assets/champions/Taric.png|128]]

## 基本情報

- **英字ID：** `Taric`
- **キー：** `44`
- **称号：** ヴァロランの守護者
- **データversion：** `16.18.1`

## 紹介

タリックは守護の神髄であり、ルーンテラの生命、愛、美の守護者として驚異的な力を発揮する。軍務放棄の汚名を受けて故郷のデマーシアから放逐され、贖罪のために霊峰ターゴンに登ったタリックは、図らずも天上の存在からさらなる使命を与えられることとなった。いにしえのターゴンから力を授かったヴァロランの守護者は、密かに侵略を進めるヴォイドの穢れに対し揺るぎなき決意と共に立ち向かっている。

## 分類

- **役割タグ：** `Support`、`Tank`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 4 |
| `defense` | 8 |
| `magic` | 5 |
| `difficulty` | 3 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 645 |
| `hpperlevel` | 99 |
| `mp` | 300 |
| `mpperlevel` | 60 |
| `movespeed` | 340 |
| `armor` | 40 |
| `armorperlevel` | 4.3 |
| `spellblock` | 28 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 150 |
| `hpregen` | 6 |
| `hpregenperlevel` | 0.5 |
| `mpregen` | 8.5 |
| `mpregenperlevel` | 0.8 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 55 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2 |
| `attackspeed` | 0.625 |

## アビリティ

- **パッシブ — ブラバド：** スキル使用後の通常攻撃2回が素早くなり、追加魔法ダメージを付与する。さらに通常スキルのクールダウンを短縮する。

- **Q — スターライトタッチ：** 周囲の味方チャンピオンの体力をチャージ数に応じて回復する。ブラバド効果中に通常攻撃を行うと、「スターライトタッチ」のチャージを1つ獲得する。
- **W — バスティオン：** 自動効果: このスキルで繋がっている味方チャンピオンとタリックの物理防御が増加する。 発動効果: 指定した味方チャンピオンと繋がり、両者にシールドを付与するが、離れすぎると繋がりは一時的に消滅する。さらにタリックの全スキルは、繋がっている味方チャンピオンからも同様に発動される。
- **E — ダズル：** 魔法ダメージとスタン効果を持つ星のビームを構え、短い遅延の後に発動する。
- **R — コズミックレディアンス：** 発動から少しして宇宙のエナジーを放ち、自身の周囲の味方を数秒間、無敵状態にする。

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Taric` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Taric.png)
