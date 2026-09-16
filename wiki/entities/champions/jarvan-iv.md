---
title: "ジャーヴァンⅣ"
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
  - role-fighter
  - role-tank
  - data-dragon
champion_id: "JarvanIV"
champion_key: "59"
data_version: "16.18.1"
roles:
  - "Fighter"
  - "Tank"
resource_type: "マナ"
image_path: "raw/assets/champions/JarvanIV.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/JarvanIV.png"
---

# ジャーヴァンⅣ

![[raw/assets/champions/JarvanIV.png|128]]

## 基本情報

- **英字ID：** `JarvanIV`
- **キー：** `59`
- **称号：** デマーシアの儀範
- **データversion：** `16.18.1`

## 紹介

ライトシールド王家の後継ぎであるジャーヴァン王子はデマーシアの王位継承者だ。母国の最大の美徳の鑑となるように育てられた彼は、寄せられる大きな期待に応えるために、最前線で戦いたいという自身の欲望を抑える必要がある。ジャーヴァンは恐れ知らずな勇敢さと自己を省みない強い決意で部隊を鼓舞し、王家の名誉にかけて未来の指導者たるべき力を示している。

## 分類

- **役割タグ：** `Fighter`、`Tank`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 6 |
| `defense` | 8 |
| `magic` | 3 |
| `difficulty` | 5 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 640 |
| `hpperlevel` | 104 |
| `mp` | 300 |
| `mpperlevel` | 55 |
| `movespeed` | 340 |
| `armor` | 36 |
| `armorperlevel` | 4.6 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 175 |
| `hpregen` | 8 |
| `hpregenperlevel` | 0.7 |
| `mpregen` | 6.5 |
| `mpregenperlevel` | 0.45 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 64 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2.5 |
| `attackspeed` | 0.658 |

## アビリティ

- **パッシブ — 武魂の律動：** 最初の通常攻撃が命中する際、対象の現在体力に応じた追加物理ダメージを与えるが、同一の敵に対しては数秒間に一度しか発動できない。

- **Q — ドラゴンストライク：** 槍を伸ばして貫通した敵ユニットに物理ダメージを与え、物理防御を低下させる。さらに「デマーシアの旗印」にこのスキルが命中した場合、自身をそこまで引き寄せ、通り道にいた敵をノックアップさせる。
- **W — ゴールデンイージス：** デマーシアの歴代王の力を借りて、ダメージを防ぐシールドを発生させ、周囲の敵にスロウを与える。
- **E — デマーシアの旗印：** デマーシアの誇りを胸に抱き、自動効果で攻撃速度が増加するようになる。発動すると指定地点にデマーシア軍の旗を投げ、地面に突き刺さると同時に魔法ダメージを与える。この旗は味方を鼓舞し、自身を含む味方チャンピオンの攻撃速度が、自動効果と同じ分だけ増加する。
- **R — 決戦場：** ジャーヴァンⅣが対象に向かって雄々しく跳躍して、物理ダメージを与える。着地と同時に猛烈な力で地面を踏みつけ、周囲の地形を変化させて対象を囲い込む。周囲の敵も着地時にダメージを受ける。

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
- **観測分類：** 終盤寄り
- **対象試合：** 253試合、全体勝率 48.2%
- **時間帯別勝率：** 〜20分 45.5%（n=44）、20〜25分 39.5%（n=38）、25〜30分 49.0%（n=51）、30〜35分 49.1%（n=55）、35分〜 53.8%（n=65）
- **最高帯：** 35分〜（判定差 8.4ポイント）
- **判定根拠：** 35分〜が最高、短時間帯との差 8.4%。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-59|ジャーヴァンⅣの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### JUNGLE（505試合）

- **実測ビルド候補：** [[wiki/entities/items/item-3065|スピリット ビサージュ]] + [[wiki/entities/items/item-6610|サンダード スカイ]]（該当n=39、71.8% / 非該当47.4%、差+24.4pt）；[[wiki/entities/items/item-3071|ブラック クリーバー]] + [[wiki/entities/items/item-3110|フローズン ハート]]（該当n=51、66.7% / 非該当47.4%、差+19.3pt）
- **ステータス傾向：** 魔法防御（該当n=215、56.3% / 非該当44.1%、差+12.1pt）；体力（該当n=425、50.8% / 非該当41.2%、差+9.6pt）
- **理論仮説：** [[wiki/entities/items/item-3050|ジーク コンバージェンス]] + [[wiki/entities/items/item-3190|ソラリのロケット]]（未観測；共通stats: 物理防御・体力・魔法防御／チャンピオン原典にも言及: 物理防御・体力）；[[wiki/entities/items/item-3050|ジーク コンバージェンス]] + [[wiki/entities/items/item-6665|変幻自在のジャック＝ショー]]（未観測；共通stats: 物理防御・体力・魔法防御／チャンピオン原典にも言及: 物理防御・体力）

