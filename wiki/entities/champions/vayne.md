---
title: "ヴェイン"
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
champion_id: "Vayne"
champion_key: "67"
data_version: "16.18.1"
roles:
  - "Marksman"
  - "Assassin"
resource_type: "マナ"
image_path: "raw/assets/champions/Vayne.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Vayne.png"
---

# ヴェイン

![[raw/assets/champions/Vayne.png|128]]

## 基本情報

- **英字ID：** `Vayne`
- **キー：** `67`
- **称号：** ナイトハンター
- **データversion：** `16.18.1`

## 紹介

シャウナ・ヴェインはデマーシアの無慈悲な怪物ハンターであり、自分の家族を殺した悪魔を見つけ出して殺すことに生涯をささげている。前腕部搭載式のクロスボウと復讐に燃える心を武器にする彼女だが、心からの喜びを感じることができるのは、影の中から銀の矢を飛ばして闇の魔術の使い手や、その不浄なる創造物を殺した時だけだ。

## 分類

- **役割タグ：** `Marksman`、`Assassin`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 10 |
| `defense` | 1 |
| `magic` | 1 |
| `difficulty` | 8 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 580 |
| `hpperlevel` | 98 |
| `mp` | 232 |
| `mpperlevel` | 35 |
| `movespeed` | 330 |
| `armor` | 23 |
| `armorperlevel` | 4.6 |
| `spellblock` | 33 |
| `spellblockperlevel` | 1.1 |
| `attackrange` | 550 |
| `hpregen` | 4 |
| `hpregenperlevel` | 0.5 |
| `mpregen` | 7 |
| `mpregenperlevel` | 0.4 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 60 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2.8 |
| `attackspeed` | 0.658 |

## アビリティ

- **パッシブ — ナイトハンター：** 敵チャンピオンに向かって移動する時、移動速度が増加する。

- **Q — タンブル：** 指定方向に前転して移動し、次の攻撃の準備をする。次の通常攻撃が追加ダメージを与える。
- **W — シルバーボルト：** 邪悪な存在が嫌う銀の矢を、クロスボウにつがえる。同じ対象に通常攻撃またはスキルを3回連続で命中させると、対象の最大体力に比例する追加確定ダメージが発生する。
- **E — パニッシュメント：** 背中に担いだ特大クロスボウを構え、指定対象に巨大な矢を撃ち込む。矢を受けたユニットはノックバックされダメージを受ける。ノックバック中に対象が地形に衝突した場合は、追加のダメージが発生し、スタン状態になる。
- **R — ファイナルアワー：** 敵を殲滅すべく特大クロスボウを構え、攻撃力が増加する。効果時間中は「タンブル」発動時にインビジブル状態になり、「タンブル」のクールダウンが短縮される。また、「ナイトハンター」の移動速度増加量が上昇する。

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
- **対象試合：** 145試合、全体勝率 47.6%
- **時間帯別勝率：** 〜20分 42.9%（n=21）、20〜25分 55.6%（n=18）、25〜30分 32.6%（n=46）、30〜35分 57.1%（n=28）、35分〜 59.4%（n=32）
- **最高帯：** 35分〜（判定差 16.5ポイント）
- **判定根拠：** 35分〜が最高、短時間帯との差 16.5%
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-67|ヴェインの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### BOTTOM（207試合）

- **実測ビルド候補：** [[wiki/entities/items/item-3124|グインソー レイジブレード]] + [[wiki/entities/items/item-6672|クラーケン スレイヤー]]（該当n=38、63.2% / 非該当43.2%、差+20.0pt）；[[wiki/entities/items/item-3124|グインソー レイジブレード]] + [[wiki/entities/items/item-3153|ルインドキング ブレード]]（該当n=113、50.4% / 非該当42.6%、差+7.9pt）
- **ステータス傾向：** 魔力（該当n=141、53.9% / 非該当31.8%、差+22.1pt）；魔法防御（該当n=52、57.7% / 非該当43.2%、差+14.5pt）
- **理論仮説：** [[wiki/entities/items/item-3073|実験的ヘクスプレート]] + [[wiki/entities/items/item-3078|トリニティ フォース]]（n=1（15未満）；共通stats: 攻撃力・攻撃速度・体力／チャンピオン原典にも言及: 攻撃力・体力）；[[wiki/entities/items/item-3087|スタティック シヴ]] + [[wiki/entities/items/item-6672|クラーケン スレイヤー]]（未観測；共通stats: 攻撃力・攻撃速度・移動速度／チャンピオン原典にも言及: 攻撃力・移動速度）

### TOP（143試合）

- **実測ビルド候補：** [[wiki/entities/items/item-3124|グインソー レイジブレード]] + [[wiki/entities/items/item-3153|ルインドキング ブレード]]（該当n=54、63.0% / 非該当44.9%、差+18.0pt）；[[wiki/entities/items/item-3073|実験的ヘクスプレート]] + [[wiki/entities/items/item-3153|ルインドキング ブレード]]（該当n=34、58.8% / 非該当49.5%、差+9.3pt）
- **ステータス傾向：** 魔力（該当n=74、58.1% / 非該当44.9%、差+13.2pt）；体力（該当n=113、54.0% / 非該当43.3%、差+10.6pt）
- **理論仮説：** [[wiki/entities/items/item-3073|実験的ヘクスプレート]] + [[wiki/entities/items/item-3078|トリニティ フォース]]（n=6（15未満）；共通stats: 攻撃力・攻撃速度・体力／チャンピオン原典にも言及: 攻撃力・体力）；[[wiki/entities/items/item-3087|スタティック シヴ]] + [[wiki/entities/items/item-6672|クラーケン スレイヤー]]（未観測；共通stats: 攻撃力・攻撃速度・移動速度／チャンピオン原典にも言及: 攻撃力・移動速度）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-67|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### BOTTOM（対象n=338）

- **高勝率コンボ候補：** [[wiki/entities/champions/lulu|ルル（Lulu）]] — 対象側勝率63.3%（19/30）、n=30（十分性の目安を満たす）。
- **カウンターピック候補：** [[wiki/entities/champions/jhin|ジン（Jhin）]] — 対象側勝率51.4%（19/37）、n=37（十分性の目安を満たす）。

### TOP（対象n=224）

- **高勝率コンボ候補：** [[wiki/entities/champions/akali|アカリ（Akali）]] — 対象側勝率80.0%（12/15）、サンプル不足（n=15、十分性の目安30未満）。
- **カウンターピック候補：** [[wiki/entities/champions/garen|ガレン（Garen）]] — 対象側勝率33.3%（6/18）、サンプル不足（n=18、十分性の目安30未満）。

> [!warning] 実測値の限界
> 味方ペアは同一試合・同一チームで同時に出場した組み合わせ、対面はMatch-v5の最終ロールから推定した同ロール候補である。パッチ、観測ランク帯、プレイヤー、試合展開、構成の交絡を調整していない。とくにサンプル不足の行は探索的な参考値に留める。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-matchups]]、[[wiki/syntheses/champion-combo-counter-ranked-matches|実測コンボ・カウンターピック分析]]
<!-- champion-matchup-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Vayne` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Vayne.png)
