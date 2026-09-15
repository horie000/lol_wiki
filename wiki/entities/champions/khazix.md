---
title: "カ＝ジックス"
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
  - role-assassin
  - data-dragon
champion_id: "Khazix"
champion_key: "121"
data_version: "16.18.1"
roles:
  - "Assassin"
resource_type: "マナ"
image_path: "raw/assets/champions/Khazix.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Khazix.png"
---

# カ＝ジックス

![[raw/assets/champions/Khazix.png|128]]

## 基本情報

- **英字ID：** `Khazix`
- **キー：** `121`
- **称号：** ヴォイドの捕食者
- **データversion：** `16.18.1`

## 紹介

ヴォイドは成長し、適応する──無数に存在するヴォイドの生物の中でカ＝ジックスほどこの真実を体現しているものは存在しない。この恐怖のミュータントの原動力となっているのは進化であり、最強の生き物を倒して生き延びることを目的として生まれてきた。獲物を倒せなければ、新たに成長してより効果的な方法を身に付ける。カ＝ジックスはもともと心を持たない獣だったが、今では形態とともに知性が発達して獲物を狙う際に計画を立てるようになり、自身が獲物の心に植え付ける恐怖すら利用するようになっている。

## 分類

- **役割タグ：** `Assassin`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 9 |
| `defense` | 4 |
| `magic` | 3 |
| `difficulty` | 6 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 643 |
| `hpperlevel` | 99 |
| `mp` | 327 |
| `mpperlevel` | 40 |
| `movespeed` | 345 |
| `armor` | 32 |
| `armorperlevel` | 4.2 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 125 |
| `hpregen` | 7.5 |
| `hpregenperlevel` | 0.75 |
| `mpregen` | 7.59 |
| `mpregenperlevel` | 0.5 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 60 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2.7 |
| `attackspeed` | 0.668 |

## アビリティ

- **パッシブ — 見えざる脅威：** 味方から「孤立」している周囲の敵ユニットをマークする。カ＝ジックスのスキルは「孤立」している対象が相手だと変化する。 敵の視界から消えるとカ＝ジックスは「見えざる脅威」を獲得し、次の通常攻撃で敵チャンピオンに追加魔法ダメージを与え、移動速度を数秒間、低下させる。

- **Q — 甘美なる恐怖：** 対象に物理ダメージを与える。「孤立」している対象にはダメージが増加する。「死鎌の進化」が完了している場合は、「孤立」している対象に使用するとクールダウンの一定割合が戻される。また、通常攻撃と「甘美なる恐怖」の射程が延びる。
- **W — ヴォイドの刺棘：** 爆発する棘を発射して、命中した敵ユニットに物理ダメージを与える。カ＝ジックスが爆発範囲内にいた場合は体力が回復する。「刺棘の進化」が完了している場合は、扇状に棘の塊が3つ発射され、命中した敵ユニットにはスロウ効果を与え、敵チャンピオンに命中した場合は2秒間可視状態になる。「孤立」した対象にはスロウ効果が強化される。
- **E — リープ：** カ＝ジックスが指定地点へと跳躍し、着地と同時に物理ダメージを与える。「翅の進化」を選択した場合は、「リープ」の飛距離が200延びて、敵チャンピオンのキルまたはアシストでクールダウンが解消する。
- **R — 捕食の本能：** 自動効果: スキルレベルが上がるたびにスキルを1つ進化させ、特殊な効果を追加できる。 発動効果: カ＝ジックスがインビジブル状態になり、「見えざる脅威」が発動して移動速度が増加する。「適応擬態の進化」が完了している場合は、「捕食の本能」のインビジブルの効果時間と使用回数が増加する。

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
- **対象試合：** 78試合、全体勝率 43.6%
- **時間帯別勝率：** 〜20分 47.1%（n=17）、20〜25分 54.5%（n=11）、25〜30分 36.8%（n=19）、30〜35分 52.9%（n=17）、35分〜 28.6%（n=14）
- **最高帯：** 20〜25分（判定差 —）
- **判定根拠：** 5つの時間帯のいずれかで15試合未満のため、時間帯の比較を保留する。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-121|カ＝ジックスの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### JUNGLE（377試合）

