---
title: "ニダリー"
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
champion_id: "Nidalee"
champion_key: "76"
data_version: "16.18.1"
roles:
  - "Assassin"
  - "Mage"
resource_type: "マナ"
image_path: "raw/assets/champions/Nidalee.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Nidalee.png"
---

# ニダリー

![[raw/assets/champions/Nidalee.png|128]]

## 基本情報

- **英字ID：** `Nidalee`
- **キー：** `76`
- **称号：** 半獣の狩人
- **データversion：** `16.18.1`

## 紹介

ジャングルの奥深くで育ったニダリーは凶暴なクーガーに自由に姿を変えることができる追跡の天才だ。女性でも獣でもなく、彼女は巧妙に仕掛けた罠と素早い投げ槍で、あらゆる侵入者から徹底して自分の縄張りを守っている。彼女は獲物の脚を傷つけて動けなくしてからクーガーの姿になって襲い掛かる──辛うじて襲撃を逃れて生き残った者たちの話によれば、剃刀のように鋭い本能と、さらに鋭い爪を持った野生の女だったという…

## 分類

- **役割タグ：** `Assassin`、`Mage`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 5 |
| `defense` | 4 |
| `magic` | 7 |
| `difficulty` | 8 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 610 |
| `hpperlevel` | 109 |
| `mp` | 295 |
| `mpperlevel` | 45 |
| `movespeed` | 335 |
| `armor` | 32 |
| `armorperlevel` | 5 |
| `spellblock` | 30 |
| `spellblockperlevel` | 1.45 |
| `attackrange` | 525 |
| `hpregen` | 6 |
| `hpregenperlevel` | 0.6 |
| `mpregen` | 6 |
| `mpregenperlevel` | 0.8 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 58 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 3.22 |
| `attackspeed` | 0.638 |

## アビリティ

- **パッシブ — 品定め：** 茂みに入ると移動速度が2秒間10%増加する。さらに、距離1400の範囲内にいる可視状態の敵チャンピオンに向かって移動する場合は30%増加する。 敵チャンピオンまたは中立モンスターに「槍投げ」または「虎挟み」でダメージを与えると、対象に4秒間「マーキング」を付与し、真の視界を得る。この間、ニダリーの移動速度が10%増加し、さらに、「マーキング」中の対象に向かって移動する場合は30%増加する。また、対象に対する「テイクダウン」と「ジャンプ」の効果が増加する。

- **Q — 槍投げ/テイクダウン：** ヒト形態: 対象に向かって槍を投げる。ダメージ量は槍の飛距離に比例して大きくなる。 クーガー形態: 次の通常攻撃時に大量の追加ダメージを与える。ダメージ量は対象の失った体力に比例して増える。
- **W — 虎挟み/ジャンプ：** ヒト形態: 地面にトラップを仕掛ける。気づかず踏んだ敵は、ダメージを受けて可視状態になる。 クーガー形態: 指定方向にジャンプし、着地点周辺の範囲内にいる敵ユニットにダメージを与える。
- **E — 高揚/クロウ：** ヒト形態: クーガーの精霊を呼び出し、味方の体力を回復して短時間攻撃速度を増加させる。 クーガー形態: かぎ爪で攻撃し、自身の前方範囲内の敵ユニットにダメージを与える。
- **R — クーガーの心：** クーガーに変身し、特別なスキルを使用する。

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
- **対象試合：** 51試合、全体勝率 47.1%
- **時間帯別勝率：** 〜20分 57.1%（n=14）、20〜25分 50.0%（n=4）、25〜30分 37.5%（n=16）、30〜35分 50.0%（n=6）、35分〜 45.5%（n=11）
- **最高帯：** 〜20分（判定差 —）
- **判定根拠：** 5つの時間帯のいずれかで15試合未満のため、時間帯の比較を保留する。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-76|ニダリーの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### JUNGLE（101試合）

- **実測ビルド候補：** [[wiki/entities/items/item-3100|リッチ ベイン]] + [[wiki/entities/items/item-4645|シャドウフレイム]]（該当n=34、47.1% / 非該当37.3%、差+9.7pt）
- **ステータス傾向：** 体力（該当n=63、42.9% / 非該当36.8%、差+6.0pt）
- **理論仮説：** [[wiki/entities/items/item-3041|メジャイ ソウルスティーラー]] + [[wiki/entities/items/item-3152|ヘクステック ロケットベルト]]（n=4（15未満）；共通stats: 魔力・体力／チャンピオン原典にも言及: 体力）；[[wiki/entities/items/item-3152|ヘクステック ロケットベルト]] + [[wiki/entities/items/item-4629|コズミック ドライブ]]（n=1（15未満）；共通stats: 魔力・体力／チャンピオン原典にも言及: 体力）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-76|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### JUNGLE（対象n=196）

- **高勝率コンボ候補：** [[wiki/entities/champions/nautilus|ノーチラス（Nautilus）]] — 対象側勝率57.9%（11/19）、サンプル不足（n=19、十分性の目安30未満）。
- **カウンターピック候補：** n=15以上の同ロール対面なし。サンプル不足のため判断保留。

### UTILITY（対象n=31）

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

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Nidalee` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Nidalee.png)
