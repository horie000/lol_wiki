---
title: "リヴェン"
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
champion_id: "Riven"
champion_key: "92"
data_version: "16.18.1"
roles:
  - "Fighter"
  - "Assassin"
resource_type: "なし"
image_path: "raw/assets/champions/Riven.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Riven.png"
---

# リヴェン

![[raw/assets/champions/Riven.png|128]]

## 基本情報

- **英字ID：** `Riven`
- **キー：** `92`
- **称号：** 贖罪の追放者
- **データversion：** `16.18.1`

## 紹介

リヴェンはかつてノクサス軍の剣術家だったが、今では自らが過去に征服しようとした土地で追放者として暮らしている。彼女は信念と非道なまでの手際よさを武器に軍隊で昇進し、伝説のルーンブレードと自らの戦団を授かった。しかし、アイオニアとの戦いで故郷への信念が試されることになり、結局、それは破壊されてしまった。ノクサスそのものが再構築されたという噂が盛んに飛び交うなか、彼女は帝国とのつながりをすべて断ち切り、砕けた世界で自分の居場所を探している。

## 分類

- **役割タグ：** `Fighter`、`Assassin`
- **リソース種別：** なし

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 8 |
| `defense` | 5 |
| `magic` | 1 |
| `difficulty` | 8 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 630 |
| `hpperlevel` | 100 |
| `mp` | 0 |
| `mpperlevel` | 0 |
| `movespeed` | 340 |
| `armor` | 33 |
| `armorperlevel` | 4.4 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 125 |
| `hpregen` | 8.5 |
| `hpregenperlevel` | 0.5 |
| `mpregen` | 0 |
| `mpregenperlevel` | 0 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 64 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 3.5 |
| `attackspeed` | 0.625 |

## アビリティ

- **パッシブ — ルーンブレード：** スキルを使用すると剣に力が宿り、通常攻撃でその力を消費して追加ダメージを与える。

- **Q — 折れた翼：** 連続して敵を斬りつける。断続的に3回まで再使用でき、3回目を命中させると周囲の敵をノックアップさせる。
- **W — 気功破：** 「気功破」を放ち、周囲にいる敵にダメージを与えてスタン効果を付与する。
- **E — 勇躍：** 前方へ短いステップを踏み、敵の攻撃を軽減するシールドを身にまとう。
- **R — 追放者の剣：** 神秘的な力によって砕けた剣を再生させ、攻撃力と射程を増加させる。さらに効果時間中、強力な遠隔攻撃である「ウィンドスラッシュ」を一度だけ発動できる。

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Riven` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Riven.png)
