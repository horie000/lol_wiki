---
title: "フィズ"
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
  - role-fighter
  - data-dragon
champion_id: "Fizz"
champion_key: "105"
data_version: "16.18.1"
roles:
  - "Assassin"
  - "Fighter"
resource_type: "マナ"
image_path: "raw/assets/champions/Fizz.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Fizz.png"
---

# フィズ

![[raw/assets/champions/Fizz.png|128]]

## 基本情報

- **英字ID：** `Fizz`
- **キー：** `105`
- **称号：** 波間のトリックスター
- **データversion：** `16.18.1`

## 紹介

フィズはビルジウォーターを囲む岩礁の間に住む水陸両性のヨードルだ。彼は迷信深い船長が海に投げる捧げものをくすめては返して遊んでいるが、どんな荒くれの船乗りでも彼を敵に回そうとはしない。というのも、このすばしこい生き物の恐ろしさを侮った者たちの話が数多く伝わっているからだ。気まぐれな海の精霊だと勘違いされがちだが、彼は深海の獣どもを操ることもできるらしく、敵も味方もなく、人々をからかっては楽しんでいる。

## 分類

- **役割タグ：** `Assassin`、`Fighter`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 6 |
| `defense` | 4 |
| `magic` | 7 |
| `difficulty` | 6 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 640 |
| `hpperlevel` | 106 |
| `mp` | 317 |
| `mpperlevel` | 52 |
| `movespeed` | 335 |
| `armor` | 26 |
| `armorperlevel` | 4.6 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 175 |
| `hpregen` | 8 |
| `hpregenperlevel` | 0.7 |
| `mpregen` | 6 |
| `mpregenperlevel` | 0.8 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 58 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 3.1 |
| `attackspeed` | 0.658 |

## アビリティ

- **パッシブ — シーファイター：** ユニットをすり抜け、すべてのダメージソースから受けるダメージを一定量軽減させる。

- **Q — ウニトゲストライク：** 対象に向かって突進し反対側へ突き抜ける。命中した対象に魔法ダメージを与え、通常攻撃時効果を発動する。
- **W — シートライデント：** 自動効果で通常攻撃が敵を出血させ、数秒間かけて魔法ダメージを与える。発動すると次の通常攻撃を強化して追加ダメージを与え、少しの間だけその後の通常攻撃が強化される。
- **E — プレイ/トリックスター：** 地面に槍を突き立て飛び上がった後、槍の上に器用に乗って敵から対象指定されなくなる。この状態からその場に着地、または再度ジャンプして別の指定地点に着地し範囲内の敵にダメージを与える。
- **R — フィッシング：** 撒き餌として魚を1匹発射する。魚が命中した敵チャンピオンはスロウ状態になり周囲を魚が旋回する。短時間後、地面から巨大なサメが飛びだして対象をノックアップさせ、周囲の敵を横に跳ね飛ばす。命中した敵は全員魔法ダメージとスロウ効果を受ける。

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
- **対象試合：** 90試合、全体勝率 54.4%
- **時間帯別勝率：** 〜20分 81.8%（n=11）、20〜25分 64.3%（n=14）、25〜30分 41.9%（n=31）、30〜35分 56.2%（n=16）、35分〜 50.0%（n=18）
- **最高帯：** 〜20分（判定差 不明）
- **判定根拠：** 全5帯で各15試合未満の帯がある。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-105|フィズの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### MIDDLE（218試合）

- **実測ビルド候補：** [[wiki/entities/items/item-3041|メジャイ ソウルスティーラー]] + [[wiki/entities/items/item-3100|リッチ ベイン]]（該当n=40、75.0% / 非該当42.7%、差+32.3pt）；[[wiki/entities/items/item-3100|リッチ ベイン]] + [[wiki/entities/items/item-3157|ゾーニャの砂時計]] + [[wiki/entities/items/item-3175|連呪使いのブーツ]]（該当n=63、63.5% / 非該当42.6%、差+20.9pt）
- **ステータス傾向：** 体力（該当n=159、53.5% / 非該当35.6%、差+17.9pt）；物理防御（該当n=158、50.6% / 非該当43.3%、差+7.3pt）
- **理論仮説：** [[wiki/entities/items/item-3118|マリグナンス]] + [[wiki/entities/items/item-6655|ルーデン エコー]]（未観測；共通stats: 魔力・マナ／チャンピオン原典にも言及: マナ）；[[wiki/entities/items/item-3118|マリグナンス]] + [[wiki/entities/items/item-6657|ロッド オブ エイジス]]（未観測；共通stats: 魔力・マナ／チャンピオン原典にも言及: マナ）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-105|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### MIDDLE（対象n=319）

- **高勝率コンボ候補（最大3件）：**
  - [[wiki/entities/champions/malphite|マルファイト（Malphite）]] — 対象側勝率62.5%（10/16）、サンプル不足（n=16、十分性の目安30未満）。
  - [[wiki/entities/champions/smolder|スモルダー（Smolder）]] — 対象側勝率62.5%（10/16）、サンプル不足（n=16、十分性の目安30未満）。
  - [[wiki/entities/champions/leona|レオナ（Leona）]] — 対象側勝率57.7%（15/26）、サンプル不足（n=26、十分性の目安30未満）。
- **低勝率カウンターピック候補（最大3件）：**
  - [[wiki/entities/champions/ahri|アーリ（Ahri）]] — 対象側勝率36.0%（9/25）、サンプル不足（n=25、十分性の目安30未満）。
  - [[wiki/entities/champions/akali|アカリ（Akali）]] — 対象側勝率40.0%（6/15）、サンプル不足（n=15、十分性の目安30未満）。
  - [[wiki/entities/champions/hwei|フェイ（Hwei）]] — 対象側勝率45.0%（9/20）、サンプル不足（n=20、十分性の目安30未満）。

### JUNGLE（対象n=39）

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

### MIDDLE（対象171試合、全体勝率52.0%）

| 順位 | 完全ルーンセット | 選択数 | 選択率 | 選択時勝率 |
| ---: | --- | ---: | ---: | ---: |
| 1 | 主系覇道：電撃／サドンインパクト・グリスリー メメント・貪欲な賞金首狩り；副系魔道：追火・至高；シャードUNKNOWN(5008)・UNKNOWN(5008)・UNKNOWN(5001) | 39/171 | 22.8% | 43.6% |
| 2 | 主系覇道：電撃／サドンインパクト・グリスリー メメント・貪欲な賞金首狩り；副系栄華：最期の慈悲・凱旋；シャードUNKNOWN(5008)・UNKNOWN(5008)・UNKNOWN(5001) | 18/171 | 10.5% | 50.0% |
| 3 | 主系覇道：電撃／サドンインパクト・グリスリー メメント・貪欲な賞金首狩り；副系魔道：至高・追火；シャードUNKNOWN(5008)・UNKNOWN(5008)・UNKNOWN(5001) | 15/171 | 8.8% | 66.7% |

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
| PLATINUM | 4 | 35 | 12勝/23敗 | 34.3% |

<!-- champion-tier-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Fizz` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Fizz.png)
