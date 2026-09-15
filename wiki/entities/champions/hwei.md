---
title: "フェイ"
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
champion_id: "Hwei"
champion_key: "910"
data_version: "16.18.1"
roles:
  - "Mage"
  - "Support"
resource_type: "マナ"
image_path: "raw/assets/champions/Hwei.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Hwei.png"
---

# フェイ

![[raw/assets/champions/Hwei.png|128]]

## 基本情報

- **英字ID：** `Hwei`
- **キー：** `910`
- **称号：** 夢想家
- **データversion：** `16.18.1`

## 紹介

フェイは陰鬱な芸術家で、見事な作品を生み出すことでアイオニアの悪人を罰し、罪なき者を慰める。暗い外面のすぐ下で、引き裂かれた感情が渦を巻き、想像力が生み出す鮮やかな情景と、寺院で起きた虐殺の凄惨な記憶とがせめぎ合っている。この明と暗を理解するための旅は、すなわち、フェイの力を解き放った芸術家を捜す旅でもある。絵筆とパレットだけを頼りに、無限の可能性を描くフェイの行く手に待つものは、心の平安か、はたまた絶望か。

## 分類

- **役割タグ：** `Mage`、`Support`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 7 |
| `defense` | 1 |
| `magic` | 8 |
| `difficulty` | 9 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 580 |
| `hpperlevel` | 109 |
| `mp` | 480 |
| `mpperlevel` | 30 |
| `movespeed` | 330 |
| `armor` | 21 |
| `armorperlevel` | 4.7 |
| `spellblock` | 30 |
| `spellblockperlevel` | 1.3 |
| `attackrange` | 550 |
| `hpregen` | 5.5 |
| `hpregenperlevel` | 0.55 |
| `mpregen` | 7.5 |
| `mpregenperlevel` | 0.75 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 54 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2.5 |
| `attackspeed` | 0.69 |

## アビリティ

- **パッシブ — 夢想家の銘：** スキルで敵チャンピオンにダメージを与えると、最後の仕上げとなるサインを施せるよう、対象を下塗りする。 2つ目の攻撃スキルを敵に命中させるとサインが完成し、対象の足元に残る。少しするとサインは爆発し、範囲内のすべての敵に魔法ダメージを与える。

- **Q — 題材: 厄災：** 終わりなき厄災を思い描き、壊滅的な一撃を描く力を得る。 このスキルは、フェイのスキルを攻撃スキル「荒廃の炎」、「断ち切る稲妻」、「沸き立つ大地」に置き換える。
- **W — 題材: 静謐：** 終わりなき静穏を思い描き、爽快な作品を描く力を得る。 このスキルは、フェイのスキルを補助系スキル「流るる蒼」、「内省の泉」、「迸る光彩」に置き換える。
- **E — 題材: 苦悩：** 終わりなき苦悩を思い描き、支配欲に満ちた表情を描く力を得る。 このスキルは、フェイのスキルを行動妨害スキル「恐怖の形相」、「深淵の眼差し」、「粉砕の牙」に置き換える。
- **R — 絶望の渦：** 純粋なる絶望のビジョンを描く。最初に命中した敵チャンピオンが拡大する絵画の中心となり、周囲の敵にスロウ効果とダメージを与える。ビジョンは最大サイズに達するか、最初に命中したチャンピオンがデスすると爆発する。

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
- **対象試合：** 433試合、全体勝率 51.3%
- **時間帯別勝率：** 〜20分 44.1%（n=68）、20〜25分 50.0%（n=52）、25〜30分 57.3%（n=89）、30〜35分 50.9%（n=108）、35分〜 51.7%（n=116）
- **最高帯：** 25〜30分（判定差 13.2ポイント）
- **判定根拠：** 5つの時間帯を比較できるが、最高帯と端点の差が8ポイント未満、または勝率が非単調だった。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-910|フェイの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### MIDDLE（799試合）

