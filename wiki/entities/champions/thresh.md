---
title: "スレッシュ"
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
  - role-support
  - role-tank
  - data-dragon
champion_id: "Thresh"
champion_key: "412"
data_version: "16.18.1"
roles:
  - "Support"
  - "Tank"
resource_type: "マナ"
image_path: "raw/assets/champions/Thresh.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Thresh.png"
---

# スレッシュ

![[raw/assets/champions/Thresh.png|128]]

## 基本情報

- **英字ID：** `Thresh`
- **キー：** `412`
- **称号：** 縛鎖の看守
- **データversion：** `16.18.1`

## 紹介

残虐で狡猾なスレッシュは、シャドウアイルを彷徨う貪欲なる亡霊だ。かつては膨大な量の古の魔法の秘密を管理する立場にあったが、生死を超える力によって亡霊となった彼は、他者を拷問し、じわじわと嬲り殺すことに生き甲斐を見出すようになった。犠牲者の魂はスレッシュの持つ邪悪なランタンの中に囚われ、尽きることのない激しい苦痛に満ちた拷問を受けながら永劫を送ることになる。

## 分類

- **役割タグ：** `Support`、`Tank`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 5 |
| `defense` | 6 |
| `magic` | 6 |
| `difficulty` | 7 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 620 |
| `hpperlevel` | 120 |
| `mp` | 274 |
| `mpperlevel` | 44 |
| `movespeed` | 330 |
| `armor` | 33 |
| `armorperlevel` | 0 |
| `spellblock` | 30 |
| `spellblockperlevel` | 1.55 |
| `attackrange` | 450 |
| `hpregen` | 7 |
| `hpregenperlevel` | 0.55 |
| `mpregen` | 6 |
| `mpregenperlevel` | 0.8 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 56 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 3.5 |
| `attackspeed` | 0.625 |

## アビリティ

- **パッシブ — 魂の束縛：** 近くで倒れた敵の魂を集め、物理防御と魔力を永続的に獲得する。

- **Q — 死の宣告：** 敵に鎖を投げ、命中した対象をそばに引き寄せる。もう一度発動すると、つないだ鎖をたぐって対象まで移動する。
- **W — 嘆きの魂灯：** ランタンを投げて、その周囲にいる味方チャンピオンにシールドを付与する。ランタンをクリックした味方チャンピオンは、スレッシュの元に素早く移動できる。
- **E — 絶望の鎖：** 前回の通常攻撃から経過した時間に応じて次の通常攻撃が強化される。発動すると鎖を投げ、範囲内の敵ユニットを鎖が投げられた方向へ弾き飛ばす。
- **R — 魂の牢獄：** 牢獄の壁を出現させる。壁を壊した者にダメージを与えスロウ効果を付与する。

<!-- power-spike:start -->
## パワースパイク

- **区分：** 終盤
- **判定：** [[wiki/syntheses/champion-power-spikes-v16-18-1|パワースパイク分類 v16.18.1]] に基づく原典ベースの推論。
- **根拠：**
  - 近くで倒れた敵の魂から物理防御と魔力を永続的に獲得する。
- **限界：** スキル基礎ダメージ・係数・アイテム完成時刻を全チャンピオンで統一比較できる原典値がないため、実戦の強さや購入優先度を断定しない。

<!-- power-spike:end -->

<!-- power-spike-match:start -->
## 試合時間別の観測

- **観測分類：** 明瞭な傾向なし
- **対象試合：** 421試合、全体勝率 53.0%
- **時間帯別勝率：** 〜20分 57.8%（n=64）、20〜25分 40.6%（n=69）、25〜30分 47.3%（n=110）、30〜35分 62.2%（n=111）、35分〜 55.2%（n=67）
- **最高帯：** 30〜35分（判定差 21.6ポイント）
- **判定根拠：** 5つの時間帯を比較できるが、最高帯と端点の差が8ポイント未満、または勝率が非単調だった。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-412|スレッシュの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### UTILITY（968試合）

