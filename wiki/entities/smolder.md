---
title: "スモルダー"
type: entity
status: active
created: 2026-09-14
updated: 2026-09-14
sources:
  - "[[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]]"
  - "[[wiki/sources/src-2026-09-14-dragontail-16-18-1]]"
tags:
  - champion
  - role-marksman
  - role-mage
champion_id: "Smolder"
champion_key: "901"
data_version: "16.18.1"
roles:
  - "Marksman"
  - "Mage"
resource_type: "マナ"
image_path: "raw/assets/champions/Smolder.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Smolder.png"
---

# スモルダー

![[raw/assets/champions/Smolder.png|128]]

## 基本情報

- **英字ID：** `Smolder`
- **キー：** `901`
- **称号：** 炎の幼龍
- **データversion：** `16.18.1`

## 紹介

ノクサスの辺境にある岩だらけの崖に身を隠し、幼きドラゴンは母親に見守られながら、カマヴォールのインペリアルドラゴンの継承者とは何たるかを学んでいる。遊び好きで意欲旺盛なスモルダーは急成長を遂げており、能力を磨けるならどんな機会も逃さない。まだ幼くともスモルダーの力は決して侮れず、火のつくものなら何でも簡単に燃やしてしまう。

## 分類

- **役割タグ：** `Marksman`、`Mage`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 8 |
| `defense` | 2 |
| `magic` | 5 |
| `difficulty` | 6 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 575 |
| `hpperlevel` | 100 |
| `mp` | 300 |
| `mpperlevel` | 40 |
| `movespeed` | 330 |
| `armor` | 24 |
| `armorperlevel` | 4 |
| `spellblock` | 33 |
| `spellblockperlevel` | 1.1 |
| `attackrange` | 550 |
| `hpregen` | 3.75 |
| `hpregenperlevel` | 0.6 |
| `mpregen` | 8.5 |
| `mpregenperlevel` | 0.7 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 58 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 4 |
| `attackspeed` | 0.638 |

## アビリティ

- **パッシブ — 駆けだしドラゴン：** スキルをチャンピオンに命中させる、または「スーパーこげこげブレス」で敵をキルすると、「駆けだしドラゴン」のスタックを1つ獲得する。スタック数に応じて通常スキルのダメージが増加する。

- **Q — スーパーこげこげブレス：** 敵1体に炎のブレスを吐きかける。スタックを獲得するほど、このスキルが強化されていく。
- **W — くしゅん！：** 可愛らしいくしゃみと共に炎を吐く。この炎は敵チャンピオンに命中すると爆発する。
- **E — パタパタパタ：** 飛翔して地形を無視するようになり、最も体力が低い敵を空から攻撃する。
- **R — ママーッ！！：** 母ドラゴンを呼び寄せて、上空から炎を吐いてもらう。炎の中心部にいる敵には、追加ダメージとスロウ効果を与える。

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Smolder` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Smolder.png)
