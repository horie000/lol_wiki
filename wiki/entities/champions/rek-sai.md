---
title: "レク＝サイ"
type: entity
status: active
created: 2026-09-14
updated: 2026-09-15
sources:
  - "[[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]]"
  - "[[wiki/sources/src-2026-09-14-dragontail-16-18-1]]"
tags:
  - champion
  - role-fighter
  - role-tank
  - data-dragon
champion_id: "RekSai"
champion_key: "421"
data_version: "16.18.1"
roles:
  - "Fighter"
  - "Tank"
resource_type: "怒り"
image_path: "raw/assets/champions/RekSai.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/RekSai.png"
---

# レク＝サイ

![[raw/assets/champions/RekSai.png|128]]

## 基本情報

- **英字ID：** `RekSai`
- **キー：** `421`
- **称号：** 地底の恐怖
- **データversion：** `16.18.1`

## 紹介

頂点捕食者であるレク＝サイは地中を移動し、獲物を奇襲して貪り食う無情なヴォイドの生物だ。かつて栄華を誇ったシュリーマ帝国があった一帯は、今や彼女の飽くなき食欲の犠牲となって荒廃している。行商や貿易商、武装隊商ですら、彼女とその子供たちの狩場を避けるために、わざわざ数百キロもの回り道をする。地平線にレク＝サイの姿が見えた時、足元から訪れる死から逃れられる者はいない。

## 分類

- **役割タグ：** `Fighter`、`Tank`
- **リソース種別：** 怒り

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 8 |
| `defense` | 5 |
| `magic` | 2 |
| `difficulty` | 3 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 600 |
| `hpperlevel` | 99 |
| `mp` | 100 |
| `mpperlevel` | 0 |
| `movespeed` | 340 |
| `armor` | 35 |
| `armorperlevel` | 4.5 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 175 |
| `hpregen` | 2.5 |
| `hpregenperlevel` | 0.5 |
| `mpregen` | 0 |
| `mpregenperlevel` | 0 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 62 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2 |
| `attackspeed` | 0.667 |

## アビリティ

- **パッシブ — ゼル＝サイの怒り：** 通常攻撃または通常スキルを当てると「フューリー」がたまる。地中潜伏中に「フューリー」を消費して自身の体力を回復する。

- **Q — 女王の怒り/獲物定め：** 次の3回の通常攻撃が近接する周囲の敵に追加物理ダメージを与える。 「潜伏」を発動すると、ヴォイドのエネルギーを帯びた大地を打ち上げ、敵にダメージを与えて命中した敵を可視化する。
- **W — 潜伏/襲撃：** 地中に潜伏して地中専用のスキルを使用できるようになり、移動速度が増加する。視界範囲は狭まり、通常攻撃を行えなくなる。 「潜伏」発動中は、「襲撃」を発動して近接する敵をノックアップさせてダメージを与えることができる。
- **E — 激情の牙/掘削：** 対象に噛み付いて物理ダメージを与え、「フューリー」が最大の場合は、2倍の確定ダメージを与える。 「潜伏」を発動すると、長時間持続し、何度も使用することができるトンネルを作る。敵は、このトンネルの開口部の上に立つことで、これを崩壊させることができる。
- **R — ヴォイドラッシュ：** ダメージを与えた対象を自動的にマークする。このスキルを発動させると、少しの間対象指定不可になり、マークした対象に突進して、相手の最大体力に応じた大ダメージを与える。

<!-- power-spike:start -->
## パワースパイク

- **区分：** 中盤
- **判定：** [[wiki/syntheses/champion-power-spikes-v16-18-1|パワースパイク分類 v16.18.1]] に基づく原典ベースの推論。
- **根拠：**
  - 本分類で採用した序盤の基礎ステータス上位15%と、終盤の能力の蓄積成長・明示的なステータス連動のいずれにも当たらないため、中盤を暫定指定する。
- **限界：** スキル基礎ダメージ・係数・アイテム完成時刻を全チャンピオンで統一比較できる原典値がないため、実戦の強さや購入優先度を断定しない。

<!-- power-spike:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.RekSai` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/RekSai.png)
