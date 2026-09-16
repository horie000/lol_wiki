---
title: "ビクター"
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
champion_id: "Viktor"
champion_key: "112"
data_version: "16.18.1"
roles:
  - "Mage"
resource_type: "マナ"
image_path: "raw/assets/champions/Viktor.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Viktor.png"
---

# ビクター

![[raw/assets/champions/Viktor.png|128]]

## 基本情報

- **英字ID：** `Viktor`
- **キー：** `112`
- **称号：** アーケインの先触れ
- **データversion：** `16.18.1`

## 紹介

かつての姿から完全なる生物力学的な進化を遂げたビクターは、輝ける進化を受け入れ、彼の支持者にとって救世主となる何かへと変わった。彼は感情を排除することで苦痛を排除できるという論理に基づき、自らの人間性を犠牲にして、ヘクスコアの啓示を世界に与えようとしている──その恩恵が誰にも理解されなかったとしても。このアーケインの達人にとっては、暴力は究極の方程式を解くために必要な変数でしかないのだ。

## 分類

- **役割タグ：** `Mage`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 2 |
| `defense` | 4 |
| `magic` | 10 |
| `difficulty` | 9 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 600 |
| `hpperlevel` | 100 |
| `mp` | 405 |
| `mpperlevel` | 45 |
| `movespeed` | 335 |
| `armor` | 23 |
| `armorperlevel` | 4.4 |
| `spellblock` | 30 |
| `spellblockperlevel` | 1.3 |
| `attackrange` | 525 |
| `hpregen` | 8 |
| `hpregenperlevel` | 0.65 |
| `mpregen` | 8 |
| `mpregenperlevel` | 0.8 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 53 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2.11 |
| `attackspeed` | 0.658 |

## アビリティ

- **パッシブ — グロリアス・エヴォリューション：** 敵を倒すたびに「ヘクス フラグメント」を獲得する。「ヘクス フラグメント」を100個獲得するごとに、発動効果スキルが1つ恒久的に強化される。すべての通常スキルをアップグレードすると、「ヘクス フラグメント」を100個獲得してアルティメットスキルが強化できる。

- **Q — パワーブラスト：** 敵ユニットを狙い撃って魔法ダメージを与え、自身にシールドを張り、次の通常攻撃のダメージが強化される。 強化: 「パワーブラスト」のシールドが60%増加し、このスキルを発動後、移動速度が増加する。
- **W — グラビティフィールド：** 強力な重力場を発生させる装置を展開し、範囲内の敵にスロウ効果を付与する。 また、装置から抜け出せなかった敵にスタン効果を付与する。 強化: スキルが敵にスロウ効果を付与する。
- **E — ヘクステック レイ：** バイオメカニカルアームから「ヘクステック レイ」を発射し、一直線にフィールドを焼き払いながら、命中した敵ユニットにダメージを与える。 強化: 「ヘクステック レイ」が焼き払った地面が爆発し、魔法ダメージを与える。
- **R — アーケインストーム：** フィールド上に「アーケインストーム」を召喚し、魔法ダメージを与えて、敵の詠唱を中断させる。嵐は一定時間ごとに周囲のすべての敵に魔法ダメージを与え、ビクターが移動方向を変えられる。 強化: 「アーケインストーム」の移動速度が25%増加し、嵐でダメージを受けたチャンピオンが倒されるたびに嵐が大きくなり、効果時間が延長される。

<!-- power-spike:start -->
## パワースパイク

- **区分：** 終盤
- **判定：** [[wiki/syntheses/champion-power-spikes-v16-18-1|パワースパイク分類 v16.18.1]] に基づく原典ベースの推論。
- **根拠：**
  - 「ヘクス フラグメント」100個ごとにスキルを恒久的に強化する。
- **限界：** スキル基礎ダメージ・係数・アイテム完成時刻を全チャンピオンで統一比較できる原典値がないため、実戦の強さや購入優先度を断定しない。

<!-- power-spike:end -->

<!-- power-spike-match:start -->
## 試合時間別の観測

- **スナップショット：** 2026-09-15生成、キュー420、完全試合4,672件、[[reports/riot-ranked-match-analysis/run-20260915T010911Z/report|詳細レポート]]。
- **観測分類：** 中盤寄り
- **対象試合：** 408試合、全体勝率 50.7%
- **時間帯別勝率：** 〜20分 43.3%（n=67）、20〜25分 51.6%（n=64）、25〜30分 57.3%（n=82）、30〜35分 59.1%（n=93）、35分〜 42.2%（n=102）
- **最高帯：** 30〜35分（判定差 15.9ポイント）
- **判定根拠：** 中間帯が最高、端点との差 15.9%。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-112|ビクターの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### MIDDLE（729試合）

