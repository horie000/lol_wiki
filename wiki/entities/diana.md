---
title: "ダイアナ"
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
champion_id: "Diana"
champion_key: "131"
data_version: "16.18.1"
roles:
  - "Fighter"
  - "Assassin"
resource_type: "マナ"
image_path: "raw/assets/champions/Diana.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Diana.png"
---

# ダイアナ

![[raw/assets/champions/Diana.png|128]]

## 基本情報

- **英字ID：** `Diana`
- **キー：** `131`
- **称号：** 嘲りの月
- **データversion：** `16.18.1`

## 紹介

三日月形の剣を掲げ振るうダイアナは、霊峰ターゴンの周辺においては迫害により途絶えて久しいルナリの教えに信仰を寄せる女戦士だ。闇の中で冷たく輝く真冬の雪を思わせる鎧を身にまとうその姿は、まさに銀月の力の具現と呼ぶに相応しい。そびえ立つ霊峰ターゴンの頂の向こうから神髄を授かったダイアナは、もはや人間を超越した存在となり、自身の力とこの世における存在意義を見出そうと模索している。

## 分類

- **役割タグ：** `Fighter`、`Assassin`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 7 |
| `defense` | 6 |
| `magic` | 8 |
| `difficulty` | 4 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 640 |
| `hpperlevel` | 109 |
| `mp` | 375 |
| `mpperlevel` | 25 |
| `movespeed` | 345 |
| `armor` | 31 |
| `armorperlevel` | 4.3 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 150 |
| `hpregen` | 6.5 |
| `hpregenperlevel` | 0.85 |
| `mpregen` | 8 |
| `mpregenperlevel` | 0.8 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 57 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2 |
| `attackspeed` | 0.625 |

## アビリティ

- **パッシブ — 繊月の刃：** 通常攻撃3回ごとに周囲の敵に追加魔法ダメージを与える。スキル使用後、5秒間、攻撃速度が増加する。

- **Q — 月影：** 弧を描くように月の力を放ち、命中した敵ユニットに魔法ダメージを与える。 命中した敵には「月光」を付与し、ステルス状態の敵をのぞいて3秒間可視状態にする。
- **W — 朧月の羽衣：** 体の周囲を3つの月光の玉が旋回し、敵と接触すると爆発して有効範囲内の敵ユニットにダメージを与える。さらに発動と同時に、ダイアナを守るシールドが発生する。3つ目の光の玉が爆発すると、シールドを再び展開する。
- **E — 月下美刃：** 復讐心に燃える月の化身となり、敵のところまでダッシュして魔法ダメージを与える。 「月光」が付与された敵に使用した場合、クールダウンがリセットされると同時に、全ての敵ユニットの「月光」が解除される。
- **R — 崩月：** 周囲のすべての敵を可視化して自身の方向に引き寄せ、スロウ効果を与える。 1体以上の敵チャンピオンを引き寄せると、少ししてから自身の上に月光が降り注ぎ、周囲の範囲内の敵に魔法ダメージを与える。このダメージは2体目以降に引き寄せた対象が1体増えるごとに増加する。

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Diana` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Diana.png)
