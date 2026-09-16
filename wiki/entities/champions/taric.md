---
title: "タリック"
type: entity
status: active
created: 2026-09-14
updated: 2026-09-16
sources:
  - "[[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]]"
  - "[[wiki/sources/src-2026-09-14-dragontail-16-18-1]]"
  - "[[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]"
  - "[[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis]]"
  - "[[wiki/sources/src-2026-09-15-riot-ranked-match-champion-matchups]]"
  - "[[wiki/sources/src-2026-09-15-riot-ranked-match-champion-rune-selection]]"
  - "[[wiki/sources/src-2026-09-16-riot-ranked-match-tier-analysis]]"
tags:
  - champion
  - role-support
  - role-tank
  - data-dragon
champion_id: "Taric"
champion_key: "44"
data_version: "16.18.1"
roles:
  - "Support"
  - "Tank"
resource_type: "マナ"
image_path: "raw/assets/champions/Taric.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Taric.png"
---

# タリック

![[raw/assets/champions/Taric.png|128]]

## 基本情報

- **英字ID：** `Taric`
- **キー：** `44`
- **称号：** ヴァロランの守護者
- **データversion：** `16.18.1`

## 紹介

タリックは守護の神髄であり、ルーンテラの生命、愛、美の守護者として驚異的な力を発揮する。軍務放棄の汚名を受けて故郷のデマーシアから放逐され、贖罪のために霊峰ターゴンに登ったタリックは、図らずも天上の存在からさらなる使命を与えられることとなった。いにしえのターゴンから力を授かったヴァロランの守護者は、密かに侵略を進めるヴォイドの穢れに対し揺るぎなき決意と共に立ち向かっている。

## 分類

- **役割タグ：** `Support`、`Tank`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 4 |
| `defense` | 8 |
| `magic` | 5 |
| `difficulty` | 3 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 645 |
| `hpperlevel` | 99 |
| `mp` | 300 |
| `mpperlevel` | 60 |
| `movespeed` | 340 |
| `armor` | 40 |
| `armorperlevel` | 4.3 |
| `spellblock` | 28 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 150 |
| `hpregen` | 6 |
| `hpregenperlevel` | 0.5 |
| `mpregen` | 8.5 |
| `mpregenperlevel` | 0.8 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 55 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2 |
| `attackspeed` | 0.625 |

## アビリティ

- **パッシブ — ブラバド：** スキル使用後の通常攻撃2回が素早くなり、追加魔法ダメージを付与する。さらに通常スキルのクールダウンを短縮する。

- **Q — スターライトタッチ：** 周囲の味方チャンピオンの体力をチャージ数に応じて回復する。ブラバド効果中に通常攻撃を行うと、「スターライトタッチ」のチャージを1つ獲得する。
- **W — バスティオン：** 自動効果: このスキルで繋がっている味方チャンピオンとタリックの物理防御が増加する。 発動効果: 指定した味方チャンピオンと繋がり、両者にシールドを付与するが、離れすぎると繋がりは一時的に消滅する。さらにタリックの全スキルは、繋がっている味方チャンピオンからも同様に発動される。
- **E — ダズル：** 魔法ダメージとスタン効果を持つ星のビームを構え、短い遅延の後に発動する。
- **R — コズミックレディアンス：** 発動から少しして宇宙のエナジーを放ち、自身の周囲の味方を数秒間、無敵状態にする。

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

- **スナップショット：** 2026-09-15生成、キュー420、完全試合4,672件、[[reports/riot-ranked-match-analysis/run-20260915T010911Z/report|詳細レポート]]。
- **観測分類：** 判定保留（分母不足）
- **対象試合：** 71試合、全体勝率 60.6%
- **時間帯別勝率：** 〜20分 40.0%（n=15）、20〜25分 56.2%（n=16）、25〜30分 76.9%（n=13）、30〜35分 60.0%（n=10）、35分〜 70.6%（n=17）
- **最高帯：** 25〜30分（判定差 不明）
- **判定根拠：** 全5帯で各15試合未満の帯がある。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-44|タリックの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### UTILITY（139試合）

- **実測ビルド候補：** [[wiki/entities/items/item-3121|フィンブルウィンター]] + [[wiki/entities/items/item-3190|ソラリのロケット]]（該当n=32、68.8% / 非該当52.3%、差+16.4pt）
- **ステータス傾向：** 該当・非該当が各30試合以上で正の差を持つ群なし。
- **理論仮説：** [[wiki/entities/items/item-2524|バンドルパイプ]] + [[wiki/entities/items/item-3190|ソラリのロケット]]（n=5（15未満）；共通stats: 物理防御・体力・魔法防御／チャンピオン原典にも言及: 物理防御・体力）；[[wiki/entities/items/item-3050|ジーク コンバージェンス]] + [[wiki/entities/items/item-3190|ソラリのロケット]]（n=2（15未満）；共通stats: 物理防御・体力・魔法防御／チャンピオン原典にも言及: 物理防御・体力）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-44|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### UTILITY（対象n=215）

- **高勝率コンボ候補（最大3件）：**
  - [[wiki/entities/champions/swain|スウェイン（Swain）]] — 対象側勝率66.7%（12/18）、サンプル不足（n=18、十分性の目安30未満）。
  - [[wiki/entities/champions/aatrox|エイトロックス（Aatrox）]] — 対象側勝率61.1%（11/18）、サンプル不足（n=18、十分性の目安30未満）。
  - [[wiki/entities/champions/master-yi|マスター・イー（MasterYi）]] — 対象側勝率55.6%（10/18）、サンプル不足（n=18、十分性の目安30未満）。
