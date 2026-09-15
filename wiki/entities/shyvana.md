---
title: "シヴァーナ"
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
champion_id: "Shyvana"
champion_key: "102"
data_version: "16.18.1"
roles:
  - "Fighter"
  - "Tank"
resource_type: "フューリー"
image_path: "raw/assets/champions/Shyvana.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Shyvana.png"
---

# シヴァーナ

![[raw/assets/champions/Shyvana.png|128]]

## 基本情報

- **英字ID：** `Shyvana`
- **キー：** `102`
- **称号：** 半龍人
- **データversion：** `16.18.1`

## 紹介

シヴァーナは恐るべき半龍の戦士だ。普段は人間の姿をしているが、ドラゴンに変身して空を飛び、炎を吐いて敵を焼き殺すこともできる。王子ジャーヴァンⅣの命を救ったことから、シヴァーナは不安を抱えながらも今や王国の近衛隊として仕え、疑念を向けるデマーシアの人々の中で受け入れられようともがいている。

## 分類

- **役割タグ：** `Fighter`、`Tank`
- **リソース種別：** フューリー

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 8 |
| `defense` | 6 |
| `magic` | 3 |
| `difficulty` | 4 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 625 |
| `hpperlevel` | 95 |
| `mp` | 100 |
| `mpperlevel` | 0 |
| `movespeed` | 350 |
| `armor` | 35 |
| `armorperlevel` | 4 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 150 |
| `hpregen` | 7 |
| `hpregenperlevel` | 0.65 |
| `mpregen` | 0 |
| `mpregenperlevel` | 0 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 62 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2 |
| `attackspeed` | 0.638 |

## アビリティ

- **パッシブ — スケールメイル：** 敵チャンピオン、大型ミニオン、大型モンスターのキルかアシストで「スケールメイル」のスタックを獲得し、シヴァーナの防御力が向上する。

- **Q — エンバーストライク：** 次の通常攻撃で、対象とその周囲の両方を攻撃する。このスキルは再発動が可能。ドラゴンフォーム中は再発動が1回追加され、単体の敵に大ダメージを与える。
- **W — インフェルノイージス：** シールドと移動速度を獲得し、少ししてから周囲を爆発させる。ドラゴンフォーム中は、爆発が敵チャンピオンに命中すると自身の体力が回復する。
- **E — モルテンバースト：** 火球を放ち、大型の対象に命中すると爆発して、スロウ効果を付与する。ドラゴンフォーム中は敵を貫通し、大型の敵に命中すると爆発して、炎の軌跡を残す。
- **R — 龍の降臨：** ドラゴンに変身して前方にジャンプし、進路上の敵を逃走させる。ドラゴンフォーム中は巨大化し、通常スキルが強化される。

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Shyvana` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Shyvana.png)
