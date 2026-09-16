---
title: "カタリナ"
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
  - role-mage
  - data-dragon
champion_id: "Katarina"
champion_key: "55"
data_version: "16.18.1"
roles:
  - "Assassin"
  - "Mage"
resource_type: "なし"
image_path: "raw/assets/champions/Katarina.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Katarina.png"
---

# カタリナ

![[raw/assets/champions/Katarina.png|128]]

## 基本情報

- **英字ID：** `Katarina`
- **キー：** `55`
- **称号：** 凶兆の刃
- **データversion：** `16.18.1`

## 紹介

優れた判断力と必殺の格闘技術を持つカタリナはノクサスで最強の暗殺者だ。有名なデュ・クートウ将軍の長女である彼女は悟られずに素早く敵を倒す才能で知られている。野心に燃える彼女は、時に味方に犠牲を強いる危険を冒してでも厳重に守られた標的を求めようとするが、どんな任務であっても、カタリナは鋸歯状の刃を持つ無数の短剣を振りかざしてためらうことなく自らの使命を全うする。

## 分類

- **役割タグ：** `Assassin`、`Mage`
- **リソース種別：** なし

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 4 |
| `defense` | 3 |
| `magic` | 9 |
| `difficulty` | 8 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 672 |
| `hpperlevel` | 108 |
| `mp` | 0 |
| `mpperlevel` | 0 |
| `movespeed` | 335 |
| `armor` | 32 |
| `armorperlevel` | 4.7 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 125 |
| `hpregen` | 7.5 |
| `hpregenperlevel` | 0.7 |
| `mpregen` | 0 |
| `mpregenperlevel` | 0 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 58 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2.74 |
| `attackspeed` | 0.658 |

## アビリティ

- **パッシブ — 貪欲なる暗殺者：** 自身がダメージを与えた敵チャンピオンがその直後にキルされると、自身の全スキルのクールダウンが大幅に短縮する。 自身が「短剣」を拾うと、周囲の敵を斬りつけて魔法ダメージを与える。

- **Q — バウンドナイフ：** カタリナが対象に向けて敵から敵へと飛び跳ねる「短剣」を投げる。「短剣」は最後に地面に落ちる。
- **W — プリペレーション：** 少しの間だけカタリナの移動速度が大幅に増加し、「短剣」を頭上に放り投げる。
- **E — 瞬歩：** 対象の地点へブリンクする。対象が敵ユニットなら攻撃し、そうでない場合はもっとも近くにいる敵ユニットを攻撃する。
- **R — デスロータス：** 刃の嵐と化し、周囲の敵チャンピオン(最大3人)に目にもとまらぬ速さで短剣を投げて強大な魔法ダメージを与える。

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
- **対象試合：** 189試合、全体勝率 44.4%
- **時間帯別勝率：** 〜20分 52.0%（n=25）、20〜25分 55.2%（n=29）、25〜30分 43.4%（n=53）、30〜35分 35.3%（n=51）、35分〜 45.2%（n=31）
- **最高帯：** 20〜25分（判定差 19.9ポイント）
- **判定根拠：** 最高帯と端点の差が8ポイント未満、または非単調。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-55|カタリナの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### MIDDLE（378試合）

- **実測ビルド候補：** [[wiki/entities/items/item-3041|メジャイ ソウルスティーラー]] + [[wiki/entities/items/item-3100|リッチ ベイン]]（該当n=32、75.0% / 非該当46.5%、差+28.5pt）；[[wiki/entities/items/item-3302|テルミヌス]] + [[wiki/entities/items/item-6672|クラーケン スレイヤー]]（該当n=35、65.7% / 非該当47.2%、差+18.5pt）
- **ステータス傾向：** 体力（該当n=285、51.2% / 非該当41.9%、差+9.3pt）；体力再生（該当n=38、55.3% / 非該当48.2%、差+7.0pt）
- **理論仮説：** [[wiki/entities/items/item-3087|スタティック シヴ]] + [[wiki/entities/items/item-6672|クラーケン スレイヤー]]（n=1（15未満）；共通stats: 攻撃力・攻撃速度・移動速度／チャンピオン原典にも言及: 移動速度）；[[wiki/entities/items/item-3172|ガンメタル ブーツ]] + [[wiki/entities/items/item-6672|クラーケン スレイヤー]]（n=2（15未満）；共通stats: 攻撃速度・移動速度／チャンピオン原典にも言及: 移動速度）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-55|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### MIDDLE（対象n=546）

- **高勝率コンボ候補（最大3件）：**
  - [[wiki/entities/champions/seraphine|セラフィーン（Seraphine）]] — 対象側勝率57.1%（20/35）、n=35（十分性の目安を満たす）。
  - [[wiki/entities/champions/miss-fortune|ミス・フォーチュン（MissFortune）]] — 対象側勝率53.8%（28/52）、n=52（十分性の目安を満たす）。
  - [[wiki/entities/champions/nautilus|ノーチラス（Nautilus）]] — 対象側勝率53.7%（22/41）、n=41（十分性の目安を満たす）。
- **低勝率カウンターピック候補（最大3件）：**
  - [[wiki/entities/champions/ahri|アーリ（Ahri）]] — 対象側勝率50.0%（21/42）、n=42（十分性の目安を満たす）。

### BOTTOM（対象n=24）

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

### MIDDLE（対象578試合、全体勝率49.7%）

| 順位 | 完全ルーンセット | 選択数 | 選択率 | 選択時勝率 |
| ---: | --- | ---: | ---: | ---: |
| 1 | 主系覇道：電撃／サドンインパクト・グリスリー メメント・執拗な賞金首狩り；副系栄華：最期の慈悲・凱旋；シャードUNKNOWN(5008)・UNKNOWN(5008)・UNKNOWN(5001) | 83/578 | 14.4% | 41.0% |
| 2 | 主系栄華：征服者／凱旋・レジェンド: 迅速・最期の慈悲；副系覇道：執拗な賞金首狩り・サドンインパクト；シャードUNKNOWN(5008)・UNKNOWN(5008)・UNKNOWN(5001) | 49/578 | 8.5% | 51.0% |
| 3 | 主系覇道：電撃／サドンインパクト・第六感・執拗な賞金首狩り；副系栄華：凱旋・最期の慈悲；シャードUNKNOWN(5008)・UNKNOWN(5008)・UNKNOWN(5011) | 33/578 | 5.7% | 39.4% |

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
| GRANDMASTER | 1 | 218 | 2.2% | 119勝/99敗 | 54.6% |

<!-- champion-tier-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Katarina` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Katarina.png)
