---
title: "フィドルスティックス"
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
  - role-support
  - data-dragon
champion_id: "Fiddlesticks"
champion_key: "9"
data_version: "16.18.1"
roles:
  - "Mage"
  - "Support"
resource_type: "マナ"
image_path: "raw/assets/champions/Fiddlesticks.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Fiddlesticks.png"
---

# フィドルスティックス

![[raw/assets/champions/Fiddlesticks.png|128]]

## 基本情報

- **英字ID：** `Fiddlesticks`
- **キー：** `9`
- **称号：** 古の恐怖
- **データversion：** `16.18.1`

## 紹介

ルーンテラの中で何かが目覚めた──古代の恐ろしい何かが。フィドルスティックスとして知られる永遠の恐怖は文明の僻地をうろつき、疑心暗鬼にさいなまれた地域に引き寄せられると、恐怖に怯える犠牲者たちを貪る。ギザギザの刃を持つ鎌をその手に、か細いガラクタを寄せ集めてできたクリーチャーは恐怖そのものを刈り取る。そして、生き延びることの方が不運だと思わせるほどに、精神を粉々に砕く。カラスの鳴き声や、人間のような姿をした何かの囁きが聞こえたら注意しなければいけない…フィドルスティックスが戻ってきたのだから。

## 分類

- **役割タグ：** `Mage`、`Support`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 2 |
| `defense` | 3 |
| `magic` | 9 |
| `difficulty` | 9 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 650 |
| `hpperlevel` | 106 |
| `mp` | 500 |
| `mpperlevel` | 28 |
| `movespeed` | 335 |
| `armor` | 34 |
| `armorperlevel` | 4.7 |
| `spellblock` | 30 |
| `spellblockperlevel` | 1.3 |
| `attackrange` | 480 |
| `hpregen` | 5.5 |
| `hpregenperlevel` | 0.6 |
| `mpregen` | 8 |
| `mpregenperlevel` | 0.8 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 55 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2.11 |
| `attackspeed` | 0.625 |

## アビリティ

- **パッシブ — 無害なカカシ：** トリンケットが「身代わり人形」に置き換わる。

- **Q — テラー：** 敵に見られていない状態からスキルで敵にダメージを与えるか、「テラー」の発動効果の対象に敵を指定すると、対象にフィアー効果を与えて一定時間逃走させる。
- **W — 豊かな収穫：** 周囲の敵から体力を奪い、効果時間終了時に対象の減少体力に応じた追加ダメージを与える。
- **E — 刈り取り：** 一定範囲を鎌で斬りつけて、命中したすべての敵にスロウ効果を与える。また、範囲の中心にいた敵にはサイレンス効果を与える。
- **R — クロウストーム：** 自身の周囲に凶暴なカラスの群れを集め、効果範囲内の敵ユニット全員に毎秒ダメージを与える。

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
- **対象試合：** 97試合、全体勝率 46.4%
- **時間帯別勝率：** 〜20分 35.7%（n=14）、20〜25分 30.0%（n=10）、25〜30分 38.9%（n=18）、30〜35分 52.0%（n=25）、35分〜 56.7%（n=30）
- **最高帯：** 35分〜（判定差 —）
- **判定根拠：** 5つの時間帯のいずれかで15試合未満のため、時間帯の比較を保留する。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-9|フィドルスティックスの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### JUNGLE（157試合）

