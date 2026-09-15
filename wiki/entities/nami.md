---
title: "ナミ"
type: entity
status: active
created: 2026-09-14
updated: 2026-09-14
sources:
  - "[[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]]"
  - "[[wiki/sources/src-2026-09-14-dragontail-16-18-1]]"
tags:
  - champion
  - role-support
  - role-mage
champion_id: "Nami"
champion_key: "267"
data_version: "16.18.1"
roles:
  - "Support"
  - "Mage"
resource_type: "マナ"
image_path: "raw/assets/champions/Nami.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Nami.png"
---

# ナミ

![[raw/assets/champions/Nami.png|128]]

## 基本情報

- **英字ID：** `Nami`
- **キー：** `267`
- **称号：** 潮呼びの巫女
- **データversion：** `16.18.1`

## 紹介

向こう見ずな性格の海の若きヴァスタヤであるナミは、ターゴン人たちとの間で太古から続いていた協約が破られた時、マライの民として初めて海を離れて陸地に上がることになった。それ以外に方法がなかったことから、彼女は部族の安全を守るための聖なる儀式を自らの手で完遂することを決めた。この新たな混沌の時代の中で、ナミは潮呼びの巫女の杖を使って海の力を召喚しながら、不安だらけの未来に固い決意で挑んでいる。

## 分類

- **役割タグ：** `Support`、`Mage`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 4 |
| `defense` | 3 |
| `magic` | 7 |
| `difficulty` | 5 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 560 |
| `hpperlevel` | 88 |
| `mp` | 365 |
| `mpperlevel` | 43 |
| `movespeed` | 335 |
| `armor` | 29 |
| `armorperlevel` | 5.2 |
| `spellblock` | 30 |
| `spellblockperlevel` | 1.3 |
| `attackrange` | 550 |
| `hpregen` | 5.5 |
| `hpregenperlevel` | 0.55 |
| `mpregen` | 11.5 |
| `mpregenperlevel` | 0.4 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 54 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2.61 |
| `attackspeed` | 0.644 |

## アビリティ

- **パッシブ — さざなみの後押し：** スキルが味方チャンピオンに命中するたびに、命中した相手の移動速度が短時間増加する。

- **Q — 水の牢獄：** 指定地点に水泡を飛ばし、着弾時に範囲内の敵ユニットにダメージを与えてスタン効果を付与する。
- **W — 潮の流れ：** 味方と敵チャンピオンの間を交互に跳ね返る水流を放つ。命中した味方は体力が回復し、敵はダメージを受ける。
- **E — 潮使いの祝福：** 短時間、味方チャンピオンに力を与える。強化された味方は次の数回の通常攻撃とスキルで、対象に追加魔法ダメージとスロウ効果を付与する。
- **R — 海神の舞：** ナミが海の力を借りて「海神の舞」を呼び寄せる。波に触れた敵ユニットはダメージを受け、ノックアップされてスロウ状態になる。命中した味方は「さざなみの後押し」の2倍の効果を得る。

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Nami` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Nami.png)
