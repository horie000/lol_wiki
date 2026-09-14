---
title: "シェン"
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
champion_id: "Shen"
champion_key: "98"
data_version: "16.18.1"
roles:
  - "Tank"
resource_type: "気"
image_path: "raw/assets/champions/Shen.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Shen.png"
---

# シェン

![[raw/assets/champions/Shen.png|128]]

## 基本情報

- **英字ID：** `Shen`
- **キー：** `98`
- **称号：** 黄昏の瞳
- **データversion：** `16.18.1`

## 紹介

シェンは「均衡の守人」として知られるアイオニアの秘密の戦士たちの長「黄昏の瞳」であり、全ての感情、偏見、自尊心などの迷いから逃れるため、霊的領域と物質世界の間に存在する見えざる道を、感情に左右されることなく歩み続けている。彼は二つの世界の均衡を保つという任務を託されており、それを脅かそうとする者には鋼の刀と魔術の力で挑む。

## 分類

- **役割タグ：** `Tank`
- **リソース種別：** 気

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 3 |
| `defense` | 9 |
| `magic` | 3 |
| `difficulty` | 4 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 610 |
| `hpperlevel` | 99 |
| `mp` | 400 |
| `mpperlevel` | 0 |
| `movespeed` | 340 |
| `armor` | 34 |
| `armorperlevel` | 4.2 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 125 |
| `hpregen` | 8.5 |
| `hpregenperlevel` | 0.75 |
| `mpregen` | 50 |
| `mpregenperlevel` | 0 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 64 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 3 |
| `attackspeed` | 0.751 |

## アビリティ

- **パッシブ — 内気功：** スキルを使用すると、自身にシールドを展開する。また味方、もしくは敵チャンピオンに対してスキルを使用すると、この効果のクールダウンが短縮される。

- **Q — 護刃招来：** 「スピリットブレード」を自身のもとへ呼び寄せ、通常攻撃に対象の最大体力に応じた追加ダメージを付与する。移動中の「スピリットブレード」が敵チャンピオンを斬りつけると追加ダメージが強化され、斬りつけられた敵はシェンから逃げる際にスロウ状態になる。
- **W — 防人の帳：** 「スピリットブレード」を中心に、敵チャンピオンの通常攻撃をブロックするフィールドを展開する。
- **E — 殺気駆け：** 指定方向にダッシュし、触れた敵チャンピオンにタウント効果を与える。
- **R — 瞬身護法：** 指定した味方チャンピオンにシールドを展開し、印を結んだあと「スピリットブレード」と共にそのチャンピオンのもとへワープする。

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Shen` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Shen.png)
