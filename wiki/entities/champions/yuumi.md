---
title: "ユーミ"
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
  - role-support
  - role-mage
  - data-dragon
champion_id: "Yuumi"
champion_key: "350"
data_version: "16.18.1"
roles:
  - "Support"
  - "Mage"
resource_type: "マナ"
image_path: "raw/assets/champions/Yuumi.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Yuumi.png"
---

# ユーミ

![[raw/assets/champions/Yuumi.png|128]]

## 基本情報

- **英字ID：** `Yuumi`
- **キー：** `350`
- **称号：** マジカルキャット
- **データversion：** `16.18.1`

## 紹介

バンドルシティからやってきた魔法ネコのユーミは、かつてはノラという名のヨードル魔女の使い魔だった。ノラが謎の失踪を遂げたことで、ユーミはノラが所有していた意識を持つ本、「境界の書」の守り手となり、そのページのポータルを通って旅をしながら飼い主を探している。ノラの愛情を懐かしむユーミは、旅の連れとなる仲間を見つけては、光の盾と固い決意で彼らを守るのだった。ブックはユーミが脇道にそれないよう注意しているが、ユーミはすぐに昼寝やら魚やらの楽しそうなことに気をとられてしまう。だがそんなユーミも、最後はいつもき...

## 分類

- **役割タグ：** `Support`、`Mage`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 5 |
| `defense` | 1 |
| `magic` | 8 |
| `difficulty` | 2 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 500 |
| `hpperlevel` | 69 |
| `mp` | 440 |
| `mpperlevel` | 45 |
| `movespeed` | 330 |
| `armor` | 25 |
| `armorperlevel` | 4.2 |
| `spellblock` | 25 |
| `spellblockperlevel` | 1.1 |
| `attackrange` | 425 |
| `hpregen` | 5 |
| `hpregenperlevel` | 0.55 |
| `mpregen` | 10 |
| `mpregenperlevel` | 0.4 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 49 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 1 |
| `attackspeed` | 0.625 |

## アビリティ

- **パッシブ — ネコはトモダチ：** 一定時間ごとに、通常攻撃またはスキルをチャンピオンに命中させると、自身および次にくっつく味方の体力が回復する。 くっついている間は、その味方との間に特別な絆が生まれる。絆が最も強い味方にくっついている間は、自身のスキルが強化される。

- **Q — きまぐれミサイル：** ミサイルを発射し、最初に当たった対象にダメージとスロウ効果を与える。発射後1.35秒以上経過すると、与えるダメージとスロウ効果が強化される。「ベストフレンド」にくっついている間は、ミサイルのスロウ効果が常に強化され、味方は通常攻撃時効果で追加ダメージを与えるようになる。 くっついている間は少しの間だけミサイルをマウスカーソルで操作できる。
- **W — ユー＆ミー！：** 対象の味方までダッシュして、タワー以外のすべてから対象指定不可状態になる。「ベストフレンド」にくっついている間は自身の体力回復/シールド効果が増加し、味方は通常攻撃時効果で体力が回復する。
- **E — バビューン！：** シールドを獲得して、移動速度と攻撃速度が増加する。くっついている場合は、自身ではなく味方にこの効果を与える。
- **R — ファイナルチャプター：** 詠唱してウェーブを5回発射する。ウェーブは対象が敵の場合はダメージを与えて、味方の場合は体力を回復する。詠唱中も移動と「バビューン！」の発動が可能で、味方にくっつくこともできる。「ベストフレンド」にくっついている間は、このスキルの発射方向をマウスで操作できる。

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
- **対象試合：** 178試合、全体勝率 27.0%
- **時間帯別勝率：** 〜20分 8.7%（n=46）、20〜25分 23.3%（n=30）、25〜30分 24.3%（n=37）、30〜35分 37.1%（n=35）、35分〜 50.0%（n=30）
- **最高帯：** 35分〜（判定差 41.3ポイント）
- **判定根拠：** 35分〜が最高、短時間帯との差 41.3%
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-350|ユーミの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### UTILITY（370試合）

- **実測ビルド候補：** [[wiki/entities/items/item-3222|ミカエルの祝福]] + [[wiki/entities/items/item-3504|アーデント センサー]] + [[wiki/entities/items/item-6617|ムーンストーンの再生]]（該当n=40、67.5% / 非該当31.8%、差+35.7pt）；[[wiki/entities/items/item-3504|アーデント センサー]] + [[wiki/entities/items/item-6617|ムーンストーンの再生]]（該当n=79、62.0% / 非該当28.5%、差+33.5pt）
- **ステータス傾向：** 体力（該当n=287、40.8% / 非該当18.1%、差+22.7pt）；移動速度（該当n=209、40.2% / 非該当29.8%、差+10.4pt）
- **理論仮説：** [[wiki/entities/items/item-3087|スタティック シヴ]] + [[wiki/entities/items/item-3124|グインソー レイジブレード]]（n=1（15未満）；共通stats: 魔力・攻撃力・攻撃速度／チャンピオン原典にも言及: 攻撃力・攻撃速度）；[[wiki/entities/items/item-3002|先人の道標]] + [[wiki/entities/items/item-3742|デッド マン プレート]]（未観測；共通stats: 物理防御・体力・移動速度／チャンピオン原典にも言及: 体力・移動速度）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-350|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### UTILITY（対象n=582）

- **高勝率コンボ候補：** [[wiki/entities/champions/viego|ヴィエゴ（Viego）]] — 対象側勝率56.2%（18/32）、n=32（十分性の目安を満たす）。
- **カウンターピック候補：** [[wiki/entities/champions/nautilus|ノーチラス（Nautilus）]] — 対象側勝率36.2%（21/58）、n=58（十分性の目安を満たす）。

### BOTTOM（対象n=2）

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

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Yuumi` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Yuumi.png)
