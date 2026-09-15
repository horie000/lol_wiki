---
title: "ナー"
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
  - "[[wiki/sources/src-2026-09-15-riot-ranked-match-champion-rune-selection]]"
tags:
  - champion
  - role-fighter
  - role-tank
  - data-dragon
champion_id: "Gnar"
champion_key: "150"
data_version: "16.18.1"
roles:
  - "Fighter"
  - "Tank"
resource_type: "怒り"
image_path: "raw/assets/champions/Gnar.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Gnar.png"
---

# ナー

![[raw/assets/champions/Gnar.png|128]]

## 基本情報

- **英字ID：** `Gnar`
- **キー：** `150`
- **称号：** ミッシングリンク
- **データversion：** `16.18.1`

## 紹介

ナーは原始時代のヨードルで、おどけて悪ふざけをしていたかと思えば、あっという間にそれが幼児の怒りとなって爆発し、巨大な破壊の野獣に変身する。真なる氷に何千年間も閉じ込められていた彼にとって、一変した世界は見たこともないような不思議でいっぱいだ。彼は自分の骨牙のブーメランであろうが近くにあった建物であろうが、手当たり次第に敵に向かって投げつけては危険な状況を楽しんでいる。

## 分類

- **役割タグ：** `Fighter`、`Tank`
- **リソース種別：** 怒り

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 6 |
| `defense` | 5 |
| `magic` | 5 |
| `difficulty` | 8 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 540 |
| `hpperlevel` | 79 |
| `mp` | 100 |
| `mpperlevel` | 0 |
| `movespeed` | 335 |
| `armor` | 32 |
| `armorperlevel` | 3.7 |
| `spellblock` | 30 |
| `spellblockperlevel` | 1.3 |
| `attackrange` | 175 |
| `hpregen` | 4.5 |
| `hpregenperlevel` | 1.25 |
| `mpregen` | 0 |
| `mpregenperlevel` | 0 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 60 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 6 |
| `attackspeed` | 0.625 |

## アビリティ

- **パッシブ — ぷんすこ：** ナーは戦闘中に「怒り」が溜まっていく。「怒り」が最大の状態でスキルを使用するとメガナーに変身し、ステータスとスキルが変化する。

- **Q — ブーメラン/ぽいっ：** ナーが投げるブーメランは、命中した敵にダメージとスロウ効果を与える。戻ってきたブーメランをキャッチすると、クールダウンが短縮される。 メガナーは、ブーメランのかわりに岩石を投げる。敵に命中するとその場に落下して、付近の敵すべてにダメージとスロウ効果を与える。落ちた岩石を拾うとクールダウンが短縮される。
- **W — ごきげん/こてんぱん：** ナーが通常攻撃とスキルで相手にマークをつけるようになる。マークがたまった敵を攻撃するとナーは興奮し、追加ダメージを与えて移動速度が増加する。 メガナーは興奮を通りこし、怒りが爆発する。片腕を目の前におもいきり振り下ろし、範囲内の敵ユニットにダメージを与えてスタン効果を付与する。
- **E — ぴょんぴょん/ドーン！：** ナーがジャンプする。ユニットの上に着地すると、頭の上をはねてさらに遠くまでジャンプする。 メガナーは体が大きすぎて弾まない。そのかわり、着地するときに体をたたきつけて衝撃波をうみだし、周囲の敵にダメージを与える。着地地点にいる敵にはスロウ効果を与える。
- **R — ナー！：** メガナーが周りのモノを根こそぎ指定方向へ投げ、命中した敵にダメージとスロウ効果を与える。投げられた敵が壁にぶつかるとスタン状態になり、追加ダメージを受ける。

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
- **対象試合：** 85試合、全体勝率 42.4%
- **時間帯別勝率：** 〜20分 64.3%（n=14）、20〜25分 33.3%（n=9）、25〜30分 36.4%（n=22）、30〜35分 40.0%（n=20）、35分〜 40.0%（n=20）
- **最高帯：** 〜20分（判定差 —）
- **判定根拠：** 5つの時間帯のいずれかで15試合未満のため、時間帯の比較を保留する。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-150|ナーの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### TOP（192試合）

- **実測ビルド候補：** [[wiki/entities/items/item-3071|ブラック クリーバー]] + [[wiki/entities/items/item-3078|トリニティ フォース]]（該当n=95、56.8% / 非該当38.1%、差+18.7pt）；[[wiki/entities/items/item-3053|ステラックの篭手]] + [[wiki/entities/items/item-3071|ブラック クリーバー]] + [[wiki/entities/items/item-3078|トリニティ フォース]]（該当n=33、57.6% / 非該当45.3%、差+12.3pt）
- **ステータス傾向：** 物理防御（該当n=137、47.4% / 非該当47.3%、差+0.2pt）
- **理論仮説：** [[wiki/entities/items/item-3087|スタティック シヴ]] + [[wiki/entities/items/item-6672|クラーケン スレイヤー]]（未観測；共通stats: 攻撃力・攻撃速度・移動速度／チャンピオン原典にも言及: 攻撃力・移動速度）；[[wiki/entities/items/item-3087|スタティック シヴ]] + [[wiki/entities/items/item-3181|ハルブレイカー]]（未観測；共通stats: 攻撃力・移動速度／チャンピオン原典にも言及: 攻撃力・移動速度）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-150|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### TOP（対象n=285）

