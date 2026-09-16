---
title: "ヨネ"
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
champion_id: "Yone"
champion_key: "777"
data_version: "16.18.1"
roles:
  - "Fighter"
  - "Assassin"
resource_type: "つむじ風"
image_path: "raw/assets/champions/Yone.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Yone.png"
---

# ヨネ

![[raw/assets/champions/Yone.png|128]]

## 基本情報

- **英字ID：** `Yone`
- **キー：** `777`
- **称号：** 忘られざる者
- **データversion：** `16.18.1`

## 紹介

生前、ヨネはヤスオの腹違いの兄であり、村の剣術道場で名を知られた生徒だった。しかし弟の手で殺されたヨネは、霊界の邪悪な存在に狙われ、その悪しき者が持っていた刀を使って殺すことを余儀なくされた。そして悪魔の仮面を被る呪いにかけられたヨネは、自らが何者に変わったのかを理解するために、そうした邪悪な存在を飽くことなく狩り続けている。

## 分類

- **役割タグ：** `Fighter`、`Assassin`
- **リソース種別：** つむじ風

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 8 |
| `defense` | 4 |
| `magic` | 4 |
| `difficulty` | 8 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 620 |
| `hpperlevel` | 105 |
| `mp` | 500 |
| `mpperlevel` | 0 |
| `movespeed` | 345 |
| `armor` | 33 |
| `armorperlevel` | 4.6 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 175 |
| `hpregen` | 7.5 |
| `hpregenperlevel` | 0.75 |
| `mpregen` | 0 |
| `mpregenperlevel` | 0 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 62 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 3.5 |
| `attackspeed` | 0.625 |

## アビリティ

- **パッシブ — 狩鬼道：** 通常攻撃2回ごとに魔法ダメージを与える。さらに、クリティカル率が増加する。

- **Q — 斬命刀：** 前方に突きを放ち、直線上の敵すべてにダメージを与える。 このスキルが命中すると「つむじ風」のスタックを数秒間得る。2スタックになると、「斬命刀」を使用した際、一陣の風をまとって前方にダッシュし、敵をノックアップさせる。
- **W — 霊断刀：** 前方をなぎ払い、扇状の範囲内にいるすべての敵にダメージを与え、シールドを獲得する。シールド量はなぎ払いが命中したチャンピオンの数に応じて増加する。 攻撃速度が増加すると「霊断刀」のクールダウンと詠唱時間が短縮される。
- **E — 縛魂の解放：** 自身の霊魂が肉体を離れ、移動速度が増加する。スキル終了時にこの霊魂は肉体に強制的に戻り、霊魂として与えたダメージの一部をもう一度与える。
- **R — 冥封一閃：** 直線上の最後にいるチャンピオンの背後に強力な斬撃を与えてブリンクし、当たった敵すべてを自身の方向に引き寄せる。

<!-- power-spike:start -->
## パワースパイク

- **区分：** 終盤
- **判定：** [[wiki/syntheses/champion-power-spikes-v16-18-1|パワースパイク分類 v16.18.1]] に基づく原典ベースの推論。
- **根拠：**
  - パッシブでクリティカル率が増加し、攻撃速度はWのクールダウンと詠唱時間に影響する。
- **限界：** スキル基礎ダメージ・係数・アイテム完成時刻を全チャンピオンで統一比較できる原典値がないため、実戦の強さや購入優先度を断定しない。

<!-- power-spike:end -->

<!-- power-spike-match:start -->
## 試合時間別の観測

- **スナップショット：** 2026-09-15生成、キュー420、完全試合4,672件、[[reports/riot-ranked-match-analysis/run-20260915T010911Z/report|詳細レポート]]。
- **観測分類：** 明瞭な傾向なし
- **対象試合：** 1,109試合、全体勝率 48.2%
- **時間帯別勝率：** 〜20分 49.5%（n=192）、20〜25分 47.8%（n=159）、25〜30分 46.4%（n=265）、30〜35分 51.8%（n=251）、35分〜 45.5%（n=242）
- **最高帯：** 30〜35分（判定差 6.3ポイント）
- **判定根拠：** 最高帯と端点の差が8ポイント未満、または非単調。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-777|ヨネの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### MIDDLE（1,187試合）

