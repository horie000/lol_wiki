---
title: "ブラウム"
type: entity
status: active
created: 2026-09-14
updated: 2026-09-15
sources:
  - "[[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]]"
  - "[[wiki/sources/src-2026-09-14-dragontail-16-18-1]]"
  - "[[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]"
  - "[[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis]]"
  - "[[wiki/sources/src-2026-09-15-riot-ranked-match-champion-matchups]]"
tags:
  - champion
  - role-tank
  - role-support
  - data-dragon
champion_id: "Braum"
champion_key: "201"
data_version: "16.18.1"
roles:
  - "Tank"
  - "Support"
resource_type: "マナ"
image_path: "raw/assets/champions/Braum.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Braum.png"
---

# ブラウム

![[raw/assets/champions/Braum.png|128]]

## 基本情報

- **英字ID：** `Braum`
- **キー：** `201`
- **称号：** フレヨルドの漢気
- **データversion：** `16.18.1`

## 紹介

巨大な筋肉が盛り上がる腕と、その筋肉よりも大きな優しい心を持つブラウムは、フレヨルドの誰もが愛する英雄だ。フロストヘルドの北の酒場では、一晩でオークの森を伐採した話や、パンチで山が崩れ去った話など、誰もが彼の怪力伝説に花を咲かせて酒を飲む。魔法の力を宿した宝物庫の扉を盾にして、その筋肉にも負けぬ立派な口ひげで微笑みながら凍てつく北部を歩き回る彼は、助けを必要とする者にとって最高に頼りになる存在だ。

## 分類

- **役割タグ：** `Tank`、`Support`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 3 |
| `defense` | 9 |
| `magic` | 4 |
| `difficulty` | 3 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 610 |
| `hpperlevel` | 112 |
| `mp` | 311 |
| `mpperlevel` | 45 |
| `movespeed` | 335 |
| `armor` | 35 |
| `armorperlevel` | 5 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 125 |
| `hpregen` | 8.5 |
| `hpregenperlevel` | 1 |
| `mpregen` | 7 |
| `mpregenperlevel` | 0.8 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 55 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 3.5 |
| `attackspeed` | 0.644 |

## アビリティ

- **パッシブ — 漢の拳：** 通常攻撃を命中させると「漢の拳」がスタックする。スタックが1つ以上ある敵には、味方の通常攻撃でも効果がスタックする。 スタックが4つ溜まると対象はスタン状態になり、魔法ダメージを受ける。スタン状態になった敵はその後、数秒間はスタックが増加しない。ただしブラウムの攻撃が命中すると追加魔法ダメージを受ける。

- **Q — 冬の凍瘡：** 盾から氷塊を発射し、最初に命中した敵ユニットに魔法ダメージとスロウ効果を与える。 命中した敵には「漢の拳」がスタックする。
- **W — ワシに任せとけ！：** 指定した味方チャンピオンまたはミニオンのもとへ跳躍する。付近に敵チャンピオンがいた場合、対象と敵チャンピオンの間に着地する。着地したあと、自身と対象の物理防御と魔法防御を数秒間増加させる。
- **E — 不破の盾：** 指定方向に巨大な盾を掲げ、数秒間すべての遠距離攻撃を体を張って食い止める。盾を構えている間は移動速度が増加し、最初に盾に当たった攻撃のダメージを無効化する。盾を構えている間、同方向から来る攻撃のダメージを軽減する。
- **R — 氷河の裂溝：** 盾を地面にたたきつけて指定方向に地割れを起こし、周囲にいる敵と地割れのライン上にいる敵をノックアップさせる。 地割れは短時間持続し、範囲内に入った敵にスロウ効果を付与する。

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
- **対象試合：** 208試合、全体勝率 48.1%
- **時間帯別勝率：** 〜20分 33.3%（n=36）、20〜25分 51.4%（n=37）、25〜30分 51.0%（n=51）、30〜35分 50.0%（n=46）、35分〜 52.6%（n=38）
- **最高帯：** 35分〜（判定差 19.3ポイント）
- **判定根拠：** 35分〜が最高、短時間帯との差 19.3%
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-201|ブラウムの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### UTILITY（563試合）

- **実測ビルド候補：** [[wiki/entities/items/item-2524|バンドルパイプ]] + [[wiki/entities/items/item-3190|ソラリのロケット]]（該当n=116、62.1% / 非該当47.2%、差+14.9pt）；[[wiki/entities/items/item-2524|バンドルパイプ]] + [[wiki/entities/items/item-3109|騎士の誓い]]（該当n=69、62.3% / 非該当48.6%、差+13.7pt）
- **ステータス傾向：** 魔力（該当n=47、53.2% / 非該当50.0%、差+3.2pt）
- **理論仮説：** [[wiki/entities/items/item-3190|ソラリのロケット]] + [[wiki/entities/items/item-6665|変幻自在のジャック＝ショー]]（n=1（15未満）；共通stats: 物理防御・体力・魔法防御／チャンピオン原典にも言及: 物理防御・魔法防御）；[[wiki/entities/items/item-2524|バンドルパイプ]] + [[wiki/entities/items/item-3050|ジーク コンバージェンス]]（n=1（15未満）；共通stats: 物理防御・体力・魔法防御／チャンピオン原典にも言及: 物理防御・魔法防御）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-201|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### UTILITY（対象n=816）

- **高勝率コンボ候補：** [[wiki/entities/champions/jhin|ジン（Jhin）]] — 対象側勝率71.4%（25/35）、n=35（十分性の目安を満たす）。
- **カウンターピック候補：** [[wiki/entities/champions/morgana|モルガナ（Morgana）]] — 対象側勝率37.5%（12/32）、n=32（十分性の目安を満たす）。

> [!warning] 実測値の限界
> 味方ペアは同一試合・同一チームで同時に出場した組み合わせ、対面はMatch-v5の最終ロールから推定した同ロール候補である。パッチ、観測ランク帯、プレイヤー、試合展開、構成の交絡を調整していない。とくにサンプル不足の行は探索的な参考値に留める。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-matchups]]、[[wiki/syntheses/champion-combo-counter-ranked-matches|実測コンボ・カウンターピック分析]]
<!-- champion-matchup-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Braum` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Braum.png)