- **低勝率カウンターピック候補（最大3件）：**
  - [[wiki/entities/champions/leona|レオナ（Leona）]] — 対象側勝率51.6%（16/31）、n=31（十分性の目安を満たす）。

### JUNGLE（対象n=5）

- **高勝率コンボ候補（最大3件）：** n=15以上の味方組み合わせなし。サンプル不足のため判断保留。
- **低勝率カウンターピック候補（最大3件）：** n=15以上の同ロール対面なし。サンプル不足のため判断保留。

> [!warning] 実測値の限界
> 味方ペアは同一試合・同一チームで同時に出場した組み合わせ、対面はMatch-v5の最終ロールから推定した同ロール候補である。パッチ、観測ランク帯、プレイヤー、試合展開、構成の交絡を調整していない。とくにサンプル不足の行は探索的な参考値に留める。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-matchups]]、[[wiki/syntheses/champion-combo-counter-ranked-matches|実測コンボ・カウンターピック分析]]
<!-- champion-matchup-analysis:end -->

<!-- champion-rune-set-analysis:start -->
## よく選ばれるルーンセット（実測）

- **スナップショット：** 2026-09-16生成、キュー420、ユニーク試合10,000件、[[reports/riot-ranked-match-analysis/run-20260916T081004Z/report|ルーンセットの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-rune-selection|Riotランク戦試合データ：チャンピオン別ルーン選択]]、[[wiki/syntheses/champion-rune-selection-ranked-matches|実測チャンピオン別ルーン選択分析]]。
- **読み方：** 主系・キーストーン・主系3枠・副系2枠・3シャードが完全一致する組み合わせを、同じチャンピオン・正規化ロールの参加者を分母に集計した。選択時勝率は記述統計であり、因果効果や推奨を示さない。

### UTILITY（対象94試合、全体勝率56.4%）

| 順位 | 完全ルーンセット | 選択数 | 選択率 | 選択時勝率 |
| ---: | --- | ---: | ---: | ---: |
| 1 | 主系天啓：グレイシャルオーグメント／魔法の靴・ビスケットデリバリー・宇宙の英知；副系不滅：心身調整・生気付与；シャードUNKNOWN(5005)・UNKNOWN(5001)・UNKNOWN(5001) | 25/94 | 26.6% | 60.0% |
| 2 | 主系不滅：ガーディアン／生命の泉・ボーンアーマー・生気付与；副系栄華：レジェンド: ヘイスト・冷静沈着；シャードUNKNOWN(5005)・UNKNOWN(5001)・UNKNOWN(5001) | 13/94 | 13.8% | 69.2% |
| 3 | 主系天啓：グレイシャルオーグメント／魔法の靴・ビスケットデリバリー・宇宙の英知；副系栄華：レジェンド: ヘイスト・冷静沈着；シャードUNKNOWN(5005)・UNKNOWN(5001)・UNKNOWN(5001) | 6/94 | 6.4% | 50.0% |

- **選定ロール：** チャンピオン・ロール別の完全試合数が最も多いロールを1つ選んだ。別ロールや全候補は詳細レポートで確認できる。
- **シャード表示：** Data Dragonで表示名を解決できない場合は`UNKNOWN(<ID>)`としてIDを保持する。

- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-rune-selection|Riotランク戦試合データ：チャンピオン別ルーン選択]]、[[wiki/syntheses/champion-rune-selection-ranked-matches|実測チャンピオン別ルーン選択分析]]。
<!-- champion-rune-set-analysis:end -->

<!-- champion-tier-analysis:start -->
## 観測ランク帯別チャンピオン候補

- **スナップショット：** 2026-09-16生成、キュー420、観測10帯、各1,000試合、統合後9,761試合、min-games 15、[[reports/riot-ranked-tier-analysis/run-20260916T083219Z/report|ランク帯別詳細レポート]]。
- **根拠：** [[wiki/sources/src-2026-09-16-riot-ranked-match-tier-analysis|Riotランク戦試合データ：観測ランク帯別特徴]]、[[wiki/syntheses/ranked-tier-characteristics|ランク帯別の試合特徴と全帯共通傾向]]。
- **読み方：** `observed_tier` はその試合を発見したプレイヤーの収集時点の所属帯であり、10人全員の試合時ランクではない。以下は各帯の上位選択と、min-games以上で機械的に抽出した高低勝率の探索候補で、推奨・因果効果・有意差を示さない。

### 高勝率候補（上位5）

| 観測帯 | 候補順位 | 試合数 | 勝敗 | 勝率 |
| --- | ---: | ---: | --- | ---: |
| BRONZE | 1 | 15 | 12勝/3敗 | 80.0% |
| SILVER | 3 | 17 | 12勝/5敗 | 70.6% |

### 低勝率候補（下位5）

| 観測帯 | 候補順位 | 試合数 | 勝敗 | 勝率 |
| --- | ---: | ---: | --- | ---: |
| GRANDMASTER | 5 | 16 | 5勝/11敗 | 31.2% |

<!-- champion-tier-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Taric` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Taric.png)