- **実測ビルド候補：** [[wiki/entities/items/item-3170|スイフトマーチ]] + [[wiki/entities/items/item-3190|ソラリのロケット]]（該当n=49、77.6% / 非該当50.4%、差+27.2pt）；[[wiki/entities/items/item-3109|騎士の誓い]] + [[wiki/entities/items/item-3170|スイフトマーチ]]（該当n=31、77.4% / 非該当50.9%、差+26.5pt）
- **ステータス傾向：** 魔力（該当n=97、58.8% / 非該当51.0%、差+7.8pt）；物理防御（該当n=926、52.1% / 非該当45.2%、差+6.8pt）
- **理論仮説：** [[wiki/entities/items/item-3190|ソラリのロケット]] + [[wiki/entities/items/item-6665|変幻自在のジャック＝ショー]]（n=2（15未満）；共通stats: 物理防御・体力・魔法防御／チャンピオン原典にも言及: 物理防御・体力）；[[wiki/entities/items/item-3050|ジーク コンバージェンス]] + [[wiki/entities/items/item-6665|変幻自在のジャック＝ショー]]（未観測；共通stats: 物理防御・体力・魔法防御／チャンピオン原典にも言及: 物理防御・体力）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-412|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### UTILITY（対象n=1,284）

- **高勝率コンボ候補（最大3件）：**
  - [[wiki/entities/champions/veigar|ベイガー（Veigar）]] — 対象側勝率66.7%（32/48）、n=48（十分性の目安を満たす）。
  - [[wiki/entities/champions/nocturne|ノクターン（Nocturne）]] — 対象側勝率63.2%（36/57）、n=57（十分性の目安を満たす）。
  - [[wiki/entities/champions/master-yi|マスター・イー（MasterYi）]] — 対象側勝率63.0%（29/46）、n=46（十分性の目安を満たす）。
- **低勝率カウンターピック候補（最大3件）：**
  - [[wiki/entities/champions/rakan|ラカン（Rakan）]] — 対象側勝率31.2%（10/32）、n=32（十分性の目安を満たす）。
  - [[wiki/entities/champions/zyra|ザイラ（Zyra）]] — 対象側勝率39.1%（18/46）、n=46（十分性の目安を満たす）。
  - [[wiki/entities/champions/karma|カルマ（Karma）]] — 対象側勝率41.0%（16/39）、n=39（十分性の目安を満たす）。

### TOP（対象n=6）

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

### UTILITY（対象1,885試合、全体勝率50.5%）

| 順位 | 完全ルーンセット | 選択数 | 選択率 | 選択時勝率 |
| ---: | --- | ---: | ---: | ---: |
| 1 | 主系不滅：アフターショック／生命の泉・ボーンアーマー・気迫；副系天啓：ビスケットデリバリー・宇宙の英知；シャードUNKNOWN(5008)・UNKNOWN(5008)・UNKNOWN(5001) | 738/1,885 | 39.2% | 52.6% |
| 2 | 主系不滅：ガーディアン／生命の泉・ボーンアーマー・気迫；副系天啓：ビスケットデリバリー・宇宙の英知；シャードUNKNOWN(5007)・UNKNOWN(5001)・UNKNOWN(5001) | 175/1,885 | 9.3% | 42.3% |
| 3 | 主系天啓：グレイシャルオーグメント／ヘクステックフラッシュネイター・ビスケットデリバリー・宇宙の英知；副系不滅：ボーンアーマー・気迫；シャードUNKNOWN(5008)・UNKNOWN(5008)・UNKNOWN(5001) | 132/1,885 | 7.0% | 42.4% |

- **選定ロール：** チャンピオン・ロール別の完全試合数が最も多いロールを1つ選んだ。別ロールや全候補は詳細レポートで確認できる。
- **シャード表示：** Data Dragonで表示名を解決できない場合は`UNKNOWN(<ID>)`としてIDを保持する。

- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-rune-selection|Riotランク戦試合データ：チャンピオン別ルーン選択]]、[[wiki/syntheses/champion-rune-selection-ranked-matches|実測チャンピオン別ルーン選択分析]]。
<!-- champion-rune-set-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Thresh` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Thresh.png)
