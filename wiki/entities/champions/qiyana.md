---
title: "キヤナ"
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
  - role-assassin
  - data-dragon
champion_id: "Qiyana"
champion_key: "246"
data_version: "16.18.1"
roles:
  - "Assassin"
resource_type: "マナ"
image_path: "raw/assets/champions/Qiyana.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Qiyana.png"
---

# キヤナ

![[raw/assets/champions/Qiyana.png|128]]

## 基本情報

- **英字ID：** `Qiyana`
- **キー：** `246`
- **称号：** エレメントの女帝
- **データversion：** `16.18.1`

## 紹介

ジャングルに囲まれた都市イシャオカンで、キヤナは玉座ユン・タルを目指して無情な策略を企てている。両親の王位を継承する権利からは遠い末娘として生まれたキヤナだが、過剰なまでの自信とエレメント魔法の無類の力をもって、己の道を邪魔する者に立ち向かう。意のままに大地を操ることができる彼女は、イシャオカン史上最高のエレメント魔法の使い手であると自負している──そしてそんな自分はひとつの都市のみならず、帝国を支配するにふさわしい者であると。

## 分類

- **役割タグ：** `Assassin`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 0 |
| `defense` | 2 |
| `magic` | 4 |
| `difficulty` | 8 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 590 |
| `hpperlevel` | 115 |
| `mp` | 375 |
| `mpperlevel` | 60 |
| `movespeed` | 335 |
| `armor` | 31 |
| `armorperlevel` | 4.5 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 150 |
| `hpregen` | 8 |
| `hpregenperlevel` | 0.9 |
| `mpregen` | 8 |
| `mpregenperlevel` | 0.7 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 64 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2.1 |
| `attackspeed` | 0.688 |

## アビリティ

- **パッシブ — 女帝の威風：** それぞれの敵に対する最初の通常攻撃またはスキルに追加ダメージが付与される。

- **Q — エレメントの怒り/イシュタルの切先：** 武器を振り、保持しているエレメントに応じた追加効果の付いたダメージを与える。
- **W — 大地の力：** 目標地点までダッシュし、武器にエレメントの力を付与する。武器にエレメントの力がついている間は、通常攻撃とスキルに追加ダメージが付与される。
- **E — 俊烈：** 敵に向かってダッシュし、ダメージを与える。
- **R — 天賦絢爛：** エレメントに命中すると爆発する衝撃波を放ち、周囲の敵をスタンさせながらダメージを与える。

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
- **対象試合：** 78試合、全体勝率 38.5%
- **時間帯別勝率：** 〜20分 40.0%（n=10）、20〜25分 50.0%（n=12）、25〜30分 28.6%（n=21）、30〜35分 22.2%（n=18）、35分〜 58.8%（n=17）
- **最高帯：** 35分〜（判定差 不明）
- **判定根拠：** 全5帯で各15試合未満の帯がある。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-246|キヤナの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### MIDDLE（117試合）

- **実測ビルド候補：** [[wiki/entities/items/item-6694|セリルダの怨恨]] + [[wiki/entities/items/item-6698|プロフェイン ハイドラ]]（該当n=35、62.9% / 非該当34.1%、差+28.7pt）；[[wiki/entities/items/item-3171|真紅のアイオニア ブーツ]] + [[wiki/entities/items/item-6698|プロフェイン ハイドラ]]（該当n=30、43.3% / 非該当42.5%、差+0.8pt）
- **ステータス傾向：** 該当・非該当が各30試合以上で正の差を持つ群なし。
- **理論仮説：** [[wiki/entities/items/item-3161|ショウジンの矛]] + [[wiki/entities/items/item-3814|ナイト エッジ]]（n=1（15未満）；共通stats: 攻撃力・体力／チャンピオン原典にも言及: 攻撃力）；[[wiki/entities/items/item-3814|ナイト エッジ]] + [[wiki/entities/items/item-6609|ケミパンク チェーンソード]]（n=1（15未満）；共通stats: 攻撃力・体力／チャンピオン原典にも言及: 攻撃力）

### JUNGLE（90試合）

