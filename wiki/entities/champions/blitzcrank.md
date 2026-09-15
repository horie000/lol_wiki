---
title: "ブリッツクランク"
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
champion_id: "Blitzcrank"
champion_key: "53"
data_version: "16.18.1"
roles:
  - "Tank"
  - "Support"
resource_type: "マナ"
image_path: "raw/assets/champions/Blitzcrank.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Blitzcrank.png"
---

# ブリッツクランク

![[raw/assets/champions/Blitzcrank.png|128]]

## 基本情報

- **英字ID：** `Blitzcrank`
- **キー：** `53`
- **称号：** 偉大なるスチームゴーレム
- **データversion：** `16.18.1`

## 紹介

ブリッツクランクはゾウンからやってきた、ほぼ破壊不能な巨大ロボットだ。もともとは危険な廃棄物を処理するために造られたが、その目的には制約が多過ぎると感じた彼は「下層」で苦しんでいる人々を助けるために自らの体を改造した。ブリッツクランクは他者を守るため、危険も省みずにパワーと耐久力を活かした優しい鉄の拳を差し出したり、エネルギーを放出したりして悪者たちをこらしめている。

## 分類

- **役割タグ：** `Tank`、`Support`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 4 |
| `defense` | 8 |
| `magic` | 5 |
| `difficulty` | 4 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 600 |
| `hpperlevel` | 109 |
| `mp` | 267 |
| `mpperlevel` | 40 |
| `movespeed` | 325 |
| `armor` | 37 |
| `armorperlevel` | 4.7 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 125 |
| `hpregen` | 7.5 |
| `hpregenperlevel` | 0.75 |
| `mpregen` | 8.5 |
| `mpregenperlevel` | 0.8 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 62 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 1.13 |
| `attackspeed` | 0.625 |

## アビリティ

- **パッシブ — マナバリア：** 体力が低下すると、マナの量に応じたシールドを獲得する。

- **Q — ロケットグラブ：** 指定方向に右手を発射する。最初に触れた敵ユニットを掴んでダメージを与え、スタン効果を付与して自身のそばに引き寄せる。
- **W — オーバードライブ：** エネルギーをスーパーチャージして、移動速度と攻撃速度を大幅に上げる。効果終了後、エネルギーが切れて一時的にスロウ状態になる。
- **E — パワーフィスト：** 拳にエネルギーを充填して次の通常攻撃のダメージを2倍にし、対象をノックアップする。
- **R — イナズマフィールド：** 通常攻撃した敵にマークを付け、1秒後に電撃のダメージを与える。また、発動すると周囲の敵ユニットのシールドを消滅させ、ダメージを与えて短時間のサイレンス効果を与える。

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
- **対象試合：** 342試合、全体勝率 55.8%
- **時間帯別勝率：** 〜20分 49.1%（n=53）、20〜25分 58.2%（n=55）、25〜30分 62.3%（n=77）、30〜35分 54.0%（n=87）、35分〜 54.3%（n=70）
- **最高帯：** 25〜30分（判定差 8.1ポイント）
- **判定根拠：** 中間帯が最高、端点との差 8.1%
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-53|ブリッツクランクの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### UTILITY（625試合）

- **実測ビルド候補：** [[wiki/entities/items/item-3170|スイフトマーチ]] + [[wiki/entities/items/item-3190|ソラリのロケット]]（該当n=36、69.4% / 非該当49.1%、差+20.4pt）；[[wiki/entities/items/item-3075|ソーンメイル]] + [[wiki/entities/items/item-3190|ソラリのロケット]]（該当n=30、66.7% / 非該当49.4%、差+17.3pt）
- **ステータス傾向：** 物理防御（該当n=532、52.4% / 非該当37.6%、差+14.8pt）；魔法防御（該当n=506、52.6% / 非該当40.3%、差+12.2pt）
- **理論仮説：** [[wiki/entities/items/item-3002|先人の道標]] + [[wiki/entities/items/item-3742|デッド マン プレート]]（未観測；共通stats: 物理防御・体力・移動速度／チャンピオン原典にも言及: 体力・移動速度）；[[wiki/entities/items/item-3742|デッド マン プレート]] + [[wiki/entities/items/item-4401|自然の力]]（n=1（15未満）；共通stats: 体力・移動速度／チャンピオン原典にも言及: 体力・移動速度）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-53|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### UTILITY（対象n=806）

- **高勝率コンボ候補：** [[wiki/entities/champions/draven|ドレイヴン（Draven）]] — 対象側勝率65.9%（27/41）、n=41（十分性の目安を満たす）。
- **カウンターピック候補：** [[wiki/entities/champions/leona|レオナ（Leona）]] — 対象側勝率45.1%（32/71）、n=71（十分性の目安を満たす）。

### JUNGLE（対象n=1）

- **高勝率コンボ候補：** n=15以上の味方組み合わせなし。サンプル不足のため判断保留。
- **カウンターピック候補：** n=15以上の同ロール対面なし。サンプル不足のため判断保留。

> [!warning] 実測値の限界
> 味方ペアは同一試合・同一チームで同時に出場した組み合わせ、対面はMatch-v5の最終ロールから推定した同ロール候補である。パッチ、観測ランク帯、プレイヤー、試合展開、構成の交絡を調整していない。とくにサンプル不足の行は探索的な参考値に留める。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-matchups]]、[[wiki/syntheses/champion-combo-counter-ranked-matches|実測コンボ・カウンターピック分析]]
<!-- champion-matchup-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Blitzcrank` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Blitzcrank.png)
