---
title: "セジュアニ"
type: entity
status: active
created: 2026-09-14
updated: 2026-09-15
sources:
  - "[[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]]"
  - "[[wiki/sources/src-2026-09-14-dragontail-16-18-1]]"
  - "[[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]"
tags:
  - champion
  - role-tank
  - data-dragon
champion_id: "Sejuani"
champion_key: "113"
data_version: "16.18.1"
roles:
  - "Tank"
resource_type: "マナ"
image_path: "raw/assets/champions/Sejuani.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Sejuani.png"
---

# セジュアニ

![[raw/assets/champions/Sejuani.png|128]]

## 基本情報

- **英字ID：** `Sejuani`
- **キー：** `113`
- **称号：** 極北の激憤
- **データversion：** `16.18.1`

## 紹介

残酷で情け容赦のないセジュアニは、フレヨルドでもっとも恐れられる部族のひとつであるウィンタークロウ族のアイスボーンの戦母だ。彼女の部族は常に過酷な自然の中で生き残りをかけた戦いを強いられており、厳しい冬を乗り切るためにノクサスやデマーシア、アヴァローサンを襲撃しなければならない状況にある。これらの危険な戦いではセジュアニ自身が戦闘に立ち、愛猪ブリストルに跨って、真なる氷のフレイルで敵を凍らせて砕き散らしている。

## 分類

- **役割タグ：** `Tank`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 5 |
| `defense` | 7 |
| `magic` | 6 |
| `difficulty` | 4 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 630 |
| `hpperlevel` | 114 |
| `mp` | 400 |
| `mpperlevel` | 40 |
| `movespeed` | 340 |
| `armor` | 34 |
| `armorperlevel` | 5.45 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 150 |
| `hpregen` | 8.5 |
| `hpregenperlevel` | 1 |
| `mpregen` | 7 |
| `mpregenperlevel` | 0.7 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 66 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 3.5 |
| `attackspeed` | 0.688 |

## アビリティ

- **パッシブ — 極北の激憤：** 非戦闘状態が続くと、「氷結の鎧」を獲得して物理防御と魔法防御が増加し、スロウ効果を受けなくなる。「氷結の鎧」はダメージを受けたあとも少しの間だけ継続する。自身がスタンさせた敵を攻撃すると、その氷が砕けて大きな魔法ダメージを与える。

- **Q — 猪突凍進：** 敵に突進してノックアップする。敵チャンピオンをノックアップすると、そこで突進が止まる。﻿
- **W — 氷河の怒り：** メイスを2回振り、ダメージとスロウ効果を与えて「凍傷」のスタックを付与する。
- **E — 永久凍土：** 「凍傷」のスタックが最大になった敵チャンピオンを凍らせてスタンさせる。
- **R — グレイシャルプリズン：** ボーラを投げて、最初に当たった敵チャンピオンを凍らせてスタンさせる。さらに氷の嵐を巻き起こして、他の敵ユニットにスロウ効果を与える。

<!-- power-spike:start -->
## パワースパイク

- **区分：** 中盤
- **判定：** [[wiki/syntheses/champion-power-spikes-v16-18-1|パワースパイク分類 v16.18.1]] に基づく原典ベースの推論。
- **根拠：**
  - 本分類で採用した序盤の基礎ステータス上位15%と、終盤の能力の蓄積成長・明示的なステータス連動のいずれにも当たらないため、中盤を暫定指定する。
- **限界：** スキル基礎ダメージ・係数・アイテム完成時刻を全チャンピオンで統一比較できる原典値がないため、実戦の強さや購入優先度を断定しない。

<!-- power-spike:end -->

<!-- power-spike-match:start -->
## 試合時間別の観測

- **観測分類：** 終盤寄り
- **対象試合：** 142試合、全体勝率 52.1%
- **時間帯別勝率：** 〜20分 42.9%（n=28）、20〜25分 56.0%（n=25）、25〜30分 43.9%（n=41）、30〜35分 56.0%（n=25）、35分〜 69.6%（n=23）
- **最高帯：** 35分〜（判定差 26.7ポイント）
- **判定根拠：** 35分〜が最高、短時間帯との差 26.7%
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Sejuani` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Sejuani.png)
