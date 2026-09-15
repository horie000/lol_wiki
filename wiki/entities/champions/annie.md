---
title: "アニー"
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
champion_id: "Annie"
champion_key: "1"
data_version: "16.18.1"
roles:
  - "Mage"
  - "Support"
resource_type: "マナ"
image_path: "raw/assets/champions/Annie.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Annie.png"
---

# アニー

![[raw/assets/champions/Annie.png|128]]

## 基本情報

- **英字ID：** `Annie`
- **キー：** `1`
- **称号：** 闇の申し子
- **データversion：** `16.18.1`

## 紹介

危険極まりなく、それでいて無邪気でおませなアニーは、強力な発火能力を持つ小さな魔女だ。ノクサスの北に位置する山々の影に忍んでいてもなお、アニーは異端者として果てしない孤独の中に生きている。生まれ持った炎を操る力は、彼女が感情をほとばしらせることになった思いがけない出来事がきっかけで目覚めた。そして次第に、アニーは「火遊び」のやり方を覚えていく。 アニーのお気に入りはクマのぬいぐるみのティバーズで、呼べばすぐにそばに来て、炎で彼女を守ってくれる。永遠に無垢な子供のままであるアニーは、暗い森をさまよい続け...

## 分類

- **役割タグ：** `Mage`、`Support`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 2 |
| `defense` | 3 |
| `magic` | 10 |
| `difficulty` | 6 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 560 |
| `hpperlevel` | 96 |
| `mp` | 418 |
| `mpperlevel` | 25 |
| `movespeed` | 335 |
| `armor` | 23 |
| `armorperlevel` | 4 |
| `spellblock` | 30 |
| `spellblockperlevel` | 1.3 |
| `attackrange` | 625 |
| `hpregen` | 5.5 |
| `hpregenperlevel` | 0.55 |
| `mpregen` | 8 |
| `mpregenperlevel` | 0.8 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 50 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 1.36 |
| `attackspeed` | 0.61 |

## アビリティ

- **パッシブ — 火遊びだいすき：** スキルを4回使用すると、次に行う攻撃スキルが対象をスタンさせる。 試合開始時および復活時は「火遊びだいすき」が使用可能な状態でスタートする。

- **Q — ファイアボール：** 火の玉を放って、指定した対象にダメージを与える。このスキルで敵ユニットを倒すと、消費したマナが回復しクールダウンが短縮する。
- **W — バーニングファイア：** 指定方向に扇状の炎を放ち、範囲内のすべての敵ユニットにダメージを与える。
- **E — モルテンシールド：** 自身または味方1体にシールドを付与し、移動速度が一時的に上昇する。また、通常攻撃かスキルで自身を攻撃した敵にダメージを与える。
- **R — やっちゃえ！ティバーズ！：** クマのティバーズを召喚し、範囲内の敵ユニットにダメージを与える。召喚されたティバーズは敵ユニットを攻撃し、身にまとう炎で周囲にいる敵に継続ダメージを与える。

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
- **対象試合：** 63試合、全体勝率 54.0%
- **時間帯別勝率：** 〜20分 47.1%（n=17）、20〜25分 42.9%（n=7）、25〜30分 63.6%（n=11）、30〜35分 52.9%（n=17）、35分〜 63.6%（n=11）
- **最高帯：** 25〜30分（判定差 —）
- **判定根拠：** 5つの時間帯のいずれかで15試合未満のため、時間帯の比較を保留する。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Annie` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Annie.png)
