---
title: "ツイステッド・フェイト"
type: entity
status: active
created: 2026-09-14
updated: 2026-09-15
sources:
  - "[[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]]"
  - "[[wiki/sources/src-2026-09-14-dragontail-16-18-1]]"
  - "[[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]"
  - "[[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis]]"
  - "[[wiki/sources/src-2026-09-15-riot-ranked-match-champion-matchups]]"
  - "[[wiki/sources/src-2026-09-15-riot-ranked-match-champion-rune-selection]]"
tags:
  - champion
  - role-mage
  - role-marksman
  - data-dragon
champion_id: "TwistedFate"
champion_key: "4"
data_version: "16.18.1"
roles:
  - "Mage"
  - "Marksman"
resource_type: "マナ"
image_path: "raw/assets/champions/TwistedFate.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/TwistedFate.png"
---

# ツイステッド・フェイト

![[raw/assets/champions/TwistedFate.png|128]]

## 基本情報

- **英字ID：** `TwistedFate`
- **キー：** `4`
- **称号：** 不敗のイカサマ師
- **データversion：** `16.18.1`

## 紹介

ツイステッド・フェイトは、世界中を渡り歩いては賭けとイカサマで成り上がってきた、悪名高きカード使いだ。金持ちから愚か者まで、嫌悪する者もいれば、惚れ込む者もいる。物事を真面目に受け止めることは滅多になく、嘲るような笑みと気怠げな足取りで迎えるのだ。そしていつでも、ありとあらゆる“切り札”をそでに忍ばせている。

## 分類

- **役割タグ：** `Mage`、`Marksman`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 6 |
| `defense` | 2 |
| `magic` | 6 |
| `difficulty` | 9 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 604 |
| `hpperlevel` | 108 |
| `mp` | 333 |
| `mpperlevel` | 39 |
| `movespeed` | 330 |
| `armor` | 24 |
| `armorperlevel` | 4.35 |
| `spellblock` | 30 |
| `spellblockperlevel` | 1.3 |
| `attackrange` | 525 |
| `hpregen` | 5.5 |
| `hpregenperlevel` | 0.6 |
| `mpregen` | 8 |
| `mpregenperlevel` | 0.8 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 52 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2.5 |
| `attackspeed` | 0.625 |

## アビリティ

- **パッシブ — イカサマダイス：** ユニットを1体倒すたびに「幸運のサイコロ」を振り、1～6の追加ゴールドを獲得する。

- **Q — ワイルドカード：** 扇状を描くように敵を貫通する3枚のカードが投げられ、命中した敵ユニットにそれぞれダメージを与える。
- **W — ドロー：** デッキから魔法のカードを1枚選び、次の通常攻撃に使用する。この通常攻撃には追加効果がつく。
- **E — スタックデッキ：** 通常攻撃4回ごとに追加ダメージがつき、攻撃速度が増加する。
- **R — デスティニー：** 敵の運命を予知し、敵のチャンピオン全員を可視状態にする。また、1.5秒後に指定位置へワープする「ゲート」を使用できるようになる。

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

- **観測分類：** 判定保留（分母不足）
- **対象試合：** 85試合、全体勝率 43.5%
- **時間帯別勝率：** 〜20分 53.8%（n=13）、20〜25分 50.0%（n=10）、25〜30分 48.1%（n=27）、30〜35分 42.1%（n=19）、35分〜 25.0%（n=16）
- **最高帯：** 〜20分（判定差 —）
- **判定根拠：** 5つの時間帯のいずれかで15試合未満のため、時間帯の比較を保留する。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-4|ツイステッド・フェイトの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### MIDDLE（242試合）

- **実測ビルド候補：** [[wiki/entities/items/item-3094|ラピッド ファイアキャノン]] + [[wiki/entities/items/item-3157|ゾーニャの砂時計]]（該当n=40、67.5% / 非該当45.0%、差+22.5pt）；[[wiki/entities/items/item-3094|ラピッド ファイアキャノン]] + [[wiki/entities/items/item-3100|リッチ ベイン]] + [[wiki/entities/items/item-3157|ゾーニャの砂時計]]（該当n=33、66.7% / 非該当45.9%、差+20.7pt）
- **ステータス傾向：** 物理防御（該当n=91、57.1% / 非該当43.7%、差+13.4pt）；攻撃速度（該当n=180、51.1% / 非該当41.9%、差+9.2pt）
- **理論仮説：** [[wiki/entities/items/item-3032|ユン・タル ワイルドアロー]] + [[wiki/entities/items/item-6672|クラーケン スレイヤー]]（n=4（15未満）；共通stats: 攻撃力・攻撃速度／チャンピオン原典にも言及: 攻撃力・攻撃速度）；[[wiki/entities/items/item-3153|ルインドキング ブレード]] + [[wiki/entities/items/item-6672|クラーケン スレイヤー]]（n=2（15未満）；共通stats: 攻撃力・攻撃速度／チャンピオン原典にも言及: 攻撃力・攻撃速度）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-4|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### MIDDLE（対象n=413）

