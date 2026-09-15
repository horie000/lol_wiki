---
title: "カイ＝サ"
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
  - role-marksman
  - role-mage
  - data-dragon
champion_id: "Kaisa"
champion_key: "145"
data_version: "16.18.1"
roles:
  - "Marksman"
  - "Mage"
resource_type: "マナ"
image_path: "raw/assets/champions/Kaisa.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Kaisa.png"
---

# カイ＝サ

![[raw/assets/champions/Kaisa.png|128]]

## 基本情報

- **英字ID：** `Kaisa`
- **キー：** `145`
- **称号：** 虚無を知る娘
- **データversion：** `16.18.1`

## 紹介

幼少期にヴォイドに囚われたカイ＝サは、不屈の精神と意志の力で生き延びた。経験を積んで卓越した狩人となった彼女であったが、一部の者にとってその存在は望まれぬ未来の先触れであった。不本意ながらヴォイド生命体の殻と共生関係を結んだカイ＝サ。自分を怪物と呼ぶ定命の者を許し、共に闇の勢力を打ち負かすのか、それとも他者のことなど忘れ、自分を置き去りにした世界をヴォイドに食い尽くさせるのか…彼女はやがて選択を迫られることになるだろう。

## 分類

- **役割タグ：** `Marksman`、`Mage`
- **リソース種別：** マナ

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
| `hp` | 640 |
| `hpperlevel` | 102 |
| `mp` | 345 |
| `mpperlevel` | 40 |
| `movespeed` | 335 |
| `armor` | 25 |
| `armorperlevel` | 4.2 |
| `spellblock` | 33 |
| `spellblockperlevel` | 1.1 |
| `attackrange` | 525 |
| `hpregen` | 4 |
| `hpregenperlevel` | 0.55 |
| `mpregen` | 8.2 |
| `mpregenperlevel` | 0.7 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 59 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 1.8 |
| `attackspeed` | 0.644 |

## アビリティ

- **パッシブ — ヴォイドスキン：** カイ＝サの通常攻撃はプラズマスタックを付与し、スタック数に応じて与える追加魔法ダメージが増加していく。味方の移動不能効果もプラズマスタックを付与する。さらに、アイテム購入によってアルティメット以外のスキルがアップグレードされる。

- **Q — イカシアの雨：** 多数のミサイルを乱射する。ミサイルは周囲の敵を追尾する。 共生兵器: 「イカシアの雨」がアップグレードされて、ミサイル数が増加する。
- **W — ヴォイドシーカー：** 遠距離ミサイルを発射して、命中した敵にプラズマスタックを付与する。 共生兵器: 「ヴォイドシーカー」がアップグレードされて、付与するスタック数が増加し、チャンピオンに当たるとクールダウンが短縮されるようになる。
- **E — スーパーチャージ：** 一時的に移動速度が増加し、その後攻撃速度が増加する。 共生兵器: 「スーパーチャージ」がアップグレードされて、一時的にインビジブル状態を獲得できるようになる。
- **R — キラーヴォイド：** 敵チャンピオンの近くまでダッシュする。

<!-- power-spike:start -->
## パワースパイク

- **区分：** 終盤
- **判定：** [[wiki/syntheses/champion-power-spikes-v16-18-1|パワースパイク分類 v16.18.1]] に基づく原典ベースの推論。
- **根拠：**
  - アイテム購入により通常スキルがアップグレードされる。
- **限界：** スキル基礎ダメージ・係数・アイテム完成時刻を全チャンピオンで統一比較できる原典値がないため、実戦の強さや購入優先度を断定しない。

<!-- power-spike:end -->

<!-- power-spike-match:start -->
## 試合時間別の観測

- **観測分類：** 序盤寄り
- **対象試合：** 554試合、全体勝率 46.2%
- **時間帯別勝率：** 〜20分 57.0%（n=86）、20〜25分 39.8%（n=83）、25〜30分 41.8%（n=134）、30〜35分 45.1%（n=122）、35分〜 48.8%（n=129）
- **最高帯：** 〜20分（判定差 8.1ポイント）
- **判定根拠：** 〜20分が最高、長時間帯との差 8.1%
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-145|カイ＝サの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### BOTTOM（1,123試合）

