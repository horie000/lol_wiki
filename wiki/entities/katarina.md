---
title: "カタリナ"
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
  - role-mage
champion_id: "Katarina"
champion_key: "55"
data_version: "16.18.1"
roles:
  - "Assassin"
  - "Mage"
resource_type: "なし"
image_path: "raw/assets/champions/Katarina.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Katarina.png"
---

# カタリナ

![[raw/assets/champions/Katarina.png|128]]

## 基本情報

- **英字ID：** `Katarina`
- **キー：** `55`
- **称号：** 凶兆の刃
- **データversion：** `16.18.1`

## 紹介

優れた判断力と必殺の格闘技術を持つカタリナはノクサスで最強の暗殺者だ。有名なデュ・クートウ将軍の長女である彼女は悟られずに素早く敵を倒す才能で知られている。野心に燃える彼女は、時に味方に犠牲を強いる危険を冒してでも厳重に守られた標的を求めようとするが、どんな任務であっても、カタリナは鋸歯状の刃を持つ無数の短剣を振りかざしてためらうことなく自らの使命を全うする。

## 分類

- **役割タグ：** `Assassin`、`Mage`
- **リソース種別：** なし

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 4 |
| `defense` | 3 |
| `magic` | 9 |
| `difficulty` | 8 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 672 |
| `hpperlevel` | 108 |
| `mp` | 0 |
| `mpperlevel` | 0 |
| `movespeed` | 335 |
| `armor` | 32 |
| `armorperlevel` | 4.7 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 125 |
| `hpregen` | 7.5 |
| `hpregenperlevel` | 0.7 |
| `mpregen` | 0 |
| `mpregenperlevel` | 0 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 58 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2.74 |
| `attackspeed` | 0.658 |

## アビリティ

- **パッシブ — 貪欲なる暗殺者：** 自身がダメージを与えた敵チャンピオンがその直後にキルされると、自身の全スキルのクールダウンが大幅に短縮する。 自身が「短剣」を拾うと、周囲の敵を斬りつけて魔法ダメージを与える。

- **Q — バウンドナイフ：** カタリナが対象に向けて敵から敵へと飛び跳ねる「短剣」を投げる。「短剣」は最後に地面に落ちる。
- **W — プリペレーション：** 少しの間だけカタリナの移動速度が大幅に増加し、「短剣」を頭上に放り投げる。
- **E — 瞬歩：** 対象の地点へブリンクする。対象が敵ユニットなら攻撃し、そうでない場合はもっとも近くにいる敵ユニットを攻撃する。
- **R — デスロータス：** 刃の嵐と化し、周囲の敵チャンピオン(最大3人)に目にもとまらぬ速さで短剣を投げて強大な魔法ダメージを与える。

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Katarina` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Katarina.png)
