---
title: "メル"
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
  - role-support
champion_id: "Mel"
champion_key: "800"
data_version: "16.18.1"
roles:
  - "Mage"
  - "Support"
resource_type: "マナ"
image_path: "raw/assets/champions/Mel.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Mel.png"
---

# メル

![[raw/assets/champions/Mel.png|128]]

## 基本情報

- **英字ID：** `Mel`
- **キー：** `800`
- **称号：** 魂の反照
- **データversion：** `16.18.1`

## 紹介

メル・メダルダは、かつてはノクサスで最大の権勢を誇ったメダルダ家の後継者と目される人物。表向きは優雅な貴族のように見えるが、その実体は、出会う相手のすべてについて知り尽くそうとする、卓越した政治家。謎に満ちた黒薔薇団との邂逅を経て、母の欺瞞の深さを知ることとなったメルは、自分自身の手に余る可能性がある状況に直面する。新たに目覚めた魔法の力を携え、答えを求めて故郷へと出帆したメル。その内なる光を押さえ込もうとする者が後を絶たない中でも、彼女の魂は決して屈することはない。

## 分類

- **役割タグ：** `Mage`、`Support`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 2 |
| `defense` | 4 |
| `magic` | 9 |
| `difficulty` | 5 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 630 |
| `hpperlevel` | 99 |
| `mp` | 480 |
| `mpperlevel` | 28 |
| `movespeed` | 330 |
| `armor` | 21 |
| `armorperlevel` | 5.2 |
| `spellblock` | 30 |
| `spellblockperlevel` | 1.3 |
| `attackrange` | 550 |
| `hpregen` | 6 |
| `hpregenperlevel` | 0.55 |
| `mpregen` | 9 |
| `mpregenperlevel` | 0.9 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 54 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2.5 |
| `attackspeed` | 0.625 |

## アビリティ

- **パッシブ — 灼熱の輝き：** スキルを使用するたび、次の通常攻撃で追加の飛翔物を3発発射する(最大9発までスタック可能)。 スキルまたは通常攻撃でダメージを与えると、敵に「圧倒」のスタックを付与する。これは無限にスタックする。敵に蓄積した「圧倒」スタックが一定のダメージ量に達すると、スタックを消費して敵にとどめを刺す。

- **Q — 輝きの連撃：** 指定地点に向かって複数の飛翔物を連続で発射する。飛翔物は爆発して範囲内の敵に繰り返しダメージを与える。
- **W — 反駁：** 自身の周囲にバリアを形成する。このバリアは敵の発射物をその敵に向けて反射し、自身が受けるダメージを防ぎ、自身の移動速度を増加させる。
- **E — 陽光の枷：** 前方に輝くオーブを発射し、中心にいた敵にはスネア効果を与え、周囲にいた敵にはスロウ効果と継続ダメージを与える。
- **R — 黄金蝕：** 距離に関係なく、「圧倒」を付与しているすべての敵を攻撃し、「圧倒」のスタック数に応じて追加ダメージを与える。 「黄金蝕」のスキルレベルが上がると、「圧倒」のダメージが増加する。

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Mel` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Mel.png)
