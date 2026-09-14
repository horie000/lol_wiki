---
title: "ポッピー"
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
champion_id: "Poppy"
champion_key: "78"
data_version: "16.18.1"
roles:
  - "Tank"
  - "Fighter"
resource_type: "マナ"
image_path: "raw/assets/champions/Poppy.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Poppy.png"
---

# ポッピー

![[raw/assets/champions/Poppy.png|128]]

## 基本情報

- **英字ID：** `Poppy`
- **キー：** `78`
- **称号：** 大鎚の守護者
- **データversion：** `16.18.1`

## 紹介

ルーンテラの地に勇敢なチャンピオンは数多いものの、ポッピーほど粘り強い者はそうはいない。自分の身長の二倍ほどもある伝説のハンマー、オーロンを携えた不屈のヨードルは、もう何年もの間、彼女のハンマーの「真の持ち主」であるといわれている伝説の戦士「デマーシアの勇者」を密かに探し続けているのだ。真の持ち主が見つかるまで、彼女は使命感を持って戦闘に挑み、ハンマーを振り回して王国の敵を押し返している。

## 分類

- **役割タグ：** `Tank`、`Fighter`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 6 |
| `defense` | 7 |
| `magic` | 2 |
| `difficulty` | 6 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 610 |
| `hpperlevel` | 110 |
| `mp` | 300 |
| `mpperlevel` | 45 |
| `movespeed` | 345 |
| `armor` | 35 |
| `armorperlevel` | 5 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 125 |
| `hpregen` | 9 |
| `hpregenperlevel` | 0.8 |
| `mpregen` | 7 |
| `mpregenperlevel` | 0.7 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 56 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2.5 |
| `attackspeed` | 0.658 |

## アビリティ

- **パッシブ — 鋼鉄の大使：** 対象にバックラーを投げつける。対象に命中し跳ね返って落ちたバックラーを拾うことで、一時的にシールドを得る。

- **Q — ハンマーショック：** ハンマーを振り下ろしてダメージを与え、敵をスロウ状態にした後時間を置いて爆発する効果範囲を作り出す。
- **W — ステッドファスト：** 自動効果で物理防御と魔法防御が増加する。このボーナスは体力が低下するとさらに増加する。発動すると移動速度が増加し、自身の周囲にいる敵のダッシュ行動を阻止する。ダッシュを中断させられた敵はスロウ状態および釘付け状態になる。
- **E — ヒロイックチャージ：** 対象に向かってダッシュし、突き飛ばす。対象が壁にぶつかった場合、スタン状態になる。
- **R — 守護者の鉄鎚：** ハンマーに力を溜め、敵を遥か彼方に殴り飛ばす。

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Poppy` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Poppy.png)
