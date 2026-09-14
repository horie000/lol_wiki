---
title: "ダリウス"
type: entity
status: active
created: 2026-09-14
updated: 2026-09-15
sources:
  - "[[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]]"
  - "[[wiki/sources/src-2026-09-14-dragontail-16-18-1]]"
tags:
  - champion
  - role-fighter
  - role-tank
  - data-dragon
champion_id: "Darius"
champion_key: "122"
data_version: "16.18.1"
roles:
  - "Fighter"
  - "Tank"
resource_type: "マナ"
image_path: "raw/assets/champions/Darius.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Darius.png"
---

# ダリウス

![[raw/assets/champions/Darius.png|128]]

## 基本情報

- **英字ID：** `Darius`
- **キー：** `122`
- **称号：** ノクサスの戦斧
- **データversion：** `16.18.1`

## 紹介

ノクサス国内で最も恐れられる百戦錬磨の戦士、ダリウス。彼ほど、同国の強さを体現する司令官はいないだろう。貧しい育ちでありながら「ノクサスの戦斧」と呼ばれるまでになった彼は、帝国の敵を薙ぎ払い続ける──その多くはノクサス人である。自身の行為の意義に決して疑いを持つことはなく、彼はひとたび斧を振りかざせば決してためらうことはない。彼はトリファリアン・レギオンのリーダーに逆らう者には一切容赦しないのである。

## 分類

- **役割タグ：** `Fighter`、`Tank`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 9 |
| `defense` | 5 |
| `magic` | 1 |
| `difficulty` | 2 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 652 |
| `hpperlevel` | 114 |
| `mp` | 263 |
| `mpperlevel` | 58 |
| `movespeed` | 340 |
| `armor` | 37 |
| `armorperlevel` | 5.2 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 175 |
| `hpregen` | 10 |
| `hpregenperlevel` | 0.95 |
| `mpregen` | 6.6 |
| `mpregenperlevel` | 0.35 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 64 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 1 |
| `attackspeed` | 0.625 |

## アビリティ

- **パッシブ — 大出血：** 通常攻撃または攻撃スキルが命中した敵を出血させ、5秒間物理ダメージを与える。最大5回まで効果をスタックさせることができる。対象のスタックが最大になると、ダリウスが激怒して攻撃力が大幅に増加する。

- **Q — 皆殺しの斧：** 斧を構えて振り抜き、周囲の敵を攻撃する。刃に当たった敵は、内側の柄に当たった敵より大きなダメージを受ける。刃に当たった敵チャンピオンと大型モンスターの数に応じて自身を回復する。
- **W — 脚削ぎ：** 次の通常攻撃で敵の動脈を狙い、出血させることでスロウ効果を付与する。
- **E — 捕縛：** 斧を研ぎ澄まし、対象の物理防御を一部無視して物理ダメージを与えるようになる。スキルを使用すると、刃で敵を引っかけてそばに引き寄せる。
- **R — ノクサスギロチン：** 敵チャンピオンに飛びかかり、斧を振り下ろして確定ダメージを与える。対象の「大出血」のスタック数に応じてダメージが増加する。「ノクサスギロチン」で敵にとどめを刺すと、少しの間クールダウンが解消される。

<!-- power-spike:start -->
## パワースパイク

- **区分：** 序盤
- **判定：** [[wiki/syntheses/champion-power-spikes-v16-18-1|パワースパイク分類 v16.18.1]] に基づく原典ベースの推論。
- **根拠：**
  - 基礎ステータス指数（体力・物理防御・攻撃力・移動速度を標準化して合算）が173件中21位（上位15%）。体力652、物理防御37、攻撃力64、移動速度340。
- **限界：** スキル基礎ダメージ・係数・アイテム完成時刻を全チャンピオンで統一比較できる原典値がないため、実戦の強さや購入優先度を断定しない。

<!-- power-spike:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Darius` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Darius.png)
