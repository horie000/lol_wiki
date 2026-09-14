---
title: "ブラウム"
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
  - role-support
champion_id: "Braum"
champion_key: "201"
data_version: "16.18.1"
roles:
  - "Tank"
  - "Support"
resource_type: "マナ"
image_path: "raw/assets/champions/Braum.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Braum.png"
---

# ブラウム

![[raw/assets/champions/Braum.png|128]]

## 基本情報

- **英字ID：** `Braum`
- **キー：** `201`
- **称号：** フレヨルドの漢気
- **データversion：** `16.18.1`

## 紹介

巨大な筋肉が盛り上がる腕と、その筋肉よりも大きな優しい心を持つブラウムは、フレヨルドの誰もが愛する英雄だ。フロストヘルドの北の酒場では、一晩でオークの森を伐採した話や、パンチで山が崩れ去った話など、誰もが彼の怪力伝説に花を咲かせて酒を飲む。魔法の力を宿した宝物庫の扉を盾にして、その筋肉にも負けぬ立派な口ひげで微笑みながら凍てつく北部を歩き回る彼は、助けを必要とする者にとって最高に頼りになる存在だ。

## 分類

- **役割タグ：** `Tank`、`Support`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 3 |
| `defense` | 9 |
| `magic` | 4 |
| `difficulty` | 3 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 610 |
| `hpperlevel` | 112 |
| `mp` | 311 |
| `mpperlevel` | 45 |
| `movespeed` | 335 |
| `armor` | 35 |
| `armorperlevel` | 5 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 125 |
| `hpregen` | 8.5 |
| `hpregenperlevel` | 1 |
| `mpregen` | 7 |
| `mpregenperlevel` | 0.8 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 55 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 3.5 |
| `attackspeed` | 0.644 |

## アビリティ

- **パッシブ — 漢の拳：** 通常攻撃を命中させると「漢の拳」がスタックする。スタックが1つ以上ある敵には、味方の通常攻撃でも効果がスタックする。 スタックが4つ溜まると対象はスタン状態になり、魔法ダメージを受ける。スタン状態になった敵はその後、数秒間はスタックが増加しない。ただしブラウムの攻撃が命中すると追加魔法ダメージを受ける。

- **Q — 冬の凍瘡：** 盾から氷塊を発射し、最初に命中した敵ユニットに魔法ダメージとスロウ効果を与える。 命中した敵には「漢の拳」がスタックする。
- **W — ワシに任せとけ！：** 指定した味方チャンピオンまたはミニオンのもとへ跳躍する。付近に敵チャンピオンがいた場合、対象と敵チャンピオンの間に着地する。着地したあと、自身と対象の物理防御と魔法防御を数秒間増加させる。
- **E — 不破の盾：** 指定方向に巨大な盾を掲げ、数秒間すべての遠距離攻撃を体を張って食い止める。盾を構えている間は移動速度が増加し、最初に盾に当たった攻撃のダメージを無効化する。盾を構えている間、同方向から来る攻撃のダメージを軽減する。
- **R — 氷河の裂溝：** 盾を地面にたたきつけて指定方向に地割れを起こし、周囲にいる敵と地割れのライン上にいる敵をノックアップさせる。 地割れは短時間持続し、範囲内に入った敵にスロウ効果を付与する。

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Braum` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Braum.png)
