---
title: "クイン"
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
  - role-assassin
  - data-dragon
champion_id: "Quinn"
champion_key: "133"
data_version: "16.18.1"
roles:
  - "Marksman"
  - "Assassin"
resource_type: "マナ"
image_path: "raw/assets/champions/Quinn.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Quinn.png"
---

# クイン

![[raw/assets/champions/Quinn.png|128]]

## 基本情報

- **英字ID：** `Quinn`
- **キー：** `133`
- **称号：** デマーシアの両翼
- **データversion：** `16.18.1`

## 紹介

クインは敵陣の奥深くに侵入して危険な任務を遂行するデマーシアの精鋭レンジャー騎士だ。彼女と伝説の鷲、ヴァロールは固い絆で結ばれており、多くの敵は、自分が戦っている相手が一人のデマーシアの英雄ではなく、コンビだったことに気づく間もなく倒されてしまう。空を飛ぶヴァロールが逃げる標的をマークし、身軽で素早いクインがクロスボウで仕留める──この一人と一羽は戦場では恐ろしいコンビとなる。

## 分類

- **役割タグ：** `Marksman`、`Assassin`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 9 |
| `defense` | 4 |
| `magic` | 2 |
| `difficulty` | 5 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 565 |
| `hpperlevel` | 107 |
| `mp` | 269 |
| `mpperlevel` | 35 |
| `movespeed` | 330 |
| `armor` | 28 |
| `armorperlevel` | 4.7 |
| `spellblock` | 33 |
| `spellblockperlevel` | 1.1 |
| `attackrange` | 525 |
| `hpregen` | 5.5 |
| `hpregenperlevel` | 0.55 |
| `mpregen` | 7 |
| `mpregenperlevel` | 0.4 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 59 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 3.1 |
| `attackspeed` | 0.668 |

## アビリティ

- **パッシブ — 鷲匠：** 相棒であるデマーシアの鷲、ヴァロールが定期的に周囲の敵を「鷲匠」でマークする。「鷲匠」のマークが付与された敵に対して、クインの次の通常攻撃が追加物理ダメージを与える。

- **Q — 暗闇の強襲：** ヴァロールを呼び、敵にマークをつけさせた後、その場の対象にダメージを与えるとともに、視界を奪う。
- **W — 鷲の眼：** 自動効果により「鷲匠」のマークが付与された敵を攻撃すると、クインの攻撃速度と移動速度が増加する。発動すると、ヴァロールが周囲の広範囲を可視化する。
- **E — 飛翔撃：** 敵に飛びかかり、対象に物理ダメージを与え、移動速度を低下させる。クインは対象に接触すると同時に、一瞬ノックバックさせて飛び離れ、自身の最大射程距離付近に着地する。
- **R — 相棒：** クインとヴァロールが連携し、高速で飛行する。スキルが終了すると「スカイストライク」が発動して周囲の敵にダメージを与え、敵チャンピオンには「鷲匠」のマークを付与する。

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
- **対象試合：** 80試合、全体勝率 53.8%
- **時間帯別勝率：** 〜20分 60.0%（n=15）、20〜25分 44.4%（n=9）、25〜30分 28.6%（n=21）、30〜35分 62.5%（n=16）、35分〜 73.7%（n=19）
- **最高帯：** 35分〜（判定差 —）
- **判定根拠：** 5つの時間帯のいずれかで15試合未満のため、時間帯の比較を保留する。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-133|クインの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### JUNGLE（61試合）

- **実測ビルド候補：** 該当・非該当が各30試合以上で正の差を持つ候補なし。
- **ステータス傾向：** 該当・非該当が各30試合以上で正の差を持つ群なし。
- **理論仮説：** [[wiki/entities/items/item-3032|ユン・タル ワイルドアロー]] + [[wiki/entities/items/item-6672|クラーケン スレイヤー]]（n=1（15未満）；共通stats: 攻撃力・攻撃速度／チャンピオン原典にも言及: 攻撃力・攻撃速度）；[[wiki/entities/items/item-3142|妖夢の霊剣]] + [[wiki/entities/items/item-6672|クラーケン スレイヤー]]（n=1（15未満）；共通stats: 攻撃力・移動速度／チャンピオン原典にも言及: 攻撃力・移動速度）

### TOP（59試合）

- **実測ビルド候補：** 該当・非該当が各30試合以上で正の差を持つ候補なし。
- **ステータス傾向：** 該当・非該当が各30試合以上で正の差を持つ群なし。
- **理論仮説：** [[wiki/entities/items/item-3087|スタティック シヴ]] + [[wiki/entities/items/item-6672|クラーケン スレイヤー]]（n=3（15未満）；共通stats: 攻撃力・攻撃速度・移動速度／チャンピオン原典にも言及: 攻撃力・攻撃速度・移動速度）；[[wiki/entities/items/item-3153|ルインドキング ブレード]] + [[wiki/entities/items/item-6672|クラーケン スレイヤー]]（n=3（15未満）；共通stats: 攻撃力・攻撃速度／チャンピオン原典にも言及: 攻撃力・攻撃速度）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-133|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### TOP（対象n=84）

- **高勝率コンボ候補：** n=15以上の味方組み合わせなし。サンプル不足のため判断保留。
- **カウンターピック候補：** n=15以上の同ロール対面なし。サンプル不足のため判断保留。

### JUNGLE（対象n=77）

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

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Quinn` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Quinn.png)
