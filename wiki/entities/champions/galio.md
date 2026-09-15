---
title: "ガリオ"
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
  - role-mage
  - data-dragon
champion_id: "Galio"
champion_key: "3"
data_version: "16.18.1"
roles:
  - "Tank"
  - "Mage"
resource_type: "マナ"
image_path: "raw/assets/champions/Galio.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Galio.png"
---

# ガリオ

![[raw/assets/champions/Galio.png|128]]

## 基本情報

- **英字ID：** `Galio`
- **キー：** `3`
- **称号：** 伝説の巨像
- **データversion：** `16.18.1`

## 紹介

輝ける都市デマーシアの外側で、石の巨像ガリオはずっと見張りを続けている。敵の魔法使いに対する防御機構として建造された彼は、強力な魔法によって生命が満たされるまで何十年も微動だにせず、ただ立ち続ける。そして、ひとたび活動を始めると、ガリオは動ける時間のほとんどを戦いのスリルと同胞たる国民を守るという稀有な名誉を味わうことに費やすのだ。だが彼の勝利はいつも皮肉なもので、彼が打ち倒すべき魔法こそ彼が動くための原動力であるために、勝利するたびに再び動かぬ彫像となってしまうのだ。

## 分類

- **役割タグ：** `Tank`、`Mage`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 1 |
| `defense` | 10 |
| `magic` | 6 |
| `difficulty` | 5 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 600 |
| `hpperlevel` | 126 |
| `mp` | 410 |
| `mpperlevel` | 40 |
| `movespeed` | 340 |
| `armor` | 24 |
| `armorperlevel` | 4.7 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 150 |
| `hpregen` | 8 |
| `hpregenperlevel` | 0.8 |
| `mpregen` | 9.5 |
| `mpregenperlevel` | 0.7 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 59 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 1.5 |
| `attackspeed` | 0.625 |

## アビリティ

- **パッシブ — 巨像の一撃：** 数秒毎に、通常攻撃が一定範囲に追加魔法ダメージを与える。

- **Q — 戦の旋風：** 2つの突風を巻き起こす。突風同士は重なり合い、継続ダメージを与える巨大な竜巻となる。
- **W — デュランドの守り：** 防御の構えを取り移動速度が低下する。構えを解くと、周囲の敵ユニットにタウント効果とダメージを与える。
- **E — 正義の鉄拳：** 少し下がってから前方に突進し、最初に当たった敵チャンピオンをノックアップする。
- **R — 英雄降臨：** 味方1体の位置を着地点として指定し、範囲内のすべての味方に魔法ダメージを防ぐシールドを付与する。少ししてから、着地点に向かって落下し、周囲の敵をノックアップする。

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
- **対象試合：** 424試合、全体勝率 48.8%
- **時間帯別勝率：** 〜20分 46.7%（n=60）、20〜25分 54.7%（n=53）、25〜30分 46.4%（n=110）、30〜35分 48.5%（n=99）、35分〜 50.0%（n=102）
- **最高帯：** 20〜25分（判定差 8.4ポイント）
- **判定根拠：** 5つの時間帯を比較できるが、最高帯と端点の差が8ポイント未満、または勝率が非単調だった。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Galio` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Galio.png)
