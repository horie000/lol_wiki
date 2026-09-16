---
title: "トリンダメア"
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
champion_id: "Tryndamere"
champion_key: "23"
data_version: "16.18.1"
roles:
  - "Fighter"
  - "Assassin"
resource_type: "フューリー"
image_path: "raw/assets/champions/Tryndamere.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Tryndamere.png"
---

# トリンダメア

![[raw/assets/champions/Tryndamere.png|128]]

## 基本情報

- **英字ID：** `Tryndamere`
- **キー：** `23`
- **称号：** 孤高の蛮王
- **データversion：** `16.18.1`

## 紹介

決して鎮まることのない激しい怒りに駆り立てられたトリンダメアは、かつては暗雲のかかる未来に備えるために北部で最強の戦士たちに次々と戦いを挑み、フレヨルド中に知られる存在だった。この激怒する蛮族は何年も同胞を滅ぼした者への復讐を果たそうとしていたが、最近になってアヴァローサンの戦母、アッシュの仲間となり、彼女の部族と共に生活するようになった。彼の人間離れした腕力と精神力は伝説となっており、幾度となく絶対的に不利な状況を乗り越えて新たな仲間たちに勝利をもたらしている。

## 分類

- **役割タグ：** `Fighter`、`Assassin`
- **リソース種別：** フューリー

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 10 |
| `defense` | 5 |
| `magic` | 2 |
| `difficulty` | 5 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 696 |
| `hpperlevel` | 108 |
| `mp` | 100 |
| `mpperlevel` | 0 |
| `movespeed` | 345 |
| `armor` | 33 |
| `armorperlevel` | 4.8 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 175 |
| `hpregen` | 8.5 |
| `hpregenperlevel` | 0.9 |
| `mpregen` | 0 |
| `mpregenperlevel` | 0 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 66 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 3.4 |
| `attackspeed` | 0.67 |

## アビリティ

- **パッシブ — 戦場の咆哮：** 通常攻撃やクリティカル発生、敵にとどめを刺した際に「フューリー」がたまっていく。 自動効果: たまった「フューリー」の量に応じてクリティカル率が増加する。 たまった「フューリー」を消費して「血の欲望」を強化して発動できる。

- **Q — 血の欲望：** 戦闘で負傷するほど攻撃力が増加する。発動させるとたまっている「フューリー」を消費し、体力を回復する。
- **W — 嘲りの叫び：** 敵を嘲る言葉を叫び、周囲にいる敵チャンピオンの攻撃力を低下させる。トリンダメアに背を向けている敵は、移動速度も低下する。
- **E — スピンスラッシュ：** 指定地点へ回転しながら移動し、移動中に当たった敵ユニットにダメージを与える。
- **R — 不死の憤激：** 戦い続けたいという強い欲望に取りつかれ、一定時間はどれだけダメージを受けても体力がゼロにならない。

<!-- power-spike:start -->
## パワースパイク

- **区分：** 序盤
- **判定：** [[wiki/syntheses/champion-power-spikes-v16-18-1|パワースパイク分類 v16.18.1]] に基づく原典ベースの推論。
- **根拠：**
  - 基礎ステータス指数（体力・物理防御・攻撃力・移動速度を標準化して合算）が173件中6位（上位15%）。体力696、物理防御33、攻撃力66、移動速度345。
- **限界：** スキル基礎ダメージ・係数・アイテム完成時刻を全チャンピオンで統一比較できる原典値がないため、実戦の強さや購入優先度を断定しない。

<!-- power-spike:end -->

<!-- power-spike-match:start -->
## 試合時間別の観測

- **スナップショット：** 2026-09-15生成、キュー420、完全試合4,672件、[[reports/riot-ranked-match-analysis/run-20260915T010911Z/report|詳細レポート]]。
- **観測分類：** 明瞭な傾向なし
- **対象試合：** 151試合、全体勝率 49.0%
- **時間帯別勝率：** 〜20分 54.8%（n=31）、20〜25分 57.9%（n=19）、25〜30分 45.7%（n=35）、30〜35分 54.8%（n=31）、35分〜 37.1%（n=35）
- **最高帯：** 20〜25分（判定差 20.8ポイント）
- **判定根拠：** 最高帯と端点の差が8ポイント未満、または非単調。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-23|トリンダメアの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### TOP（250試合）

