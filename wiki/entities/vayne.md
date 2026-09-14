---
title: "ヴェイン"
type: entity
status: active
created: 2026-09-14
updated: 2026-09-14
sources:
  - "[[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]]"
  - "[[wiki/sources/src-2026-09-14-dragontail-16-18-1]]"
tags:
  - champion
  - role-marksman
  - role-assassin
champion_id: "Vayne"
champion_key: "67"
data_version: "16.18.1"
roles:
  - "Marksman"
  - "Assassin"
resource_type: "マナ"
image_path: "raw/assets/champions/Vayne.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Vayne.png"
---

# ヴェイン

![[raw/assets/champions/Vayne.png|128]]

## 基本情報

- **英字ID：** `Vayne`
- **キー：** `67`
- **称号：** ナイトハンター
- **データversion：** `16.18.1`

## 紹介

シャウナ・ヴェインはデマーシアの無慈悲な怪物ハンターであり、自分の家族を殺した悪魔を見つけ出して殺すことに生涯をささげている。前腕部搭載式のクロスボウと復讐に燃える心を武器にする彼女だが、心からの喜びを感じることができるのは、影の中から銀の矢を飛ばして闇の魔術の使い手や、その不浄なる創造物を殺した時だけだ。

## 分類

- **役割タグ：** `Marksman`、`Assassin`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 10 |
| `defense` | 1 |
| `magic` | 1 |
| `difficulty` | 8 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 580 |
| `hpperlevel` | 98 |
| `mp` | 232 |
| `mpperlevel` | 35 |
| `movespeed` | 330 |
| `armor` | 23 |
| `armorperlevel` | 4.6 |
| `spellblock` | 33 |
| `spellblockperlevel` | 1.1 |
| `attackrange` | 550 |
| `hpregen` | 4 |
| `hpregenperlevel` | 0.5 |
| `mpregen` | 7 |
| `mpregenperlevel` | 0.4 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 60 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2.8 |
| `attackspeed` | 0.658 |

## アビリティ

- **パッシブ — ナイトハンター：** 敵チャンピオンに向かって移動する時、移動速度が増加する。

- **Q — タンブル：** 指定方向に前転して移動し、次の攻撃の準備をする。次の通常攻撃が追加ダメージを与える。
- **W — シルバーボルト：** 邪悪な存在が嫌う銀の矢を、クロスボウにつがえる。同じ対象に通常攻撃またはスキルを3回連続で命中させると、対象の最大体力に比例する追加確定ダメージが発生する。
- **E — パニッシュメント：** 背中に担いだ特大クロスボウを構え、指定対象に巨大な矢を撃ち込む。矢を受けたユニットはノックバックされダメージを受ける。ノックバック中に対象が地形に衝突した場合は、追加のダメージが発生し、スタン状態になる。
- **R — ファイナルアワー：** 敵を殲滅すべく特大クロスボウを構え、攻撃力が増加する。効果時間中は「タンブル」発動時にインビジブル状態になり、「タンブル」のクールダウンが短縮される。また、「ナイトハンター」の移動速度増加量が上昇する。

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Vayne` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Vayne.png)
