---
title: "サミーラ"
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
champion_id: "Samira"
champion_key: "360"
data_version: "16.18.1"
roles:
  - "Marksman"
  - "Assassin"
resource_type: "マナ"
image_path: "raw/assets/champions/Samira.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Samira.png"
---

# サミーラ

![[raw/assets/champions/Samira.png|128]]

## 基本情報

- **英字ID：** `Samira`
- **キー：** `360`
- **称号：** 砂漠の薔薇
- **データversion：** `16.18.1`

## 紹介

サミーラはゆるぎない自信を浮かべた目で死を見つめ、行く先々でスリルを探し求める。幼少期にシュリーマの家が破壊された後、サミーラはノクサスで天職を見つけた。そこで彼女は危険な任務を請け負い、クールなスタイルの命知らずとしての評判を築いた。黒色火薬の拳銃と特注の剣を携え、サミーラは立ちはだかる者は誰であろうと排除し、生きるか死ぬかの状況を切り抜ける。

## 分類

- **役割タグ：** `Marksman`、`Assassin`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 8 |
| `defense` | 5 |
| `magic` | 3 |
| `difficulty` | 6 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 630 |
| `hpperlevel` | 108 |
| `mp` | 349 |
| `mpperlevel` | 38 |
| `movespeed` | 335 |
| `armor` | 26 |
| `armorperlevel` | 4.7 |
| `spellblock` | 33 |
| `spellblockperlevel` | 1.1 |
| `attackrange` | 500 |
| `hpregen` | 3.25 |
| `hpregenperlevel` | 0.55 |
| `mpregen` | 8.2 |
| `mpregenperlevel` | 0.7 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 57 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 3.3 |
| `attackspeed` | 0.658 |

## アビリティ

- **パッシブ — デアデビルインパルス：** 直前に命中したものとは異なる通常攻撃またはスキルを命中させることでコンボが増加していく。近接攻撃射程の通常攻撃は追加魔法ダメージを与える。移動不能効果を受けた敵に通常攻撃を行うと、自身の射程内までダッシュする。敵がノックアップしていた場合は、少しの間だけノックアップさせたままにする。

- **Q — フレア：** 銃を発砲するか、剣を振ってダメージを与える。「ワイルドラッシュ」中に使用した場合は、ダッシュ後に通り道にいたすべての敵を攻撃する。
- **W — ブレードワール：** 周囲を斬りつけて敵にダメージを与え、敵の飛翔物を破壊する。
- **E — ワイルドラッシュ：** 敵(建造物を含む)を通り抜けるようにダッシュし、接触した敵を斬りつけて、攻撃速度が増加する。敵チャンピオンをキルすると、このスキルのクールダウンが解消される。
- **R — インフェルノトリガー：** 銃から弾丸を高速で連射し、周囲のすべての敵に攻撃を行う。

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
- **対象試合：** 135試合、全体勝率 50.4%
- **時間帯別勝率：** 〜20分 47.8%（n=23）、20〜25分 45.0%（n=20）、25〜30分 56.8%（n=37）、30〜35分 44.8%（n=29）、35分〜 53.8%（n=26）
- **最高帯：** 25〜30分（判定差 11.9ポイント）
- **判定根拠：** 5つの時間帯を比較できるが、最高帯と端点の差が8ポイント未満、または勝率が非単調だった。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-360|サミーラの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### BOTTOM（294試合）

- **実測ビルド候補：** [[wiki/entities/items/item-3031|インフィニティ エッジ]] + [[wiki/entities/items/item-6676|コレクター]]（該当n=214、57.9% / 非該当35.0%、差+22.9pt）；[[wiki/entities/items/item-3031|インフィニティ エッジ]] + [[wiki/entities/items/item-6673|イモータル シールドボウ]]（該当n=91、67.0% / 非該当44.8%、差+22.2pt）
- **ステータス傾向：** 該当・非該当が各30試合以上で正の差を持つ群なし。
- **理論仮説：** [[wiki/entities/items/item-3072|ブラッドサースター]] + [[wiki/entities/items/item-3139|マーキュリアル シミター]]（n=1（15未満）；共通stats: 攻撃力・ライフスティール／チャンピオン原典にも言及: 攻撃力）；[[wiki/entities/items/item-3026|ガーディアン エンジェル]] + [[wiki/entities/items/item-6333|デス ダンス]]（未観測；共通stats: 物理防御・攻撃力／チャンピオン原典にも言及: 攻撃力）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-360|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### BOTTOM（対象n=415）

- **高勝率コンボ候補：** [[wiki/entities/champions/leona|レオナ（Leona）]] — 対象側勝率60.0%（51/85）、n=85（十分性の目安を満たす）。
- **カウンターピック候補：** [[wiki/entities/champions/caitlyn|ケイトリン（Caitlyn）]] — 対象側勝率44.7%（17/38）、n=38（十分性の目安を満たす）。

### TOP（対象n=3）

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

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Samira` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Samira.png)
