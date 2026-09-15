---
title: "フィドルスティックス"
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
champion_id: "Fiddlesticks"
champion_key: "9"
data_version: "16.18.1"
roles:
  - "Mage"
  - "Support"
resource_type: "マナ"
image_path: "raw/assets/champions/Fiddlesticks.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Fiddlesticks.png"
---

# フィドルスティックス

![[raw/assets/champions/Fiddlesticks.png|128]]

## 基本情報

- **英字ID：** `Fiddlesticks`
- **キー：** `9`
- **称号：** 古の恐怖
- **データversion：** `16.18.1`

## 紹介

ルーンテラの中で何かが目覚めた──古代の恐ろしい何かが。フィドルスティックスとして知られる永遠の恐怖は文明の僻地をうろつき、疑心暗鬼にさいなまれた地域に引き寄せられると、恐怖に怯える犠牲者たちを貪る。ギザギザの刃を持つ鎌をその手に、か細いガラクタを寄せ集めてできたクリーチャーは恐怖そのものを刈り取る。そして、生き延びることの方が不運だと思わせるほどに、精神を粉々に砕く。カラスの鳴き声や、人間のような姿をした何かの囁きが聞こえたら注意しなければいけない…フィドルスティックスが戻ってきたのだから。

## 分類

- **役割タグ：** `Mage`、`Support`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 2 |
| `defense` | 3 |
| `magic` | 9 |
| `difficulty` | 9 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 650 |
| `hpperlevel` | 106 |
| `mp` | 500 |
| `mpperlevel` | 28 |
| `movespeed` | 335 |
| `armor` | 34 |
| `armorperlevel` | 4.7 |
| `spellblock` | 30 |
| `spellblockperlevel` | 1.3 |
| `attackrange` | 480 |
| `hpregen` | 5.5 |
| `hpregenperlevel` | 0.6 |
| `mpregen` | 8 |
| `mpregenperlevel` | 0.8 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 55 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2.11 |
| `attackspeed` | 0.625 |

## アビリティ

- **パッシブ — 無害なカカシ：** トリンケットが「身代わり人形」に置き換わる。

- **Q — テラー：** 敵に見られていない状態からスキルで敵にダメージを与えるか、「テラー」の発動効果の対象に敵を指定すると、対象にフィアー効果を与えて一定時間逃走させる。
- **W — 豊かな収穫：** 周囲の敵から体力を奪い、効果時間終了時に対象の減少体力に応じた追加ダメージを与える。
- **E — 刈り取り：** 一定範囲を鎌で斬りつけて、命中したすべての敵にスロウ効果を与える。また、範囲の中心にいた敵にはサイレンス効果を与える。
- **R — クロウストーム：** 自身の周囲に凶暴なカラスの群れを集め、効果範囲内の敵ユニット全員に毎秒ダメージを与える。

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Fiddlesticks` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Fiddlesticks.png)
