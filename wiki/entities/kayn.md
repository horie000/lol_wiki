---
title: "ケイン"
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
champion_id: "Kayn"
champion_key: "141"
data_version: "16.18.1"
roles:
  - "Fighter"
  - "Assassin"
resource_type: "マナ"
image_path: "raw/assets/champions/Kayn.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Kayn.png"
---

# ケイン

![[raw/assets/champions/Kayn.png|128]]

## 基本情報

- **英字ID：** `Kayn`
- **キー：** `141`
- **称号：** 無情の影
- **データversion：** `16.18.1`

## 紹介

恐るべき影の魔術の卓越した使い手であるシエダ・ケイン。彼は己の真の運命──いつの日か自分が「影の一団」を率い、アイオニアが覇権を握る新時代を拓く、という未来のために戦っている。彼が手にする、自我を持つダーキンの武器「ラースト」はケインの心身を着実に侵しつつあるが、気に留める様子はない。あり得る結末はただ二つ。ケインが強い意志で武器をねじ伏せるか、または邪悪な武器に完全に乗っ取られ、ルーンテラを滅亡の道へと誘う扉を開くかだ。

## 分類

- **役割タグ：** `Fighter`、`Assassin`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 10 |
| `defense` | 6 |
| `magic` | 1 |
| `difficulty` | 8 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 655 |
| `hpperlevel` | 103 |
| `mp` | 410 |
| `mpperlevel` | 50 |
| `movespeed` | 340 |
| `armor` | 38 |
| `armorperlevel` | 4.5 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 175 |
| `hpregen` | 8 |
| `hpregenperlevel` | 0.75 |
| `mpregen` | 11.5 |
| `mpregenperlevel` | 0.95 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 68 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2.7 |
| `attackspeed` | 0.669 |

## アビリティ

- **パッシブ — 緋眼の大鎌：** ケインは自我を持つダーキンの古代武器ラーストを用いており、両者は常に互いの支配権をかけて争っている。この戦いはダーキンがケインを取り込むか、ケインがラーストを使いこなし影の暗殺者となるまで続く。 ダーキン: 敵チャンピオンにスキルで与えたダメージの一定割合にあたる体力を回復する。 影の暗殺者: 敵チャンピオンと戦闘開始直後の数秒間、追加ダメージを与える。

- **Q — 飛影斬：** ダッシュしてから斬りつける。その両方でダメージを与える。
- **W — 刃影襲：** 直線上にいる敵にダメージとスロウ効果を与える。
- **E — 影抜き：** ケインが地形を無視して歩くことができる。
- **R — 真影侵壊：** 敵の体の中に侵入して、出てくる時に大ダメージを与える。

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Kayn` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Kayn.png)
