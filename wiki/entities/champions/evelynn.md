---
title: "イブリン"
type: entity
status: active
created: 2026-09-14
updated: 2026-09-15
sources:
  - "[[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]]"
  - "[[wiki/sources/src-2026-09-14-dragontail-16-18-1]]"
tags:
  - champion
  - role-assassin
  - role-mage
  - data-dragon
champion_id: "Evelynn"
champion_key: "28"
data_version: "16.18.1"
roles:
  - "Assassin"
  - "Mage"
resource_type: "マナ"
image_path: "raw/assets/champions/Evelynn.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Evelynn.png"
---

# イブリン

![[raw/assets/champions/Evelynn.png|128]]

## 基本情報

- **英字ID：** `Evelynn`
- **キー：** `28`
- **称号：** 苦悶の抱擁
- **データversion：** `16.18.1`

## 紹介

ルーンテラ中の暗がりで悪魔イブリンは次の犠牲者を物色する。艶かしい女性の姿で獲物を誘い、相手を魅了したところで真の姿を露わす。そして彼女は、言葉では言い表せないほどの苦痛を相手に与え、苦悶する様を糧（かて）に愉悦に浸る。だがこの悪魔にとっては、そんな火遊びもただの気まぐれに過ぎない。ルーンテラの人々にとって、それは欲望が暴走した末路を描くおぞましい物語であり、節度なき快楽がもたらす代償を思い知らせる恐怖の象徴なのだ。

## 分類

- **役割タグ：** `Assassin`、`Mage`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 4 |
| `defense` | 2 |
| `magic` | 7 |
| `difficulty` | 10 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 642 |
| `hpperlevel` | 98 |
| `mp` | 315 |
| `mpperlevel` | 42 |
| `movespeed` | 335 |
| `armor` | 37 |
| `armorperlevel` | 4.7 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 125 |
| `hpregen` | 8.5 |
| `hpregenperlevel` | 0.75 |
| `mpregen` | 8.11 |
| `mpregenperlevel` | 0.6 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 61 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2.1 |
| `attackspeed` | 0.667 |

## アビリティ

- **パッシブ — 妖魔の影：** 戦闘中以外は「妖魔の影」に包まれ、体力が低下している場合は体力が回復する。レベル6以降は「妖魔の影」でカモフラージュも獲得する。

- **Q — ヘイトスパイク：** 鞭を振って最初に当たった敵ユニットにダメージを与える。その後、地面から一直線に貫通するトゲを近くの敵に数回放つことができる。
- **W — アリュール：** 対象に呪いをかける。少ししてから次に行う通常攻撃またはスキルがその敵にチャーム効果を与え、魔法防御を低下させる。
- **E — ウィップラッシュ：** 対象を鞭で打ってダメージを与え、その後少しの間だけ移動速度が増加する。
- **R — ラストカレス：** 少しの間だけ対象指定不可になり、自身の正面の範囲内にいる敵に大ダメージを与えてから後方に大きくワープする。

<!-- power-spike:start -->
## パワースパイク

- **区分：** 中盤
- **判定：** [[wiki/syntheses/champion-power-spikes-v16-18-1|パワースパイク分類 v16.18.1]] に基づく原典ベースの推論。
- **根拠：**
  - 本分類で採用した序盤の基礎ステータス上位15%と、終盤の能力の蓄積成長・明示的なステータス連動のいずれにも当たらないため、中盤を暫定指定する。
- **限界：** スキル基礎ダメージ・係数・アイテム完成時刻を全チャンピオンで統一比較できる原典値がないため、実戦の強さや購入優先度を断定しない。

<!-- power-spike:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Evelynn` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Evelynn.png)
