---
title: "ヴェル＝コズ"
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
  - role-support
champion_id: "Velkoz"
champion_key: "161"
data_version: "16.18.1"
roles:
  - "Mage"
  - "Support"
resource_type: "マナ"
image_path: "raw/assets/champions/Velkoz.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Velkoz.png"
---

# ヴェル＝コズ

![[raw/assets/champions/Velkoz.png|128]]

## 基本情報

- **英字ID：** `Velkoz`
- **キー：** `161`
- **称号：** ヴォイドの瞳
- **データversion：** `16.18.1`

## 紹介

ルーンテラに現れた最初のヴォイドの生物がヴェル＝コズであるかどうかは定かではないが、彼の残酷さと計算された知性にかなうヴォイドの生物は他に存在しない。彼の同族たちは周囲のあらゆるものを貪り食うか破滅させるかのどちらかだが、ヴェル＝コズは物質世界とそこに住む戦争好きの奇妙な生き物たちをを詳細に調べて研究し、ヴォイドが利用できる弱点がないか探そうとしている。ただし、ヴェル＝コズは受動的な観察者などからは程遠い存在であり、襲ってくる者がいれば恐怖のプラズマで反撃し、この世界の構造そのものを破壊しようとする。

## 分類

- **役割タグ：** `Mage`、`Support`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 2 |
| `defense` | 2 |
| `magic` | 10 |
| `difficulty` | 8 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 590 |
| `hpperlevel` | 102 |
| `mp` | 469 |
| `mpperlevel` | 21 |
| `movespeed` | 340 |
| `armor` | 22 |
| `armorperlevel` | 4.7 |
| `spellblock` | 30 |
| `spellblockperlevel` | 1.3 |
| `attackrange` | 525 |
| `hpregen` | 5.5 |
| `hpregenperlevel` | 0.55 |
| `mpregen` | 8 |
| `mpregenperlevel` | 0.8 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 55 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 1.59 |
| `attackspeed` | 0.643 |

## アビリティ

- **パッシブ — 有機分解：** スキルが命中するたびに対象の「有機分解」が進行していき、3スタックすると確定ダメージを与える。

- **Q — 電離炸裂弾：** 再発動させるか敵に命中するとT字に分裂するプラズマ弾を発射する。この弾は命中した敵にスロウ効果とダメージを与える。
- **W — ヴォイドの裂谷：** ヴォイドへ通じる裂け目を大地に呼び出し、触れた敵にダメージを与える。裂け目は少ししてから爆発し、再度ダメージを与える。
- **E — 地殻砕裂：** 指定したエリアを爆発させ、範囲内の敵にダメージを与えてノックアップさせる。 至近距離にいる敵は、わずかにふき飛ばされる。
- **R — 生体破壊光線：** 指定方向へ2.5秒間、強力なビームを発射し、触れた敵に魔法ダメージを与える。このスキルによって「有機分解」されて解析が完了したチャンピオンは確定ダメージを代わりに受ける。

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Velkoz` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Velkoz.png)
