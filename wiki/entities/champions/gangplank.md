---
title: "ガングプランク"
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
  - role-fighter
  - data-dragon
champion_id: "Gangplank"
champion_key: "41"
data_version: "16.18.1"
roles:
  - "Fighter"
resource_type: "マナ"
image_path: "raw/assets/champions/Gangplank.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Gangplank.png"
---

# ガングプランク

![[raw/assets/champions/Gangplank.png|128]]

## 基本情報

- **英字ID：** `Gangplank`
- **キー：** `41`
- **称号：** 大海原の大災厄
- **データversion：** `16.18.1`

## 紹介

気まぐれにして残忍、「略奪の王」を名乗るもその玉座を追われたガングプランクの名は、七つの海に轟き恐れられていた。かつてビルジウォーターの港町を牛耳っていた彼だが、その座を奪われた今、逆に彼はさらに危険な存在になったと考える者もいる。誰かにこの街を奪われるくらいなら、ガングプランクは再びビルジウォーターを血の海にしてやるだろう。ピストル、カトラス、火薬の樽を携え、彼は何としてでも奪われたものを取り返すつもりだ。

## 分類

- **役割タグ：** `Fighter`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 7 |
| `defense` | 6 |
| `magic` | 4 |
| `difficulty` | 9 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 630 |
| `hpperlevel` | 114 |
| `mp` | 280 |
| `mpperlevel` | 60 |
| `movespeed` | 345 |
| `armor` | 31 |
| `armorperlevel` | 4.7 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 125 |
| `hpregen` | 6 |
| `hpregenperlevel` | 0.6 |
| `mpregen` | 8 |
| `mpregenperlevel` | 0.7 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 64 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 3.2 |
| `attackspeed` | 0.658 |

## アビリティ

- **パッシブ — 背水の銃剣：** 数秒毎に近接攻撃で敵に火を点ける。

- **Q — 偽りの発砲：** 対象を撃ち抜き、そのユニットを倒すことでゴールドを奪うことができる。
- **W — 壊血病治癒：** オレンジをかじり、自身が受けている行動妨害効果を解消し、体力を回復する。
- **E — 火薬樽：** 指定地点に火薬樽を設置する。火薬樽はガングプランクが攻撃すると爆発し、範囲内の敵にその攻撃と同じダメージを与え、スロウ効果を付与する。
- **R — 一斉砲撃：** 海賊船に合図を送って指定したエリアを砲撃させ、効果範囲内の敵にスロウ効果とダメージを与える。

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
- **対象試合：** 72試合、全体勝率 43.1%
- **時間帯別勝率：** 〜20分 23.5%（n=17）、20〜25分 75.0%（n=8）、25〜30分 80.0%（n=15）、30〜35分 20.0%（n=10）、35分〜 31.8%（n=22）
- **最高帯：** 25〜30分（判定差 不明）
- **判定根拠：** 全5帯で各15試合未満の帯がある。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-41|ガングプランクの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### TOP（192試合）

- **実測ビルド候補：** [[wiki/entities/items/item-3031|インフィニティ エッジ]] + [[wiki/entities/items/item-3078|トリニティ フォース]] + [[wiki/entities/items/item-6676|コレクター]]（該当n=30、60.0% / 非該当44.4%、差+15.6pt）；[[wiki/entities/items/item-3031|インフィニティ エッジ]] + [[wiki/entities/items/item-3078|トリニティ フォース]]（該当n=34、58.8% / 非該当44.3%、差+14.5pt）
- **ステータス傾向：** 攻撃速度（該当n=79、51.9% / 非該当43.4%、差+8.5pt）；体力（該当n=115、47.8% / 非該当45.5%、差+2.4pt）
- **理論仮説：** [[wiki/entities/items/item-3071|ブラック クリーバー]] + [[wiki/entities/items/item-3078|トリニティ フォース]]（n=1（15未満）；共通stats: 攻撃力・体力／チャンピオン原典にも言及: 体力）；[[wiki/entities/items/item-3143|ランデュイン オーメン]] + [[wiki/entities/items/item-6662|アイスボーン ガントレット]]（n=1（15未満）；共通stats: 物理防御・体力／チャンピオン原典にも言及: 体力）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-41|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### TOP（対象n=329）

- **高勝率コンボ候補（最大3件）：**
  - [[wiki/entities/champions/leona|レオナ（Leona）]] — 対象側勝率66.7%（18/27）、サンプル不足（n=27、十分性の目安30未満）。
  - [[wiki/entities/champions/akali|アカリ（Akali）]] — 対象側勝率62.5%（10/16）、サンプル不足（n=16、十分性の目安30未満）。
  - [[wiki/entities/champions/miss-fortune|ミス・フォーチュン（MissFortune）]] — 対象側勝率55.6%（15/27）、サンプル不足（n=27、十分性の目安30未満）。
- **低勝率カウンターピック候補（最大3件）：**
  - [[wiki/entities/champions/aatrox|エイトロックス（Aatrox）]] — 対象側勝率34.8%（8/23）、サンプル不足（n=23、十分性の目安30未満）。
  - [[wiki/entities/champions/garen|ガレン（Garen）]] — 対象側勝率60.0%（9/15）、サンプル不足（n=15、十分性の目安30未満）。
  - [[wiki/entities/champions/mordekaiser|モルデカイザー（Mordekaiser）]] — 対象側勝率63.2%（12/19）、サンプル不足（n=19、十分性の目安30未満）。

### MIDDLE（対象n=53）

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

### TOP（対象269試合、全体勝率45.0%）

| 順位 | 完全ルーンセット | 選択数 | 選択率 | 選択時勝率 |
| ---: | --- | ---: | ---: | ---: |
| 1 | 主系魔道：死神の残り火／ニンバスクローク・至高・追火；副系栄華：切り崩し・レジェンド: ヘイスト；シャードUNKNOWN(5008)・UNKNOWN(5008)・UNKNOWN(5011) | 59/269 | 21.9% | 39.0% |
| 2 | 主系魔道：死神の残り火／ニンバスクローク・至高・追火；副系不滅：ボーンアーマー・気迫；シャードUNKNOWN(5008)・UNKNOWN(5008)・UNKNOWN(5011) | 37/269 | 13.8% | 51.4% |
| 3 | 主系魔道：死神の残り火／ニンバスクローク・至高・追火；副系栄華：レジェンド: ヘイスト・切り崩し；シャードUNKNOWN(5008)・UNKNOWN(5008)・UNKNOWN(5011) | 33/269 | 12.3% | 39.4% |

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
| BRONZE | 3 | 23 | 7勝/16敗 | 30.4% |

<!-- champion-tier-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Gangplank` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Gangplank.png)
