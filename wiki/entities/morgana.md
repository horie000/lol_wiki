---
title: "モルガナ"
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
champion_id: "Morgana"
champion_key: "25"
data_version: "16.18.1"
roles:
  - "Support"
  - "Mage"
resource_type: "マナ"
image_path: "raw/assets/champions/Morgana.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Morgana.png"
---

# モルガナ

![[raw/assets/champions/Morgana.png|128]]

## 基本情報

- **英字ID：** `Morgana`
- **キー：** `25`
- **称号：** 堕天の高潔
- **データversion：** `16.18.1`

## 紹介

天界の存在であると同時に定命でもあるという二つの性質の間で葛藤を抱えるモルガナは、人間性をつなぎとめるために自身の翼を縛り付け、己の苦痛と悔恨を味わわせるために、偽善者や腐敗した者たちに挑みかかる。法律や伝統であっても、自分が不当だと思えば断固として拒絶する。彼女はデマーシアの影に身を潜め──たとえ他の者たちが圧制を試みようと──闇の炎で自らを守り、あるいはそれを鎖として用い、真実のために戦う。そんなモルガナは流刑者や追放の身にある者たちであっても、いつの日か立ち上がることができるのだと信じてやまない。

## 分類

- **役割タグ：** `Support`、`Mage`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 1 |
| `defense` | 6 |
| `magic` | 8 |
| `difficulty` | 1 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 630 |
| `hpperlevel` | 104 |
| `mp` | 340 |
| `mpperlevel` | 60 |
| `movespeed` | 335 |
| `armor` | 25 |
| `armorperlevel` | 4.2 |
| `spellblock` | 30 |
| `spellblockperlevel` | 1.3 |
| `attackrange` | 450 |
| `hpregen` | 5.5 |
| `hpregenperlevel` | 0.4 |
| `mpregen` | 11 |
| `mpregenperlevel` | 0.4 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 56 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 1.53 |
| `attackspeed` | 0.625 |

## アビリティ

- **パッシブ — ソウルサイフォン：** 敵チャンピオン、大型ミニオン、中型および大型ジャングルモンスターにダメージを与えると自身の体力を回復する。

- **Q — ダークバインド：** 闇の魔力で敵にスネア効果と魔法ダメージを与え、冒した罪の深さを思い知らせる。
- **W — 苦悶の影：** 周囲に呪いの闇を発生させ、範囲内にいる敵に継続的な魔法ダメージを与える。このダメージは対象の体力が低いほど増加する。
- **E — ブラックシールド：** 仲間のチャンピオンに星炎の加護によるバリアを付与する。このバリアは魔法ダメージと行動妨害を無効化する。
- **R — 魂の足枷：** 天界の力を解放し、翼を広げて空中に浮かぶ。周囲の敵チャンピオンを黒き痛みの鎖で縛り、そのチャンピオンへ向かう際の移動速度が上昇する。命中時にダメージとスロウ効果を与え、一定時間内に鎖から逃れることができなかった敵には追加でスタン効果を与える。

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Morgana` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Morgana.png)
