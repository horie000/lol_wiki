---
title: "フェイ"
type: entity
status: active
created: 2026-09-14
updated: 2026-09-15
sources:
  - "[[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]]"
  - "[[wiki/sources/src-2026-09-14-dragontail-16-18-1]]"
  - "[[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]"
tags:
  - champion
  - role-mage
  - role-support
  - data-dragon
champion_id: "Hwei"
champion_key: "910"
data_version: "16.18.1"
roles:
  - "Mage"
  - "Support"
resource_type: "マナ"
image_path: "raw/assets/champions/Hwei.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Hwei.png"
---

# フェイ

![[raw/assets/champions/Hwei.png|128]]

## 基本情報

- **英字ID：** `Hwei`
- **キー：** `910`
- **称号：** 夢想家
- **データversion：** `16.18.1`

## 紹介

フェイは陰鬱な芸術家で、見事な作品を生み出すことでアイオニアの悪人を罰し、罪なき者を慰める。暗い外面のすぐ下で、引き裂かれた感情が渦を巻き、想像力が生み出す鮮やかな情景と、寺院で起きた虐殺の凄惨な記憶とがせめぎ合っている。この明と暗を理解するための旅は、すなわち、フェイの力を解き放った芸術家を捜す旅でもある。絵筆とパレットだけを頼りに、無限の可能性を描くフェイの行く手に待つものは、心の平安か、はたまた絶望か。

## 分類

- **役割タグ：** `Mage`、`Support`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 7 |
| `defense` | 1 |
| `magic` | 8 |
| `difficulty` | 9 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 580 |
| `hpperlevel` | 109 |
| `mp` | 480 |
| `mpperlevel` | 30 |
| `movespeed` | 330 |
| `armor` | 21 |
| `armorperlevel` | 4.7 |
| `spellblock` | 30 |
| `spellblockperlevel` | 1.3 |
| `attackrange` | 550 |
| `hpregen` | 5.5 |
| `hpregenperlevel` | 0.55 |
| `mpregen` | 7.5 |
| `mpregenperlevel` | 0.75 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 54 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2.5 |
| `attackspeed` | 0.69 |

## アビリティ

- **パッシブ — 夢想家の銘：** スキルで敵チャンピオンにダメージを与えると、最後の仕上げとなるサインを施せるよう、対象を下塗りする。 2つ目の攻撃スキルを敵に命中させるとサインが完成し、対象の足元に残る。少しするとサインは爆発し、範囲内のすべての敵に魔法ダメージを与える。

- **Q — 題材: 厄災：** 終わりなき厄災を思い描き、壊滅的な一撃を描く力を得る。 このスキルは、フェイのスキルを攻撃スキル「荒廃の炎」、「断ち切る稲妻」、「沸き立つ大地」に置き換える。
- **W — 題材: 静謐：** 終わりなき静穏を思い描き、爽快な作品を描く力を得る。 このスキルは、フェイのスキルを補助系スキル「流るる蒼」、「内省の泉」、「迸る光彩」に置き換える。
- **E — 題材: 苦悩：** 終わりなき苦悩を思い描き、支配欲に満ちた表情を描く力を得る。 このスキルは、フェイのスキルを行動妨害スキル「恐怖の形相」、「深淵の眼差し」、「粉砕の牙」に置き換える。
- **R — 絶望の渦：** 純粋なる絶望のビジョンを描く。最初に命中した敵チャンピオンが拡大する絵画の中心となり、周囲の敵にスロウ効果とダメージを与える。ビジョンは最大サイズに達するか、最初に命中したチャンピオンがデスすると爆発する。

<!-- power-spike:start -->
## パワースパイク

- **区分：** 中盤
- **判定：** [[wiki/syntheses/champion-power-spikes-v16-18-1|パワースパイク分類 v16.18.1]] に基づく原典ベースの推論。
- **根拠：**
  - 本分類で採用した序盤の基礎ステータス上位15%と、終盤の能力の蓄積成長・明示的なステータス連動のいずれにも当たらないため、中盤を暫定指定する。
- **限界：** スキル基礎ダメージ・係数・アイテム完成時刻を全チャンピオンで統一比較できる原典値がないため、実戦の強さや購入優先度を断定しない。

<!-- power-spike:end -->

<!-- power-spike-match:start -->
## 試合時間別の観測

- **観測分類：** 明瞭な傾向なし
- **対象試合：** 433試合、全体勝率 51.3%
- **時間帯別勝率：** 〜20分 44.1%（n=68）、20〜25分 50.0%（n=52）、25〜30分 57.3%（n=89）、30〜35分 50.9%（n=108）、35分〜 51.7%（n=116）
- **最高帯：** 25〜30分（判定差 13.2ポイント）
- **判定根拠：** 5つの時間帯を比較できるが、最高帯と端点の差が8ポイント未満、または勝率が非単調だった。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Hwei` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Hwei.png)
