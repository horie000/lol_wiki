---
title: "ザック"
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
tags:
  - champion
  - role-tank
  - role-fighter
  - data-dragon
champion_id: "Zac"
champion_key: "154"
data_version: "16.18.1"
roles:
  - "Tank"
  - "Fighter"
resource_type: "なし"
image_path: "raw/assets/champions/Zac.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Zac.png"
---

# ザック

![[raw/assets/champions/Zac.png|128]]

## 基本情報

- **英字ID：** `Zac`
- **キー：** `154`
- **称号：** 親愛なる秘密兵器
- **データversion：** `16.18.1`

## 紹介

ケミテック層を流れ、ゾウンの汚水地区の奥深く、ぽつんと隔離された大空洞に溜まった有毒液の池。その澱みの中で、ザックは覚醒した。そんな哀れな出自でありながらも、ザックは原始的な粘体生物から思考する存在へと成長を遂げ、都市のパイプの中に潜んで暮らし、時には助けが必要な者を助けるために飛び出したり、ゾウンの破損したインフラを修理するのである。

## 分類

- **役割タグ：** `Tank`、`Fighter`
- **リソース種別：** なし

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 3 |
| `defense` | 7 |
| `magic` | 7 |
| `difficulty` | 8 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 685 |
| `hpperlevel` | 109 |
| `mp` | 0 |
| `mpperlevel` | 0 |
| `movespeed` | 340 |
| `armor` | 33 |
| `armorperlevel` | 5.2 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 175 |
| `hpregen` | 5 |
| `hpregenperlevel` | 0.5 |
| `mpregen` | 0 |
| `mpregenperlevel` | 0 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 60 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 1.6 |
| `attackspeed` | 0.736 |

## アビリティ

- **パッシブ — はぐれスライム：** スキルによる攻撃を命中させるたびスライムが飛び散り、回収すると体力が回復する。致命的なダメージを受けた場合、ザックは4体のスライムに分裂する。その後数秒かけて再融合し、この時に生き残っていたスライムの体力に応じた体力で復活する。各スライムはザックの最大体力、物理防御、魔法防御の数パーセントに相当するステータスを持つ。ザックは一度分裂すると、ふたたび分裂するために5分間のクールダウンが必要になる。

- **Q — スライムパンチ：** 片手を伸ばして敵ユニットを掴む。別の敵ユニットを攻撃すると両者を互いにぶつけ合わせる。
- **W — スライムクラッシュ：** 体を爆発させることで近くの敵に向かって突進し、最大体力の一定割合を魔法ダメージとして与える。
- **E — ブッ飛びスライム：** ザックが両手をついて反発力を溜め込み、対象に勢いよく飛びかかる。
- **R — レッツバウンス！：** 4回バウンドし、命中した敵をノックアップさせてスロウ状態にする。

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
- **対象試合：** 94試合、全体勝率 47.9%
- **時間帯別勝率：** 〜20分 42.1%（n=19）、20〜25分 46.2%（n=13）、25〜30分 50.0%（n=22）、30〜35分 57.1%（n=21）、35分〜 42.1%（n=19）
- **最高帯：** 30〜35分（判定差 不明）
- **判定根拠：** 全5帯で各15試合未満の帯がある。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-154|ザックの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### JUNGLE（202試合）

- **実測ビルド候補：** [[wiki/entities/items/item-3065|スピリット ビサージュ]] + [[wiki/entities/items/item-3075|ソーンメイル]]（該当n=43、67.4% / 非該当49.1%、差+18.4pt）；[[wiki/entities/items/item-3065|スピリット ビサージュ]] + [[wiki/entities/items/item-3068|サンファイア イージス]] + [[wiki/entities/items/item-3075|ソーンメイル]]（該当n=41、65.9% / 非該当49.7%、差+16.2pt）
- **ステータス傾向：** 魔力（該当n=122、58.2% / 非該当45.0%、差+13.2pt）；魔法防御（該当n=147、55.8% / 非該当45.5%、差+10.3pt）
- **理論仮説：** [[wiki/entities/items/item-3050|ジーク コンバージェンス]] + [[wiki/entities/items/item-6665|変幻自在のジャック＝ショー]]（未観測；共通stats: 物理防御・体力・魔法防御／チャンピオン原典にも言及: 物理防御・体力・魔法防御）；[[wiki/entities/items/item-2524|バンドルパイプ]] + [[wiki/entities/items/item-3050|ジーク コンバージェンス]]（未観測；共通stats: 物理防御・体力・魔法防御／チャンピオン原典にも言及: 物理防御・体力・魔法防御）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-154|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### JUNGLE（対象n=305）

- **高勝率コンボ候補（最大3件）：**
  - [[wiki/entities/champions/leona|レオナ（Leona）]] — 対象側勝率64.5%（20/31）、n=31（十分性の目安を満たす）。
- **低勝率カウンターピック候補（最大3件）：**
  - [[wiki/entities/champions/viego|ヴィエゴ（Viego）]] — 対象側勝率55.6%（10/18）、サンプル不足（n=18、十分性の目安30未満）。

### TOP（対象n=45）

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

### JUNGLE（対象136試合、全体勝率52.9%）

| 順位 | 完全ルーンセット | 選択数 | 選択率 | 選択時勝率 |
| ---: | --- | ---: | ---: | ---: |
| 1 | 主系栄華：征服者／凱旋・レジェンド: ヘイスト・背水の陣；副系天啓：宇宙の英知・魔法の靴；シャードUNKNOWN(5007)・UNKNOWN(5008)・UNKNOWN(5001) | 40/136 | 29.4% | 52.5% |
| 2 | 主系不滅：アフターショック／生命の泉・心身調整・生気付与；副系栄華：レジェンド: ヘイスト・凱旋；シャードUNKNOWN(5007)・UNKNOWN(5008)・UNKNOWN(5001) | 24/136 | 17.6% | 62.5% |
| 3 | 主系栄華：征服者／凱旋・レジェンド: ヘイスト・背水の陣；副系天啓：キャッシュバック・トリプル トニック；シャードUNKNOWN(5007)・UNKNOWN(5001)・UNKNOWN(5013) | 10/136 | 7.4% | 30.0% |

- **選定ロール：** チャンピオン・ロール別の完全試合数が最も多いロールを1つ選んだ。別ロールや全候補は詳細レポートで確認できる。
- **シャード表示：** Data Dragonで表示名を解決できない場合は`UNKNOWN(<ID>)`としてIDを保持する。

- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-rune-selection|Riotランク戦試合データ：チャンピオン別ルーン選択]]、[[wiki/syntheses/champion-rune-selection-ranked-matches|実測チャンピオン別ルーン選択分析]]。
<!-- champion-rune-set-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Zac` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Zac.png)