- **実測ビルド候補：** 該当・非該当が各30試合以上で正の差を持つ候補なし。
- **ステータス傾向：** 体力（該当n=43、51.2% / 非該当36.2%、差+15.0pt）
- **理論仮説：** [[wiki/entities/items/item-3026|ガーディアン エンジェル]] + [[wiki/entities/items/item-6333|デス ダンス]]（未観測；共通stats: 物理防御・攻撃力／チャンピオン原典にも言及: 攻撃力）；[[wiki/entities/items/item-3071|ブラック クリーバー]] + [[wiki/entities/items/item-3814|ナイト エッジ]]（未観測；共通stats: 攻撃力・体力／チャンピオン原典にも言及: 攻撃力）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-246|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### MIDDLE（対象n=186）

- **高勝率コンボ候補（最大3件）：**
  - [[wiki/entities/champions/miss-fortune|ミス・フォーチュン（MissFortune）]] — 対象側勝率63.0%（17/27）、サンプル不足（n=27、十分性の目安30未満）。
  - [[wiki/entities/champions/ezreal|エズリアル（Ezreal）]] — 対象側勝率43.8%（7/16）、サンプル不足（n=16、十分性の目安30未満）。
- **低勝率カウンターピック候補（最大3件）：** n=15以上の同ロール対面なし。サンプル不足のため判断保留。

### JUNGLE（対象n=126）

- **高勝率コンボ候補（最大3件）：**
  - [[wiki/entities/champions/ashe|アッシュ（Ashe）]] — 対象側勝率41.2%（7/17）、サンプル不足（n=17、十分性の目安30未満）。
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

### JUNGLE（対象183試合、全体勝率48.1%）

| 順位 | 完全ルーンセット | 選択数 | 選択率 | 選択時勝率 |
| ---: | --- | ---: | ---: | ---: |
| 1 | 主系天啓：ファーストストライク／キャッシュバック・トリプル トニック・宇宙の英知；副系覇道：サドンインパクト・貪欲な賞金首狩り；シャードUNKNOWN(5008)・UNKNOWN(5008)・UNKNOWN(5011) | 39/183 | 21.3% | 56.4% |
| 2 | 主系天啓：ファーストストライク／魔法の靴・トリプル トニック・宇宙の英知；副系覇道：サドンインパクト・至極の賞金首狩り；シャードUNKNOWN(5008)・UNKNOWN(5008)・UNKNOWN(5001) | 37/183 | 20.2% | 45.9% |
| 3 | 主系天啓：ファーストストライク／キャッシュバック・トリプル トニック・宇宙の英知；副系覇道：サドンインパクト・至極の賞金首狩り；シャードUNKNOWN(5008)・UNKNOWN(5008)・UNKNOWN(5011) | 29/183 | 15.8% | 48.3% |

- **選定ロール：** チャンピオン・ロール別の完全試合数が最も多いロールを1つ選んだ。別ロールや全候補は詳細レポートで確認できる。
- **シャード表示：** Data Dragonで表示名を解決できない場合は`UNKNOWN(<ID>)`としてIDを保持する。

- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-rune-selection|Riotランク戦試合データ：チャンピオン別ルーン選択]]、[[wiki/syntheses/champion-rune-selection-ranked-matches|実測チャンピオン別ルーン選択分析]]。
<!-- champion-rune-set-analysis:end -->

<!-- champion-tier-analysis:start -->
## 観測ランク帯別チャンピオン候補

- **スナップショット：** 2026-09-16生成、キュー420、観測10帯、各1,000試合、統合後9,761試合、min-games 15、[[reports/riot-ranked-tier-analysis/run-20260916T083219Z/report|ランク帯別詳細レポート]]。
- **根拠：** [[wiki/sources/src-2026-09-16-riot-ranked-match-tier-analysis|Riotランク戦試合データ：観測ランク帯別特徴]]、[[wiki/syntheses/ranked-tier-characteristics|ランク帯別の試合特徴と全帯共通傾向]]。
- **読み方：** `observed_tier` はその試合を発見したプレイヤーの収集時点の所属帯であり、10人全員の試合時ランクではない。以下は各帯の上位選択と、min-games以上で機械的に抽出した高低勝率の探索候補で、推奨・因果効果・有意差を示さない。

### 低勝率候補（下位5）

| 観測帯 | 候補順位 | 試合数 | 勝敗 | 勝率 |
| --- | ---: | ---: | --- | ---: |
| BRONZE | 5 | 23 | 8勝/15敗 | 34.8% |

<!-- champion-tier-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Qiyana` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Qiyana.png)
