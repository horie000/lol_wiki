---
title: "カーサス"
type: entity
status: active
created: 2026-09-14
updated: 2026-09-14
sources:
  - "[[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]]"
  - "[[wiki/sources/src-2026-09-14-dragontail-16-18-1]]"
tags:
  - champion
  - role-mage
champion_id: "Karthus"
champion_key: "30"
data_version: "16.18.1"
roles:
  - "Mage"
resource_type: "マナ"
image_path: "raw/assets/champions/Karthus.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Karthus.png"
---

# カーサス

![[raw/assets/champions/Karthus.png|128]]

## 基本情報

- **英字ID：** `Karthus`
- **キー：** `30`
- **称号：** 死を歌う者
- **データversion：** `16.18.1`

## 紹介

忘却の使徒、不死の亡霊カーサスは、呪いの歌を口にしながらその不吉な姿を露わにする。命ある者は不死がもたらす永遠を恐れるが、カーサスの目に映るのはそこに内包された美しさと純粋さ、すわなち生と死の完全なる統合のみだ。シャドウアイルから現れ出でるカーサスは、不死の使徒として生ける者に死という愉悦を与える。

## 分類

- **役割タグ：** `Mage`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 2 |
| `defense` | 2 |
| `magic` | 10 |
| `difficulty` | 7 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 620 |
| `hpperlevel` | 110 |
| `mp` | 467 |
| `mpperlevel` | 31 |
| `movespeed` | 335 |
| `armor` | 21 |
| `armorperlevel` | 4.7 |
| `spellblock` | 30 |
| `spellblockperlevel` | 1.3 |
| `attackrange` | 450 |
| `hpregen` | 6.5 |
| `hpregenperlevel` | 0.55 |
| `mpregen` | 8 |
| `mpregenperlevel` | 0.8 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 46 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2.11 |
| `attackspeed` | 0.625 |

## アビリティ

- **パッシブ — 怨嗟の叫び：** カーサスは死亡すると同時に霊体化し、その場でスキルを発動できるようになる。

- **Q — 根絶やし：** 指定地点を時間差で爆発させ、周囲の敵にダメージを与える。命中した敵が1体の場合は与えるダメージが増加する。
- **W — 嘆きの壁：** エネルギーを搾取する霊的な壁を出現させ、そこを通り抜けた敵の移動速度と魔法防御を一定時間低下させる。
- **E — 冒涜：** 自動効果として、カーサスが倒した敵から生気を奪いマナを回復する。 発動すると自身の周囲に倒した獲物の魂を召喚し、範囲内の敵にダメージを与えるがマナを著しく消耗する。
- **R — 鎮魂歌：** 3秒間の詠唱後、すべての敵チャンピオンにダメージを与える。

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Karthus` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Karthus.png)
