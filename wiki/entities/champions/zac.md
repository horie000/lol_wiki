---
title: "ザック"
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
  - role-tank
  - role-fighter
  - data-dragon
champion_id: "Zac"
champion_key: "154"
data_version: "16.18.1"
roles:
  - "Tank"
  - "Fighter"
resource_type: "なし"
image_path: "raw/assets/champions/Zac.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Zac.png"
---

# ザック

![[raw/assets/champions/Zac.png|128]]

## 基本情報

- **英字ID：** `Zac`
- **キー：** `154`
- **称号：** 親愛なる秘密兵器
- **データversion：** `16.18.1`

## 紹介

ケミテック層を流れ、ゾウンの汚水地区の奥深く、ぽつんと隔離された大空洞に溜まった有毒液の池。その澱みの中で、ザックは覚醒した。そんな哀れな出自でありながらも、ザックは原始的な粘体生物から思考する存在へと成長を遂げ、都市のパイプの中に潜んで暮らし、時には助けが必要な者を助けるために飛び出したり、ゾウンの破損したインフラを修理するのである。

## 分類

- **役割タグ：** `Tank`、`Fighter`
- **リソース種別：** なし

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 3 |
| `defense` | 7 |
| `magic` | 7 |
| `difficulty` | 8 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 685 |
| `hpperlevel` | 109 |
| `mp` | 0 |
| `mpperlevel` | 0 |
| `movespeed` | 340 |
| `armor` | 33 |
| `armorperlevel` | 5.2 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 175 |
| `hpregen` | 5 |
| `hpregenperlevel` | 0.5 |
| `mpregen` | 0 |
| `mpregenperlevel` | 0 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 60 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 1.6 |
| `attackspeed` | 0.736 |

## アビリティ

- **パッシブ — はぐれスライム：** スキルによる攻撃を命中させるたびスライムが飛び散り、回収すると体力が回復する。致命的なダメージを受けた場合、ザックは4体のスライムに分裂する。その後数秒かけて再融合し、この時に生き残っていたスライムの体力に応じた体力で復活する。各スライムはザックの最大体力、物理防御、魔法防御の数パーセントに相当するステータスを持つ。ザックは一度分裂すると、ふたたび分裂するために5分間のクールダウンが必要になる。

- **Q — スライムパンチ：** 片手を伸ばして敵ユニットを掴む。別の敵ユニットを攻撃すると両者を互いにぶつけ合わせる。
- **W — スライムクラッシュ：** 体を爆発させることで近くの敵に向かって突進し、最大体力の一定割合を魔法ダメージとして与える。
- **E — ブッ飛びスライム：** ザックが両手をついて反発力を溜め込み、対象に勢いよく飛びかかる。
- **R — レッツバウンス！：** 4回バウンドし、命中した敵をノックアップさせてスロウ状態にする。

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

- **観測分類：** 判定保留（分母不足）
- **対象試合：** 94試合、全体勝率 47.9%
- **時間帯別勝率：** 〜20分 42.1%（n=19）、20〜25分 46.2%（n=13）、25〜30分 50.0%（n=22）、30〜35分 57.1%（n=21）、35分〜 42.1%（n=19）
- **最高帯：** 30〜35分（判定差 —）
- **判定根拠：** 5つの時間帯のいずれかで15試合未満のため、時間帯の比較を保留する。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Zac` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Zac.png)