- **実測ビルド候補：** [[wiki/entities/items/item-3142|妖夢の霊剣]] + [[wiki/entities/items/item-6697|ヒュブリス]] + [[wiki/entities/items/item-6701|オポチュニティー]]（該当n=46、73.9% / 非該当51.7%、差+22.3pt）；[[wiki/entities/items/item-3142|妖夢の霊剣]] + [[wiki/entities/items/item-6697|ヒュブリス]]（該当n=124、68.5% / 非該当47.4%、差+21.1pt）
- **ステータス傾向：** 移動速度（該当n=345、55.1% / 非該当46.9%、差+8.2pt）；体力（該当n=102、55.9% / 非該当53.8%、差+2.1pt）
- **理論仮説：** [[wiki/entities/items/item-3071|ブラック クリーバー]] + [[wiki/entities/items/item-3748|タイタン ハイドラ]]（n=1（15未満）；共通stats: 攻撃力・体力／チャンピオン原典にも言及: 攻撃力・体力）；[[wiki/entities/items/item-3748|タイタン ハイドラ]] + [[wiki/entities/items/item-3814|ナイト エッジ]]（未観測；共通stats: 攻撃力・体力／チャンピオン原典にも言及: 攻撃力・体力）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-121|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### JUNGLE（対象n=503）

- **高勝率コンボ候補（最大3件）：**
  - [[wiki/entities/champions/caitlyn|ケイトリン（Caitlyn）]] — 対象側勝率60.0%（18/30）、n=30（十分性の目安を満たす）。
  - [[wiki/entities/champions/ashe|アッシュ（Ashe）]] — 対象側勝率59.5%（22/37）、n=37（十分性の目安を満たす）。
  - [[wiki/entities/champions/malzahar|マルザハール（Malzahar）]] — 対象側勝率56.7%（17/30）、n=30（十分性の目安を満たす）。
- **低勝率カウンターピック候補（最大3件）：**
  - [[wiki/entities/champions/viego|ヴィエゴ（Viego）]] — 対象側勝率52.4%（22/42）、n=42（十分性の目安を満たす）。

### MIDDLE（対象n=4）

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

### JUNGLE（対象641試合、全体勝率51.0%）

| 順位 | 完全ルーンセット | 選択数 | 選択率 | 選択時勝率 |
| ---: | --- | ---: | ---: | ---: |
| 1 | 主系天啓：ファーストストライク／キャッシュバック・トリプル トニック・宇宙の英知；副系覇道：サドンインパクト・貪欲な賞金首狩り；シャードUNKNOWN(5008)・UNKNOWN(5008)・UNKNOWN(5001) | 176/641 | 27.5% | 49.4% |
| 2 | 主系天啓：ファーストストライク／キャッシュバック・トリプル トニック・宇宙の英知；副系覇道：サドンインパクト・貪欲な賞金首狩り；シャードUNKNOWN(5008)・UNKNOWN(5008)・UNKNOWN(5011) | 84/641 | 13.1% | 56.0% |
| 3 | 主系覇道：魂の収穫／サドンインパクト・グリスリー メメント・貪欲な賞金首狩り；副系栄華：最期の慈悲・凱旋；シャードUNKNOWN(5008)・UNKNOWN(5008)・UNKNOWN(5001) | 33/641 | 5.1% | 33.3% |

- **選定ロール：** チャンピオン・ロール別の完全試合数が最も多いロールを1つ選んだ。別ロールや全候補は詳細レポートで確認できる。
- **シャード表示：** Data Dragonで表示名を解決できない場合は`UNKNOWN(<ID>)`としてIDを保持する。

- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-rune-selection|Riotランク戦試合データ：チャンピオン別ルーン選択]]、[[wiki/syntheses/champion-rune-selection-ranked-matches|実測チャンピオン別ルーン選択分析]]。
<!-- champion-rune-set-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Khazix` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Khazix.png)
