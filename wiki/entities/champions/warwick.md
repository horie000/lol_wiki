---
title: "ワーウィック"
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
  - role-tank
  - data-dragon
champion_id: "Warwick"
champion_key: "19"
data_version: "16.18.1"
roles:
  - "Fighter"
  - "Tank"
resource_type: "マナ"
image_path: "raw/assets/champions/Warwick.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Warwick.png"
---

# ワーウィック

![[raw/assets/champions/Warwick.png|128]]

## 基本情報

- **英字ID：** `Warwick`
- **キー：** `19`
- **称号：** 解き放たれたゾウンの激憤
- **データversion：** `16.18.1`

## 紹介

ワーウィックはゾウンの灰色の路地を徘徊する怪物だ。苦痛を伴う実験によって変性した彼の肉体に融合された、ポンプやシリンダーで構成された複雑なシステムが、錬金術的に合成された憤怒を彼の血流に送り込んでいる。物陰から飛び出しては、都市の深部を脅かしている犯罪者を餌食とするのだ。ワーウィックは血に引き寄せられ、その匂いは彼の正気を失わせる。血を流す者は、決して彼から逃れることはできない。

## 分類

- **役割タグ：** `Fighter`、`Tank`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 9 |
| `defense` | 5 |
| `magic` | 3 |
| `difficulty` | 3 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 620 |
| `hpperlevel` | 99 |
| `mp` | 280 |
| `mpperlevel` | 35 |
| `movespeed` | 335 |
| `armor` | 33 |
| `armorperlevel` | 4.4 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 125 |
| `hpregen` | 4 |
| `hpregenperlevel` | 0.75 |
| `mpregen` | 7.45 |
| `mpregenperlevel` | 0.6 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 65 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2 |
| `attackspeed` | 0.638 |

## アビリティ

- **パッシブ — 永遠の渇き：** 通常攻撃が追加魔法ダメージを与える。自身の体力が50%未満の場合、追加魔法ダメージと同量の体力を回復する。自身の体力が25%未満の場合、この回復効果は3倍になる。

- **Q — 野獣の牙：** 前方にダッシュして対象に噛みつき、対象の最大体力に応じたダメージを与え、与えたダメージに応じて自身の体力を回復する。
- **W — 血の追跡：** 体力が50%未満の敵ユニットを感知して、その敵ユニットに向かう際に移動速度と攻撃速度が増加する。その敵ユニットの体力が25%未満に低下した場合は、ワーウィックが狂乱状態になってこれらの効果が3倍になる。
- **E — 怒りの咆哮：** 2.5秒間、受けるダメージが減少する。効果の終了時、またはスキルを再発動すると、咆哮をあげて周囲の敵ユニットを1秒間逃走させる。
- **R — 絶狼牙連撃：** 指定方向にジャンプして、最初に接触した敵チャンピオンに1.5秒間サプレッション効果を与える(増加した移動速度に応じて射程が拡大)。

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
- **対象試合：** 314試合、全体勝率 51.3%
- **時間帯別勝率：** 〜20分 40.4%（n=47）、20〜25分 52.1%（n=48）、25〜30分 53.7%（n=67）、30〜35分 55.1%（n=78）、35分〜 51.4%（n=74）
- **最高帯：** 30〜35分（判定差 14.7ポイント）
- **判定根拠：** 最高帯と端点の差が8ポイント未満、または非単調。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-19|ワーウィックの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### JUNGLE（480試合）

- **実測ビルド候補：** [[wiki/entities/items/item-3053|ステラックの篭手]] + [[wiki/entities/items/item-3153|ルインドキング ブレード]]（該当n=30、60.0% / 非該当49.8%、差+10.2pt）；[[wiki/entities/items/item-3065|スピリット ビサージュ]] + [[wiki/entities/items/item-3075|ソーンメイル]]（該当n=60、58.3% / 非該当49.3%、差+9.0pt）
- **ステータス傾向：** ライフスティール（該当n=389、53.2% / 非該当38.5%、差+14.8pt）；魔法防御（該当n=286、53.1% / 非該当46.4%、差+6.8pt）
- **理論仮説：** [[wiki/entities/items/item-3073|実験的ヘクスプレート]] + [[wiki/entities/items/item-6631|ストライドブレイカー]]（n=2（15未満）；共通stats: 攻撃力・攻撃速度・体力／チャンピオン原典にも言及: 攻撃力・攻撃速度・体力）；[[wiki/entities/items/item-3087|スタティック シヴ]] + [[wiki/entities/items/item-6672|クラーケン スレイヤー]]（n=1（15未満）；共通stats: 攻撃力・攻撃速度・移動速度／チャンピオン原典にも言及: 攻撃力・攻撃速度・移動速度）

### TOP（129試合）