- **高勝率コンボ候補（最大3件）：**
  - [[wiki/entities/champions/nautilus|ノーチラス（Nautilus）]] — 対象側勝率78.9%（15/19）、サンプル不足（n=19、十分性の目安30未満）。
  - [[wiki/entities/champions/jhin|ジン（Jhin）]] — 対象側勝率72.0%（18/25）、サンプル不足（n=25、十分性の目安30未満）。
  - [[wiki/entities/champions/ezreal|エズリアル（Ezreal）]] — 対象側勝率66.7%（12/18）、サンプル不足（n=18、十分性の目安30未満）。
- **低勝率カウンターピック候補（最大3件）：**
  - [[wiki/entities/champions/malphite|マルファイト（Malphite）]] — 対象側勝率35.3%（6/17）、サンプル不足（n=17、十分性の目安30未満）。
  - [[wiki/entities/champions/mordekaiser|モルデカイザー（Mordekaiser）]] — 対象側勝率46.7%（7/15）、サンプル不足（n=15、十分性の目安30未満）。
  - [[wiki/entities/champions/k-sante|カ・サンテ（KSante）]] — 対象側勝率57.1%（12/21）、サンプル不足（n=21、十分性の目安30未満）。

### BOTTOM（対象n=2）

- **高勝率コンボ候補（最大3件）：** n=15以上の味方組み合わせなし。サンプル不足のため判断保留。
- **低勝率カウンターピック候補（最大3件）：** n=15以上の同ロール対面なし。サンプル不足のため判断保留。

> [!warning] 実測値の限界
> 味方ペアは同一試合・同一チームで同時に出場した組み合わせ、対面はMatch-v5の最終ロールから推定した同ロール候補である。パッチ、観測ランク帯、プレイヤー、試合展開、構成の交絡を調整していない。とくにサンプル不足の行は探索的な参考値に留める。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-matchups]]、[[wiki/syntheses/champion-combo-counter-ranked-matches|実測コンボ・カウンターピック分析]]
<!-- champion-matchup-analysis:end -->

<!-- champion-rune-set-analysis:start -->
## よく選ばれるルーンセット（実測）

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合20,010件、[[reports/riot-ranked-match-analysis/run-20260915T103154Z/report|ルーンセットの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-rune-selection|Riotランク戦試合データ：チャンピオン別ルーン選択]]、[[wiki/syntheses/champion-rune-selection-ranked-matches|実測チャンピオン別ルーン選択分析]]。
- **読み方：** 主系・キーストーン・主系3枠・副系2枠・3シャードが完全一致する組み合わせを、同じチャンピオン・正規化ロールの参加者を分母に集計した。選択時勝率は記述統計であり、因果効果や推奨を示さない。

### TOP（対象402試合、全体勝率51.5%）

| 順位 | 完全ルーンセット | 選択数 | 選択率 | 選択時勝率 |
| ---: | --- | ---: | ---: | ---: |
| 1 | 主系栄華：フリートフットワーク／凱旋・レジェンド: 迅速・背水の陣；副系不滅：ボーンアーマー・超成長；シャードUNKNOWN(5005)・UNKNOWN(5008)・UNKNOWN(5001) | 109/402 | 27.1% | 50.5% |
| 2 | 主系不滅：不死者の握撃／打ちこわし・ボーンアーマー・超成長；副系栄華：レジェンド: 迅速・凱旋；シャードUNKNOWN(5005)・UNKNOWN(5008)・UNKNOWN(5001) | 31/402 | 7.7% | 58.1% |
| 3 | 主系栄華：リーサルテンポ／凱旋・レジェンド: 迅速・背水の陣；副系不滅：ボーンアーマー・超成長；シャードUNKNOWN(5005)・UNKNOWN(5008)・UNKNOWN(5001) | 26/402 | 6.5% | 38.5% |

- **選定ロール：** チャンピオン・ロール別の完全試合数が最も多いロールを1つ選んだ。別ロールや全候補は詳細レポートで確認できる。
- **シャード表示：** Data Dragonで表示名を解決できない場合は`UNKNOWN(<ID>)`としてIDを保持する。

- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-rune-selection|Riotランク戦試合データ：チャンピオン別ルーン選択]]、[[wiki/syntheses/champion-rune-selection-ranked-matches|実測チャンピオン別ルーン選択分析]]。
<!-- champion-rune-set-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Gnar` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Gnar.png)
