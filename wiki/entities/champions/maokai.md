---
title: "マオカイ"
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
  - role-tank
  - role-support
  - data-dragon
champion_id: "Maokai"
champion_key: "57"
data_version: "16.18.1"
roles:
  - "Tank"
  - "Support"
resource_type: "マナ"
image_path: "raw/assets/champions/Maokai.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Maokai.png"
---

# マオカイ

![[raw/assets/champions/Maokai.png|128]]

## 基本情報

- **英字ID：** `Maokai`
- **キー：** `57`
- **称号：** 歪みし樹人
- **データversion：** `16.18.1`

## 紹介

荒々しい巨大な樹人、マオカイは、シャドウアイルで自然界にあってはならない怨念に立ち向かう。大異変が起こり、故郷が破滅するのを目の当たりにした彼は、否応なく報復に生きる運命を背負わされた。幹の中心に浸透していた生命の水の力で、マオカイはこの災禍を生き延びた。かつて穏やかな自然界の精霊だった彼は、今や不死の亡霊という厄災をシャドウアイルから追放し、かつて美しかった故郷を取り戻すために猛然と戦っている。

## 分類

- **役割タグ：** `Tank`、`Support`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 3 |
| `defense` | 8 |
| `magic` | 6 |
| `difficulty` | 3 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 665 |
| `hpperlevel` | 109 |
| `mp` | 375 |
| `mpperlevel` | 43 |
| `movespeed` | 335 |
| `armor` | 35 |
| `armorperlevel` | 5.2 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 125 |
| `hpregen` | 5 |
| `hpregenperlevel` | 0.75 |
| `mpregen` | 6 |
| `mpregenperlevel` | 0.6 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 64 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2.125 |
| `attackspeed` | 0.8 |

## アビリティ

- **パッシブ — 魔樹液：** 通常攻撃が自身の体力を回復し、追加ダメージを与える。この効果にはある程度のクールダウンはあるが、スキルを使用するか、敵のスキルが自身に命中すると、このクールダウンが短縮される。

- **Q — 茨打ち：** 衝撃波で周囲の敵ユニットをノックバックして魔法ダメージとスロウ効果を与える。
- **W — 樹人の進撃：** 巨大な根の塊になって対象指定されなくなり、指定した対象に向かってダッシュする。対象に到達するとスネア効果を与える。
- **E — 苗木投げ：** 指定地点に苗木を投げて見張らせる。茂みの中ならより効果的になる。
- **R — 大地の捕縛：** 大量の茨や棘で出来た巨大な壁を召喚する。壁はゆっくりと前進しながら、通り道にいる敵ユニットにダメージとスネア効果を与える。

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
- **観測分類：** 明瞭な傾向なし
- **対象試合：** 215試合、全体勝率 46.5%
- **時間帯別勝率：** 〜20分 44.4%（n=36）、20〜25分 45.0%（n=20）、25〜30分 48.9%（n=47）、30〜35分 47.3%（n=55）、35分〜 45.6%（n=57）
- **最高帯：** 25〜30分（判定差 4.5ポイント）
- **判定根拠：** 最高帯と端点の差が8ポイント未満、または非単調。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-57|マオカイの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### UTILITY（348試合）

- **実測ビルド候補：** [[wiki/entities/items/item-3002|先人の道標]] + [[wiki/entities/items/item-3190|ソラリのロケット]]（該当n=51、58.8% / 非該当45.1%、差+13.7pt）
- **ステータス傾向：** 魔法防御（該当n=254、50.0% / 非該当39.4%、差+10.6pt）
- **理論仮説：** [[wiki/entities/items/item-3050|ジーク コンバージェンス]] + [[wiki/entities/items/item-3190|ソラリのロケット]]（n=2（15未満）；共通stats: 物理防御・体力・魔法防御／チャンピオン原典にも言及: 体力）；[[wiki/entities/items/item-2524|バンドルパイプ]] + [[wiki/entities/items/item-3050|ジーク コンバージェンス]]（n=2（15未満）；共通stats: 物理防御・体力・魔法防御／チャンピオン原典にも言及: 体力）

### TOP（49試合）

- **実測ビルド候補：** 該当・非該当が各30試合以上で正の差を持つ候補なし。
- **ステータス傾向：** 該当・非該当が各30試合以上で正の差を持つ群なし。
- **理論仮説：** [[wiki/entities/items/item-3119|冬の訪れ]] + [[wiki/entities/items/item-3121|フィンブルウィンター]]（未観測；共通stats: 体力・マナ／チャンピオン原典にも言及: 体力・マナ）；[[wiki/entities/items/item-2502|終わりなき絶望]] + [[wiki/entities/items/item-3068|サンファイア イージス]]（n=8（15未満）；共通stats: 物理防御・体力／チャンピオン原典にも言及: 体力）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-57|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### UTILITY（対象n=441）

- **高勝率コンボ候補（最大3件）：**
  - [[wiki/entities/champions/mordekaiser|モルデカイザー（Mordekaiser）]] — 対象側勝率65.6%（21/32）、n=32（十分性の目安を満たす）。
  - [[wiki/entities/champions/ezreal|エズリアル（Ezreal）]] — 対象側勝率60.0%（18/30）、n=30（十分性の目安を満たす）。
  - [[wiki/entities/champions/ashe|アッシュ（Ashe）]] — 対象側勝率56.1%（23/41）、n=41（十分性の目安を満たす）。
- **低勝率カウンターピック候補（最大3件）：**
  - [[wiki/entities/champions/nautilus|ノーチラス（Nautilus）]] — 対象側勝率47.1%（16/34）、n=34（十分性の目安を満たす）。

### TOP（対象n=65）

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

### UTILITY（対象173試合、全体勝率52.0%）

| 順位 | 完全ルーンセット | 選択数 | 選択率 | 選択時勝率 |
| ---: | --- | ---: | ---: | ---: |
| 1 | 主系不滅：アフターショック／生命の泉・ボーンアーマー・気迫；副系天啓：ビスケットデリバリー・宇宙の英知；シャードUNKNOWN(5008)・UNKNOWN(5001)・UNKNOWN(5001) | 58/173 | 33.5% | 51.7% |
| 2 | 主系不滅：アフターショック／生命の泉・息継ぎ・気迫；副系天啓：ビスケットデリバリー・宇宙の英知；シャードUNKNOWN(5007)・UNKNOWN(5010)・UNKNOWN(5011) | 23/173 | 13.3% | 56.5% |
| 3 | 主系不滅：アフターショック／生命の泉・心身調整・超成長；副系栄華：レジェンド: ヘイスト・凱旋；シャードUNKNOWN(5005)・UNKNOWN(5008)・UNKNOWN(5001) | 11/173 | 6.4% | 54.5% |

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
| GRANDMASTER | 3 | 32 | 22勝/10敗 | 68.8% |

<!-- champion-tier-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Maokai` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Maokai.png)
