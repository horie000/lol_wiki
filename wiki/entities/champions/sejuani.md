---
title: "セジュアニ"
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
  - data-dragon
champion_id: "Sejuani"
champion_key: "113"
data_version: "16.18.1"
roles:
  - "Tank"
resource_type: "マナ"
image_path: "raw/assets/champions/Sejuani.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Sejuani.png"
---

# セジュアニ

![[raw/assets/champions/Sejuani.png|128]]

## 基本情報

- **英字ID：** `Sejuani`
- **キー：** `113`
- **称号：** 極北の激憤
- **データversion：** `16.18.1`

## 紹介

残酷で情け容赦のないセジュアニは、フレヨルドでもっとも恐れられる部族のひとつであるウィンタークロウ族のアイスボーンの戦母だ。彼女の部族は常に過酷な自然の中で生き残りをかけた戦いを強いられており、厳しい冬を乗り切るためにノクサスやデマーシア、アヴァローサンを襲撃しなければならない状況にある。これらの危険な戦いではセジュアニ自身が戦闘に立ち、愛猪ブリストルに跨って、真なる氷のフレイルで敵を凍らせて砕き散らしている。

## 分類

- **役割タグ：** `Tank`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 5 |
| `defense` | 7 |
| `magic` | 6 |
| `difficulty` | 4 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 630 |
| `hpperlevel` | 114 |
| `mp` | 400 |
| `mpperlevel` | 40 |
| `movespeed` | 340 |
| `armor` | 34 |
| `armorperlevel` | 5.45 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 150 |
| `hpregen` | 8.5 |
| `hpregenperlevel` | 1 |
| `mpregen` | 7 |
| `mpregenperlevel` | 0.7 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 66 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 3.5 |
| `attackspeed` | 0.688 |

## アビリティ

- **パッシブ — 極北の激憤：** 非戦闘状態が続くと、「氷結の鎧」を獲得して物理防御と魔法防御が増加し、スロウ効果を受けなくなる。「氷結の鎧」はダメージを受けたあとも少しの間だけ継続する。自身がスタンさせた敵を攻撃すると、その氷が砕けて大きな魔法ダメージを与える。

- **Q — 猪突凍進：** 敵に突進してノックアップする。敵チャンピオンをノックアップすると、そこで突進が止まる。﻿
- **W — 氷河の怒り：** メイスを2回振り、ダメージとスロウ効果を与えて「凍傷」のスタックを付与する。
- **E — 永久凍土：** 「凍傷」のスタックが最大になった敵チャンピオンを凍らせてスタンさせる。
- **R — グレイシャルプリズン：** ボーラを投げて、最初に当たった敵チャンピオンを凍らせてスタンさせる。さらに氷の嵐を巻き起こして、他の敵ユニットにスロウ効果を与える。

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

- **観測分類：** 終盤寄り
- **対象試合：** 142試合、全体勝率 52.1%
- **時間帯別勝率：** 〜20分 42.9%（n=28）、20〜25分 56.0%（n=25）、25〜30分 43.9%（n=41）、30〜35分 56.0%（n=25）、35分〜 69.6%（n=23）
- **最高帯：** 35分〜（判定差 26.7ポイント）
- **判定根拠：** 35分〜が最高、短時間帯との差 26.7%
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-113|セジュアニの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### JUNGLE（247試合）

- **実測ビルド候補：** [[wiki/entities/items/item-3075|ソーンメイル]] + [[wiki/entities/items/item-3084|心の鋼]]（該当n=55、67.3% / 非該当46.4%、差+20.9pt）；[[wiki/entities/items/item-2502|終わりなき絶望]] + [[wiki/entities/items/item-3075|ソーンメイル]] + [[wiki/entities/items/item-3084|心の鋼]]（該当n=35、68.6% / 非該当48.1%、差+20.5pt）
- **ステータス傾向：** 魔法防御（該当n=137、54.7% / 非該当46.4%、差+8.4pt）
- **理論仮説：** [[wiki/entities/items/item-2524|バンドルパイプ]] + [[wiki/entities/items/item-3050|ジーク コンバージェンス]]（n=2（15未満）；共通stats: 物理防御・体力・魔法防御／チャンピオン原典にも言及: 物理防御・魔法防御）；[[wiki/entities/items/item-3050|ジーク コンバージェンス]] + [[wiki/entities/items/item-6665|変幻自在のジャック＝ショー]]（未観測；共通stats: 物理防御・体力・魔法防御／チャンピオン原典にも言及: 物理防御・魔法防御）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-113|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### JUNGLE（対象n=328）

- **高勝率コンボ候補（最大3件）：**
  - [[wiki/entities/champions/jinx|ジンクス（Jinx）]] — 対象側勝率60.6%（20/33）、n=33（十分性の目安を満たす）。
  - [[wiki/entities/champions/miss-fortune|ミス・フォーチュン（MissFortune）]] — 対象側勝率60.0%（18/30）、n=30（十分性の目安を満たす）。
  - [[wiki/entities/champions/nautilus|ノーチラス（Nautilus）]] — 対象側勝率45.5%（15/33）、n=33（十分性の目安を満たす）。
- **低勝率カウンターピック候補（最大3件）：**
  - [[wiki/entities/champions/viego|ヴィエゴ（Viego）]] — 対象側勝率39.1%（9/23）、サンプル不足（n=23、十分性の目安30未満）。
  - [[wiki/entities/champions/nocturne|ノクターン（Nocturne）]] — 対象側勝率50.0%（8/16）、サンプル不足（n=16、十分性の目安30未満）。

### TOP（対象n=27）

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

### JUNGLE（対象177試合、全体勝率57.1%）

| 順位 | 完全ルーンセット | 選択数 | 選択率 | 選択時勝率 |
| ---: | --- | ---: | ---: | ---: |
| 1 | 主系不滅：アフターショック／生命の泉・心身調整・超成長；副系栄華：レジェンド: 迅速・凱旋；シャードUNKNOWN(5005)・UNKNOWN(5001)・UNKNOWN(5001) | 98/177 | 55.4% | 57.1% |
| 2 | 主系不滅：アフターショック／生命の泉・心身調整・超成長；副系覇道：追い打ち・至極の賞金首狩り；シャードUNKNOWN(5005)・UNKNOWN(5008)・UNKNOWN(5001) | 23/177 | 13.0% | 65.2% |
| 3 | 主系不滅：アフターショック／生命の泉・心身調整・超成長；副系栄華：凱旋・レジェンド: 迅速；シャードUNKNOWN(5005)・UNKNOWN(5001)・UNKNOWN(5001) | 15/177 | 8.5% | 80.0% |

- **選定ロール：** チャンピオン・ロール別の完全試合数が最も多いロールを1つ選んだ。別ロールや全候補は詳細レポートで確認できる。
- **シャード表示：** Data Dragonで表示名を解決できない場合は`UNKNOWN(<ID>)`としてIDを保持する。

- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-rune-selection|Riotランク戦試合データ：チャンピオン別ルーン選択]]、[[wiki/syntheses/champion-rune-selection-ranked-matches|実測チャンピオン別ルーン選択分析]]。
<!-- champion-rune-set-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Sejuani` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Sejuani.png)
