---
title: "ヌヌ＆ウィルンプ"
type: entity
status: active
created: 2026-09-14
updated: 2026-09-15
sources:
  - "[[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]]"
  - "[[wiki/sources/src-2026-09-14-dragontail-16-18-1]]"
  - "[[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]"
  - "[[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis]]"
tags:
  - champion
  - role-tank
  - role-mage
  - data-dragon
champion_id: "Nunu"
champion_key: "20"
data_version: "16.18.1"
roles:
  - "Tank"
  - "Mage"
resource_type: "マナ"
image_path: "raw/assets/champions/Nunu.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Nunu.png"
---

# ヌヌ＆ウィルンプ

![[raw/assets/champions/Nunu.png|128]]

## 基本情報

- **英字ID：** `Nunu`
- **キー：** `20`
- **称号：** 少年とイエティ
- **データversion：** `16.18.1`

## 紹介

昔々あるところに、恐ろしい怪物を倒して英雄になりたいと願う少年がいた。しかし怪物の正体を知ってみれば、それは魔力を持った独りぼっちのイエティで、彼はただ友達が欲しいだけだった。古き力によって結ばれ、雪玉遊びの楽しさを共に分かち合ったヌヌとウィルンプは、フレヨルド各地を冒険してまわっている。そしていつかどこかで、ヌヌの母親を見つけ出すことを願っている。彼女を救い出すことができれば、本物の英雄になれるかもしれないのだ…

## 分類

- **役割タグ：** `Tank`、`Mage`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 4 |
| `defense` | 6 |
| `magic` | 7 |
| `difficulty` | 4 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 610 |
| `hpperlevel` | 90 |
| `mp` | 280 |
| `mpperlevel` | 42 |
| `movespeed` | 345 |
| `armor` | 29 |
| `armorperlevel` | 4.2 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 125 |
| `hpregen` | 5 |
| `hpregenperlevel` | 0.8 |
| `mpregen` | 7 |
| `mpregenperlevel` | 0.5 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 61 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2.25 |
| `attackspeed` | 0.625 |

## アビリティ

- **パッシブ — フレヨルドの呼び声：** ヌヌがウィルンプと近くにいる味方1体の攻撃速度と移動速度を増加させる。さらに、ウィルンプの通常攻撃が対象の周囲にいる敵にもダメージを与えるようになる。

- **Q — 丸かじり：** ウィルンプがミニオンかモンスター、または敵チャンピオンにかぶりつき、ダメージを与えて自身の体力を回復する。
- **W — 超特大の雪玉！：** ウィルンプが雪玉をつくって転がす。雪玉を転がす間、雪玉のサイズとスピードが増加していく。雪玉は敵にダメージを与えてノックアップする。
- **E — 雪玉連射：** ヌヌが雪玉を複数投げて敵にダメージを与える。その後、雪玉が当たったチャンピオンと大型モンスターにウィルンプがスネア効果を与える。
- **R — アブソリュート・ゼロ：** ヌヌとウィルンプが一定範囲内に強力な猛吹雪をつくりだして敵にスロウ効果を与え、詠唱完了時に大ダメージを与える。

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
- **対象試合：** 98試合、全体勝率 46.9%
- **時間帯別勝率：** 〜20分 50.0%（n=18）、20〜25分 41.7%（n=12）、25〜30分 45.8%（n=24）、30〜35分 52.4%（n=21）、35分〜 43.5%（n=23）
- **最高帯：** 30〜35分（判定差 —）
- **判定根拠：** 5つの時間帯のいずれかで15試合未満のため、時間帯の比較を保留する。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-20|ヌヌ＆ウィルンプの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### JUNGLE（189試合）

- **実測ビルド候補：** 該当・非該当が各30試合以上で正の差を持つ候補なし。
- **ステータス傾向：** 魔法防御（該当n=89、52.8% / 非該当48.0%、差+4.8pt）；物理防御（該当n=133、51.1% / 非該当48.2%、差+2.9pt）
- **理論仮説：** ヘクステック ロケットベルト + ライアンドリーの仮面（n=9（15未満）；共通stats: 魔力・体力／チャンピオン原典にも言及: 魔力・体力）；メジャイ ソウルスティーラー + ヘクステック ロケットベルト（n=2（15未満）；共通stats: 魔力・体力／チャンピオン原典にも言及: 魔力・体力）

<!-- champion-build-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Nunu` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Nunu.png)
