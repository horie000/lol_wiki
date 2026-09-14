---
title: "ジャンナ"
type: entity
status: active
created: 2026-09-14
updated: 2026-09-14
sources:
  - "[[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]]"
  - "[[wiki/sources/src-2026-09-14-dragontail-16-18-1]]"
tags:
  - champion
  - role-support
  - role-mage
champion_id: "Janna"
champion_key: "40"
data_version: "16.18.1"
roles:
  - "Support"
  - "Mage"
resource_type: "マナ"
image_path: "raw/assets/champions/Janna.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Janna.png"
---

# ジャンナ

![[raw/assets/champions/Janna.png|128]]

## 基本情報

- **英字ID：** `Janna`
- **キー：** `40`
- **称号：** 嵐の怒り
- **データversion：** `16.18.1`

## 紹介

ルーンテラの嵐を操るジャンナは、謎めいた風の精霊として寄る辺ないゾウンの人々を守っている。彼女は、大嵐に遭う危険も顧みず海に出るルーンテラの船乗りたちが、無事に航海できるよう乞い願う気持ちから生まれたとも言われる。ジャンナの恵みと庇護はゾウンの奥深くにまで届き、救いを求める人々に希望の光を与える。いつ、どこに現れるかは誰にもわからないが、彼女は窮地に陥った者に手を差し伸べてくれるのだ。

## 分類

- **役割タグ：** `Support`、`Mage`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 3 |
| `defense` | 5 |
| `magic` | 7 |
| `difficulty` | 7 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 570 |
| `hpperlevel` | 90 |
| `mp` | 360 |
| `mpperlevel` | 50 |
| `movespeed` | 325 |
| `armor` | 28 |
| `armorperlevel` | 4.5 |
| `spellblock` | 30 |
| `spellblockperlevel` | 1.3 |
| `attackrange` | 550 |
| `hpregen` | 5.5 |
| `hpregenperlevel` | 0.55 |
| `mpregen` | 11.5 |
| `mpregenperlevel` | 0.4 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 47 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 3 |
| `attackspeed` | 0.625 |

## アビリティ

- **パッシブ — テイルウィンド：** ジャンナに向かって移動する際、味方チャンピオンは移動速度が増加する。 通常攻撃時効果および「ゼファー」で、増加移動速度の一定割合にあたる追加魔法ダメージを与える。

- **Q — ハウリングゲイル：** 大気を操り、小さな竜巻を生み出す。竜巻は時間とともに成長し、時間がたつか再度このスキルを使うことで指定方向へ直進して、進路上の敵ユニットにダメージとノックアップを与える。
- **W — ゼファー：** 風の精霊を召喚し、自動効果として移動速度が増加すると同時に、ユニットをすり抜けるようになる。発動すると対象に風の精霊を飛ばして、ダメージとスロウ効果を与える。
- **E — ストームブレス：** 対象に魔法の風を呼び寄せる。風はシールドとなって味方チャンピオンやタワーをダメージから守ると同時に、攻撃力を増加させる。
- **R — モンスーン：** 魔法の嵐に包まれ、周囲の敵を吹き飛ばす。その後詠唱を続け、癒しの風によって範囲内の味方の体力を回復する。

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Janna` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Janna.png)