- **実測ビルド候補：** [[wiki/entities/items/item-3031|インフィニティ エッジ]] + [[wiki/entities/items/item-3033|モータル リマインダー]] + [[wiki/entities/items/item-3153|ルインドキング ブレード]]（該当n=31、67.7% / 非該当49.2%、差+18.5pt）；[[wiki/entities/items/item-3031|インフィニティ エッジ]] + [[wiki/entities/items/item-3153|ルインドキング ブレード]] + [[wiki/entities/items/item-6333|デス ダンス]]（該当n=68、66.2% / 非該当48.7%、差+17.5pt）
- **ステータス傾向：** 移動速度（該当n=1147、50.4% / 非該当30.0%、差+20.4pt）；クリティカル率（該当n=1007、52.0% / 非該当36.7%、差+15.4pt）
- **理論仮説：** [[wiki/entities/items/item-3046|ファントム ダンサー]] + [[wiki/entities/items/item-6675|ナヴォリ フリッカーブレード]]（未観測；共通stats: 攻撃速度・クリティカル率・移動速度／チャンピオン原典にも言及: 攻撃速度・クリティカル率・移動速度）；[[wiki/entities/items/item-2512|フィーンドハンターの矢]] + [[wiki/entities/items/item-6675|ナヴォリ フリッカーブレード]]（未観測；共通stats: 攻撃速度・クリティカル率・移動速度／チャンピオン原典にも言及: 攻撃速度・クリティカル率・移動速度）

### TOP（716試合）

- **実測ビルド候補：** [[wiki/entities/items/item-3026|ガーディアン エンジェル]] + [[wiki/entities/items/item-6673|イモータル シールドボウ]]（該当n=37、67.6% / 非該当46.8%、差+20.7pt）；[[wiki/entities/items/item-3026|ガーディアン エンジェル]] + [[wiki/entities/items/item-3153|ルインドキング ブレード]] + [[wiki/entities/items/item-6673|イモータル シールドボウ]]（該当n=34、67.6% / 非該当46.9%、差+20.7pt）
- **ステータス傾向：** クリティカル率（該当n=604、50.8% / 非該当32.1%、差+18.7pt）；魔法防御（該当n=70、60.0% / 非該当46.6%、差+13.4pt）
- **理論仮説：** [[wiki/entities/items/item-3046|ファントム ダンサー]] + [[wiki/entities/items/item-6675|ナヴォリ フリッカーブレード]]（未観測；共通stats: 攻撃速度・クリティカル率・移動速度／チャンピオン原典にも言及: 攻撃速度・クリティカル率・移動速度）；[[wiki/entities/items/item-3031|インフィニティ エッジ]] + [[wiki/entities/items/item-3036|ドミニク リガード]]（n=14（15未満）；共通stats: 攻撃力・クリティカル率／チャンピオン原典にも言及: 攻撃力・クリティカル率）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-777|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### MIDDLE（対象n=1,454）

- **高勝率コンボ候補（最大3件）：**
  - [[wiki/entities/champions/jarvan-iv|ジャーヴァンⅣ（JarvanIV）]] — 対象側勝率72.7%（24/33）、n=33（十分性の目安を満たす）。
  - [[wiki/entities/champions/rell|レル（Rell）]] — 対象側勝率66.7%（32/48）、n=48（十分性の目安を満たす）。
  - [[wiki/entities/champions/leona|レオナ（Leona）]] — 対象側勝率55.6%（74/133）、n=133（十分性の目安を満たす）。
- **低勝率カウンターピック候補（最大3件）：**
  - [[wiki/entities/champions/sylas|サイラス（Sylas）]] — 対象側勝率46.3%（38/82）、n=82（十分性の目安を満たす）。
  - [[wiki/entities/champions/viktor|ビクター（Viktor）]] — 対象側勝率46.4%（26/56）、n=56（十分性の目安を満たす）。
  - [[wiki/entities/champions/akali|アカリ（Akali）]] — 対象側勝率47.5%（47/99）、n=99（十分性の目安を満たす）。

