---
title: "ヴィエゴ"
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
  - role-fighter
  - role-assassin
  - data-dragon
champion_id: "Viego"
champion_key: "234"
data_version: "16.18.1"
roles:
  - "Fighter"
  - "Assassin"
resource_type: "なし"
image_path: "raw/assets/champions/Viego.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Viego.png"
---

# ヴィエゴ

![[raw/assets/champions/Viego.png|128]]

## 基本情報

- **英字ID：** `Viego`
- **キー：** `234`
- **称号：** 滅びの王
- **データversion：** `16.18.1`

## 紹介

遠い昔に滅びた王国の支配者であったヴィエゴは、千年以上前に亡き妻を甦らせようと試みたことで「破滅」と呼ばれる魔力の大災厄を引き起こし、自らも命を落とした。遥か昔に喪った王妃への執着と愛に苛まれ、強力な不死の霊と化したヴィエゴは「滅びの王」として君臨し、王妃を甦らせる術を求め、「暗黒の刻」を操ってこの世界を調べ回っている。その行く手を阻むものは、空虚で冷酷なる胸からとめどなく流れ出でる「黒き霧」によってことごとく滅ぼされるだろう。

## 分類

- **役割タグ：** `Fighter`、`Assassin`
- **リソース種別：** なし

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 6 |
| `defense` | 4 |
| `magic` | 2 |
| `difficulty` | 5 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 630 |
| `hpperlevel` | 109 |
| `mp` | 10000 |
| `mpperlevel` | 0 |
| `movespeed` | 345 |
| `armor` | 34 |
| `armorperlevel` | 4.6 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 200 |
| `hpregen` | 7 |
| `hpregenperlevel` | 0.7 |
| `mpregen` | 0 |
| `mpregenperlevel` | 0 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 57 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2.75 |
| `attackspeed` | 0.658 |

## アビリティ

- **パッシブ — 王の支配：** ヴィエゴの周囲で倒された敵は亡霊になる。ヴィエゴは亡霊に通常攻撃を行うことで、その倒された敵の死体を一時的に操れるようになり、対象の最大体力の一定割合にあたる体力を回復し、対象の通常スキルとアイテムを使用できる。対象のアルティメットスキルは自身のものと入れ替わり、自由に1回発動できるようになる。

- **Q — 滅びの王剣：** 自動効果により、霊体の刃が通常攻撃時効果で現在体力に応じた追加ダメージを与える。直前にスキルで攻撃した敵には2回攻撃を行い、体力を奪う。 このスキルを発動すると、剣で前方に突きを放ち、自身の前にいる敵を貫く。
- **W — 亡霊の嘆き：** チャージしてから前方にダッシュし、凝縮した「黒き霧」を発射して最初に当たった敵をスタンさせる。
- **E — 彷徨える苦悶：** 「黒き霧」を出現させて、地形の周囲を覆う。自身は「霧」の中では亡霊となって隠れることができ、カモフラージュ状態となり、移動速度と攻撃速度が増加する。
- **R — ハートブレイカー：** 近くの地点に瞬間移動し、到着時に敵チャンピオンを斬りつけ、対象の心臓を貫いて衝撃を発生させ、周囲の敵をノックバックさせる。

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

- **観測分類：** 明瞭な傾向なし
- **対象試合：** 507試合、全体勝率 45.8%
- **時間帯別勝率：** 〜20分 48.8%（n=84）、20〜25分 51.4%（n=70）、25〜30分 40.4%（n=114）、30〜35分 47.2%（n=127）、35分〜 43.8%（n=112）
- **最高帯：** 20〜25分（判定差 11.1ポイント）
- **判定根拠：** 5つの時間帯を比較できるが、最高帯と端点の差が8ポイント未満、または勝率が非単調だった。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-234|ヴィエゴの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### JUNGLE（1,094試合）

