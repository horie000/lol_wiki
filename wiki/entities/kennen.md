---
title: "ケネン"
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
champion_id: "Kennen"
champion_key: "85"
data_version: "16.18.1"
roles:
  - "Mage"
resource_type: "気"
image_path: "raw/assets/champions/Kennen.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Kennen.png"
---

# ケネン

![[raw/assets/champions/Kennen.png|128]]

## 基本情報

- **英字ID：** `Kennen`
- **キー：** `85`
- **称号：** 雷雲の担い手
- **データversion：** `16.18.1`

## 紹介

ケネンは電光石化の素早さでアイオニアの均衡を保つだけでなく、「均衡の守人」の中で唯一のヨードルでもある。小さな毛皮で覆われた姿とは裏腹に、彼は手裏剣の竜巻と底知れぬ熱意を持ってあらゆる脅威に立ち向かっていく。破壊的な電気エネルギーを浴びせて現れた敵を倒しながら、彼は師匠のシェンとともに霊的領域を巡回している。

## 分類

- **役割タグ：** `Mage`
- **リソース種別：** 気

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 6 |
| `defense` | 4 |
| `magic` | 7 |
| `difficulty` | 4 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 580 |
| `hpperlevel` | 98 |
| `mp` | 200 |
| `mpperlevel` | 0 |
| `movespeed` | 335 |
| `armor` | 29 |
| `armorperlevel` | 4.95 |
| `spellblock` | 30 |
| `spellblockperlevel` | 1.3 |
| `attackrange` | 550 |
| `hpregen` | 5.5 |
| `hpregenperlevel` | 0.65 |
| `mpregen` | 50 |
| `mpregenperlevel` | 0 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 48 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 3.4 |
| `attackspeed` | 0.625 |

## アビリティ

- **パッシブ — 嵐の刻印：** スキルを3回命中させた敵をスタンさせる。

- **Q — 雷遁手裏剣：** ケネンが狙った場所に手裏剣を連投し、命中した敵ユニットにダメージと「嵐の刻印」を与える。
- **W — 稲妻の奔流：** 自動効果: ケネンの数回ごとの攻撃が、対象に追加ダメージと「嵐の刻印」を与えるようになる。 発動効果: 周囲の刻印を受けている対象にダメージを与え、 新たに「嵐の刻印」を付与する。
- **E — 疾風迅雷：** 稲妻と化したケネンがユニットをすり抜け、接触したユニットに「嵐の刻印」を与える。この形態になるときに移動速度が増加し、この形態から抜けるときには攻撃速度が増加する。
- **R — 雷撃の大嵐：** ケネンが雷雲を召喚し、周囲にいる敵チャンピオンに魔法ダメージを与える。

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Kennen` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Kennen.png)
