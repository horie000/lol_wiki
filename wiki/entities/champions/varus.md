---
title: "ヴァルス"
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
  - role-mage
  - data-dragon
champion_id: "Varus"
champion_key: "110"
data_version: "16.18.1"
roles:
  - "Marksman"
  - "Mage"
resource_type: "マナ"
image_path: "raw/assets/champions/Varus.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Varus.png"
---

# ヴァルス

![[raw/assets/champions/Varus.png|128]]

## 基本情報

- **英字ID：** `Varus`
- **キー：** `110`
- **称号：** 報復の一矢
- **データversion：** `16.18.1`

## 紹介

古代のダーキン種族のひとつに属するヴァルスは、敵を苦しめ狂気に追い込んでから矢でとどめを刺す恐ろしい殺戮者だった。彼はダーキンの大戦争の最後に幽閉され、数世紀後に二人のアイオニアの狩人の肉体を使って復活した。二人の狩人は予期せず彼を解放してしまい、彼の一部を閉じ込めた弓と一体化する呪いを受けたのだった。ヴァルスは自分を幽閉した者を探し出して残酷な復讐を遂げようとしているものの、彼の中に残る定命の魂が常にそれに抗おうとしている。

## 分類

- **役割タグ：** `Marksman`、`Mage`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 7 |
| `defense` | 3 |
| `magic` | 4 |
| `difficulty` | 2 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 600 |
| `hpperlevel` | 105 |
| `mp` | 320 |
| `mpperlevel` | 40 |
| `movespeed` | 330 |
| `armor` | 24 |
| `armorperlevel` | 4 |
| `spellblock` | 33 |
| `spellblockperlevel` | 1.1 |
| `attackrange` | 575 |
| `hpregen` | 3.5 |
| `hpregenperlevel` | 0.55 |
| `mpregen` | 8 |
| `mpregenperlevel` | 0.8 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 59 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 3.5 |
| `attackspeed` | 0.658 |

## アビリティ

- **パッシブ — 復讐の化身：** キルまたはアシストを獲得すると、一時的に攻撃力と魔力が増加する。相手が敵チャンピオンの場合、このボーナスはさらに大きくなる。

- **Q — 乾坤一擲：** 弓を引き絞り、強力な一矢を放つ。構えてから発動するまでの時間が長ければ長いほど、射程距離とダメージ量が増加する。
- **W — 枯死の矢筒：** 自動効果: 通常攻撃に追加魔法ダメージがつき、命中時に「枯死の呪い」を付与する。「枯死の呪い」がかかった敵に自身の他のスキルが命中すると、対象の最大体力に応じた魔法ダメージを与える。 発動効果: 次の「乾坤一擲」が強化される。
- **E — 滅びの矢雨：** 複数の矢を射かけて物理ダメージを与え、範囲内の土壌に穢れをもたらす。穢された範囲内に入った敵は、スロウ状態になり、自己回復スキルの効果と、体力自動回復が低下する。
- **R — 穢れの連鎖：** 穢れの蔓を放ち、最初に命中した敵にダメージを与え、スネア効果を付与する。蔓は近接する別のチャンピオンの位置に向かって拡散し、命中するとそのチャンピオンにも同様にダメージを与えてスネア効果を付与する。

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
- **対象試合：** 356試合、全体勝率 47.5%
- **時間帯別勝率：** 〜20分 48.0%（n=50）、20〜25分 42.6%（n=47）、25〜30分 51.8%（n=85）、30〜35分 48.1%（n=79）、35分〜 45.3%（n=95）
- **最高帯：** 25〜30分（判定差 9.2ポイント）
- **判定根拠：** 5つの時間帯を比較できるが、最高帯と端点の差が8ポイント未満、または勝率が非単調だった。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-110|ヴァルスの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### BOTTOM（792試合）

- **実測ビルド候補：** [[wiki/entities/items/item-3142|妖夢の霊剣]] + [[wiki/entities/items/item-3170|スイフトマーチ]]（該当n=35、82.9% / 非該当46.8%、差+36.1pt）；[[wiki/entities/items/item-3042|ムラマナ]] + [[wiki/entities/items/item-3170|スイフトマーチ]]（該当n=34、82.4% / 非該当46.8%、差+35.5pt）
- **ステータス傾向：** 物理防御（該当n=187、56.1% / 非該当46.0%、差+10.2pt）；移動速度（該当n=716、49.3% / 非該当39.5%、差+9.8pt）
- **理論仮説：** [[wiki/entities/items/item-2510|黄昏と暁]] + [[wiki/entities/items/item-4633|リフトメーカー]]（n=4（15未満）；共通stats: 魔力・体力／チャンピオン原典にも言及: 魔力・体力）；[[wiki/entities/items/item-3003|アークエンジェル スタッフ]] + [[wiki/entities/items/item-3118|マリグナンス]]（未観測；共通stats: 魔力・マナ／チャンピオン原典にも言及: 魔力・マナ）

### TOP（79試合）

- **実測ビルド候補：** 該当・非該当が各30試合以上で正の差を持つ候補なし。
- **ステータス傾向：** 該当・非該当が各30試合以上で正の差を持つ群なし。
- **理論仮説：** [[wiki/entities/items/item-3087|スタティック シヴ]] + [[wiki/entities/items/item-3124|グインソー レイジブレード]]（n=2（15未満）；共通stats: 魔力・攻撃力・攻撃速度／チャンピオン原典にも言及: 魔力・攻撃力）；[[wiki/entities/items/item-2510|黄昏と暁]] + [[wiki/entities/items/item-4633|リフトメーカー]]（n=13（15未満）；共通stats: 魔力・体力／チャンピオン原典にも言及: 魔力・体力）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-110|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### BOTTOM（対象n=974）

- **高勝率コンボ候補：** [[wiki/entities/champions/morgana|モルガナ（Morgana）]] — 対象側勝率64.3%（27/42）、n=42（十分性の目安を満たす）。
- **カウンターピック候補：** [[wiki/entities/champions/miss-fortune|ミス・フォーチュン（MissFortune）]] — 対象側勝率41.8%（33/79）、n=79（十分性の目安を満たす）。

### TOP（対象n=130）

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

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Varus` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Varus.png)