- **実測ビルド候補：** [[wiki/entities/items/item-3153|ルインドキング ブレード]] + [[wiki/entities/items/item-6631|ストライドブレイカー]]（該当n=62、54.8% / 非該当37.3%、差+17.5pt）
- **ステータス傾向：** 魔法防御（該当n=61、54.1% / 非該当38.2%、差+15.9pt）
- **理論仮説：** [[wiki/entities/items/item-3078|トリニティ フォース]] + [[wiki/entities/items/item-6631|ストライドブレイカー]]（n=1（15未満）；共通stats: 攻撃力・攻撃速度・体力／チャンピオン原典にも言及: 攻撃力・攻撃速度・体力）；[[wiki/entities/items/item-3073|実験的ヘクスプレート]] + [[wiki/entities/items/item-6631|ストライドブレイカー]]（未観測；共通stats: 攻撃力・攻撃速度・体力／チャンピオン原典にも言及: 攻撃力・攻撃速度・体力）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-19|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### JUNGLE（対象n=584）

- **高勝率コンボ候補（最大3件）：**
  - [[wiki/entities/champions/yorick|ヨリック（Yorick）]] — 対象側勝率76.7%（23/30）、n=30（十分性の目安を満たす）。
  - [[wiki/entities/champions/malzahar|マルザハール（Malzahar）]] — 対象側勝率67.7%（21/31）、n=31（十分性の目安を満たす）。
  - [[wiki/entities/champions/caitlyn|ケイトリン（Caitlyn）]] — 対象側勝率66.7%（26/39）、n=39（十分性の目安を満たす）。
- **低勝率カウンターピック候補（最大3件）：**
  - [[wiki/entities/champions/nocturne|ノクターン（Nocturne）]] — 対象側勝率52.9%（18/34）、n=34（十分性の目安を満たす）。

### TOP（対象n=188）

- **高勝率コンボ候補（最大3件）：**
  - [[wiki/entities/champions/ashe|アッシュ（Ashe）]] — 対象側勝率46.7%（7/15）、サンプル不足（n=15、十分性の目安30未満）。
  - [[wiki/entities/champions/nautilus|ノーチラス（Nautilus）]] — 対象側勝率37.5%（6/16）、サンプル不足（n=16、十分性の目安30未満）。
- **低勝率カウンターピック候補（最大3件）：**
  - [[wiki/entities/champions/mordekaiser|モルデカイザー（Mordekaiser）]] — 対象側勝率44.0%（11/25）、サンプル不足（n=25、十分性の目安30未満）。

> [!warning] 実測値の限界
> 味方ペアは同一試合・同一チームで同時に出場した組み合わせ、対面はMatch-v5の最終ロールから推定した同ロール候補である。パッチ、観測ランク帯、プレイヤー、試合展開、構成の交絡を調整していない。とくにサンプル不足の行は探索的な参考値に留める。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-matchups]]、[[wiki/syntheses/champion-combo-counter-ranked-matches|実測コンボ・カウンターピック分析]]
<!-- champion-matchup-analysis:end -->

<!-- champion-rune-set-analysis:start -->
## よく選ばれるルーンセット（実測）

- **スナップショット：** 2026-09-16生成、キュー420、ユニーク試合10,000件、[[reports/riot-ranked-match-analysis/run-20260916T081004Z/report|ルーンセットの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-rune-selection|Riotランク戦試合データ：チャンピオン別ルーン選択]]、[[wiki/syntheses/champion-rune-selection-ranked-matches|実測チャンピオン別ルーン選択分析]]。
- **読み方：** 主系・キーストーン・主系3枠・副系2枠・3シャードが完全一致する組み合わせを、同じチャンピオン・正規化ロールの参加者を分母に集計した。選択時勝率は記述統計であり、因果効果や推奨を示さない。

### JUNGLE（対象284試合、全体勝率50.7%）

| 順位 | 完全ルーンセット | 選択数 | 選択率 | 選択時勝率 |
| ---: | --- | ---: | ---: | ---: |
| 1 | 主系栄華：リーサルテンポ／凱旋・レジェンド: 迅速・背水の陣；副系魔道：追い風・水走り；シャードUNKNOWN(5005)・UNKNOWN(5008)・UNKNOWN(5001) | 134/284 | 47.2% | 50.0% |
| 2 | 主系栄華：プレスアタック／凱旋・レジェンド: 迅速・背水の陣；副系魔道：追い風・水走り；シャードUNKNOWN(5005)・UNKNOWN(5008)・UNKNOWN(5001) | 33/284 | 11.6% | 51.5% |
| 3 | 主系栄華：プレスアタック／凱旋・レジェンド: 迅速・背水の陣；副系覇道：グリスリー メメント・執拗な賞金首狩り；シャードUNKNOWN(5005)・UNKNOWN(5008)・UNKNOWN(5001) | 13/284 | 4.6% | 61.5% |

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
| IRON | 3 | 48 | 33勝/15敗 | 68.8% |

<!-- champion-tier-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Warwick` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Warwick.png)
