---
title: "ゼド"
type: entity
status: active
created: 2026-09-14
updated: 2026-09-14
sources:
  - "[[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]]"
  - "[[wiki/sources/src-2026-09-14-dragontail-16-18-1]]"
tags:
  - champion
  - role-assassin
champion_id: "Zed"
champion_key: "238"
data_version: "16.18.1"
roles:
  - "Assassin"
resource_type: "気"
image_path: "raw/assets/champions/Zed.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Zed.png"
---

# ゼド

![[raw/assets/champions/Zed.png|128]]

## 基本情報

- **英字ID：** `Zed`
- **キー：** `238`
- **称号：** 影の頭領
- **データversion：** `16.18.1`

## 紹介

無慈悲で非情なゼドは、ノクサスの侵略者たちを追い出すためにアイオニアの伝統的な魔法と武術を軍事利用することを目的とした組織、「影の一団」の頭領である。戦争のさなか、追い込まれた彼は強力だが危険な穢れをもたらす邪悪な霊界の魔法を使い、秘密の影の形態を解放した。あらゆる禁忌の術を身に付けたゼドは、自分の祖国と自分が新たに創設した組織の脅威とみなした者は、誰であろうと抹殺する。

## 分類

- **役割タグ：** `Assassin`
- **リソース種別：** 気

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 9 |
| `defense` | 2 |
| `magic` | 1 |
| `difficulty` | 7 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 654 |
| `hpperlevel` | 99 |
| `mp` | 200 |
| `mpperlevel` | 0 |
| `movespeed` | 345 |
| `armor` | 32 |
| `armorperlevel` | 4.7 |
| `spellblock` | 29 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 125 |
| `hpregen` | 7 |
| `hpregenperlevel` | 0.65 |
| `mpregen` | 50 |
| `mpregenperlevel` | 0 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 63 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 3.3 |
| `attackspeed` | 0.651 |

## アビリティ

- **パッシブ — 弱者必衰：** 残り体力の少ない敵を通常攻撃した場合、追加魔法ダメージを与える。同じ敵チャンピオンには数秒に1度しか効果が発生しない。

- **Q — 風魔手裏剣：** 自身と影が平型手裏剣を投げる。 手裏剣が命中した敵それぞれにダメージを与える。
- **W — 影分身：** 自動効果: 自身と影が特定の敵に同一のスキルを命中させるたびに、気が回復する(各スキルの発動中、一度のみ有効)。 発動効果: 影を指定方向に放つ。影は数秒間その場に留まる。再発動で自身と影の位置が入れ替わる。
- **E — 影薙ぎ：** 自身と影が回転斬りを放ち、周囲の敵にダメージを与える。影の回転斬りが命中した敵はスロウ効果を受ける。
- **R — 死の刻印：** 対象指定されなくなり、指定した敵チャンピオンにダッシュして印を付与する。3秒後に印が爆発して、印が付与されている間に自身が対象に与えた全ダメージの一定割合のダメージをもう一度与える。

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Zed` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Zed.png)
