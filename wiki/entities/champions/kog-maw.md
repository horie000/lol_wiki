---
title: "コグ＝マウ"
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
  - role-mage
  - data-dragon
champion_id: "KogMaw"
champion_key: "96"
data_version: "16.18.1"
roles:
  - "Marksman"
  - "Mage"
resource_type: "マナ"
image_path: "raw/assets/champions/KogMaw.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/KogMaw.png"
---

# コグ＝マウ

![[raw/assets/champions/KogMaw.png|128]]

## 基本情報

- **英字ID：** `KogMaw`
- **キー：** `96`
- **称号：** 深淵のアギト
- **データversion：** `16.18.1`

## 紹介

イカシアの荒れ地の奥深くにあるヴォイドの浸食から生まれたコグ＝マウは腐食性の大きな口を持つ好奇心旺盛な腐敗した生物だ。このヴォイドの生物は周囲に存在するものを真に理解するためには、それをかじって唾をかける必要がある。本質的に悪意がある訳ではないが、コグ＝マウの愉快な無邪気さは危険であり、それは狂乱状態になって何かを食べようとする前触れだ──彼は生きるために食べているのではなく、尽きぬ好奇心を満たすために食べている。

## 分類

- **役割タグ：** `Marksman`、`Mage`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 8 |
| `defense` | 2 |
| `magic` | 5 |
| `difficulty` | 6 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 635 |
| `hpperlevel` | 99 |
| `mp` | 325 |
| `mpperlevel` | 40 |
| `movespeed` | 330 |
| `armor` | 24 |
| `armorperlevel` | 4.45 |
| `spellblock` | 33 |
| `spellblockperlevel` | 1.1 |
| `attackrange` | 500 |
| `hpregen` | 3.75 |
| `hpregenperlevel` | 0.55 |
| `mpregen` | 8.75 |
| `mpregenperlevel` | 0.7 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 61 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2.65 |
| `attackspeed` | 0.665 |

## アビリティ

- **パッシブ — イカシアの自爆：** 倒されてから4秒後、コグ＝マウは爆発して周囲の敵に確定ダメージを与える。

- **Q — 腐食粘液：** 苛性の粘液を飛ばし、対象に魔法ダメージを与え、物理防御と魔法防御を短時間低下させる。さらにコグ＝マウの攻撃速度が増加する。
- **W — 有機性魔力砲：** 通常攻撃の射程距離が増加し、対象の最大体力に比例した魔法ダメージ%i:OnHit%通常攻撃時効果を与える。
- **E — ヴォイド分泌液：** 敵を貫通する謎の粘液を発射し、命中した敵ユニットにダメージを与える。粘液は通過したエリアにしばらく残り、踏んだ敵にスロウ効果を付与する。
- **R — 生体空撃砲：** 射程の長い砲弾を発射して魔法ダメージ (体力が低い敵には大幅に増加) を与えるとともに、敵を可視状態にする。ただし、ステルス状態の敵の位置を把握することはできない。このスキルを短時間で連発すると、消費マナが増加する。

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
- **対象試合：** 76試合、全体勝率 47.4%
- **時間帯別勝率：** 〜20分 58.3%（n=12）、20〜25分 40.0%（n=10）、25〜30分 31.6%（n=19）、30〜35分 59.1%（n=22）、35分〜 46.2%（n=13）
- **最高帯：** 30〜35分（判定差 —）
- **判定根拠：** 5つの時間帯のいずれかで15試合未満のため、時間帯の比較を保留する。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.KogMaw` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/KogMaw.png)
