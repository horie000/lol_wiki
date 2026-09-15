---
title: "カルマ"
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
champion_id: "Karma"
champion_key: "43"
data_version: "16.18.1"
roles:
  - "Mage"
  - "Support"
resource_type: "マナ"
image_path: "raw/assets/champions/Karma.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Karma.png"
---

# カルマ

![[raw/assets/champions/Karma.png|128]]

## 基本情報

- **英字ID：** `Karma`
- **キー：** `43`
- **称号：** 目覚めし者
- **データversion：** `16.18.1`

## 紹介

カルマは他の誰にも増して、アイオニアの精神性を重んじる伝統を体現する存在だ。彼女は無限に生まれ変わる古代の魂が実体化した存在であり、過去からの記憶をすべて新たな生へと継承するだけでなく、常人には到底理解の及ばない力を授かっている。近年訪れた危機の折には全力で人々を導いた彼女だが、平和と調和を手にするには多大な犠牲を払わなければならない場合があることを知っている──自分自身にとっても、そして何より大切な故郷にとっても。

## 分類

- **役割タグ：** `Mage`、`Support`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 1 |
| `defense` | 7 |
| `magic` | 8 |
| `difficulty` | 5 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 630 |
| `hpperlevel` | 109 |
| `mp` | 374 |
| `mpperlevel` | 40 |
| `movespeed` | 335 |
| `armor` | 28 |
| `armorperlevel` | 5 |
| `spellblock` | 30 |
| `spellblockperlevel` | 1.3 |
| `attackrange` | 525 |
| `hpregen` | 5.5 |
| `hpregenperlevel` | 0.55 |
| `mpregen` | 13 |
| `mpregenperlevel` | 0.8 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 49 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2.3 |
| `attackspeed` | 0.625 |

## アビリティ

- **パッシブ — 寄せ火：** 自身の攻撃スキルが「マントラ」のクールダウンを短縮する。

- **Q — 心炎：** 精神の炎を解き放ち、敵に命中すると爆発してダメージを与える。 マントラボーナス: 爆発の威力が増し、さらに対象の足下に力場を発生させて範囲内に時間差でダメージを与える。
- **W — 魂縛：** 自身と標的を鎖でつなぎダメージを与え、ステルス状態を見破る。効果終了時まで鎖が破壊されなければ、敵はその場でスネア状態となり再びダメージを受ける。 マントラボーナス: 鎖が強化され自身の体力を回復し、敵に与えるスネア状態の効果時間が延長される。
- **E — 激励：** 指定した味方ユニットにシールドを付与し、ダメージから守ると同時に移動速度を増加させる。 マントラボーナス: 対象からエネルギーが放射され、初期シールドを強化し、周囲にいる味方チャンピオンにも「激励」の効果を付与する。
- **R — マントラ：** カルマが次に使用するスキルを強化し追加効果を付与する。 「マントラ」はレベル1から使用でき、スキルポイントを必要としない。

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Karma` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Karma.png)
