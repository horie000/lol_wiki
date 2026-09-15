---
title: "エリス"
type: entity
status: active
created: 2026-09-14
updated: 2026-09-14
sources:
  - "[[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]]"
  - "[[wiki/sources/src-2026-09-14-dragontail-16-18-1]]"
tags:
  - champion
  - role-assassin
  - role-mage
champion_id: "Elise"
champion_key: "60"
data_version: "16.18.1"
roles:
  - "Assassin"
  - "Mage"
resource_type: "マナ"
image_path: "raw/assets/champions/Elise.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Elise.png"
---

# エリス

![[raw/assets/champions/Elise.png|128]]

## 基本情報

- **英字ID：** `Elise`
- **キー：** `60`
- **称号：** 蜘蛛の女帝
- **データversion：** `16.18.1`

## 紹介

冷酷無比な捕食者エリスは、ノクサスの古都の地下にある、光も差さない閉ざされた邸宅に棲む。かつては定命の者だった彼女は有力な一族の家長だったが、おぞましい半神に噛まれ、美しくも人間ではない何か──獲物を騙して巣におびき寄せる、蜘蛛のような生き物へと成り代わった。永遠の若さを保つため、エリスは世間知らずで信仰を持たない者を好んで餌食にする。その魅力に抗える者は少ない。

## 分類

- **役割タグ：** `Assassin`、`Mage`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 6 |
| `defense` | 5 |
| `magic` | 7 |
| `difficulty` | 9 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 620 |
| `hpperlevel` | 109 |
| `mp` | 324 |
| `mpperlevel` | 50 |
| `movespeed` | 330 |
| `armor` | 30 |
| `armorperlevel` | 4.5 |
| `spellblock` | 30 |
| `spellblockperlevel` | 1.3 |
| `attackrange` | 550 |
| `hpregen` | 5.5 |
| `hpregenperlevel` | 0.6 |
| `mpregen` | 6 |
| `mpregenperlevel` | 0.8 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 55 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 1.75 |
| `attackspeed` | 0.625 |

## アビリティ

- **パッシブ — 蜘蛛の女帝：** ヒト形態: スキルが敵に命中するたびに、幼体が1体誕生する。 蜘蛛形態: 通常攻撃に追加魔法ダメージが付与され、攻撃のたびに体力が回復する。

- **Q — 神経毒/毒牙：** ヒト形態: 対象の敵ユニットにダメージを与える。対象の現在体力が多いほど与えるダメージが増加する。 蜘蛛形態: 対象の敵ユニットに飛びかかって噛み付く。対象の現在体力が少ないほど与えるダメージが増加する。
- **W — 子蜘蛛爆弾/猛食：** ヒト形態: 毒液が詰まった幼体を放つ。幼体は敵ユニットに近づくと爆発する。 蜘蛛形態: エリスと幼体の攻撃速度が増加する。
- **E — 繭化/蜘蛛の糸：** ヒト形態: 繭を放って最初に命中した敵にスタン効果を付与し、ステルス状態の敵を除いて可視状態にする。 蜘蛛形態: 幼体とともに空中に跳びあがり、指定した敵のもとへ降下し、「蜘蛛の女帝」から得られる追加ダメージと回復量が増加する。
- **R — 蜘蛛形態：** 恐ろしい蜘蛛の姿になる。射程距離は短くなるが、移動速度が増加して新しいスキルを使用できるようになり、エリスと共に敵を攻撃する幼体の群れを呼び出す。

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Elise` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Elise.png)
