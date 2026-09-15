---
title: "シャコ"
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
  - role-assassin
  - data-dragon
champion_id: "Shaco"
champion_key: "35"
data_version: "16.18.1"
roles:
  - "Assassin"
resource_type: "マナ"
image_path: "raw/assets/champions/Shaco.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Shaco.png"
---

# シャコ

![[raw/assets/champions/Shaco.png|128]]

## 基本情報

- **英字ID：** `Shaco`
- **キー：** `35`
- **称号：** 悪魔の道化師
- **データversion：** `16.18.1`

## 紹介

殺人と暴力に悦びを見出すシャコは、かつては寂しい王子の遊び道具として作られた魔法の操り人形だった。闇の魔法に穢されて、自らが愛していた役目を失ったことで、優しい操り人形は憐れな者たちを苦しめることに悦びを見出すように成り果てた。彼はおもちゃや単純なトリックを駆使して殺人を行い、その血塗られた「ゲーム」を楽しんで笑っている。夜中に彼の不気味な笑い声が聞こえたら…それは悪魔の道化師があなたを次のおもちゃとして選んだ証かもしれない。

## 分類

- **役割タグ：** `Assassin`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 8 |
| `defense` | 4 |
| `magic` | 6 |
| `difficulty` | 9 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 630 |
| `hpperlevel` | 99 |
| `mp` | 297 |
| `mpperlevel` | 40 |
| `movespeed` | 345 |
| `armor` | 30 |
| `armorperlevel` | 4 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 125 |
| `hpregen` | 8.5 |
| `hpregenperlevel` | 0.55 |
| `mpregen` | 6 |
| `mpregenperlevel` | 0.35 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 63 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 3 |
| `attackspeed` | 0.694 |

## アビリティ

- **パッシブ — バックスタブ：** 対象の背後から攻撃した場合、通常攻撃と「ポイズンダガー」が追加ダメージを与える。

- **Q — 幻惑：** インビジブル状態になり、瞬間移動する。 インビジブル中の最初の通常攻撃は追加ダメージを与え、対象の背後から攻撃した場合はクリティカルになる。
- **W — びっくり箱：** 隠された「びっくり箱」をフィールド上に設置する。敵が近づくと発動して、周囲の敵すべてを恐怖に陥れて攻撃する。
- **E — ポイズンダガー：** 「ポイズンダガー」は自動効果により通常攻撃が命中した敵に毒を与え、移動速度を低下させる。発動した場合は対象にナイフを投げ、ダメージと毒を与える。対象の体力が30%未満の場合は追加ダメージが発生する。
- **R — ハルシネイト：** シャコの分身が生成され周囲の敵を攻撃する(タワーに対してはダメージが減少する)。分身の体力が尽きると爆発して、3つの「ミニびっくり箱」を発生させ、周囲の敵にダメージを与える。

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

- **観測分類：** 中盤寄り
- **対象試合：** 142試合、全体勝率 54.9%
- **時間帯別勝率：** 〜20分 57.1%（n=21）、20〜25分 60.9%（n=23）、25〜30分 66.7%（n=33）、30〜35分 46.2%（n=39）、35分〜 46.2%（n=26）
- **最高帯：** 25〜30分（判定差 9.5ポイント）
- **判定根拠：** 中間帯が最高、端点との差 9.5%
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-35|シャコの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### UTILITY（456試合）

- **実測ビルド候補：** インフィニティ エッジ + コレクター + ヒュブリス（該当n=54、61.1% / 非該当51.7%、差+9.4pt）；コレクター + ヒュブリス（該当n=96、59.4% / 非該当51.1%、差+8.3pt）
- **ステータス傾向：** ライフスティール（該当n=48、58.3% / 非該当52.2%、差+6.1pt）；体力（該当n=107、57.0% / 非該当51.6%、差+5.4pt）
- **理論仮説：** ファントム ダンサー + ナヴォリ フリッカーブレード（未観測；共通stats: 攻撃速度・クリティカル率・移動速度／チャンピオン原典にも言及: クリティカル率・移動速度）；ドミニク リガード + コレクター（n=11（15未満）；共通stats: 攻撃力・クリティカル率／チャンピオン原典にも言及: 攻撃力・クリティカル率）

### JUNGLE（344試合）

- **実測ビルド候補：** 黒炎のトーチ + ライアンドリーの仮面（該当n=60、68.3% / 非該当52.1%、差+16.2pt）；インフィニティ エッジ + ユン・タル ワイルドアロー（該当n=68、66.2% / 非該当52.2%、差+14.0pt）
- **ステータス傾向：** 魔力（該当n=99、66.7% / 非該当50.2%、差+16.5pt）；マナ（該当n=84、66.7% / 非該当51.2%、差+15.5pt）
- **理論仮説：** スタティック シヴ + クラーケン スレイヤー（未観測；共通stats: 攻撃力・攻撃速度・移動速度／チャンピオン原典にも言及: 攻撃力・移動速度）；トリニティ フォース + ストライドブレイカー（未観測；共通stats: 攻撃力・攻撃速度・体力／チャンピオン原典にも言及: 攻撃力・体力）

<!-- champion-build-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Shaco` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Shaco.png)
