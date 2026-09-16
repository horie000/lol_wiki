---
title: "ゾーイ"
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
  - role-mage
  - data-dragon
champion_id: "Zoe"
champion_key: "142"
data_version: "16.18.1"
roles:
  - "Mage"
resource_type: "マナ"
image_path: "raw/assets/champions/Zoe.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Zoe.png"
---

# ゾーイ

![[raw/assets/champions/Zoe.png|128]]

## 基本情報

- **英字ID：** `Zoe`
- **キー：** `142`
- **称号：** 超常の遊び
- **データversion：** `16.18.1`

## 紹介

いたずら、想像、変化を具現化する存在であるゾーイは、時空を駆け抜けて霊峰ターゴンのメッセージ──世界の再編を招く出来事の到来──を告げる。彼女の存在は、現実を支配する聖なる数学に歪みを生み出し、時に激変を引き起こす。意識的にではないし、悪意もない。だからこそゾーイはたっぷりと時間をかけて遊びに集中し、定命の者をからかい、あるいはただ楽しいからという理由で、平然とその義務を果たせるのだろう。ゾーイに出会うと気分が高揚して前向きな気持ちになるが、実際にはそれは常に危険と隣り合わせだ。

## 分類

- **役割タグ：** `Mage`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 1 |
| `defense` | 7 |
| `magic` | 8 |
| `difficulty` | 5 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 630 |
| `hpperlevel` | 106 |
| `mp` | 425 |
| `mpperlevel` | 25 |
| `movespeed` | 340 |
| `armor` | 21 |
| `armorperlevel` | 4.7 |
| `spellblock` | 30 |
| `spellblockperlevel` | 1.3 |
| `attackrange` | 550 |
| `hpregen` | 7.5 |
| `hpregenperlevel` | 0.6 |
| `mpregen` | 8 |
| `mpregenperlevel` | 0.65 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 58 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2.5 |
| `attackspeed` | 0.658 |

## アビリティ

- **パッシブ — スパークル！：** スキル使用後、次に行う通常攻撃が追加魔法ダメージを与える。

- **Q — パドルスター：** 途中で進行方向を変えられる星を飛ばす。真っすぐ飛んだ距離の長さに応じてダメージが増加する。
- **W — スペルシーフ：** 敵のサモナースペルと発動効果アイテムのかけらを拾って1回使用できる。サモナースペルを使用するごとに最大3つの魔法の弾を最も近くにいる対象に向かって飛ばす。
- **E — スリープバブル：** 対象に眠気を与えてから眠らせる。眠っている間は、対象の魔法防御が低下する。眠りを覚ます攻撃は2倍のダメージを与える(上限あり)。
- **R — ポータルジャンプ：** 近くの指定した位置に1秒間ブリンクして、もとの位置に戻る。

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
- **対象試合：** 137試合、全体勝率 55.5%
- **時間帯別勝率：** 〜20分 63.6%（n=22）、20〜25分 47.4%（n=19）、25〜30分 51.9%（n=27）、30〜35分 56.2%（n=32）、35分〜 56.8%（n=37）
- **最高帯：** 〜20分（判定差 16.3ポイント）
- **判定根拠：** 最高帯と端点の差が8ポイント未満、または非単調。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-142|ゾーイの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### MIDDLE（232試合）

- **実測ビルド候補：** [[wiki/entities/items/item-4645|シャドウフレイム]] + [[wiki/entities/items/item-6655|ルーデン エコー]]（該当n=102、56.9% / 非該当50.0%、差+6.9pt）；[[wiki/entities/items/item-3175|連呪使いのブーツ]] + [[wiki/entities/items/item-4645|シャドウフレイム]]（該当n=76、56.6% / 非該当51.3%、差+5.3pt）
- **ステータス傾向：** 物理防御（該当n=33、66.7% / 非該当50.8%、差+15.9pt）；体力（該当n=164、55.5% / 非該当47.1%、差+8.4pt）
- **理論仮説：** [[wiki/entities/items/item-3003|アークエンジェル スタッフ]] + [[wiki/entities/items/item-3040|セラフ エンブレイス]]（未観測；共通stats: 魔力・マナ／チャンピオン原典にも言及: マナ）；[[wiki/entities/items/item-3003|アークエンジェル スタッフ]] + [[wiki/entities/items/item-6655|ルーデン エコー]]（未観測；共通stats: 魔力・マナ／チャンピオン原典にも言及: マナ）

### UTILITY（39試合）

- **実測ビルド候補：** 該当・非該当が各30試合以上で正の差を持つ候補なし。
- **ステータス傾向：** 該当・非該当が各30試合以上で正の差を持つ群なし。
- **理論仮説：** [[wiki/entities/items/item-3190|ソラリのロケット]] + [[wiki/entities/items/item-8020|アビサル マスク]]（未観測；共通stats: 体力・魔法防御／チャンピオン原典にも言及: 魔法防御）；[[wiki/entities/items/item-2503|黒炎のトーチ]] + [[wiki/entities/items/item-6655|ルーデン エコー]]（未観測；共通stats: 魔力・マナ／チャンピオン原典にも言及: マナ）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-142|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### MIDDLE（対象n=326）

- **高勝率コンボ候補（最大3件）：**
  - [[wiki/entities/champions/jhin|ジン（Jhin）]] — 対象側勝率70.0%（21/30）、n=30（十分性の目安を満たす）。
  - [[wiki/entities/champions/nautilus|ノーチラス（Nautilus）]] — 対象側勝率51.6%（16/31）、n=31（十分性の目安を満たす）。
- **低勝率カウンターピック候補（最大3件）：**
  - [[wiki/entities/champions/malzahar|マルザハール（Malzahar）]] — 対象側勝率29.4%（5/17）、サンプル不足（n=17、十分性の目安30未満）。
  - [[wiki/entities/champions/ahri|アーリ（Ahri）]] — 対象側勝率58.3%（14/24）、サンプル不足（n=24、十分性の目安30未満）。
  - [[wiki/entities/champions/sylas|サイラス（Sylas）]] — 対象側勝率58.8%（10/17）、サンプル不足（n=17、十分性の目安30未満）。

### UTILITY（対象n=47）

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

### MIDDLE（対象131試合、全体勝率54.2%）

| 順位 | 完全ルーンセット | 選択数 | 選択率 | 選択時勝率 |
| ---: | --- | ---: | ---: | ---: |
| 1 | 主系覇道：電撃／サドンインパクト・グリスリー メメント・執拗な賞金首狩り；副系魔道：ニンバスクローク・至高；シャードUNKNOWN(5005)・UNKNOWN(5008)・UNKNOWN(5001) | 54/131 | 41.2% | 42.6% |
| 2 | 主系覇道：電撃／血の味わい・グリスリー メメント・執拗な賞金首狩り；副系栄華：切り崩し・レジェンド: ヘイスト；シャードUNKNOWN(5005)・UNKNOWN(5008)・UNKNOWN(5011) | 11/131 | 8.4% | 72.7% |
| 3 | 主系魔道：エアリー召喚／ニンバスクローク・追い風・追火；副系覇道：サドンインパクト・執拗な賞金首狩り；シャードUNKNOWN(5005)・UNKNOWN(5008)・UNKNOWN(5011) | 10/131 | 7.6% | 40.0% |

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
| PLATINUM | 1 | 22 | 16勝/6敗 | 72.7% |

<!-- champion-tier-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Zoe` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Zoe.png)
