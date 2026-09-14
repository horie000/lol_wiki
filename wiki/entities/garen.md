---
title: "ガレン"
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
  - role-tank
champion_id: "Garen"
champion_key: "86"
data_version: "16.18.1"
roles:
  - "Fighter"
  - "Tank"
resource_type: "なし"
image_path: "raw/assets/champions/Garen.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Garen.png"
---

# ガレン

![[raw/assets/champions/Garen.png|128]]

## 基本情報

- **英字ID：** `Garen`
- **キー：** `86`
- **称号：** デマーシアの勇士
- **データversion：** `16.18.1`

## 紹介

仲間からは好かれ、敵からも尊敬を集めているガレンは誇り高きドーントレス前衛隊の戦士だ。彼は名門クラウンガード家の後継ぎとして、デマーシアの国家とその理念を守る任務を与えられている。魔力を防ぐ鎧を身に付けて、強力なブロードソードを振りかざし、ガレンは魔術師たちが待つ戦場に、鋼鉄の勇気の竜巻となって飛び込んでいく。

## 分類

- **役割タグ：** `Fighter`、`Tank`
- **リソース種別：** なし

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 7 |
| `defense` | 7 |
| `magic` | 1 |
| `difficulty` | 5 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 690 |
| `hpperlevel` | 98 |
| `mp` | 0 |
| `mpperlevel` | 0 |
| `movespeed` | 340 |
| `armor` | 38 |
| `armorperlevel` | 4.2 |
| `spellblock` | 32 |
| `spellblockperlevel` | 1.55 |
| `attackrange` | 175 |
| `hpregen` | 8 |
| `hpregenperlevel` | 0.5 |
| `mpregen` | 0 |
| `mpregenperlevel` | 0 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 69 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 3.65 |
| `attackspeed` | 0.625 |

## アビリティ

- **パッシブ — タフガイ：** 一定時間ダメージや敵のスキルを受けていなければ、毎秒最大体力の一定割合を回復する。

- **Q — 断固たる一撃：** 自身にかけられたスロウ効果を解除し、移動速度が増加する。次の攻撃で敵の急所を斬りつけて追加ダメージを与え、サイレンス効果を付与する。
- **W — 勇気の護り：** 自動効果: 敵ユニットを倒すたびに物理防御と魔法防御が増加する。 発動効果: 瞬間的にシールドと行動妨害耐性を獲得し、その後は軽減率が低下するものの、ダメージ軽減効果が長い時間持続する。
- **E — ジャッジメント：** 高速で回転しながら剣を振り回し、周囲の敵に物理ダメージを与える。
- **R — デマーシアの正義：** デマーシア魂を燃え上がらせ、指定した敵チャンピオンに必殺の一撃を繰り出す。

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Garen` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Garen.png)