- **実測ビルド候補：** [[wiki/entities/items/item-3031|インフィニティ エッジ]] + [[wiki/entities/items/item-6672|クラーケン スレイヤー]] + [[wiki/entities/items/item-6673|イモータル シールドボウ]]（該当n=44、72.7% / 非該当46.9%、差+25.9pt）；[[wiki/entities/items/item-3031|インフィニティ エッジ]] + [[wiki/entities/items/item-6672|クラーケン スレイヤー]]（該当n=65、69.2% / 非該当46.6%、差+22.7pt）
- **ステータス傾向：** クリティカル率（該当n=798、48.9% / 非該当45.3%、差+3.6pt）；魔法防御（該当n=385、49.1% / 非該当47.2%、差+1.8pt）
- **理論仮説：** [[wiki/entities/items/item-3073|実験的ヘクスプレート]] + [[wiki/entities/items/item-3078|トリニティ フォース]]（未観測；共通stats: 攻撃力・攻撃速度・体力／チャンピオン原典にも言及: 攻撃力・攻撃速度・体力）；[[wiki/entities/items/item-3078|トリニティ フォース]] + [[wiki/entities/items/item-6672|クラーケン スレイヤー]]（n=12（15未満）；共通stats: 攻撃力・攻撃速度／チャンピオン原典にも言及: 攻撃力・攻撃速度）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-234|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### JUNGLE（対象n=1,468）

- **高勝率コンボ候補（最大3件）：**
  - [[wiki/entities/champions/karma|カルマ（Karma）]] — 対象側勝率69.4%（25/36）、n=36（十分性の目安を満たす）。
  - [[wiki/entities/champions/morgana|モルガナ（Morgana）]] — 対象側勝率63.1%（41/65）、n=65（十分性の目安を満たす）。
  - [[wiki/entities/champions/miss-fortune|ミス・フォーチュン（MissFortune）]] — 対象側勝率57.3%（59/103）、n=103（十分性の目安を満たす）。
- **低勝率カウンターピック候補（最大3件）：**
  - [[wiki/entities/champions/talon|タロン（Talon）]] — 対象側勝率35.1%（13/37）、n=37（十分性の目安を満たす）。
  - [[wiki/entities/champions/vi|ヴァイ（Vi）]] — 対象側勝率35.2%（19/54）、n=54（十分性の目安を満たす）。
  - [[wiki/entities/champions/kayn|ケイン（Kayn）]] — 対象側勝率35.3%（18/51）、n=51（十分性の目安を満たす）。

### MIDDLE（対象n=17）

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

### JUNGLE（対象2,101試合、全体勝率49.2%）

| 順位 | 完全ルーンセット | 選択数 | 選択率 | 選択時勝率 |
| ---: | --- | ---: | ---: | ---: |
| 1 | 主系栄華：征服者／凱旋・レジェンド: 迅速・最期の慈悲；副系天啓：宇宙の英知・魔法の靴；シャードUNKNOWN(5005)・UNKNOWN(5008)・UNKNOWN(5001) | 873/2,101 | 41.6% | 49.8% |
| 2 | 主系栄華：征服者／凱旋・レジェンド: 迅速・最期の慈悲；副系天啓：魔法の靴・宇宙の英知；シャードUNKNOWN(5005)・UNKNOWN(5008)・UNKNOWN(5001) | 305/2,101 | 14.5% | 49.8% |
| 3 | 主系栄華：征服者／凱旋・レジェンド: 迅速・最期の慈悲；副系覇道：サドンインパクト・貪欲な賞金首狩り；シャードUNKNOWN(5005)・UNKNOWN(5008)・UNKNOWN(5001) | 156/2,101 | 7.4% | 48.1% |

- **選定ロール：** チャンピオン・ロール別の完全試合数が最も多いロールを1つ選んだ。別ロールや全候補は詳細レポートで確認できる。
- **シャード表示：** Data Dragonで表示名を解決できない場合は`UNKNOWN(<ID>)`としてIDを保持する。

- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-rune-selection|Riotランク戦試合データ：チャンピオン別ルーン選択]]、[[wiki/syntheses/champion-rune-selection-ranked-matches|実測チャンピオン別ルーン選択分析]]。
<!-- champion-rune-set-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Viego` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Viego.png)
