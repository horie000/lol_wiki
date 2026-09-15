---
title: "ナフィーリ"
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
  - role-fighter
  - data-dragon
champion_id: "Naafiri"
champion_key: "950"
data_version: "16.18.1"
roles:
  - "Assassin"
  - "Fighter"
resource_type: "マナ"
image_path: "raw/assets/champions/Naafiri.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Naafiri.png"
---

# ナフィーリ

![[raw/assets/champions/Naafiri.png|128]]

## 基本情報

- **英字ID：** `Naafiri`
- **キー：** `950`
- **称号：** 百刃の猟犬
- **データversion：** `16.18.1`

## 紹介

シュリーマの砂漠に、遠吠えが重なり響き渡る。群れを成し、この不毛の地で獲物を狩ろうと争う獰猛な捕食者、デューンハウンドの咆哮だ。その中に、ひと際目立つ群れがある。彼らは猟犬としての本能だけでなく、ダーキンの古の力に駆り立てられているのだ。

## 分類

- **役割タグ：** `Assassin`、`Fighter`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 9 |
| `defense` | 5 |
| `magic` | 0 |
| `difficulty` | 2 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 610 |
| `hpperlevel` | 105 |
| `mp` | 400 |
| `mpperlevel` | 55 |
| `movespeed` | 340 |
| `armor` | 28 |
| `armorperlevel` | 4.2 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 125 |
| `hpregen` | 6.25 |
| `hpregenperlevel` | 0.6 |
| `mpregen` | 7.5 |
| `mpregenperlevel` | 1 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 55 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2.1 |
| `attackspeed` | 0.663 |

## アビリティ

- **パッシブ — 我らは一つ：** 「群れの同胞」を出現させる。「群れの同胞」はナフィーリの通常攻撃およびスキルの対象を攻撃する。

- **Q — ダーキンダガー：** 最大2本の短剣を放つ。短剣はそれぞれ出血を付与し、対象がすでに出血中の場合は、それぞれ追加ダメージを与える。 「群れの同胞」はこのスキルが最初に命中したチャンピオンまたはモンスターに飛びかかって攻撃する。
- **W — 群れの呼び声：** 対象指定不可状態になって群れを強化し、追加の群れの同胞を出現させて、移動速度と攻撃力が増加する。
- **E — 獰猛なる刃：** ダッシュして、自身の周囲にいる敵にダメージを与える。その際、「群れの同胞」を呼び寄せて、体力を全回復させる。
- **R — 猟犬の追跡：** ナフィーリと「群れの同胞」がチャンピオンに向かってダッシュしてダメージを与える。キルまたはアシストを獲得すると自身の周囲の敵が可視化され、このスキルを再発動可能になる。2回目の使用時はシールドを獲得する。

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
- **対象試合：** 363試合、全体勝率 52.3%
- **時間帯別勝率：** 〜20分 53.1%（n=49）、20〜25分 48.1%（n=52）、25〜30分 55.2%（n=87）、30〜35分 43.2%（n=95）、35分〜 62.5%（n=80）
- **最高帯：** 35分〜（判定差 9.4ポイント）
- **判定根拠：** 35分〜が最高、短時間帯との差 9.4%
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-950|ナフィーリの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### JUNGLE（338試合）

- **実測ビルド候補：** [[wiki/entities/items/item-6694|セリルダの怨恨]] + [[wiki/entities/items/item-6697|ヒュブリス]]（該当n=33、66.7% / 非該当44.6%、差+22.1pt）；[[wiki/entities/items/item-6333|デス ダンス]] + [[wiki/entities/items/item-6699|ボルテイク サイクロソード]]（該当n=34、64.7% / 非該当44.7%、差+20.0pt）
- **ステータス傾向：** 物理防御（該当n=155、54.2% / 非該当40.4%、差+13.8pt）；魔法防御（該当n=43、53.5% / 非該当45.8%、差+7.7pt）
- **理論仮説：** [[wiki/entities/items/item-3071|ブラック クリーバー]] + [[wiki/entities/items/item-3814|ナイト エッジ]]（n=8（15未満）；共通stats: 攻撃力・体力／チャンピオン原典にも言及: 攻撃力・体力）；[[wiki/entities/items/item-3161|ショウジンの矛]] + [[wiki/entities/items/item-3814|ナイト エッジ]]（n=6（15未満）；共通stats: 攻撃力・体力／チャンピオン原典にも言及: 攻撃力・体力）

### MIDDLE（337試合）

- **実測ビルド候補：** [[wiki/entities/items/item-3814|ナイト エッジ]] + [[wiki/entities/items/item-6694|セリルダの怨恨]] + [[wiki/entities/items/item-6699|ボルテイク サイクロソード]]（該当n=47、66.0% / 非該当47.6%、差+18.4pt）；[[wiki/entities/items/item-3168|不滅の道]] + [[wiki/entities/items/item-6696|アクシオム アーク]]（該当n=40、65.0% / 非該当48.1%、差+16.9pt）
- **ステータス傾向：** 魔法防御（該当n=64、53.1% / 非該当49.5%、差+3.7pt）；体力（該当n=258、50.8% / 非該当48.1%、差+2.7pt）
- **理論仮説：** [[wiki/entities/items/item-3161|ショウジンの矛]] + [[wiki/entities/items/item-3814|ナイト エッジ]]（n=9（15未満）；共通stats: 攻撃力・体力／チャンピオン原典にも言及: 攻撃力・体力）；[[wiki/entities/items/item-3071|ブラック クリーバー]] + [[wiki/entities/items/item-3814|ナイト エッジ]]（n=5（15未満）；共通stats: 攻撃力・体力／チャンピオン原典にも言及: 攻撃力・体力）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-950|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### JUNGLE（対象n=506）

- **高勝率コンボ候補：** [[wiki/entities/champions/ahri|アーリ（Ahri）]] — 対象側勝率53.7%（22/41）、n=41（十分性の目安を満たす）。
- **カウンターピック候補：** [[wiki/entities/champions/viego|ヴィエゴ（Viego）]] — 対象側勝率40.0%（12/30）、n=30（十分性の目安を満たす）。

### MIDDLE（対象n=426）

- **高勝率コンボ候補：** [[wiki/entities/champions/ashe|アッシュ（Ashe）]] — 対象側勝率58.3%（21/36）、n=36（十分性の目安を満たす）。
- **カウンターピック候補：** [[wiki/entities/champions/yone|ヨネ（Yone）]] — 対象側勝率56.7%（17/30）、n=30（十分性の目安を満たす）。

> [!warning] 実測値の限界
> 味方ペアは同一試合・同一チームで同時に出場した組み合わせ、対面はMatch-v5の最終ロールから推定した同ロール候補である。パッチ、観測ランク帯、プレイヤー、試合展開、構成の交絡を調整していない。とくにサンプル不足の行は探索的な参考値に留める。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-matchups]]、[[wiki/syntheses/champion-combo-counter-ranked-matches|実測コンボ・カウンターピック分析]]
<!-- champion-matchup-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Naafiri` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Naafiri.png)
