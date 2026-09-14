---
title: "エイトロックス"
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
champion_id: "Aatrox"
champion_key: "266"
data_version: "16.18.1"
roles:
  - "Fighter"
resource_type: "ブラッドウェル"
image_path: "raw/assets/champions/Aatrox.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Aatrox.png"
---

# エイトロックス

![[raw/assets/champions/Aatrox.png|128]]

## 基本情報

- **英字ID：** `Aatrox`
- **キー：** `266`
- **称号：** ダーキンの暴剣
- **データversion：** `16.18.1`

## 紹介

ヴォイドからシュリーマを守り抜いた誇り高き存在であったエイトロックスとその同胞は、いつしかルーンテラにとってヴォイドを上回る脅威となり、狡猾な定命の者の魔法の前に敗れ去った。数世紀にも及ぶ幽閉を経て、エイトロックスは彼の精髄を封じていた魔の武器を手にした愚か者の肉体を奪い、再び自由の身となることに成功した。奪った肉体をかつての姿へと変え、ルーンテラを闊歩する彼は、長らく望んできた復讐──世界を終焉させる機会をうかがっている。

## 分類

- **役割タグ：** `Fighter`
- **リソース種別：** ブラッドウェル

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 8 |
| `defense` | 4 |
| `magic` | 3 |
| `difficulty` | 4 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 650 |
| `hpperlevel` | 114 |
| `mp` | 0 |
| `mpperlevel` | 0 |
| `movespeed` | 345 |
| `armor` | 38 |
| `armorperlevel` | 4.8 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 175 |
| `hpregen` | 3 |
| `hpregenperlevel` | 0.5 |
| `mpregen` | 0 |
| `mpregenperlevel` | 0 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 60 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2.5 |
| `attackspeed` | 0.651 |

## アビリティ

- **パッシブ — 死兆の構え：** 一定時間ごとに、次の通常攻撃が対象の最大体力に応じた追加魔法ダメージを与え、同量の体力を回復する。

- **Q — ダーキンブレード：** 大剣を叩きつけて物理ダメージを与える。剣を3回振ることが可能で、振るごとに効果範囲が変化する。
- **W — 炎獄の鎖：** 地面を叩きつけて、最初に命中した敵にダメージを与える。チャンピオンと大型モンスターは数秒以内に攻撃範囲から出なければ、中央に引き寄せられて再度ダメージを受ける。
- **E — 影進撃：** 自動効果として、敵チャンピオンにダメージを与えると体力が回復する。発動すると、指定方向に向かってダッシュする。
- **R — ワールドエンダー：** 悪魔形態を解放して周囲の敵ミニオンにフィアー効果を与え、攻撃力、回復量、移動速度が増加する。キルまたはアシストを獲得した場合、この効果が延長される。

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Aatrox` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Aatrox.png)
