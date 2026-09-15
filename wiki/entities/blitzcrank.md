---
title: "ブリッツクランク"
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
champion_id: "Blitzcrank"
champion_key: "53"
data_version: "16.18.1"
roles:
  - "Tank"
  - "Support"
resource_type: "マナ"
image_path: "raw/assets/champions/Blitzcrank.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Blitzcrank.png"
---

# ブリッツクランク

![[raw/assets/champions/Blitzcrank.png|128]]

## 基本情報

- **英字ID：** `Blitzcrank`
- **キー：** `53`
- **称号：** 偉大なるスチームゴーレム
- **データversion：** `16.18.1`

## 紹介

ブリッツクランクはゾウンからやってきた、ほぼ破壊不能な巨大ロボットだ。もともとは危険な廃棄物を処理するために造られたが、その目的には制約が多過ぎると感じた彼は「下層」で苦しんでいる人々を助けるために自らの体を改造した。ブリッツクランクは他者を守るため、危険も省みずにパワーと耐久力を活かした優しい鉄の拳を差し出したり、エネルギーを放出したりして悪者たちをこらしめている。

## 分類

- **役割タグ：** `Tank`、`Support`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 4 |
| `defense` | 8 |
| `magic` | 5 |
| `difficulty` | 4 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 600 |
| `hpperlevel` | 109 |
| `mp` | 267 |
| `mpperlevel` | 40 |
| `movespeed` | 325 |
| `armor` | 37 |
| `armorperlevel` | 4.7 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 125 |
| `hpregen` | 7.5 |
| `hpregenperlevel` | 0.75 |
| `mpregen` | 8.5 |
| `mpregenperlevel` | 0.8 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 62 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 1.13 |
| `attackspeed` | 0.625 |

## アビリティ

- **パッシブ — マナバリア：** 体力が低下すると、マナの量に応じたシールドを獲得する。

- **Q — ロケットグラブ：** 指定方向に右手を発射する。最初に触れた敵ユニットを掴んでダメージを与え、スタン効果を付与して自身のそばに引き寄せる。
- **W — オーバードライブ：** エネルギーをスーパーチャージして、移動速度と攻撃速度を大幅に上げる。効果終了後、エネルギーが切れて一時的にスロウ状態になる。
- **E — パワーフィスト：** 拳にエネルギーを充填して次の通常攻撃のダメージを2倍にし、対象をノックアップする。
- **R — イナズマフィールド：** 通常攻撃した敵にマークを付け、1秒後に電撃のダメージを与える。また、発動すると周囲の敵ユニットのシールドを消滅させ、ダメージを与えて短時間のサイレンス効果を与える。

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Blitzcrank` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Blitzcrank.png)
