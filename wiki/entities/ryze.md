---
title: "ライズ"
type: entity
status: active
created: 2026-09-14
updated: 2026-09-14
sources:
  - "[[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]]"
  - "[[wiki/sources/src-2026-09-14-dragontail-16-18-1]]"
tags:
  - champion
  - role-mage
champion_id: "Ryze"
champion_key: "13"
data_version: "16.18.1"
roles:
  - "Mage"
resource_type: "マナ"
image_path: "raw/assets/champions/Ryze.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Ryze.png"
---

# ライズ

![[raw/assets/champions/Ryze.png|128]]

## 基本情報

- **英字ID：** `Ryze`
- **キー：** `13`
- **称号：** ルーンの魔導師
- **データversion：** `16.18.1`

## 紹介

ライズは類まれな能力を持つルーンテラ屈指の魔術師として知られ、古くから揺るぎない信念を持って活動している。その信念の裏に、彼は耐え難いほどの重荷を背負っている。ライズは計り知れない才能と神秘の力に関する膨大な知識を駆使し、ワールドルーン──無から世界を形成したとされる原始の魔法の断片──を探すことに人生を捧げる。古代文字が刻まれたルーンは、妄用される前に回収しなければならない。ルーンテラを創生した古代文字は、ルーンテラを破壊する力をも秘めているのだ。

## 分類

- **役割タグ：** `Mage`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 2 |
| `defense` | 2 |
| `magic` | 10 |
| `difficulty` | 7 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 620 |
| `hpperlevel` | 124 |
| `mp` | 300 |
| `mpperlevel` | 70 |
| `movespeed` | 340 |
| `armor` | 22 |
| `armorperlevel` | 4.2 |
| `spellblock` | 32 |
| `spellblockperlevel` | 1.3 |
| `attackrange` | 550 |
| `hpregen` | 8 |
| `hpregenperlevel` | 0.8 |
| `mpregen` | 8 |
| `mpregenperlevel` | 1 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 55 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2.11 |
| `attackspeed` | 0.658 |

## アビリティ

- **パッシブ — 古代の呪術：** ライズのスキルは増加したマナに応じて追加ダメージを与え、魔力に応じて最大マナが一定割合増加する。

- **Q — オーバーロード：** 自動効果: 他の通常スキルを使うと「オーバーロード」のクールダウンがリセットされ、「ルーン」がチャージされる。「ルーン」が2つチャージされた状態で「オーバーロード」を使用すると、少しの間移動速度が増加する。 発動効果: 凝縮したエネルギー弾を直線上に発射して、最初に当たった敵にダメージを与える。すでに対象に「フラックス」が付与されていた場合、「オーバーロード」は追加ダメージを与え、周囲の敵に「フラックス」が波及する。
- **W — ルーンプリズン：** 対象をルーンの檻に捕らえ、ダメージとスロウ効果を与える。対象に「フラックス」が付与されている場合は、スロウの代わりにスネア状態にする。
- **E — スペルフラックス：** 純粋な魔力を凝縮したオーブを発射して対象にダメージを与え、対象とその周囲のすべての敵にデバフを与える。ライズのスキルはデバフを受けた敵には追加効果を与える。
- **R — ポータルワープ：** 自動効果: 「フラックス」が付与された対象に「オーバーロード」で与える追加ダメージが増加する。 発動効果: 近くにポータルを発生させる。数秒後、指定した場所にポータルの範囲内の味方をテレポートさせる。

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Ryze` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Ryze.png)
