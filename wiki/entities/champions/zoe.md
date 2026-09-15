---
title: "ゾーイ"
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
  - role-mage
  - data-dragon
champion_id: "Zoe"
champion_key: "142"
data_version: "16.18.1"
roles:
  - "Mage"
resource_type: "マナ"
image_path: "raw/assets/champions/Zoe.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Zoe.png"
---

# ゾーイ

![[raw/assets/champions/Zoe.png|128]]

## 基本情報

- **英字ID：** `Zoe`
- **キー：** `142`
- **称号：** 超常の遊び
- **データversion：** `16.18.1`

## 紹介

いたずら、想像、変化を具現化する存在であるゾーイは、時空を駆け抜けて霊峰ターゴンのメッセージ──世界の再編を招く出来事の到来──を告げる。彼女の存在は、現実を支配する聖なる数学に歪みを生み出し、時に激変を引き起こす。意識的にではないし、悪意もない。だからこそゾーイはたっぷりと時間をかけて遊びに集中し、定命の者をからかい、あるいはただ楽しいからという理由で、平然とその義務を果たせるのだろう。ゾーイに出会うと気分が高揚して前向きな気持ちになるが、実際にはそれは常に危険と隣り合わせだ。

## 分類

- **役割タグ：** `Mage`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 1 |
| `defense` | 7 |
| `magic` | 8 |
| `difficulty` | 5 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 630 |
| `hpperlevel` | 106 |
| `mp` | 425 |
| `mpperlevel` | 25 |
| `movespeed` | 340 |
| `armor` | 21 |
| `armorperlevel` | 4.7 |
| `spellblock` | 30 |
| `spellblockperlevel` | 1.3 |
| `attackrange` | 550 |
| `hpregen` | 7.5 |
| `hpregenperlevel` | 0.6 |
| `mpregen` | 8 |
| `mpregenperlevel` | 0.65 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 58 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2.5 |
| `attackspeed` | 0.658 |

## アビリティ

- **パッシブ — スパークル！：** スキル使用後、次に行う通常攻撃が追加魔法ダメージを与える。

- **Q — パドルスター：** 途中で進行方向を変えられる星を飛ばす。真っすぐ飛んだ距離の長さに応じてダメージが増加する。
- **W — スペルシーフ：** 敵のサモナースペルと発動効果アイテムのかけらを拾って1回使用できる。サモナースペルを使用するごとに最大3つの魔法の弾を最も近くにいる対象に向かって飛ばす。
- **E — スリープバブル：** 対象に眠気を与えてから眠らせる。眠っている間は、対象の魔法防御が低下する。眠りを覚ます攻撃は2倍のダメージを与える(上限あり)。
- **R — ポータルジャンプ：** 近くの指定した位置に1秒間ブリンクして、もとの位置に戻る。

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
- **対象試合：** 137試合、全体勝率 55.5%
- **時間帯別勝率：** 〜20分 63.6%（n=22）、20〜25分 47.4%（n=19）、25〜30分 51.9%（n=27）、30〜35分 56.2%（n=32）、35分〜 56.8%（n=37）
- **最高帯：** 〜20分（判定差 16.3ポイント）
- **判定根拠：** 5つの時間帯を比較できるが、最高帯と端点の差が8ポイント未満、または勝率が非単調だった。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-142|ゾーイの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### MIDDLE（232試合）

- **実測ビルド候補：** シャドウフレイム + ルーデン エコー（該当n=102、56.9% / 非該当50.0%、差+6.9pt）；連呪使いのブーツ + シャドウフレイム（該当n=76、56.6% / 非該当51.3%、差+5.3pt）
- **ステータス傾向：** 物理防御（該当n=33、66.7% / 非該当50.8%、差+15.9pt）；体力（該当n=164、55.5% / 非該当47.1%、差+8.4pt）
- **理論仮説：** アークエンジェル スタッフ + セラフ エンブレイス（未観測；共通stats: 魔力・マナ／チャンピオン原典にも言及: マナ）；アークエンジェル スタッフ + ルーデン エコー（未観測；共通stats: 魔力・マナ／チャンピオン原典にも言及: マナ）

### UTILITY（39試合）

- **実測ビルド候補：** 該当・非該当が各30試合以上で正の差を持つ候補なし。
- **ステータス傾向：** 該当・非該当が各30試合以上で正の差を持つ群なし。
- **理論仮説：** ソラリのロケット + アビサル マスク（未観測；共通stats: 体力・魔法防御／チャンピオン原典にも言及: 魔法防御）；黒炎のトーチ + ルーデン エコー（未観測；共通stats: 魔力・マナ／チャンピオン原典にも言及: マナ）

<!-- champion-build-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Zoe` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Zoe.png)