- **実測ビルド候補：** [[wiki/entities/items/item-3172|ガンメタル ブーツ]] + [[wiki/entities/items/item-6672|クラーケン スレイヤー]]（該当n=52、78.8% / 非該当46.7%、差+32.2pt）；[[wiki/entities/items/item-3124|グインソー レイジブレード]] + [[wiki/entities/items/item-3172|ガンメタル ブーツ]] + [[wiki/entities/items/item-6672|クラーケン スレイヤー]]（該当n=51、78.4% / 非該当46.7%、差+31.7pt）
- **ステータス傾向：** ライフスティール（該当n=104、66.3% / 非該当46.3%、差+20.0pt）；物理防御（該当n=455、54.7% / 非該当43.7%、差+11.0pt）
- **理論仮説：** [[wiki/entities/items/item-2512|フィーンドハンターの矢]] + [[wiki/entities/items/item-3046|ファントム ダンサー]]（n=1（15未満）；共通stats: 攻撃速度・クリティカル率・移動速度／チャンピオン原典にも言及: 攻撃速度・移動速度）；[[wiki/entities/items/item-3046|ファントム ダンサー]] + [[wiki/entities/items/item-6675|ナヴォリ フリッカーブレード]]（未観測；共通stats: 攻撃速度・クリティカル率・移動速度／チャンピオン原典にも言及: 攻撃速度・移動速度）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-145|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### BOTTOM（対象n=1,537）

- **高勝率コンボ候補（最大3件）：**
  - [[wiki/entities/champions/lulu|ルル（Lulu）]] — 対象側勝率66.7%（20/30）、n=30（十分性の目安を満たす）。
  - [[wiki/entities/champions/diana|ダイアナ（Diana）]] — 対象側勝率63.4%（26/41）、n=41（十分性の目安を満たす）。
  - [[wiki/entities/champions/leona|レオナ（Leona）]] — 対象側勝率59.1%（91/154）、n=154（十分性の目安を満たす）。
- **低勝率カウンターピック候補（最大3件）：**
  - [[wiki/entities/champions/lucian|ルシアン（Lucian）]] — 対象側勝率34.8%（16/46）、n=46（十分性の目安を満たす）。
  - [[wiki/entities/champions/jinx|ジンクス（Jinx）]] — 対象側勝率40.5%（49/121）、n=121（十分性の目安を満たす）。
  - [[wiki/entities/champions/miss-fortune|ミス・フォーチュン（MissFortune）]] — 対象側勝率40.9%（56/137）、n=137（十分性の目安を満たす）。

### MIDDLE（対象n=16）

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

### BOTTOM（対象2,444試合、全体勝率49.3%）

| 順位 | 完全ルーンセット | 選択数 | 選択率 | 選択時勝率 |
| ---: | --- | ---: | ---: | ---: |
| 1 | 主系栄華：リーサルテンポ／冷静沈着・レジェンド: 血脈・最期の慈悲；副系天啓：ビスケットデリバリー・魔法の靴；シャードUNKNOWN(5005)・UNKNOWN(5008)・UNKNOWN(5001) | 591/2,444 | 24.2% | 48.7% |
| 2 | 主系栄華：リーサルテンポ／凱旋・レジェンド: 血脈・切り崩し；副系天啓：キャッシュバック・トリプル トニック；シャードUNKNOWN(5005)・UNKNOWN(5008)・UNKNOWN(5011) | 237/2,444 | 9.7% | 52.3% |
| 3 | 主系栄華：リーサルテンポ／冷静沈着・レジェンド: 血脈・最期の慈悲；副系天啓：魔法の靴・ビスケットデリバリー；シャードUNKNOWN(5005)・UNKNOWN(5008)・UNKNOWN(5001) | 177/2,444 | 7.2% | 46.9% |

- **選定ロール：** チャンピオン・ロール別の完全試合数が最も多いロールを1つ選んだ。別ロールや全候補は詳細レポートで確認できる。
- **シャード表示：** Data Dragonで表示名を解決できない場合は`UNKNOWN(<ID>)`としてIDを保持する。

- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-rune-selection|Riotランク戦試合データ：チャンピオン別ルーン選択]]、[[wiki/syntheses/champion-rune-selection-ranked-matches|実測チャンピオン別ルーン選択分析]]。
<!-- champion-rune-set-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Kaisa` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Kaisa.png)
