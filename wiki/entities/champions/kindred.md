---
title: "キンドレッド"
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
  - role-marksman
  - data-dragon
champion_id: "Kindred"
champion_key: "203"
data_version: "16.18.1"
roles:
  - "Marksman"
resource_type: "マナ"
image_path: "raw/assets/champions/Kindred.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Kindred.png"
---

# キンドレッド

![[raw/assets/champions/Kindred.png|128]]

## 基本情報

- **英字ID：** `Kindred`
- **キー：** `203`
- **称号：** 永遠なる狩人
- **データversion：** `16.18.1`

## 紹介

別々の存在なれど、決して離れることはない──キンドレッドは死の本質を対で指し示す。子羊の放つ矢は、己の運命を受け入れた者を速やかにこの世から解放する。狼は死から逃れようとする者を追い詰め、強靭な顎で噛み砕き、惨たらしい最期を遂げさせる。キンドレッドの真髄についてはルーンテラ全域で諸説囁かれるが、いずれにせよ、生ける者は全て、死の本質を選ぶ必要に迫られる。

## 分類

- **役割タグ：** `Marksman`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 8 |
| `defense` | 2 |
| `magic` | 2 |
| `difficulty` | 4 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 595 |
| `hpperlevel` | 104 |
| `mp` | 300 |
| `mpperlevel` | 35 |
| `movespeed` | 325 |
| `armor` | 29 |
| `armorperlevel` | 4.7 |
| `spellblock` | 33 |
| `spellblockperlevel` | 1.1 |
| `attackrange` | 500 |
| `hpregen` | 7 |
| `hpregenperlevel` | 0.55 |
| `mpregen` | 7 |
| `mpregenperlevel` | 0.4 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 65 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 3.5 |
| `attackspeed` | 0.625 |

## アビリティ

- **パッシブ — キンドレッドの刻印：** 獲物とする対象に印を付ける。印をつけた獲物を狩ることで、通常スキルを恒常的に強化する。獲物を4体狩るごとに、通常攻撃の射程も強化される。

- **Q — 矢の輪舞：** 素早く移動し、周囲の対象に最大3本の矢を放つ。
- **W — 狼の激昂：** 狼が猛り、周囲の敵に攻撃を繰り出す。子羊は自動効果により移動と通常攻撃でスタックを獲得する。チャージが完了すると子羊の次の攻撃で体力が回復する。
- **E — 忍び寄る恐怖：** 子羊が対象に狙いを定めて攻撃し、スロウ効果を与える。子羊が同じ対象をさらに2回攻撃すると、その次の攻撃で狼が代わりに襲撃して大ダメージを与える。
- **R — 羊の執行猶予：** 子羊が展開した効果範囲内にいるすべての生命は死から免れる。効果時間中は誰も倒されることはない。効果時間終了時に全ユニットの体力が一定数回復する。

<!-- power-spike:start -->
## パワースパイク

- **区分：** 終盤
- **判定：** [[wiki/syntheses/champion-power-spikes-v16-18-1|パワースパイク分類 v16.18.1]] に基づく原典ベースの推論。
- **根拠：**
  - 獲物を狩ることで通常スキルと通常攻撃射程を恒常的に強化する。
- **限界：** スキル基礎ダメージ・係数・アイテム完成時刻を全チャンピオンで統一比較できる原典値がないため、実戦の強さや購入優先度を断定しない。

<!-- power-spike:end -->

<!-- power-spike-match:start -->
## 試合時間別の観測

- **観測分類：** 明瞭な傾向なし
- **対象試合：** 114試合、全体勝率 43.9%
- **時間帯別勝率：** 〜20分 43.8%（n=16）、20〜25分 41.7%（n=24）、25〜30分 56.0%（n=25）、30〜35分 24.0%（n=25）、35分〜 54.2%（n=24）
- **最高帯：** 25〜30分（判定差 32.0ポイント）
- **判定根拠：** 5つの時間帯を比較できるが、最高帯と端点の差が8ポイント未満、または勝率が非単調だった。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-203|キンドレッドの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### JUNGLE（237試合）

- **実測ビルド候補：** [[wiki/entities/items/item-3036|ドミニク リガード]] + [[wiki/entities/items/item-6676|コレクター]]（該当n=55、65.5% / 非該当41.8%、差+23.7pt）；[[wiki/entities/items/item-3031|インフィニティ エッジ]] + [[wiki/entities/items/item-6676|コレクター]]（該当n=67、64.2% / 非該当40.6%、差+23.6pt）
- **ステータス傾向：** 体力（該当n=54、57.4% / 非該当44.3%、差+13.1pt）；クリティカル率（該当n=195、49.2% / 非該当38.1%、差+11.1pt）
- **理論仮説：** [[wiki/entities/items/item-3071|ブラック クリーバー]] + [[wiki/entities/items/item-3078|トリニティ フォース]]（n=3（15未満）；共通stats: 攻撃力・体力／チャンピオン原典にも言及: 攻撃力・体力）；[[wiki/entities/items/item-3031|インフィニティ エッジ]] + [[wiki/entities/items/item-3033|モータル リマインダー]]（n=9（15未満）；共通stats: 攻撃力・クリティカル率／チャンピオン原典にも言及: 攻撃力）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-203|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### JUNGLE（対象n=378）

- **高勝率コンボ候補：** [[wiki/entities/champions/leona|レオナ（Leona）]] — 対象側勝率48.6%（18/37）、n=37（十分性の目安を満たす）。
- **カウンターピック候補：** [[wiki/entities/champions/viego|ヴィエゴ（Viego）]] — 対象側勝率45.5%（10/22）、サンプル不足（n=22、十分性の目安30未満）。

### BOTTOM（対象n=8）

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

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Kindred` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Kindred.png)