- **高勝率コンボ候補（最大3件）：**
  - [[wiki/entities/champions/miss-fortune|ミス・フォーチュン（MissFortune）]] — 対象側勝率60.0%（18/30）、n=30（十分性の目安を満たす）。
  - [[wiki/entities/champions/leona|レオナ（Leona）]] — 対象側勝率50.0%（16/32）、n=32（十分性の目安を満たす）。
- **低勝率カウンターピック候補（最大3件）：**
  - [[wiki/entities/champions/akali|アカリ（Akali）]] — 対象側勝率27.8%（5/18）、サンプル不足（n=18、十分性の目安30未満）。
  - [[wiki/entities/champions/malzahar|マルザハール（Malzahar）]] — 対象側勝率39.3%（11/28）、サンプル不足（n=28、十分性の目安30未満）。
  - [[wiki/entities/champions/hwei|フェイ（Hwei）]] — 対象側勝率40.0%（6/15）、サンプル不足（n=15、十分性の目安30未満）。

### TOP（対象n=17）

- **高勝率コンボ候補（最大3件）：** n=15以上の味方組み合わせなし。サンプル不足のため判断保留。
- **低勝率カウンターピック候補（最大3件）：** n=15以上の同ロール対面なし。サンプル不足のため判断保留。

> [!warning] 実測値の限界
> 味方ペアは同一試合・同一チームで同時に出場した組み合わせ、対面はMatch-v5の最終ロールから推定した同ロール候補である。パッチ、観測ランク帯、プレイヤー、試合展開、構成の交絡を調整していない。とくにサンプル不足の行は探索的な参考値に留める。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-matchups]]、[[wiki/syntheses/champion-combo-counter-ranked-matches|実測コンボ・カウンターピック分析]]
<!-- champion-matchup-analysis:end -->

<!-- champion-rune-set-analysis:start -->
## よく選ばれるルーンセット（実測）

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合20,010件、[[reports/riot-ranked-match-analysis/run-20260915T103154Z/report|ルーンセットの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-rune-selection|Riotランク戦試合データ：チャンピオン別ルーン選択]]、[[wiki/syntheses/champion-rune-selection-ranked-matches|実測チャンピオン別ルーン選択分析]]。
- **読み方：** 主系・キーストーン・主系3枠・副系2枠・3シャードが完全一致する組み合わせを、同じチャンピオン・正規化ロールの参加者を分母に集計した。選択時勝率は記述統計であり、因果効果や推奨を示さない。

### MIDDLE（対象592試合、全体勝率48.6%）

| 順位 | 完全ルーンセット | 選択数 | 選択率 | 選択時勝率 |
| ---: | --- | ---: | ---: | ---: |
| 1 | 主系魔道：秘儀の彗星／マナフローバンド・追い風・追火；副系不滅：ボーンアーマー・気迫；シャードUNKNOWN(5005)・UNKNOWN(5010)・UNKNOWN(5011) | 124/592 | 20.9% | 43.5% |
| 2 | 主系天啓：解放の魔導書／キャッシュバック・ビスケットデリバリー・なんでも屋；副系不滅：ボーンアーマー・気迫；シャードUNKNOWN(5005)・UNKNOWN(5010)・UNKNOWN(5011) | 32/592 | 5.4% | 53.1% |
| 3 | 主系覇道：電撃／血の味わい・グリスリー メメント・貪欲な賞金首狩り；副系不滅：ボーンアーマー・超成長；シャードUNKNOWN(5005)・UNKNOWN(5008)・UNKNOWN(5011) | 28/592 | 4.7% | 60.7% |

- **選定ロール：** チャンピオン・ロール別の完全試合数が最も多いロールを1つ選んだ。別ロールや全候補は詳細レポートで確認できる。
- **シャード表示：** Data Dragonで表示名を解決できない場合は`UNKNOWN(<ID>)`としてIDを保持する。

- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-rune-selection|Riotランク戦試合データ：チャンピオン別ルーン選択]]、[[wiki/syntheses/champion-rune-selection-ranked-matches|実測チャンピオン別ルーン選択分析]]。
<!-- champion-rune-set-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.TwistedFate` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/TwistedFate.png)