### TOP（対象n=882）

- **高勝率コンボ候補（最大3件）：**
  - [[wiki/entities/champions/galio|ガリオ（Galio）]] — 対象側勝率69.0%（29/42）、n=42（十分性の目安を満たす）。
  - [[wiki/entities/champions/leona|レオナ（Leona）]] — 対象側勝率56.2%（45/80）、n=80（十分性の目安を満たす）。
  - [[wiki/entities/champions/miss-fortune|ミス・フォーチュン（MissFortune）]] — 対象側勝率50.0%（48/96）、n=96（十分性の目安を満たす）。
- **低勝率カウンターピック候補（最大3件）：**
  - [[wiki/entities/champions/ambessa|アンベッサ（Ambessa）]] — 対象側勝率26.7%（8/30）、n=30（十分性の目安を満たす）。
  - [[wiki/entities/champions/darius|ダリウス（Darius）]] — 対象側勝率34.3%（12/35）、n=35（十分性の目安を満たす）。
  - [[wiki/entities/champions/sett|セト（Sett）]] — 対象側勝率41.7%（15/36）、n=36（十分性の目安を満たす）。

> [!warning] 実測値の限界
> 味方ペアは同一試合・同一チームで同時に出場した組み合わせ、対面はMatch-v5の最終ロールから推定した同ロール候補である。パッチ、観測ランク帯、プレイヤー、試合展開、構成の交絡を調整していない。とくにサンプル不足の行は探索的な参考値に留める。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-matchups]]、[[wiki/syntheses/champion-combo-counter-ranked-matches|実測コンボ・カウンターピック分析]]
<!-- champion-matchup-analysis:end -->

<!-- champion-rune-set-analysis:start -->
## よく選ばれるルーンセット（実測）

- **スナップショット：** 2026-09-16生成、キュー420、ユニーク試合10,000件、[[reports/riot-ranked-match-analysis/run-20260916T081004Z/report|ルーンセットの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-rune-selection|Riotランク戦試合データ：チャンピオン別ルーン選択]]、[[wiki/syntheses/champion-rune-selection-ranked-matches|実測チャンピオン別ルーン選択分析]]。
- **読み方：** 主系・キーストーン・主系3枠・副系2枠・3シャードが完全一致する組み合わせを、同じチャンピオン・正規化ロールの参加者を分母に集計した。選択時勝率は記述統計であり、因果効果や推奨を示さない。

### MIDDLE（対象919試合、全体勝率48.4%）

| 順位 | 完全ルーンセット | 選択数 | 選択率 | 選択時勝率 |
| ---: | --- | ---: | ---: | ---: |
| 1 | 主系栄華：リーサルテンポ／体力吸収・レジェンド: 迅速・背水の陣；副系不滅：超成長・息継ぎ；シャードUNKNOWN(5005)・UNKNOWN(5008)・UNKNOWN(5001) | 293/919 | 31.9% | 44.0% |
| 2 | 主系栄華：フリートフットワーク／体力吸収・レジェンド: 迅速・背水の陣；副系不滅：超成長・息継ぎ；シャードUNKNOWN(5005)・UNKNOWN(5008)・UNKNOWN(5001) | 112/919 | 12.2% | 50.0% |
| 3 | 主系栄華：リーサルテンポ／体力吸収・レジェンド: 迅速・背水の陣；副系不滅：息継ぎ・超成長；シャードUNKNOWN(5005)・UNKNOWN(5008)・UNKNOWN(5001) | 76/919 | 8.3% | 52.6% |

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
| IRON | 1 | 294 | 2.9% | 139勝/155敗 | 47.3% |
| BRONZE | 1 | 303 | 3.0% | 139勝/164敗 | 45.9% |
| SILVER | 1 | 223 | 2.2% | 107勝/116敗 | 48.0% |
| PLATINUM | 3 | 183 | 1.8% | 94勝/89敗 | 51.4% |
| EMERALD | 5 | 137 | 1.4% | 61勝/76敗 | 44.5% |

<!-- champion-tier-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Yone` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Yone.png)
