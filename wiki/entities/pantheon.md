---
title: "パンテオン"
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
  - role-assassin
champion_id: "Pantheon"
champion_key: "80"
data_version: "16.18.1"
roles:
  - "Fighter"
  - "Assassin"
resource_type: "マナ"
image_path: "raw/assets/champions/Pantheon.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Pantheon.png"
---

# パンテオン

![[raw/assets/champions/Pantheon.png|128]]

## 基本情報

- **英字ID：** `Pantheon`
- **キー：** `80`
- **称号：** 砕けぬ槍
- **データversion：** `16.18.1`

## 紹介

かつて不本意にも戦の神髄の器となったアトレウスは、天空から星々を切り離した一撃により自身に宿るその天の力を殺されながらも、屈することなく生き延びた。やがて彼は定命であるがゆえの力を、そしてその粘り強い不屈の精神を貴ぶようになった。今は亡き神髄の武器に不屈の意志を注ぎ、パンテオンの生まれ変わりとなったアトレウスは神的な存在に立ち向かう。

## 分類

- **役割タグ：** `Fighter`、`Assassin`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 9 |
| `defense` | 4 |
| `magic` | 3 |
| `difficulty` | 4 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 650 |
| `hpperlevel` | 109 |
| `mp` | 317 |
| `mpperlevel` | 31 |
| `movespeed` | 345 |
| `armor` | 40 |
| `armorperlevel` | 4.95 |
| `spellblock` | 28 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 175 |
| `hpregen` | 6 |
| `hpregenperlevel` | 0.65 |
| `mpregen` | 7.35 |
| `mpregenperlevel` | 0.45 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 64 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2.95 |
| `attackspeed` | 0.658 |

## アビリティ

- **パッシブ — 定命の意志：** スキルまたは通常攻撃を数回行うと、次のスキルが強化される。

- **Q — 彗星の槍：** 指定方向に槍を突く、または槍を投げる。
- **W — 跳撃の盾：** 対象に向かってダッシュし、ダメージを与えてスタンさせる。
- **E — イージスの猛攻：** 盾を構え、正面からのダメージを無効化しながら、槍で連続攻撃を繰り出す。
- **R — 偉大なる星路：** 精神を集中させて空高く跳びあがり、流星となって指定地点に上空から突撃する。

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Pantheon` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Pantheon.png)
