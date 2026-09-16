---
title: "リー・シン"
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
  - role-assassin
  - data-dragon
champion_id: "LeeSin"
champion_key: "64"
data_version: "16.18.1"
roles:
  - "Fighter"
  - "Assassin"
resource_type: "気"
image_path: "raw/assets/champions/LeeSin.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/LeeSin.png"
---

# リー・シン

![[raw/assets/champions/LeeSin.png|128]]

## 基本情報

- **英字ID：** `LeeSin`
- **キー：** `64`
- **称号：** 盲目の修行僧
- **データversion：** `16.18.1`

## 紹介

アイオニアの古代の格闘技をマスターしたリー・シンは、龍の精霊のエッセンスを操ってあらゆる困難を克服する厳しい訓練を積んだ格闘家だ。何年も前に視力を失ったが、この戦闘僧は聖なる均衡を破ろうとするあらゆる脅威から故郷を守るために、自らの人生を捧げている。深い瞑想から得た彼の力を侮る敵は、彼の伝説の燃える拳と炎の回し蹴りの餌食となるだろう。

## 分類

- **役割タグ：** `Fighter`、`Assassin`
- **リソース種別：** 気

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 8 |
| `defense` | 5 |
| `magic` | 3 |
| `difficulty` | 6 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 645 |
| `hpperlevel` | 108 |
| `mp` | 200 |
| `mpperlevel` | 0 |
| `movespeed` | 345 |
| `armor` | 36 |
| `armorperlevel` | 4.5 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 125 |
| `hpregen` | 7.5 |
| `hpregenperlevel` | 0.7 |
| `mpregen` | 50 |
| `mpregenperlevel` | 0 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 66 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 3 |
| `attackspeed` | 0.651 |

## アビリティ

- **パッシブ — 練気：** スキル使用後、次の通常攻撃2回の攻撃速度が増加し、それぞれ気を回復する。

- **Q — 響掌/共鳴撃：** 響掌: 敵の位置を探るひずんだ音波を発射して、最初に当たった敵に物理ダメージを与える。また、命中してから3秒間は「共鳴撃」を発動できる。 共鳴撃: 「響掌」が命中した敵に素早く接近し、対象の減少体力に応じた物理ダメージを与える。
- **W — 守りの型/鉄の意志：** 守りの型: 指定した味方に素早く接近し、シールドを出現させてダメージから自身を守る。接近した相手が味方チャンピオンの場合、自身と相手を両方シールドで保護する。また、使用後は「鉄の意志」を発動できる。 鉄の意志: 厳しい修行の成果により、オムニヴァンプを獲得する。
- **E — 破風/縛脚：** 破風: 地面を強打して衝撃波を発生させることで魔法ダメージを与え、命中した敵ユニットを可視状態にする。「破風」が敵に命中した場合は、「縛脚」で追撃できる。 縛脚: 「破風」でダメージを受けた敵にスロウ効果を付与する。低下した移動速度は時間の経過とともに徐々に元に戻る。
- **R — 龍の怒り：** 対象に強力な回し蹴りを食らわせ、物理ダメージを与えると同時に後方へノックバックさせ、その際に衝突した敵ユニットにも物理ダメージを与える。ノックバックした対象と接触した敵は、短時間ノックアップ状態になる(この技はジェシー・パーリングにより伝授されたものだが、リー・シンはプレイヤーをゲームからキックすることはない…きっと)。

<!-- power-spike:start -->
## パワースパイク

- **区分：** 序盤
- **判定：** [[wiki/syntheses/champion-power-spikes-v16-18-1|パワースパイク分類 v16.18.1]] に基づく原典ベースの推論。
- **根拠：**
  - 基礎ステータス指数（体力・物理防御・攻撃力・移動速度を標準化して合算）が173件中14位（上位15%）。体力645、物理防御36、攻撃力66、移動速度345。
- **限界：** スキル基礎ダメージ・係数・アイテム完成時刻を全チャンピオンで統一比較できる原典値がないため、実戦の強さや購入優先度を断定しない。

<!-- power-spike:end -->

<!-- power-spike-match:start -->
## 試合時間別の観測

- **スナップショット：** 2026-09-15生成、キュー420、完全試合4,672件、[[reports/riot-ranked-match-analysis/run-20260915T010911Z/report|詳細レポート]]。
- **観測分類：** 序盤寄り
- **対象試合：** 241試合、全体勝率 44.8%
- **時間帯別勝率：** 〜20分 55.6%（n=45）、20〜25分 42.9%（n=28）、25〜30分 42.4%（n=59）、30〜35分 42.9%（n=56）、35分〜 41.5%（n=53）
- **最高帯：** 〜20分（判定差 14.0ポイント）
- **判定根拠：** 〜20分が最高、長時間帯との差 14.0%。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-64|リー・シンの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### JUNGLE（613試合）

