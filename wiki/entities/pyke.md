---
title: "パイク"
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
  - role-assassin
champion_id: "Pyke"
champion_key: "555"
data_version: "16.18.1"
roles:
  - "Support"
  - "Assassin"
resource_type: "マナ"
image_path: "raw/assets/champions/Pyke.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Pyke.png"
---

# パイク

![[raw/assets/champions/Pyke.png|128]]

## 基本情報

- **英字ID：** `Pyke`
- **キー：** `555`
- **称号：** ブラッドハーバーの殺戮鬼
- **データversion：** `16.18.1`

## 紹介

ビルジウォーターのスロータードックでは名の知れたモリ撃ちだったパイクは、巨大なジョールフィッシュの胃の中で死を迎えるはずであったが、その息を吹き返した。彼は故郷の町の湿っぽい路地や裏通りを音もなく歩き、他者から搾取することで財を成す人々を追い詰めては、新たに身に着けた超自然的な能力で、彼らに速やかにして非情な死を与える。怪物を狩ることを誇りとしていた都市が、今では怪物に狩られているのだ。

## 分類

- **役割タグ：** `Support`、`Assassin`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 9 |
| `defense` | 3 |
| `magic` | 1 |
| `difficulty` | 7 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 670 |
| `hpperlevel` | 110 |
| `mp` | 415 |
| `mpperlevel` | 50 |
| `movespeed` | 330 |
| `armor` | 37 |
| `armorperlevel` | 4.7 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 150 |
| `hpregen` | 7 |
| `hpregenperlevel` | 0.5 |
| `mpregen` | 8 |
| `mpregenperlevel` | 1 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 62 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2.5 |
| `attackspeed` | 0.667 |

## アビリティ

- **パッシブ — 沈みし者の力：** 敵の視界外にいると、直前にチャンピオンからの攻撃で失った体力を回復する。また、パイクはいずれのソースからも増加最大体力を得ることはできず、代わりに増加攻撃力を得る。

- **Q — ボーンスキューア：** 前方にいる1体の敵を突き刺すか、1体の敵を引き寄せる。
- **W — ゴーストウォーター：** カモフラージュ状態になり、移動速度が大きく増加する。移動速度は徐々に元に戻る。
- **E — 亡者の引き波：** 亡霊を残してダッシュする。亡霊はパイクのところまで戻ってきて触れた敵チャンピオンをスタンさせる。
- **R — 水底の急襲：** ブリンクして体力の低下した敵にとどめを刺す。とどめを刺すと再度使用可能になり、アシストした味方1人に追加ゴールドを付与する。

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Pyke` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Pyke.png)