- **実測ビルド候補：** [[wiki/entities/items/item-3157|ゾーニャの砂時計]] + [[wiki/entities/items/item-4645|シャドウフレイム]]（該当n=30、63.3% / 非該当43.3%、差+20.0pt）；[[wiki/entities/items/item-3118|マリグナンス]] + [[wiki/entities/items/item-4645|シャドウフレイム]]（該当n=30、60.0% / 非該当44.1%、差+15.9pt）
- **ステータス傾向：** マナ（該当n=95、49.5% / 非該当43.5%、差+5.9pt）；物理防御（該当n=100、49.0% / 非該当43.9%、差+5.1pt）
- **理論仮説：** [[wiki/entities/items/item-3152|ヘクステック ロケットベルト]] + [[wiki/entities/items/item-6653|ライアンドリーの仮面]]（n=8（15未満）；共通stats: 魔力・体力／チャンピオン原典にも言及: 体力）；[[wiki/entities/items/item-3041|メジャイ ソウルスティーラー]] + [[wiki/entities/items/item-6653|ライアンドリーの仮面]]（n=6（15未満）；共通stats: 魔力・体力／チャンピオン原典にも言及: 体力）

### UTILITY（36試合）

- **実測ビルド候補：** 該当・非該当が各30試合以上で正の差を持つ候補なし。
- **ステータス傾向：** 該当・非該当が各30試合以上で正の差を持つ群なし。
- **理論仮説：** [[wiki/entities/items/item-3050|ジーク コンバージェンス]] + [[wiki/entities/items/item-3190|ソラリのロケット]]（n=2（15未満）；共通stats: 物理防御・体力・魔法防御／チャンピオン原典にも言及: 体力）；[[wiki/entities/items/item-3002|先人の道標]] + [[wiki/entities/items/item-3190|ソラリのロケット]]（n=4（15未満）；共通stats: 物理防御・体力／チャンピオン原典にも言及: 体力）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-9|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### JUNGLE（対象n=226）

- **高勝率コンボ候補（最大3件）：**
  - [[wiki/entities/champions/miss-fortune|ミス・フォーチュン（MissFortune）]] — 対象側勝率80.0%（12/15）、サンプル不足（n=15、十分性の目安30未満）。
  - [[wiki/entities/champions/leona|レオナ（Leona）]] — 対象側勝率62.5%（10/16）、サンプル不足（n=16、十分性の目安30未満）。
  - [[wiki/entities/champions/ashe|アッシュ（Ashe）]] — 対象側勝率52.0%（13/25）、サンプル不足（n=25、十分性の目安30未満）。
- **低勝率カウンターピック候補（最大3件）：** n=15以上の同ロール対面なし。サンプル不足のため判断保留。

### UTILITY（対象n=49）

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

### JUNGLE（対象96試合、全体勝率49.0%）

| 順位 | 完全ルーンセット | 選択数 | 選択率 | 選択時勝率 |
| ---: | --- | ---: | ---: | ---: |
| 1 | 主系覇道：電撃／追い打ち・グリスリー メメント・至極の賞金首狩り；副系魔道：アクシオム アルカニスト・至高；シャードUNKNOWN(5008)・UNKNOWN(5008)・UNKNOWN(5001) | 19/96 | 19.8% | 47.4% |
| 2 | 主系覇道：魂の収穫／追い打ち・グリスリー メメント・至極の賞金首狩り；副系天啓：キャッシュバック・宇宙の英知；シャードUNKNOWN(5008)・UNKNOWN(5008)・UNKNOWN(5001) | 11/96 | 11.5% | 54.5% |
| 3 | 主系覇道：電撃／サドンインパクト・グリスリー メメント・至極の賞金首狩り；副系魔道：アクシオム アルカニスト・英気集中；シャードUNKNOWN(5008)・UNKNOWN(5008)・UNKNOWN(5011) | 8/96 | 8.3% | 50.0% |

- **選定ロール：** チャンピオン・ロール別の完全試合数が最も多いロールを1つ選んだ。別ロールや全候補は詳細レポートで確認できる。
- **シャード表示：** Data Dragonで表示名を解決できない場合は`UNKNOWN(<ID>)`としてIDを保持する。

- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-rune-selection|Riotランク戦試合データ：チャンピオン別ルーン選択]]、[[wiki/syntheses/champion-rune-selection-ranked-matches|実測チャンピオン別ルーン選択分析]]。
<!-- champion-rune-set-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Fiddlesticks` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Fiddlesticks.png)