### UTILITY（30試合）

- **実測ビルド候補：** 該当・非該当が各30試合以上で正の差を持つ候補なし。
- **ステータス傾向：** 該当・非該当が各30試合以上で正の差を持つ群なし。
- **理論仮説：** [[wiki/entities/items/item-3050|ジーク コンバージェンス]] + [[wiki/entities/items/item-3190|ソラリのロケット]]（n=2（15未満）；共通stats: 物理防御・体力・魔法防御／チャンピオン原典にも言及: 物理防御・体力）；[[wiki/entities/items/item-2524|バンドルパイプ]] + [[wiki/entities/items/item-3050|ジーク コンバージェンス]]（n=2（15未満）；共通stats: 物理防御・体力・魔法防御／チャンピオン原典にも言及: 物理防御・体力）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-59|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### JUNGLE（対象n=714）

- **高勝率コンボ候補（最大3件）：**
  - [[wiki/entities/champions/yone|ヨネ（Yone）]] — 対象側勝率72.7%（24/33）、n=33（十分性の目安を満たす）。
  - [[wiki/entities/champions/hwei|フェイ（Hwei）]] — 対象側勝率56.4%（22/39）、n=39（十分性の目安を満たす）。
  - [[wiki/entities/champions/miss-fortune|ミス・フォーチュン（MissFortune）]] — 対象側勝率51.4%（37/72）、n=72（十分性の目安を満たす）。
- **低勝率カウンターピック候補（最大3件）：**
  - [[wiki/entities/champions/lillia|リリア（Lillia）]] — 対象側勝率37.5%（12/32）、n=32（十分性の目安を満たす）。
  - [[wiki/entities/champions/viego|ヴィエゴ（Viego）]] — 対象側勝率38.8%（19/49）、n=49（十分性の目安を満たす）。
  - [[wiki/entities/champions/nocturne|ノクターン（Nocturne）]] — 対象側勝率42.4%（14/33）、n=33（十分性の目安を満たす）。

### UTILITY（対象n=39）

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

### JUNGLE（対象477試合、全体勝率47.0%）

| 順位 | 完全ルーンセット | 選択数 | 選択率 | 選択時勝率 |
| ---: | --- | ---: | ---: | ---: |
| 1 | 主系栄華：征服者／凱旋・レジェンド: 迅速・最期の慈悲；副系天啓：宇宙の英知・魔法の靴；シャードUNKNOWN(5005)・UNKNOWN(5008)・UNKNOWN(5001) | 184/477 | 38.6% | 47.8% |
| 2 | 主系栄華：征服者／凱旋・レジェンド: 迅速・最期の慈悲；副系天啓：魔法の靴・宇宙の英知；シャードUNKNOWN(5005)・UNKNOWN(5008)・UNKNOWN(5001) | 66/477 | 13.8% | 50.0% |
| 3 | 主系栄華：征服者／凱旋・レジェンド: 迅速・最期の慈悲；副系覇道：執拗な賞金首狩り・サドンインパクト；シャードUNKNOWN(5005)・UNKNOWN(5008)・UNKNOWN(5001) | 54/477 | 11.3% | 51.9% |

- **選定ロール：** チャンピオン・ロール別の完全試合数が最も多いロールを1つ選んだ。別ロールや全候補は詳細レポートで確認できる。
- **シャード表示：** Data Dragonで表示名を解決できない場合は`UNKNOWN(<ID>)`としてIDを保持する。

- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-rune-selection|Riotランク戦試合データ：チャンピオン別ルーン選択]]、[[wiki/syntheses/champion-rune-selection-ranked-matches|実測チャンピオン別ルーン選択分析]]。
<!-- champion-rune-set-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.JarvanIV` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/JarvanIV.png)