- **実測ビルド候補：** [[wiki/entities/items/item-2503|黒炎のトーチ]] + [[wiki/entities/items/item-3171|真紅のアイオニア ブーツ]] + [[wiki/entities/items/item-4645|シャドウフレイム]]（該当n=32、68.8% / 非該当50.5%、差+18.3pt）；[[wiki/entities/items/item-3171|真紅のアイオニア ブーツ]] + [[wiki/entities/items/item-4645|シャドウフレイム]]（該当n=38、68.4% / 非該当50.3%、差+18.1pt）
- **ステータス傾向：** 移動速度（該当n=767、51.4% / 非該当46.9%、差+4.5pt）
- **理論仮説：** [[wiki/entities/items/item-2503|黒炎のトーチ]] + [[wiki/entities/items/item-6655|ルーデン エコー]]（n=10（15未満）；共通stats: 魔力・マナ／チャンピオン原典にも言及: マナ）；[[wiki/entities/items/item-3040|セラフ エンブレイス]] + [[wiki/entities/items/item-6655|ルーデン エコー]]（n=5（15未満）；共通stats: 魔力・マナ／チャンピオン原典にも言及: マナ）

### BOTTOM（60試合）

- **実測ビルド候補：** 該当・非該当が各30試合以上で正の差を持つ候補なし。
- **ステータス傾向：** 該当・非該当が各30試合以上で正の差を持つ群なし。
- **理論仮説：** [[wiki/entities/items/item-2503|黒炎のトーチ]] + [[wiki/entities/items/item-3040|セラフ エンブレイス]]（n=1（15未満）；共通stats: 魔力・マナ／チャンピオン原典にも言及: マナ）；[[wiki/entities/items/item-2503|黒炎のトーチ]] + [[wiki/entities/items/item-6655|ルーデン エコー]]（n=1（15未満）；共通stats: 魔力・マナ／チャンピオン原典にも言及: マナ）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-910|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### MIDDLE（対象n=1,023）

- **高勝率コンボ候補（最大3件）：**
  - [[wiki/entities/champions/ambessa|アンベッサ（Ambessa）]] — 対象側勝率65.7%（23/35）、n=35（十分性の目安を満たす）。
  - [[wiki/entities/champions/nasus|ナサス（Nasus）]] — 対象側勝率64.5%（20/31）、n=31（十分性の目安を満たす）。
  - [[wiki/entities/champions/sivir|シヴィア（Sivir）]] — 対象側勝率64.5%（20/31）、n=31（十分性の目安を満たす）。
- **低勝率カウンターピック候補（最大3件）：**
  - [[wiki/entities/champions/galio|ガリオ（Galio）]] — 対象側勝率33.3%（12/36）、n=36（十分性の目安を満たす）。
  - [[wiki/entities/champions/veigar|ベイガー（Veigar）]] — 対象側勝率42.4%（14/33）、n=33（十分性の目安を満たす）。
  - [[wiki/entities/champions/ahri|アーリ（Ahri）]] — 対象側勝率43.1%（22/51）、n=51（十分性の目安を満たす）。

### BOTTOM（対象n=82）

- **高勝率コンボ候補（最大3件）：**
  - [[wiki/entities/champions/yone|ヨネ（Yone）]] — 対象側勝率58.8%（10/17）、サンプル不足（n=17、十分性の目安30未満）。
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

### MIDDLE（対象1,336試合、全体勝率51.3%）

| 順位 | 完全ルーンセット | 選択数 | 選択率 | 選択時勝率 |
| ---: | --- | ---: | ---: | ---: |
| 1 | 主系魔道：秘儀の彗星／マナフローバンド・至高・追火；副系栄華：切り崩し・レジェンド: ヘイスト；シャードUNKNOWN(5005)・UNKNOWN(5008)・UNKNOWN(5001) | 437/1,336 | 32.7% | 51.0% |
| 2 | 主系魔道：死神の残り火／マナフローバンド・至高・追火；副系栄華：切り崩し・レジェンド: ヘイスト；シャードUNKNOWN(5005)・UNKNOWN(5008)・UNKNOWN(5001) | 189/1,336 | 14.1% | 48.7% |
| 3 | 主系魔道：秘儀の彗星／マナフローバンド・至高・追火；副系天啓：ビスケットデリバリー・宇宙の英知；シャードUNKNOWN(5008)・UNKNOWN(5008)・UNKNOWN(5001) | 80/1,336 | 6.0% | 53.8% |

- **選定ロール：** チャンピオン・ロール別の完全試合数が最も多いロールを1つ選んだ。別ロールや全候補は詳細レポートで確認できる。
- **シャード表示：** Data Dragonで表示名を解決できない場合は`UNKNOWN(<ID>)`としてIDを保持する。

- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-rune-selection|Riotランク戦試合データ：チャンピオン別ルーン選択]]、[[wiki/syntheses/champion-rune-selection-ranked-matches|実測チャンピオン別ルーン選択分析]]。
<!-- champion-rune-set-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Hwei` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Hwei.png)
