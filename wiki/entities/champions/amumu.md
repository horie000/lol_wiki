---
title: "アムム"
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
  - role-tank
  - role-support
  - data-dragon
champion_id: "Amumu"
champion_key: "32"
data_version: "16.18.1"
roles:
  - "Tank"
  - "Support"
resource_type: "マナ"
image_path: "raw/assets/champions/Amumu.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Amumu.png"
---

# アムム

![[raw/assets/champions/Amumu.png|128]]

## 基本情報

- **英字ID：** `Amumu`
- **キー：** `32`
- **称号：** めそめそミイラ
- **データversion：** `16.18.1`

## 紹介

孤独で悲しい魂を抱いて古代シュリーマで生まれたアムムは、友達を探して世界中を彷徨っている。アムムは古代の呪いによって永遠に独りぼっちでいる運命を背負わされており、触れた者は死を免れず、愛した者は破滅の一途を辿る。アムムを目にした者曰く「彼は生ける屍だ。その体は小さく、苔の生した包帯でぐるぐる巻きにされている。」アムムは何世代にも渡って語り継がれる神話や民話、伝説にも登場する。こうした物語には、往々にして空想と真実が入り混じっている。

## 分類

- **役割タグ：** `Tank`、`Support`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 2 |
| `defense` | 6 |
| `magic` | 8 |
| `difficulty` | 3 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 685 |
| `hpperlevel` | 94 |
| `mp` | 285 |
| `mpperlevel` | 40 |
| `movespeed` | 335 |
| `armor` | 33 |
| `armorperlevel` | 4 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 125 |
| `hpregen` | 9 |
| `hpregenperlevel` | 0.85 |
| `mpregen` | 7.4 |
| `mpregenperlevel` | 0.55 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 57 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2.18 |
| `attackspeed` | 0.736 |

## アビリティ

- **パッシブ — 呪いの手：** 通常攻撃で敵に「呪い」をかける。呪われた対象は、魔法ダメージを受ける際に追加確定ダメージを受けるようになる。

- **Q — 絡みつく包帯：** 指定方向にべとべとの包帯を投げつける。敵に当たるとダメージとスタンを与え、包帯をたぐって相手の近くに素早く移動する。
- **W — めそめそ：** 涙を流し、触れた敵に最大体力の一定割合のダメージを毎秒与え、対象に付与された「呪い」の効果時間を更新する。
- **E — だだっこ：** 敵から受ける物理ダメージを恒久的に軽減する。発動して怒りを爆発させると、周囲の敵にダメージを与える。自身が攻撃を受けるたびに「だだっこ」のクールダウンが短縮される。
- **R — めそめそミイラの呪い：** 周囲の敵ユニットを包帯で拘束して「呪い」を付与する。さらにダメージを与えてスタンさせる。

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
- **対象試合：** 270試合、全体勝率 55.6%
- **時間帯別勝率：** 〜20分 42.1%（n=38）、20〜25分 67.7%（n=31）、25〜30分 50.0%（n=66）、30〜35分 55.4%（n=74）、35分〜 63.9%（n=61）
- **最高帯：** 20〜25分（判定差 25.6ポイント）
- **判定根拠：** 5つの時間帯を比較できるが、最高帯と端点の差が8ポイント未満、または勝率が非単調だった。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-32|アムムの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### JUNGLE（436試合）

- **実測ビルド候補：** [[wiki/entities/items/item-3174|装甲強化の進撃]] + [[wiki/entities/items/item-6653|ライアンドリーの仮面]]（該当n=32、75.0% / 非該当51.5%、差+23.5pt）；[[wiki/entities/items/item-3068|サンファイア イージス]] + [[wiki/entities/items/item-6665|変幻自在のジャック＝ショー]]（該当n=44、63.6% / 非該当52.0%、差+11.6pt）
- **ステータス傾向：** 物理防御（該当n=392、54.6% / 非該当40.9%、差+13.7pt）；魔力（該当n=385、54.3% / 非該当45.1%、差+9.2pt）
- **理論仮説：** [[wiki/entities/items/item-2502|終わりなき絶望]] + [[wiki/entities/items/item-3068|サンファイア イージス]]（n=13（15未満）；共通stats: 物理防御・体力／チャンピオン原典にも言及: 体力）；[[wiki/entities/items/item-2504|ケイニック ルーケルン]] + [[wiki/entities/items/item-6665|変幻自在のジャック＝ショー]]（n=9（15未満）；共通stats: 体力・魔法防御／チャンピオン原典にも言及: 体力）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-32|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### JUNGLE（対象n=492）

- **高勝率コンボ候補（最大3件）：**
  - [[wiki/entities/champions/yone|ヨネ（Yone）]] — 対象側勝率59.4%（19/32）、n=32（十分性の目安を満たす）。
  - [[wiki/entities/champions/caitlyn|ケイトリン（Caitlyn）]] — 対象側勝率57.5%（23/40）、n=40（十分性の目安を満たす）。
  - [[wiki/entities/champions/jinx|ジンクス（Jinx）]] — 対象側勝率57.4%（31/54）、n=54（十分性の目安を満たす）。
- **低勝率カウンターピック候補（最大3件）：**
  - [[wiki/entities/champions/briar|ブライアー（Briar）]] — 対象側勝率38.1%（8/21）、サンプル不足（n=21、十分性の目安30未満）。
  - [[wiki/entities/champions/shyvana|シヴァーナ（Shyvana）]] — 対象側勝率38.9%（7/18）、サンプル不足（n=18、十分性の目安30未満）。
  - [[wiki/entities/champions/diana|ダイアナ（Diana）]] — 対象側勝率42.9%（9/21）、サンプル不足（n=21、十分性の目安30未満）。

### UTILITY（対象n=39）

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

### JUNGLE（対象263試合、全体勝率50.2%）

| 順位 | 完全ルーンセット | 選択数 | 選択率 | 選択時勝率 |
| ---: | --- | ---: | ---: | ---: |
| 1 | 主系栄華：征服者／凱旋・レジェンド: ヘイスト・背水の陣；副系覇道：追い打ち・至極の賞金首狩り；シャードUNKNOWN(5005)・UNKNOWN(5008)・UNKNOWN(5001) | 133/263 | 50.6% | 52.6% |
| 2 | 主系不滅：アフターショック／生命の泉・ボーンアーマー・気迫；副系覇道：追い打ち・至極の賞金首狩り；シャードUNKNOWN(5008)・UNKNOWN(5008)・UNKNOWN(5001) | 41/263 | 15.6% | 56.1% |
| 3 | 主系栄華：征服者／凱旋・レジェンド: ヘイスト・背水の陣；副系不滅：心身調整・超成長；シャードUNKNOWN(5008)・UNKNOWN(5008)・UNKNOWN(5001) | 26/263 | 9.9% | 65.4% |

- **選定ロール：** チャンピオン・ロール別の完全試合数が最も多いロールを1つ選んだ。別ロールや全候補は詳細レポートで確認できる。
- **シャード表示：** Data Dragonで表示名を解決できない場合は`UNKNOWN(<ID>)`としてIDを保持する。

- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-rune-selection|Riotランク戦試合データ：チャンピオン別ルーン選択]]、[[wiki/syntheses/champion-rune-selection-ranked-matches|実測チャンピオン別ルーン選択分析]]。
<!-- champion-rune-set-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Amumu` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Amumu.png)
