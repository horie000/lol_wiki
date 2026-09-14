---
title: "ブラッドミア"
type: entity
status: active
created: 2026-09-14
updated: 2026-09-15
sources:
  - "[[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]]"
  - "[[wiki/sources/src-2026-09-14-dragontail-16-18-1]]"
tags:
  - champion
  - role-mage
  - role-fighter
  - data-dragon
champion_id: "Vladimir"
champion_key: "8"
data_version: "16.18.1"
roles:
  - "Mage"
  - "Fighter"
resource_type: "真紅の衝動"
image_path: "raw/assets/champions/Vladimir.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Vladimir.png"
---

# ブラッドミア

![[raw/assets/champions/Vladimir.png|128]]

## 基本情報

- **英字ID：** `Vladimir`
- **キー：** `8`
- **称号：** 真紅の死神
- **データversion：** `16.18.1`

## 紹介

ブラッドミアは定命の者の血に飢えた悪魔であり、帝国の建国時代からずっとノクサスの政治に影響を与えてきている。彼は異常なやり方で自らの命を長らえているだけでなく、習得した血を操る魔術を使い、他者の肉体と精神を自分のものとして扱うこともできる。この能力を活かして、ノクサスの貴族たちが集まるきらびやかなサロンで自分を崇拝する熱狂的な信者たちを作り出し、粗末な路地裏では敵の血を最後の一滴まで搾り取っている。

## 分類

- **役割タグ：** `Mage`、`Fighter`
- **リソース種別：** 真紅の衝動

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 2 |
| `defense` | 6 |
| `magic` | 8 |
| `difficulty` | 7 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 600 |
| `hpperlevel` | 110 |
| `mp` | 2 |
| `mpperlevel` | 0 |
| `movespeed` | 330 |
| `armor` | 24 |
| `armorperlevel` | 4.5 |
| `spellblock` | 30 |
| `spellblockperlevel` | 1.3 |
| `attackrange` | 450 |
| `hpregen` | 7 |
| `hpregenperlevel` | 0.6 |
| `mpregen` | 0 |
| `mpregenperlevel` | 0 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 55 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2 |
| `attackspeed` | 0.658 |

## アビリティ

- **パッシブ — 真紅の盟約：** 増加体力を30得るたび魔力が1増加する。また、魔力1につき体力が1.6増加する(この固有スキル自身の効果とは重複しない)。

- **Q — 吸血：** 指定した敵ユニットから血を吸い取り、体力を吸収する。リソースが溜まっている状態の時、「吸血」のダメージと回復量が一定時間大幅に増加する。
- **W — 紅血の沼：** 2秒間血の池に潜り、敵に対象指定されなくなる。また、池に接触した敵にスロウとダメージを与え、与えたダメージに応じた体力を吸収する。
- **E — 血液奔流：** 自分の体力を消費して血液をチャージし、解放した時に自分の周囲にダメージを与える。この攻撃は敵ユニットを貫通せず、遮られる。
- **R — 呪血の渦：** 指定範囲に急速に進行する疫病をばら撒き、感染した敵は一定時間、あらゆる被ダメージが増加する。さらに数秒後爆発が起こり、感染した敵は魔法ダメージを受け、さらにブラッドミアは感染させた敵チャンピオンの数に応じて体力を回復する。

<!-- power-spike:start -->
## パワースパイク

- **区分：** 終盤
- **判定：** [[wiki/syntheses/champion-power-spikes-v16-18-1|パワースパイク分類 v16.18.1]] に基づく原典ベースの推論。
- **根拠：**
  - 増加体力と魔力を相互に増加させる。
- **限界：** スキル基礎ダメージ・係数・アイテム完成時刻を全チャンピオンで統一比較できる原典値がないため、実戦の強さや購入優先度を断定しない。

<!-- power-spike:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Vladimir` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Vladimir.png)
