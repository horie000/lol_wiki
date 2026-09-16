---
title: "コグ＝マウ"
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
tags:
  - champion
  - role-marksman
  - role-mage
  - data-dragon
champion_id: "KogMaw"
champion_key: "96"
data_version: "16.18.1"
roles:
  - "Marksman"
  - "Mage"
resource_type: "マナ"
image_path: "raw/assets/champions/KogMaw.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/KogMaw.png"
---

# コグ＝マウ

![[raw/assets/champions/KogMaw.png|128]]

## 基本情報

- **英字ID：** `KogMaw`
- **キー：** `96`
- **称号：** 深淵のアギト
- **データversion：** `16.18.1`

## 紹介

イカシアの荒れ地の奥深くにあるヴォイドの浸食から生まれたコグ＝マウは腐食性の大きな口を持つ好奇心旺盛な腐敗した生物だ。このヴォイドの生物は周囲に存在するものを真に理解するためには、それをかじって唾をかける必要がある。本質的に悪意がある訳ではないが、コグ＝マウの愉快な無邪気さは危険であり、それは狂乱状態になって何かを食べようとする前触れだ──彼は生きるために食べているのではなく、尽きぬ好奇心を満たすために食べている。

## 分類

- **役割タグ：** `Marksman`、`Mage`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 8 |
| `defense` | 2 |
| `magic` | 5 |
| `difficulty` | 6 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 635 |
| `hpperlevel` | 99 |
| `mp` | 325 |
| `mpperlevel` | 40 |
| `movespeed` | 330 |
| `armor` | 24 |
| `armorperlevel` | 4.45 |
| `spellblock` | 33 |
| `spellblockperlevel` | 1.1 |
| `attackrange` | 500 |
| `hpregen` | 3.75 |
| `hpregenperlevel` | 0.55 |
| `mpregen` | 8.75 |
| `mpregenperlevel` | 0.7 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 61 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2.65 |
| `attackspeed` | 0.665 |

## アビリティ

- **パッシブ — イカシアの自爆：** 倒されてから4秒後、コグ＝マウは爆発して周囲の敵に確定ダメージを与える。

- **Q — 腐食粘液：** 苛性の粘液を飛ばし、対象に魔法ダメージを与え、物理防御と魔法防御を短時間低下させる。さらにコグ＝マウの攻撃速度が増加する。
- **W — 有機性魔力砲：** 通常攻撃の射程距離が増加し、対象の最大体力に比例した魔法ダメージ%i:OnHit%通常攻撃時効果を与える。
- **E — ヴォイド分泌液：** 敵を貫通する謎の粘液を発射し、命中した敵ユニットにダメージを与える。粘液は通過したエリアにしばらく残り、踏んだ敵にスロウ効果を付与する。
- **R — 生体空撃砲：** 射程の長い砲弾を発射して魔法ダメージ (体力が低い敵には大幅に増加) を与えるとともに、敵を可視状態にする。ただし、ステルス状態の敵の位置を把握することはできない。このスキルを短時間で連発すると、消費マナが増加する。

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
- **対象試合：** 76試合、全体勝率 47.4%
- **時間帯別勝率：** 〜20分 58.3%（n=12）、20〜25分 40.0%（n=10）、25〜30分 31.6%（n=19）、30〜35分 59.1%（n=22）、35分〜 46.2%（n=13）
- **最高帯：** 30〜35分（判定差 不明）
- **判定根拠：** 全5帯で各15試合未満の帯がある。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-96|コグ＝マウの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### BOTTOM（133試合）

- **実測ビルド候補：** [[wiki/entities/items/item-3085|ルナーン ハリケーン]] + [[wiki/entities/items/item-3124|グインソー レイジブレード]] + [[wiki/entities/items/item-3153|ルインドキング ブレード]]（該当n=30、76.7% / 非該当45.6%、差+31.0pt）；[[wiki/entities/items/item-3085|ルナーン ハリケーン]] + [[wiki/entities/items/item-3153|ルインドキング ブレード]]（該当n=46、69.6% / 非該当43.7%、差+25.9pt）
- **ステータス傾向：** 物理防御（該当n=33、69.7% / 非該当47.0%、差+22.7pt）；移動速度（該当n=103、57.3% / 非該当36.7%、差+20.6pt）
- **理論仮説：** [[wiki/entities/items/item-3087|スタティック シヴ]] + [[wiki/entities/items/item-3124|グインソー レイジブレード]]（n=2（15未満）；共通stats: 魔力・攻撃力・攻撃速度／チャンピオン原典にも言及: 魔力・攻撃力・攻撃速度）；[[wiki/entities/items/item-3087|スタティック シヴ]] + [[wiki/entities/items/item-6672|クラーケン スレイヤー]]（n=1（15未満）；共通stats: 攻撃力・攻撃速度・移動速度／チャンピオン原典にも言及: 攻撃力・攻撃速度）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-96|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### BOTTOM（対象n=180）

- **高勝率コンボ候補（最大3件）：**
  - [[wiki/entities/champions/lulu|ルル（Lulu）]] — 対象側勝率50.0%（16/32）、n=32（十分性の目安を満たす）。
- **低勝率カウンターピック候補（最大3件）：**
  - [[wiki/entities/champions/jinx|ジンクス（Jinx）]] — 対象側勝率42.1%（8/19）、サンプル不足（n=19、十分性の目安30未満）。
  - [[wiki/entities/champions/ashe|アッシュ（Ashe）]] — 対象側勝率57.7%（15/26）、サンプル不足（n=26、十分性の目安30未満）。

### MIDDLE（対象n=19）

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

### BOTTOM（対象36試合、全体勝率55.6%）

| 順位 | 完全ルーンセット | 選択数 | 選択率 | 選択時勝率 |
| ---: | --- | ---: | ---: | ---: |
| 1 | 主系栄華：リーサルテンポ／凱旋・レジェンド: 血脈・背水の陣；副系不滅：心身調整・超成長；シャードUNKNOWN(5005)・UNKNOWN(5008)・UNKNOWN(5001) | 8/36 | 22.2% | 50.0% |
| 2 | 主系魔道：秘儀の彗星／マナフローバンド・英気集中・追火；副系栄華：切り崩し・冷静沈着；シャードUNKNOWN(5005)・UNKNOWN(5008)・UNKNOWN(5011) | 4/36 | 11.1% | 0.0% |
| 3 | 主系天啓：ファーストストライク／キャッシュバック・トリプル トニック・なんでも屋；副系魔道：マナフローバンド・強まる嵐；シャードUNKNOWN(5008)・UNKNOWN(5008)・UNKNOWN(5001) | 2/36 | 5.6% | 100.0% |

- **選定ロール：** チャンピオン・ロール別の完全試合数が最も多いロールを1つ選んだ。別ロールや全候補は詳細レポートで確認できる。
- **シャード表示：** Data Dragonで表示名を解決できない場合は`UNKNOWN(<ID>)`としてIDを保持する。

- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-rune-selection|Riotランク戦試合データ：チャンピオン別ルーン選択]]、[[wiki/syntheses/champion-rune-selection-ranked-matches|実測チャンピオン別ルーン選択分析]]。
<!-- champion-rune-set-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.KogMaw` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/KogMaw.png)
