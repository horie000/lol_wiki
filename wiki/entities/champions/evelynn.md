---
title: "イブリン"
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
tags:
  - champion
  - role-assassin
  - role-mage
  - data-dragon
champion_id: "Evelynn"
champion_key: "28"
data_version: "16.18.1"
roles:
  - "Assassin"
  - "Mage"
resource_type: "マナ"
image_path: "raw/assets/champions/Evelynn.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Evelynn.png"
---

# イブリン

![[raw/assets/champions/Evelynn.png|128]]

## 基本情報

- **英字ID：** `Evelynn`
- **キー：** `28`
- **称号：** 苦悶の抱擁
- **データversion：** `16.18.1`

## 紹介

ルーンテラ中の暗がりで悪魔イブリンは次の犠牲者を物色する。艶かしい女性の姿で獲物を誘い、相手を魅了したところで真の姿を露わす。そして彼女は、言葉では言い表せないほどの苦痛を相手に与え、苦悶する様を糧（かて）に愉悦に浸る。だがこの悪魔にとっては、そんな火遊びもただの気まぐれに過ぎない。ルーンテラの人々にとって、それは欲望が暴走した末路を描くおぞましい物語であり、節度なき快楽がもたらす代償を思い知らせる恐怖の象徴なのだ。

## 分類

- **役割タグ：** `Assassin`、`Mage`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 4 |
| `defense` | 2 |
| `magic` | 7 |
| `difficulty` | 10 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 642 |
| `hpperlevel` | 98 |
| `mp` | 315 |
| `mpperlevel` | 42 |
| `movespeed` | 335 |
| `armor` | 37 |
| `armorperlevel` | 4.7 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 125 |
| `hpregen` | 8.5 |
| `hpregenperlevel` | 0.75 |
| `mpregen` | 8.11 |
| `mpregenperlevel` | 0.6 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 61 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2.1 |
| `attackspeed` | 0.667 |

## アビリティ

- **パッシブ — 妖魔の影：** 戦闘中以外は「妖魔の影」に包まれ、体力が低下している場合は体力が回復する。レベル6以降は「妖魔の影」でカモフラージュも獲得する。

- **Q — ヘイトスパイク：** 鞭を振って最初に当たった敵ユニットにダメージを与える。その後、地面から一直線に貫通するトゲを近くの敵に数回放つことができる。
- **W — アリュール：** 対象に呪いをかける。少ししてから次に行う通常攻撃またはスキルがその敵にチャーム効果を与え、魔法防御を低下させる。
- **E — ウィップラッシュ：** 対象を鞭で打ってダメージを与え、その後少しの間だけ移動速度が増加する。
- **R — ラストカレス：** 少しの間だけ対象指定不可になり、自身の正面の範囲内にいる敵に大ダメージを与えてから後方に大きくワープする。

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

- **観測分類：** 中盤寄り
- **対象試合：** 133試合、全体勝率 48.9%
- **時間帯別勝率：** 〜20分 44.8%（n=29）、20〜25分 50.0%（n=20）、25〜30分 50.0%（n=28）、30〜35分 55.6%（n=27）、35分〜 44.8%（n=29）
- **最高帯：** 30〜35分（判定差 10.7ポイント）
- **判定根拠：** 中間帯が最高、端点との差 10.7%
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-28|イブリンの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### JUNGLE（273試合）

- **実測ビルド候補：** [[wiki/entities/items/item-3041|メジャイ ソウルスティーラー]] + [[wiki/entities/items/item-3100|リッチ ベイン]]（該当n=88、65.9% / 非該当37.8%、差+28.1pt）；[[wiki/entities/items/item-3041|メジャイ ソウルスティーラー]] + [[wiki/entities/items/item-3089|ラバドン デスキャップ]]（該当n=66、62.1% / 非該当42.0%、差+20.1pt）
- **ステータス傾向：** 体力（該当n=198、51.0% / 非該当36.0%、差+15.0pt）；魔法防御（該当n=49、57.1% / 非該当44.6%、差+12.5pt）
- **理論仮説：** [[wiki/entities/items/item-3041|メジャイ ソウルスティーラー]] + [[wiki/entities/items/item-3152|ヘクステック ロケットベルト]]（n=1（15未満）；共通stats: 魔力・体力／チャンピオン原典にも言及: 体力）；[[wiki/entities/items/item-3100|リッチ ベイン]] + [[wiki/entities/items/item-3176|永遠の前進]]（n=1（15未満）；共通stats: 移動速度／チャンピオン原典にも言及: 移動速度）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-28|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### JUNGLE（対象n=367）

- **高勝率コンボ候補：** [[wiki/entities/champions/yone|ヨネ（Yone）]] — 対象側勝率60.0%（18/30）、n=30（十分性の目安を満たす）。
- **カウンターピック候補：** [[wiki/entities/champions/kayn|ケイン（Kayn）]] — 対象側勝率12.5%（2/16）、サンプル不足（n=16、十分性の目安30未満）。

### UTILITY（対象n=3）

- **高勝率コンボ候補：** n=15以上の味方組み合わせなし。サンプル不足のため判断保留。
- **カウンターピック候補：** n=15以上の同ロール対面なし。サンプル不足のため判断保留。

> [!warning] 実測値の限界
> 味方ペアは同一試合・同一チームで同時に出場した組み合わせ、対面はMatch-v5の最終ロールから推定した同ロール候補である。パッチ、観測ランク帯、プレイヤー、試合展開、構成の交絡を調整していない。とくにサンプル不足の行は探索的な参考値に留める。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-matchups]]、[[wiki/syntheses/champion-combo-counter-ranked-matches|実測コンボ・カウンターピック分析]]
<!-- champion-matchup-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Evelynn` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Evelynn.png)
