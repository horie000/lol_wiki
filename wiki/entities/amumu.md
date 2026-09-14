---
title: "アムム"
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
  - role-support
champion_id: "Amumu"
champion_key: "32"
data_version: "16.18.1"
roles:
  - "Tank"
  - "Support"
resource_type: "マナ"
image_path: "raw/assets/champions/Amumu.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Amumu.png"
---

# アムム

![[raw/assets/champions/Amumu.png|128]]

## 基本情報

- **英字ID：** `Amumu`
- **キー：** `32`
- **称号：** めそめそミイラ
- **データversion：** `16.18.1`

## 紹介

孤独で悲しい魂を抱いて古代シュリーマで生まれたアムムは、友達を探して世界中を彷徨っている。アムムは古代の呪いによって永遠に独りぼっちでいる運命を背負わされており、触れた者は死を免れず、愛した者は破滅の一途を辿る。アムムを目にした者曰く「彼は生ける屍だ。その体は小さく、苔の生した包帯でぐるぐる巻きにされている。」アムムは何世代にも渡って語り継がれる神話や民話、伝説にも登場する。こうした物語には、往々にして空想と真実が入り混じっている。

## 分類

- **役割タグ：** `Tank`、`Support`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 2 |
| `defense` | 6 |
| `magic` | 8 |
| `difficulty` | 3 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 685 |
| `hpperlevel` | 94 |
| `mp` | 285 |
| `mpperlevel` | 40 |
| `movespeed` | 335 |
| `armor` | 33 |
| `armorperlevel` | 4 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 125 |
| `hpregen` | 9 |
| `hpregenperlevel` | 0.85 |
| `mpregen` | 7.4 |
| `mpregenperlevel` | 0.55 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 57 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2.18 |
| `attackspeed` | 0.736 |

## アビリティ

- **パッシブ — 呪いの手：** 通常攻撃で敵に「呪い」をかける。呪われた対象は、魔法ダメージを受ける際に追加確定ダメージを受けるようになる。

- **Q — 絡みつく包帯：** 指定方向にべとべとの包帯を投げつける。敵に当たるとダメージとスタンを与え、包帯をたぐって相手の近くに素早く移動する。
- **W — めそめそ：** 涙を流し、触れた敵に最大体力の一定割合のダメージを毎秒与え、対象に付与された「呪い」の効果時間を更新する。
- **E — だだっこ：** 敵から受ける物理ダメージを恒久的に軽減する。発動して怒りを爆発させると、周囲の敵にダメージを与える。自身が攻撃を受けるたびに「だだっこ」のクールダウンが短縮される。
- **R — めそめそミイラの呪い：** 周囲の敵ユニットを包帯で拘束して「呪い」を付与する。さらにダメージを与えてスタンさせる。

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Amumu` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Amumu.png)
