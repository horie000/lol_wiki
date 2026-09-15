---
title: "ノクターン"
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
champion_id: "Nocturne"
champion_key: "56"
data_version: "16.18.1"
roles:
  - "Fighter"
  - "Assassin"
resource_type: "マナ"
image_path: "raw/assets/champions/Nocturne.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Nocturne.png"
---

# ノクターン

![[raw/assets/champions/Nocturne.png|128]]

## 基本情報

- **英字ID：** `Nocturne`
- **キー：** `56`
- **称号：** 終わりなき悪夢
- **データversion：** `16.18.1`

## 紹介

知覚を持つあらゆる生物が見る悪夢が融合してできたノクターンとして知られるこの恐ろしい存在は、純悪の根源的な力である。混沌として明確な姿は持たず、顔の無い影の中に冷たい目が浮かんでおり、複数の不気味な刃を持っている。霊的領域から脱したノクターンは、目覚め始めた世界に降り立ち、真の闇にしか存在しない恐怖を糧にして生きている。

## 分類

- **役割タグ：** `Fighter`、`Assassin`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 9 |
| `defense` | 5 |
| `magic` | 2 |
| `difficulty` | 4 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 640 |
| `hpperlevel` | 109 |
| `mp` | 275 |
| `mpperlevel` | 35 |
| `movespeed` | 345 |
| `armor` | 36 |
| `armorperlevel` | 4.2 |
| `spellblock` | 32 |
| `spellblockperlevel` | 1.55 |
| `attackrange` | 125 |
| `hpregen` | 7 |
| `hpregenperlevel` | 0.75 |
| `mpregen` | 7 |
| `mpregenperlevel` | 0.45 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 62 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2.7 |
| `attackspeed` | 0.721 |

## アビリティ

- **パッシブ — 夢幻斬：** 数秒ごとに次の攻撃が範囲攻撃になり、周囲の敵に追加物理ダメージを与えて自身の体力を回復する。 通常攻撃するたびにクールダウンが短縮する。

- **Q — 闇の手：** 指定方向に影の刃を投げてダメージを与える。刃の軌跡や命中した敵チャンピオンが残す影の上にいる間はユニットをすり抜けられ、移動速度と攻撃力が増加する。
- **W — 漆黒の帳：** 自動効果: 刃に念が送られ、攻撃速度が増加する。 発動効果: 魔法のバリアを張って敵のスキルを一度だけ無効化する。無効化成功後は自動効果による攻撃速度の増加率が倍になる。
- **E — 底知れぬ恐怖：** 対象におぞましい悪夢を見せ、毎秒ダメージを与える。効果終了までに範囲内から抜け出せなかった対象にはフィアー効果を与える。
- **R — パラノイア：** すべての敵チャンピオンの視界が悪化し、自分以外の視界を失う。効果中、指定した近くの敵チャンピオンに突撃して攻撃できる。

<!-- power-spike:start -->
## パワースパイク

- **区分：** 序盤
- **判定：** [[wiki/syntheses/champion-power-spikes-v16-18-1|パワースパイク分類 v16.18.1]] に基づく原典ベースの推論。
- **根拠：**
  - 基礎ステータス指数（体力・物理防御・攻撃力・移動速度を標準化して合算）が173件中24位（上位15%）。体力640、物理防御36、攻撃力62、移動速度345。
- **限界：** スキル基礎ダメージ・係数・アイテム完成時刻を全チャンピオンで統一比較できる原典値がないため、実戦の強さや購入優先度を断定しない。

<!-- power-spike:end -->

<!-- power-spike-match:start -->
## 試合時間別の観測

- **観測分類：** 明瞭な傾向なし
- **対象試合：** 554試合、全体勝率 52.5%
- **時間帯別勝率：** 〜20分 59.3%（n=81）、20〜25分 50.0%（n=68）、25〜30分 51.9%（n=131）、30〜35分 49.0%（n=143）、35分〜 54.2%（n=131）
- **最高帯：** 〜20分（判定差 10.3ポイント）
- **判定根拠：** 5つの時間帯を比較できるが、最高帯と端点の差が8ポイント未満、または勝率が非単調だった。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-56|ノクターンの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### JUNGLE（970試合）

- **実測ビルド候補：** ブラック クリーバー + デス ダンス（該当n=43、72.1% / 非該当53.3%、差+18.8pt）；実験的ヘクスプレート + 装甲強化の進撃 + ストライドブレイカー（該当n=36、72.2% / 非該当53.4%、差+18.8pt）
- **ステータス傾向：** クリティカル率（該当n=61、67.2% / 非該当53.2%、差+14.0pt）；魔法防御（該当n=298、56.7% / 非該当53.0%、差+3.7pt）
- **理論仮説：** トリニティ フォース + ストライドブレイカー（未観測；共通stats: 攻撃力・攻撃速度・体力／チャンピオン原典にも言及: 攻撃力・攻撃速度・体力）；実験的ヘクスプレート + トリニティ フォース（未観測；共通stats: 攻撃力・攻撃速度・体力／チャンピオン原典にも言及: 攻撃力・攻撃速度・体力）

<!-- champion-build-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Nocturne` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Nocturne.png)
