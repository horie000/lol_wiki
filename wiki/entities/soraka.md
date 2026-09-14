---
title: "ソラカ"
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
  - role-mage
champion_id: "Soraka"
champion_key: "16"
data_version: "16.18.1"
roles:
  - "Support"
  - "Mage"
resource_type: "マナ"
image_path: "raw/assets/champions/Soraka.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Soraka.png"
---

# ソラカ

![[raw/assets/champions/Soraka.png|128]]

## 基本情報

- **英字ID：** `Soraka`
- **キー：** `16`
- **称号：** 星の子
- **データversion：** `16.18.1`

## 紹介

霊峰ターゴンの彼方にある宇宙の次元をさまよっていたソラカは、定命の種族を彼らの暴力的な本能から守るために、自らの永遠の命を手放してやってきた。彼女は出会ったものすべてに慈悲と情けの美徳を広めようと努めており、彼女を傷つけようとするものですら治癒を施す。この世界で様々な紛争を目にしてきたにもかかわらず、彼女は今も、ルーンテラの人々には可能性が残っていると信じている。

## 分類

- **役割タグ：** `Support`、`Mage`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 2 |
| `defense` | 5 |
| `magic` | 7 |
| `difficulty` | 3 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 605 |
| `hpperlevel` | 88 |
| `mp` | 425 |
| `mpperlevel` | 40 |
| `movespeed` | 325 |
| `armor` | 32 |
| `armorperlevel` | 5 |
| `spellblock` | 30 |
| `spellblockperlevel` | 1.3 |
| `attackrange` | 550 |
| `hpregen` | 2.5 |
| `hpregenperlevel` | 0.5 |
| `mpregen` | 11.5 |
| `mpregenperlevel` | 0.4 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 50 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2.14 |
| `attackspeed` | 0.625 |

## アビリティ

- **パッシブ — 救済の足音：** 近くにいる体力の少ない味方に向かって移動する際に、ソラカの移動速度が増加する。

- **Q — 星のささやき：** 指定地点に流れ星が落ち、周囲の敵ユニットに魔法ダメージとスロウ効果を与える。敵チャンピオンに「星のささやき」が命中した場合、ソラカの体力が回復する。
- **W — 星霊の癒し：** 自身の体力を消費し、指定した味方チャンピオンの体力を回復する。
- **E — 星の静寂：** 指定した場所に時空の渦を生じさせ、巻き込んだ敵チャンピオンすべてにサイレンス効果を付与する。さらに渦が消滅した瞬間に渦の範囲内に居るすべての敵チャンピオンにスネア効果を付与する。
- **R — 星に願いを：** ソラカとすべての味方チャンピオンが降り注ぐ希望の光で満たされ、瞬時に体力が回復する。

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Soraka` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Soraka.png)
