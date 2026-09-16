---
title: "パイク"
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
  - role-assassin
  - data-dragon
champion_id: "Pyke"
champion_key: "555"
data_version: "16.18.1"
roles:
  - "Support"
  - "Assassin"
resource_type: "マナ"
image_path: "raw/assets/champions/Pyke.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Pyke.png"
---

# パイク

![[raw/assets/champions/Pyke.png|128]]

## 基本情報

- **英字ID：** `Pyke`
- **キー：** `555`
- **称号：** ブラッドハーバーの殺戮鬼
- **データversion：** `16.18.1`

## 紹介

ビルジウォーターのスロータードックでは名の知れたモリ撃ちだったパイクは、巨大なジョールフィッシュの胃の中で死を迎えるはずであったが、その息を吹き返した。彼は故郷の町の湿っぽい路地や裏通りを音もなく歩き、他者から搾取することで財を成す人々を追い詰めては、新たに身に着けた超自然的な能力で、彼らに速やかにして非情な死を与える。怪物を狩ることを誇りとしていた都市が、今では怪物に狩られているのだ。

## 分類

- **役割タグ：** `Support`、`Assassin`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 9 |
| `defense` | 3 |
| `magic` | 1 |
| `difficulty` | 7 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 670 |
| `hpperlevel` | 110 |
| `mp` | 415 |
| `mpperlevel` | 50 |
| `movespeed` | 330 |
| `armor` | 37 |
| `armorperlevel` | 4.7 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 150 |
| `hpregen` | 7 |
| `hpregenperlevel` | 0.5 |
| `mpregen` | 8 |
| `mpregenperlevel` | 1 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 62 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2.5 |
| `attackspeed` | 0.667 |

## アビリティ

- **パッシブ — 沈みし者の力：** 敵の視界外にいると、直前にチャンピオンからの攻撃で失った体力を回復する。また、パイクはいずれのソースからも増加最大体力を得ることはできず、代わりに増加攻撃力を得る。

- **Q — ボーンスキューア：** 前方にいる1体の敵を突き刺すか、1体の敵を引き寄せる。
- **W — ゴーストウォーター：** カモフラージュ状態になり、移動速度が大きく増加する。移動速度は徐々に元に戻る。
- **E — 亡者の引き波：** 亡霊を残してダッシュする。亡霊はパイクのところまで戻ってきて触れた敵チャンピオンをスタンさせる。
- **R — 水底の急襲：** ブリンクして体力の低下した敵にとどめを刺す。とどめを刺すと再度使用可能になり、アシストした味方1人に追加ゴールドを付与する。

<!-- power-spike:start -->
## パワースパイク

- **区分：** 終盤
- **判定：** [[wiki/syntheses/champion-power-spikes-v16-18-1|パワースパイク分類 v16.18.1]] に基づく原典ベースの推論。
- **根拠：**
  - 増加最大体力を得られない代わりに増加攻撃力へ変換する。
- **限界：** スキル基礎ダメージ・係数・アイテム完成時刻を全チャンピオンで統一比較できる原典値がないため、実戦の強さや購入優先度を断定しない。

<!-- power-spike:end -->

<!-- power-spike-match:start -->
## 試合時間別の観測

- **スナップショット：** 2026-09-15生成、キュー420、完全試合4,672件、[[reports/riot-ranked-match-analysis/run-20260915T010911Z/report|詳細レポート]]。
- **観測分類：** 明瞭な傾向なし
- **対象試合：** 256試合、全体勝率 48.8%
- **時間帯別勝率：** 〜20分 53.2%（n=47）、20〜25分 51.6%（n=31）、25〜30分 41.5%（n=53）、30〜35分 53.6%（n=56）、35分〜 46.4%（n=69）
- **最高帯：** 30〜35分（判定差 12.1ポイント）
- **判定根拠：** 最高帯と端点の差が8ポイント未満、または非単調。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-555|パイクの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### UTILITY（548試合）

- **実測ビルド候補：** 該当・非該当が各30試合以上で正の差を持つ候補なし。
- **ステータス傾向：** 攻撃力（該当n=514、50.0% / 非該当38.2%、差+11.8pt）；物理防御（該当n=35、57.1% / 非該当48.7%、差+8.4pt）
- **理論仮説：** [[wiki/entities/items/item-3814|ナイト エッジ]] + [[wiki/entities/items/item-6609|ケミパンク チェーンソード]]（n=1（15未満）；共通stats: 攻撃力・体力／チャンピオン原典にも言及: 攻撃力・体力）；[[wiki/entities/items/item-6609|ケミパンク チェーンソード]] + [[wiki/entities/items/item-6610|サンダード スカイ]]（未観測；共通stats: 攻撃力・体力／チャンピオン原典にも言及: 攻撃力・体力）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-555|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### UTILITY（対象n=709）

- **高勝率コンボ候補（最大3件）：**
  - [[wiki/entities/champions/aatrox|エイトロックス（Aatrox）]] — 対象側勝率66.7%（22/33）、n=33（十分性の目安を満たす）。
  - [[wiki/entities/champions/caitlyn|ケイトリン（Caitlyn）]] — 対象側勝率58.5%（24/41）、n=41（十分性の目安を満たす）。
  - [[wiki/entities/champions/miss-fortune|ミス・フォーチュン（MissFortune）]] — 対象側勝率56.4%（31/55）、n=55（十分性の目安を満たす）。
- **低勝率カウンターピック候補（最大3件）：**
  - [[wiki/entities/champions/nautilus|ノーチラス（Nautilus）]] — 対象側勝率43.9%（29/66）、n=66（十分性の目安を満たす）。
  - [[wiki/entities/champions/leona|レオナ（Leona）]] — 対象側勝率46.6%（27/58）、n=58（十分性の目安を満たす）。
  - [[wiki/entities/champions/seraphine|セラフィーン（Seraphine）]] — 対象側勝率50.0%（24/48）、n=48（十分性の目安を満たす）。

### JUNGLE（対象n=2）

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

### UTILITY（対象599試合、全体勝率49.1%）

| 順位 | 完全ルーンセット | 選択数 | 選択率 | 選択時勝率 |
| ---: | --- | ---: | ---: | ---: |
| 1 | 主系覇道：ヘイルブレード／追い打ち・第六感・至極の賞金首狩り；副系不滅：ボーンアーマー・気迫；シャードUNKNOWN(5008)・UNKNOWN(5008)・UNKNOWN(5001) | 217/599 | 36.2% | 50.7% |
| 2 | 主系覇道：ヘイルブレード／サドンインパクト・第六感・貪欲な賞金首狩り；副系天啓：宇宙の英知・魔法の靴；シャードUNKNOWN(5008)・UNKNOWN(5008)・UNKNOWN(5001) | 53/599 | 8.8% | 54.7% |
| 3 | 主系覇道：ヘイルブレード／サドンインパクト・ディープワード・執拗な賞金首狩り；副系栄華：凱旋・切り崩し；シャードUNKNOWN(5005)・UNKNOWN(5008)・UNKNOWN(5011) | 27/599 | 4.5% | 48.1% |

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
| EMERALD | 3 | 46 | 13勝/33敗 | 28.3% |

<!-- champion-tier-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Pyke` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Pyke.png)
