---
title: "アニビア"
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
champion_id: "Anivia"
champion_key: "34"
data_version: "16.18.1"
roles:
  - "Mage"
resource_type: "マナ"
image_path: "raw/assets/champions/Anivia.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Anivia.png"
---

# アニビア

![[raw/assets/champions/Anivia.png|128]]

## 基本情報

- **英字ID：** `Anivia`
- **キー：** `34`
- **称号：** 氷の不死鳥
- **データversion：** `16.18.1`

## 紹介

アニビアは翼を持った慈悲の守護者であり、無限に繰り返される生と死、そして再誕の繰り返しに耐えてフレヨルドを守っている。凍てつくような氷と激しい風の中から生まれた半神は、その元素の力を操って侵略者から自分の故郷を守り、過酷な環境の北部に住む部族たちを守り導いている。彼らにとってアニビアは希望の象徴であり、大いなる変化の前触れとして崇拝されている。彼女は自らの命が尽きるまで戦う。自身を犠牲にすることで彼女の記憶は留まり、新たな明日に向かって生まれ変われることを知っているからだ。

## 分類

- **役割タグ：** `Mage`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 1 |
| `defense` | 4 |
| `magic` | 10 |
| `difficulty` | 10 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 550 |
| `hpperlevel` | 92 |
| `mp` | 495 |
| `mpperlevel` | 45 |
| `movespeed` | 325 |
| `armor` | 19 |
| `armorperlevel` | 4.1 |
| `spellblock` | 30 |
| `spellblockperlevel` | 1.3 |
| `attackrange` | 600 |
| `hpregen` | 5.5 |
| `hpregenperlevel` | 0.55 |
| `mpregen` | 8 |
| `mpregenperlevel` | 0.8 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 51 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 1.68 |
| `attackspeed` | 0.658 |

## アビリティ

- **パッシブ — 再誕：** アニビアは力尽きると、体力が最大の状態で卵に戻る。

- **Q — フラッシュフロスト：** 指定方向に両翼で力強く羽ばたいて、氷の塊を放つ。氷は触れた敵に魔法ダメージと「チルド」を与える。最大距離に達するかこのスキルを再使用すると氷の塊が炸裂して、範囲内の敵にダメージとスタンを与える。
- **W — アイスウォール：** 空気中の水分を凝縮して氷の壁をつくり、相手の移動を妨害する。壁は数秒後に溶けて消滅する。
- **E — フロストバイト：** 翼をはためかせて対象を凍てつく氷柱で攻撃し、ダメージを与える。直前に「フラッシュフロスト」が当たったか、最大範囲の「ブリザード」でダメージを受けた対象には、2倍のダメージを与える。
- **R — ブリザード：** 指定範囲に激しい吹雪を召喚する。吹雪は範囲内の敵に継続ダメージを与え「チルド」を付与する。

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Anivia` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Anivia.png)
