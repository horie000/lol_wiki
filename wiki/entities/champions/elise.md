---
title: "エリス"
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
champion_id: "Elise"
champion_key: "60"
data_version: "16.18.1"
roles:
  - "Assassin"
  - "Mage"
resource_type: "マナ"
image_path: "raw/assets/champions/Elise.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Elise.png"
---

# エリス

![[raw/assets/champions/Elise.png|128]]

## 基本情報

- **英字ID：** `Elise`
- **キー：** `60`
- **称号：** 蜘蛛の女帝
- **データversion：** `16.18.1`

## 紹介

冷酷無比な捕食者エリスは、ノクサスの古都の地下にある、光も差さない閉ざされた邸宅に棲む。かつては定命の者だった彼女は有力な一族の家長だったが、おぞましい半神に噛まれ、美しくも人間ではない何か──獲物を騙して巣におびき寄せる、蜘蛛のような生き物へと成り代わった。永遠の若さを保つため、エリスは世間知らずで信仰を持たない者を好んで餌食にする。その魅力に抗える者は少ない。

## 分類

- **役割タグ：** `Assassin`、`Mage`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 6 |
| `defense` | 5 |
| `magic` | 7 |
| `difficulty` | 9 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 620 |
| `hpperlevel` | 109 |
| `mp` | 324 |
| `mpperlevel` | 50 |
| `movespeed` | 330 |
| `armor` | 30 |
| `armorperlevel` | 4.5 |
| `spellblock` | 30 |
| `spellblockperlevel` | 1.3 |
| `attackrange` | 550 |
| `hpregen` | 5.5 |
| `hpregenperlevel` | 0.6 |
| `mpregen` | 6 |
| `mpregenperlevel` | 0.8 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 55 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 1.75 |
| `attackspeed` | 0.625 |

## アビリティ

- **パッシブ — 蜘蛛の女帝：** ヒト形態: スキルが敵に命中するたびに、幼体が1体誕生する。 蜘蛛形態: 通常攻撃に追加魔法ダメージが付与され、攻撃のたびに体力が回復する。

- **Q — 神経毒/毒牙：** ヒト形態: 対象の敵ユニットにダメージを与える。対象の現在体力が多いほど与えるダメージが増加する。 蜘蛛形態: 対象の敵ユニットに飛びかかって噛み付く。対象の現在体力が少ないほど与えるダメージが増加する。
- **W — 子蜘蛛爆弾/猛食：** ヒト形態: 毒液が詰まった幼体を放つ。幼体は敵ユニットに近づくと爆発する。 蜘蛛形態: エリスと幼体の攻撃速度が増加する。
- **E — 繭化/蜘蛛の糸：** ヒト形態: 繭を放って最初に命中した敵にスタン効果を付与し、ステルス状態の敵を除いて可視状態にする。 蜘蛛形態: 幼体とともに空中に跳びあがり、指定した敵のもとへ降下し、「蜘蛛の女帝」から得られる追加ダメージと回復量が増加する。
- **R — 蜘蛛形態：** 恐ろしい蜘蛛の姿になる。射程距離は短くなるが、移動速度が増加して新しいスキルを使用できるようになり、エリスと共に敵を攻撃する幼体の群れを呼び出す。

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
- **対象試合：** 45試合、全体勝率 35.6%
- **時間帯別勝率：** 〜20分 25.0%（n=8）、20〜25分 28.6%（n=7）、25〜30分 37.5%（n=8）、30〜35分 43.8%（n=16）、35分〜 33.3%（n=6）
- **最高帯：** 30〜35分（判定差 —）
- **判定根拠：** 5つの時間帯のいずれかで15試合未満のため、時間帯の比較を保留する。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-60|エリスの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### UTILITY（74試合）

- **実測ビルド候補：** 該当・非該当が各30試合以上で正の差を持つ候補なし。
- **ステータス傾向：** 物理防御（該当n=34、47.1% / 非該当37.5%、差+9.6pt）；体力（該当n=41、43.9% / 非該当39.4%、差+4.5pt）
- **理論仮説：** [[wiki/entities/items/item-2524|バンドルパイプ]] + [[wiki/entities/items/item-3050|ジーク コンバージェンス]]（n=1（15未満）；共通stats: 物理防御・体力・魔法防御／チャンピオン原典にも言及: 体力）；[[wiki/entities/items/item-2524|バンドルパイプ]] + [[wiki/entities/items/item-3190|ソラリのロケット]]（n=1（15未満）；共通stats: 物理防御・体力・魔法防御／チャンピオン原典にも言及: 体力）

### JUNGLE（63試合）

- **実測ビルド候補：** 該当・非該当が各30試合以上で正の差を持つ候補なし。
- **ステータス傾向：** 該当・非該当が各30試合以上で正の差を持つ群なし。
- **理論仮説：** [[wiki/entities/items/item-3116|リーライ クリスタル セプター]] + [[wiki/entities/items/item-8010|ブラッドレターの呪い]]（n=1（15未満）；共通stats: 魔力・体力／チャンピオン原典にも言及: 体力）；[[wiki/entities/items/item-3152|ヘクステック ロケットベルト]] + [[wiki/entities/items/item-8010|ブラッドレターの呪い]]（未観測；共通stats: 魔力・体力／チャンピオン原典にも言及: 体力）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-60|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### UTILITY（対象n=135）

- **高勝率コンボ候補：** [[wiki/entities/champions/jhin|ジン（Jhin）]] — 対象側勝率61.1%（11/18）、サンプル不足（n=18、十分性の目安30未満）。
- **カウンターピック候補：** n=15以上の同ロール対面なし。サンプル不足のため判断保留。

### JUNGLE（対象n=130）

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

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Elise` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Elise.png)