- **実測ビルド候補：** [[wiki/entities/items/item-3026|ガーディアン エンジェル]] + [[wiki/entities/items/item-6610|サンダード スカイ]] + [[wiki/entities/items/item-6692|赤月の刃]]（該当n=35、68.6% / 非該当45.0%、差+23.6pt）；[[wiki/entities/items/item-3026|ガーディアン エンジェル]] + [[wiki/entities/items/item-6610|サンダード スカイ]]（該当n=46、67.4% / 非該当44.6%、差+22.8pt）
- **ステータス傾向：** 物理防御（該当n=407、50.1% / 非該当38.8%、差+11.3pt）；体力（該当n=546、46.5% / 非該当44.8%、差+1.7pt）
- **理論仮説：** [[wiki/entities/items/item-6609|ケミパンク チェーンソード]] + [[wiki/entities/items/item-6610|サンダード スカイ]]（n=3（15未満）；共通stats: 攻撃力・体力／チャンピオン原典にも言及: 攻撃力・体力）；[[wiki/entities/items/item-3071|ブラック クリーバー]] + [[wiki/entities/items/item-6609|ケミパンク チェーンソード]]（n=3（15未満）；共通stats: 攻撃力・体力／チャンピオン原典にも言及: 攻撃力・体力）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-64|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### JUNGLE（対象n=959）

- **高勝率コンボ候補（最大3件）：**
  - [[wiki/entities/champions/garen|ガレン（Garen）]] — 対象側勝率66.7%（26/39）、n=39（十分性の目安を満たす）。
  - [[wiki/entities/champions/renekton|レネクトン（Renekton）]] — 対象側勝率66.7%（22/33）、n=33（十分性の目安を満たす）。
  - [[wiki/entities/champions/viktor|ビクター（Viktor）]] — 対象側勝率57.4%（27/47）、n=47（十分性の目安を満たす）。
- **低勝率カウンターピック候補（最大3件）：**
  - [[wiki/entities/champions/shyvana|シヴァーナ（Shyvana）]] — 対象側勝率27.3%（9/33）、n=33（十分性の目安を満たす）。
  - [[wiki/entities/champions/nocturne|ノクターン（Nocturne）]] — 対象側勝率36.0%（18/50）、n=50（十分性の目安を満たす）。
  - [[wiki/entities/champions/kayn|ケイン（Kayn）]] — 対象側勝率36.4%（12/33）、n=33（十分性の目安を満たす）。

### TOP（対象n=20）

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

### JUNGLE（対象1,015試合、全体勝率48.1%）

| 順位 | 完全ルーンセット | 選択数 | 選択率 | 選択時勝率 |
| ---: | --- | ---: | ---: | ---: |
| 1 | 主系栄華：征服者／凱旋・レジェンド: 迅速・最期の慈悲；副系天啓：宇宙の英知・魔法の靴；シャードUNKNOWN(5005)・UNKNOWN(5008)・UNKNOWN(5001) | 421/1,015 | 41.5% | 47.3% |
| 2 | 主系栄華：征服者／凱旋・レジェンド: 迅速・最期の慈悲；副系天啓：魔法の靴・宇宙の英知；シャードUNKNOWN(5005)・UNKNOWN(5008)・UNKNOWN(5001) | 180/1,015 | 17.7% | 51.1% |
| 3 | 主系栄華：征服者／凱旋・レジェンド: 迅速・最期の慈悲；副系覇道：サドンインパクト・貪欲な賞金首狩り；シャードUNKNOWN(5005)・UNKNOWN(5008)・UNKNOWN(5001) | 64/1,015 | 6.3% | 51.6% |

- **選定ロール：** チャンピオン・ロール別の完全試合数が最も多いロールを1つ選んだ。別ロールや全候補は詳細レポートで確認できる。
- **シャード表示：** Data Dragonで表示名を解決できない場合は`UNKNOWN(<ID>)`としてIDを保持する。

- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-rune-selection|Riotランク戦試合データ：チャンピオン別ルーン選択]]、[[wiki/syntheses/champion-rune-selection-ranked-matches|実測チャンピオン別ルーン選択分析]]。
<!-- champion-rune-set-analysis:end -->

<!-- champion-tier-analysis:start -->
## 観測ランク帯別チャンピオン候補

- **スナップショット：** 2026-09-16生成、キュー420、観測10帯、各1,000試合、統合後9,761試合、min-games 15、[[reports/riot-ranked-tier-analysis/run-20260916T083219Z/report|ランク帯別詳細レポート]]。
- **根拠：** [[wiki/sources/src-2026-09-16-riot-ranked-match-tier-analysis|Riotランク戦試合データ：観測ランク帯別特徴]]、[[wiki/syntheses/ranked-tier-characteristics|ランク帯別の試合特徴と全帯共通傾向]]。
- **読み方：** `observed_tier` はその試合を発見したプレイヤーの収集時点の所属帯であり、10人全員の試合時ランクではない。以下は各帯の上位選択と、min-games以上で機械的に抽出した高低勝率の探索候補で、推奨・因果効果・有意差を示さない。

### ピック数上位5に入った帯

| 観測帯 | 帯内順位 | 試合数 | ピック率 | 勝敗 | 勝率 |
| --- | ---: | ---: | ---: | --- | ---: |
| DIAMOND | 2 | 175 | 1.8% | 93勝/82敗 | 53.1% |
| GRANDMASTER | 5 | 172 | 1.7% | 75勝/97敗 | 43.6% |
| CHALLENGER | 4 | 175 | 1.8% | 86勝/89敗 | 49.1% |

<!-- champion-tier-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.LeeSin` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/LeeSin.png)
