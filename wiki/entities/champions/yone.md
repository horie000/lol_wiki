---
title: "ヨネ"
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
  - role-fighter
  - role-assassin
  - data-dragon
champion_id: "Yone"
champion_key: "777"
data_version: "16.18.1"
roles:
  - "Fighter"
  - "Assassin"
resource_type: "つむじ風"
image_path: "raw/assets/champions/Yone.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Yone.png"
---

# ヨネ

![[raw/assets/champions/Yone.png|128]]

## 基本情報

- **英字ID：** `Yone`
- **キー：** `777`
- **称号：** 忘られざる者
- **データversion：** `16.18.1`

## 紹介

生前、ヨネはヤスオの腹違いの兄であり、村の剣術道場で名を知られた生徒だった。しかし弟の手で殺されたヨネは、霊界の邪悪な存在に狙われ、その悪しき者が持っていた刀を使って殺すことを余儀なくされた。そして悪魔の仮面を被る呪いにかけられたヨネは、自らが何者に変わったのかを理解するために、そうした邪悪な存在を飽くことなく狩り続けている。

## 分類

- **役割タグ：** `Fighter`、`Assassin`
- **リソース種別：** つむじ風

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 8 |
| `defense` | 4 |
| `magic` | 4 |
| `difficulty` | 8 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 620 |
| `hpperlevel` | 105 |
| `mp` | 500 |
| `mpperlevel` | 0 |
| `movespeed` | 345 |
| `armor` | 33 |
| `armorperlevel` | 4.6 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 175 |
| `hpregen` | 7.5 |
| `hpregenperlevel` | 0.75 |
| `mpregen` | 0 |
| `mpregenperlevel` | 0 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 62 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 3.5 |
| `attackspeed` | 0.625 |

## アビリティ

- **パッシブ — 狩鬼道：** 通常攻撃2回ごとに魔法ダメージを与える。さらに、クリティカル率が増加する。

- **Q — 斬命刀：** 前方に突きを放ち、直線上の敵すべてにダメージを与える。 このスキルが命中すると「つむじ風」のスタックを数秒間得る。2スタックになると、「斬命刀」を使用した際、一陣の風をまとって前方にダッシュし、敵をノックアップさせる。
- **W — 霊断刀：** 前方をなぎ払い、扇状の範囲内にいるすべての敵にダメージを与え、シールドを獲得する。シールド量はなぎ払いが命中したチャンピオンの数に応じて増加する。 攻撃速度が増加すると「霊断刀」のクールダウンと詠唱時間が短縮される。
- **E — 縛魂の解放：** 自身の霊魂が肉体を離れ、移動速度が増加する。スキル終了時にこの霊魂は肉体に強制的に戻り、霊魂として与えたダメージの一部をもう一度与える。
- **R — 冥封一閃：** 直線上の最後にいるチャンピオンの背後に強力な斬撃を与えてブリンクし、当たった敵すべてを自身の方向に引き寄せる。

<!-- power-spike:start -->
## パワースパイク

- **区分：** 終盤
- **判定：** [[wiki/syntheses/champion-power-spikes-v16-18-1|パワースパイク分類 v16.18.1]] に基づく原典ベースの推論。
- **根拠：**
  - パッシブでクリティカル率が増加し、攻撃速度はWのクールダウンと詠唱時間に影響する。
- **限界：** スキル基礎ダメージ・係数・アイテム完成時刻を全チャンピオンで統一比較できる原典値がないため、実戦の強さや購入優先度を断定しない。

<!-- power-spike:end -->

<!-- power-spike-match:start -->
## 試合時間別の観測

- **観測分類：** 明瞭な傾向なし
- **対象試合：** 1109試合、全体勝率 48.2%
- **時間帯別勝率：** 〜20分 49.5%（n=192）、20〜25分 47.8%（n=159）、25〜30分 46.4%（n=265）、30〜35分 51.8%（n=251）、35分〜 45.5%（n=242）
- **最高帯：** 30〜35分（判定差 6.3ポイント）
- **判定根拠：** 5つの時間帯を比較できるが、最高帯と端点の差が8ポイント未満、または勝率が非単調だった。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-777|ヨネの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### MIDDLE（1,187試合）

- **実測ビルド候補：** インフィニティ エッジ + モータル リマインダー + ルインドキング ブレード（該当n=31、67.7% / 非該当49.2%、差+18.5pt）；インフィニティ エッジ + ルインドキング ブレード + デス ダンス（該当n=68、66.2% / 非該当48.7%、差+17.5pt）
- **ステータス傾向：** 移動速度（該当n=1147、50.4% / 非該当30.0%、差+20.4pt）；クリティカル率（該当n=1007、52.0% / 非該当36.7%、差+15.4pt）
- **理論仮説：** ファントム ダンサー + ナヴォリ フリッカーブレード（未観測；共通stats: 攻撃速度・クリティカル率・移動速度／チャンピオン原典にも言及: 攻撃速度・クリティカル率・移動速度）；フィーンドハンターの矢 + ナヴォリ フリッカーブレード（未観測；共通stats: 攻撃速度・クリティカル率・移動速度／チャンピオン原典にも言及: 攻撃速度・クリティカル率・移動速度）

### TOP（716試合）

- **実測ビルド候補：** ガーディアン エンジェル + イモータル シールドボウ（該当n=37、67.6% / 非該当46.8%、差+20.7pt）；ガーディアン エンジェル + ルインドキング ブレード + イモータル シールドボウ（該当n=34、67.6% / 非該当46.9%、差+20.7pt）
- **ステータス傾向：** クリティカル率（該当n=604、50.8% / 非該当32.1%、差+18.7pt）；魔法防御（該当n=70、60.0% / 非該当46.6%、差+13.4pt）
- **理論仮説：** ファントム ダンサー + ナヴォリ フリッカーブレード（未観測；共通stats: 攻撃速度・クリティカル率・移動速度／チャンピオン原典にも言及: 攻撃速度・クリティカル率・移動速度）；インフィニティ エッジ + ドミニク リガード（n=14（15未満）；共通stats: 攻撃力・クリティカル率／チャンピオン原典にも言及: 攻撃力・クリティカル率）

<!-- champion-build-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Yone` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Yone.png)
