---
title: "スカーナー"
type: entity
status: active
created: 2026-09-14
updated: 2026-09-14
sources:
  - "[[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]]"
  - "[[wiki/sources/src-2026-09-14-dragontail-16-18-1]]"
tags:
  - champion
  - role-tank
  - role-fighter
champion_id: "Skarner"
champion_key: "72"
data_version: "16.18.1"
roles:
  - "Tank"
  - "Fighter"
resource_type: "マナ"
image_path: "raw/assets/champions/Skarner.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Skarner.png"
---

# スカーナー

![[raw/assets/champions/Skarner.png|128]]

## 基本情報

- **英字ID：** `Skarner`
- **キー：** `72`
- **称号：** 原始の守護者
- **データversion：** `16.18.1`

## 紹介

古代の巨大生物種ブラカーンであるスカーナーは、イシュタルの支配層“ユン・タル”初代メンバーのひとりとして崇拝されている。自らの国家を外敵から守ることにすべてを捧げたスカーナーは、イシャオカン地下の居室で大地の震動に耳を澄ませ、脅威を察知しようとしている。イシュタルが外界から隔絶されていることに対し、ユン・タルの面々が疑問を呈せば呈すほど、スカーナーはますます偏執的に、頑なになり、是が非でもイシュタルとその民を守ろうとするのだった──それがいかなる代償を伴おうとも。

## 分類

- **役割タグ：** `Tank`、`Fighter`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 7 |
| `defense` | 8 |
| `magic` | 5 |
| `difficulty` | 5 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 630 |
| `hpperlevel` | 110 |
| `mp` | 320 |
| `mpperlevel` | 40 |
| `movespeed` | 335 |
| `armor` | 33 |
| `armorperlevel` | 4.5 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 150 |
| `hpregen` | 7.5 |
| `hpregenperlevel` | 0.75 |
| `mpregen` | 7.2 |
| `mpregenperlevel` | 0.75 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 63 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2 |
| `attackspeed` | 0.625 |

## アビリティ

- **パッシブ — 響振動：** スカーナーの通常攻撃、「砕けし大地」、「大地の怒り」、「インペイル」は、敵に「振動」を付与する。「振動」が最大スタックになると、その効果時間をかけて敵に最大体力に応じた魔法ダメージを与える。

- **Q — 砕けし大地/大地の怒り：** 地面から通常攻撃を強化する巨大な岩を掘り起こす。岩は強力な飛翔物として投げることができる。
- **W — 激震の砦：** シールドを獲得して地震を発生させ、衝撃波で敵にダメージとスロウ効果を与える。
- **E — イシュタルの衝動：** 前方に突撃して地形を通り抜ける。チャンピオンか大型モンスターに衝突すると、対象を次にぶつかった壁に叩きつけ、ダメージを与えてスタンさせる。
- **R — インペイル：** 尻尾で前方を貫き、敵チャンピオンにサプレッション効果を与える。サプレッション効果を受けた犠牲者は、スカーナーの動きに追従して引きずられる。

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Skarner` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Skarner.png)
