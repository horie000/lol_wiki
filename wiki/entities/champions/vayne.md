---
title: "ヴェイン"
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
  - role-marksman
  - role-assassin
  - data-dragon
champion_id: "Vayne"
champion_key: "67"
data_version: "16.18.1"
roles:
  - "Marksman"
  - "Assassin"
resource_type: "マナ"
image_path: "raw/assets/champions/Vayne.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Vayne.png"
---

# ヴェイン

![[raw/assets/champions/Vayne.png|128]]

## 基本情報

- **英字ID：** `Vayne`
- **キー：** `67`
- **称号：** ナイトハンター
- **データversion：** `16.18.1`

## 紹介

シャウナ・ヴェインはデマーシアの無慈悲な怪物ハンターであり、自分の家族を殺した悪魔を見つけ出して殺すことに生涯をささげている。前腕部搭載式のクロスボウと復讐に燃える心を武器にする彼女だが、心からの喜びを感じることができるのは、影の中から銀の矢を飛ばして闇の魔術の使い手や、その不浄なる創造物を殺した時だけだ。

## 分類

- **役割タグ：** `Marksman`、`Assassin`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 10 |
| `defense` | 1 |
| `magic` | 1 |
| `difficulty` | 8 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 580 |
| `hpperlevel` | 98 |
| `mp` | 232 |
| `mpperlevel` | 35 |
| `movespeed` | 330 |
| `armor` | 23 |
| `armorperlevel` | 4.6 |
| `spellblock` | 33 |
| `spellblockperlevel` | 1.1 |
| `attackrange` | 550 |
| `hpregen` | 4 |
| `hpregenperlevel` | 0.5 |
| `mpregen` | 7 |
| `mpregenperlevel` | 0.4 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 60 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2.8 |
| `attackspeed` | 0.658 |

## アビリティ

- **パッシブ — ナイトハンター：** 敵チャンピオンに向かって移動する時、移動速度が増加する。

- **Q — タンブル：** 指定方向に前転して移動し、次の攻撃の準備をする。次の通常攻撃が追加ダメージを与える。
- **W — シルバーボルト：** 邪悪な存在が嫌う銀の矢を、クロスボウにつがえる。同じ対象に通常攻撃またはスキルを3回連続で命中させると、対象の最大体力に比例する追加確定ダメージが発生する。
- **E — パニッシュメント：** 背中に担いだ特大クロスボウを構え、指定対象に巨大な矢を撃ち込む。矢を受けたユニットはノックバックされダメージを受ける。ノックバック中に対象が地形に衝突した場合は、追加のダメージが発生し、スタン状態になる。
- **R — ファイナルアワー：** 敵を殲滅すべく特大クロスボウを構え、攻撃力が増加する。効果時間中は「タンブル」発動時にインビジブル状態になり、「タンブル」のクールダウンが短縮される。また、「ナイトハンター」の移動速度増加量が上昇する。

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

- **観測分類：** 終盤寄り
- **対象試合：** 145試合、全体勝率 47.6%
- **時間帯別勝率：** 〜20分 42.9%（n=21）、20〜25分 55.6%（n=18）、25〜30分 32.6%（n=46）、30〜35分 57.1%（n=28）、35分〜 59.4%（n=32）
- **最高帯：** 35分〜（判定差 16.5ポイント）
- **判定根拠：** 35分〜が最高、短時間帯との差 16.5%
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Vayne` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Vayne.png)