- **実測ビルド候補：** [[wiki/entities/items/item-3046|ファントム ダンサー]] + [[wiki/entities/items/item-3074|ラヴァナス ハイドラ]]（該当n=75、56.0% / 非該当46.3%、差+9.7pt）；[[wiki/entities/items/item-3046|ファントム ダンサー]] + [[wiki/entities/items/item-3153|ルインドキング ブレード]]（該当n=42、54.8% / 非該当48.1%、差+6.7pt）
- **ステータス傾向：** クリティカル率（該当n=212、49.5% / 非該当47.4%、差+2.2pt）
- **理論仮説：** [[wiki/entities/items/item-3046|ファントム ダンサー]] + [[wiki/entities/items/item-6675|ナヴォリ フリッカーブレード]]（n=12（15未満）；共通stats: 攻撃速度・クリティカル率・移動速度／チャンピオン原典にも言及: クリティカル率・移動速度）；[[wiki/entities/items/item-2512|フィーンドハンターの矢]] + [[wiki/entities/items/item-6675|ナヴォリ フリッカーブレード]]（n=1（15未満）；共通stats: 攻撃速度・クリティカル率・移動速度／チャンピオン原典にも言及: クリティカル率・移動速度）

### JUNGLE（67試合）

- **実測ビルド候補：** 該当・非該当が各30試合以上で正の差を持つ候補なし。
- **ステータス傾向：** 該当・非該当が各30試合以上で正の差を持つ群なし。
- **理論仮説：** [[wiki/entities/items/item-3087|スタティック シヴ]] + [[wiki/entities/items/item-6672|クラーケン スレイヤー]]（n=1（15未満）；共通stats: 攻撃力・攻撃速度・移動速度／チャンピオン原典にも言及: 攻撃力・移動速度）；[[wiki/entities/items/item-2512|フィーンドハンターの矢]] + [[wiki/entities/items/item-3046|ファントム ダンサー]]（n=1（15未満）；共通stats: 攻撃速度・クリティカル率・移動速度／チャンピオン原典にも言及: クリティカル率・移動速度）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-23|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### TOP（対象n=372）

- **高勝率コンボ候補（最大3件）：**
  - [[wiki/entities/champions/miss-fortune|ミス・フォーチュン（MissFortune）]] — 対象側勝率56.2%（18/32）、n=32（十分性の目安を満たす）。
  - [[wiki/entities/champions/ashe|アッシュ（Ashe）]] — 対象側勝率41.5%（17/41）、n=41（十分性の目安を満たす）。
- **低勝率カウンターピック候補（最大3件）：**
  - [[wiki/entities/champions/yorick|ヨリック（Yorick）]] — 対象側勝率34.6%（9/26）、サンプル不足（n=26、十分性の目安30未満）。
  - [[wiki/entities/champions/k-sante|カ・サンテ（KSante）]] — 対象側勝率44.4%（8/18）、サンプル不足（n=18、十分性の目安30未満）。
  - [[wiki/entities/champions/garen|ガレン（Garen）]] — 対象側勝率45.0%（9/20）、サンプル不足（n=20、十分性の目安30未満）。

### JUNGLE（対象n=73）

- **高勝率コンボ候補（最大3件）：**
  - [[wiki/entities/champions/mordekaiser|モルデカイザー（Mordekaiser）]] — 対象側勝率47.1%（8/17）、サンプル不足（n=17、十分性の目安30未満）。
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

### TOP（対象427試合、全体勝率53.4%）

| 順位 | 完全ルーンセット | 選択数 | 選択率 | 選択時勝率 |
| ---: | --- | ---: | ---: | ---: |
| 1 | 主系覇道：ヘイルブレード／サドンインパクト・グリスリー メメント・貪欲な賞金首狩り；副系栄華：背水の陣・レジェンド: 迅速；シャードUNKNOWN(5008)・UNKNOWN(5008)・UNKNOWN(5011) | 117/427 | 27.4% | 55.6% |
| 2 | 主系覇道：ヘイルブレード／サドンインパクト・グリスリー メメント・貪欲な賞金首狩り；副系栄華：レジェンド: 迅速・背水の陣；シャードUNKNOWN(5008)・UNKNOWN(5008)・UNKNOWN(5011) | 76/427 | 17.8% | 50.0% |
| 3 | 主系不滅：不死者の握撃／打ちこわし・息継ぎ・生気付与；副系栄華：背水の陣・レジェンド: 迅速；シャードUNKNOWN(5005)・UNKNOWN(5008)・UNKNOWN(5011) | 29/427 | 6.8% | 37.9% |

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
| DIAMOND | 4 | 173 | 1.7% | 93勝/80敗 | 53.8% |

<!-- champion-tier-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Tryndamere` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Tryndamere.png)