- **実測ビルド候補：** [[wiki/entities/items/item-2503|黒炎のトーチ]] + [[wiki/entities/items/item-3100|リッチ ベイン]]（該当n=41、65.9% / 非該当49.4%、差+16.4pt）；[[wiki/entities/items/item-4645|シャドウフレイム]] + [[wiki/entities/items/item-6653|ライアンドリーの仮面]]（該当n=35、65.7% / 非該当49.6%、差+16.1pt）
- **ステータス傾向：** 魔法防御（該当n=87、58.6% / 非該当49.2%、差+9.4pt）；物理防御（該当n=370、53.2% / 非該当47.4%、差+5.9pt）
- **理論仮説：** [[wiki/entities/items/item-3152|ヘクステック ロケットベルト]] + [[wiki/entities/items/item-6653|ライアンドリーの仮面]]（n=8（15未満）；共通stats: 魔力・体力／チャンピオン原典にも言及: 体力）；[[wiki/entities/items/item-3165|モレロノミコン]] + [[wiki/entities/items/item-6653|ライアンドリーの仮面]]（n=7（15未満）；共通stats: 魔力・体力／チャンピオン原典にも言及: 体力）

### BOTTOM（83試合）

- **実測ビルド候補：** 該当・非該当が各30試合以上で正の差を持つ候補なし。
- **ステータス傾向：** 物理防御（該当n=43、55.8% / 非該当47.5%、差+8.3pt）
- **理論仮説：** [[wiki/entities/items/item-3152|ヘクステック ロケットベルト]] + [[wiki/entities/items/item-6653|ライアンドリーの仮面]]（n=3（15未満）；共通stats: 魔力・体力／チャンピオン原典にも言及: 体力）；[[wiki/entities/items/item-6653|ライアンドリーの仮面]] + [[wiki/entities/items/item-6657|ロッド オブ エイジス]]（n=2（15未満）；共通stats: 魔力・体力／チャンピオン原典にも言及: 体力）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-112|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### MIDDLE（対象n=1,011）

- **高勝率コンボ候補（最大3件）：**
  - [[wiki/entities/champions/sivir|シヴィア（Sivir）]] — 対象側勝率70.3%（26/37）、n=37（十分性の目安を満たす）。
  - [[wiki/entities/champions/smolder|スモルダー（Smolder）]] — 対象側勝率67.6%（25/37）、n=37（十分性の目安を満たす）。
  - [[wiki/entities/champions/jhin|ジン（Jhin）]] — 対象側勝率61.6%（45/73）、n=73（十分性の目安を満たす）。
- **低勝率カウンターピック候補（最大3件）：**
  - [[wiki/entities/champions/ahri|アーリ（Ahri）]] — 対象側勝率40.3%（25/62）、n=62（十分性の目安を満たす）。
  - [[wiki/entities/champions/xerath|ゼラス（Xerath）]] — 対象側勝率45.9%（17/37）、n=37（十分性の目安を満たす）。
  - [[wiki/entities/champions/veigar|ベイガー（Veigar）]] — 対象側勝率51.2%（22/43）、n=43（十分性の目安を満たす）。

### BOTTOM（対象n=117）

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

### MIDDLE（対象905試合、全体勝率48.6%）

| 順位 | 完全ルーンセット | 選択数 | 選択率 | 選択時勝率 |
| ---: | --- | ---: | ---: | ---: |
| 1 | 主系魔道：死神の残り火／マナフローバンド・至高・追火；副系不滅：ボーンアーマー・シールドバッシュ；シャードUNKNOWN(5005)・UNKNOWN(5008)・UNKNOWN(5001) | 320/905 | 35.4% | 50.9% |
| 2 | 主系魔道：死神の残り火／マナフローバンド・至高・追火；副系不滅：シールドバッシュ・ボーンアーマー；シャードUNKNOWN(5005)・UNKNOWN(5008)・UNKNOWN(5001) | 73/905 | 8.1% | 43.8% |
| 3 | 主系魔道：死神の残り火／マナフローバンド・追い風・追火；副系栄華：切り崩し・レジェンド: ヘイスト；シャードUNKNOWN(5005)・UNKNOWN(5008)・UNKNOWN(5011) | 66/905 | 7.3% | 40.9% |

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
| MASTER | 5 | 171 | 1.7% | 82勝/89敗 | 48.0% |
| CHALLENGER | 5 | 174 | 1.7% | 82勝/92敗 | 47.1% |

<!-- champion-tier-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Viktor` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Viktor.png)
