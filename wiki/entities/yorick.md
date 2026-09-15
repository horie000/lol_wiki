---
title: "ヨリック"
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
champion_id: "Yorick"
champion_key: "83"
data_version: "16.18.1"
roles:
  - "Fighter"
  - "Tank"
resource_type: "マナ"
image_path: "raw/assets/champions/Yorick.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Yorick.png"
---

# ヨリック

![[raw/assets/champions/Yorick.png|128]]

## 基本情報

- **英字ID：** `Yorick`
- **キー：** `83`
- **称号：** 魂の導き手
- **データversion：** `16.18.1`

## 紹介

ヨリックは忘れ去られて久しいある教団の修道士として唯一生き残った。彼は死者を操ることができるが、その力は恵みであり、また呪いでもある。シャドウアイルに囚われた彼の仲間と呼べるのは、朽ちた屍と、甲高い叫び声を上げながら集まってくる亡霊のみだ。ヨリックの恐ろしい行いは、「破滅」の呪いから故郷を解放したいという彼の崇高な決意と相反するようにも見える。

## 分類

- **役割タグ：** `Fighter`、`Tank`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 6 |
| `defense` | 6 |
| `magic` | 4 |
| `difficulty` | 6 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 650 |
| `hpperlevel` | 114 |
| `mp` | 300 |
| `mpperlevel` | 60 |
| `movespeed` | 340 |
| `armor` | 36 |
| `armorperlevel` | 4.5 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 175 |
| `hpregen` | 8 |
| `hpregenperlevel` | 0.8 |
| `mpregen` | 7.5 |
| `mpregenperlevel` | 0.75 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 62 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2 |
| `attackspeed` | 0.625 |

## アビリティ

- **パッシブ — 魂の導き手：** 呪われし一群: 周囲の敵に襲いかかり攻撃する「ミストウォーカー」を召喚する。

- **Q — 葬送：** 次に行う通常攻撃が追加ダメージを与えて自身を回復する。対象がチャンピオンか大型モンスターだった場合、または対象が倒された場合は墓が掘られる。
- **W — 屍の列：** 指定した地点に破壊可能な壁を召喚し、敵ユニットの動きを阻止する。
- **E — 悲嘆の霧：** 「黒き霧」の塊を投げつけて物理防御を低下させ、ダメージとスロウ効果を与え、対象をマークする。召喚したユニットはマークされた対象に向かう際は移動速度が増加する。
- **R — 嘆きの墓標：** ヨリックが「霧の乙女」を召喚する。「霧の乙女」が攻撃している対象を自身が攻撃すると追加ダメージを与える。「霧の乙女」は倒された敵から自動的に「ミストウォーカー」を召喚する。

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Yorick` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Yorick.png)
