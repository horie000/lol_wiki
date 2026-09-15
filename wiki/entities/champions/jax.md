---
title: "ジャックス"
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
  - role-fighter
  - data-dragon
champion_id: "Jax"
champion_key: "24"
data_version: "16.18.1"
roles:
  - "Fighter"
resource_type: "マナ"
image_path: "raw/assets/champions/Jax.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Jax.png"
---

# ジャックス

![[raw/assets/champions/Jax.png|128]]

## 基本情報

- **英字ID：** `Jax`
- **キー：** `24`
- **称号：** 最強の武器使い
- **データversion：** `16.18.1`

## 紹介

ジャックスはイカシアで現存する最後の武器使いだ。独特な武器を使う技術と辛辣な皮肉で彼の右に出る者はいない。傲慢さにより解放されたヴォイドによって故郷が破壊され、ジャックスは仲間とともに残ったわずかな土地を守り抜くことを誓った。魔法が世界に広まり、この眠れる脅威が再び騒動を巻き起こす中、ジャックスはイカシアの最後の灯りを武器に、共に戦ってくれる仲間を求めて、出会ったあらゆる戦士に戦いを挑んでその実力を測りながらヴァロランを旅している。

## 分類

- **役割タグ：** `Fighter`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 7 |
| `defense` | 5 |
| `magic` | 7 |
| `difficulty` | 5 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 650 |
| `hpperlevel` | 103 |
| `mp` | 339 |
| `mpperlevel` | 52 |
| `movespeed` | 350 |
| `armor` | 36 |
| `armorperlevel` | 4.2 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 125 |
| `hpregen` | 8.5 |
| `hpregenperlevel` | 0.55 |
| `mpregen` | 8.2 |
| `mpregenperlevel` | 0.7 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 68 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 3.4 |
| `attackspeed` | 0.638 |

## アビリティ

- **パッシブ — アサルトアタック：** ジャックスは通常攻撃ごとにスタックが溜まり、そのスタック数に応じて攻撃速度が増加する。

- **Q — リープストライク：** 対象のユニットに跳躍し、敵ユニットの場合は武器で攻撃する。
- **W — パワーバッシュ：** 武器に力を込め、次の攻撃で追加ダメージを与える。
- **E — カウンターストライク：** 短時間、その卓越した戦闘技術を用いてあらゆる通常攻撃を回避した後、すばやく反撃に転じて、周囲の敵ユニットにスタン効果を付与する。
- **R — ウェポングランドマスター：** 3回連続して通常攻撃を行うたびに、追加魔法ダメージを与える。また、このスキルを発動すると周囲にダメージを与え、決意を固めて短時間、物理防御と魔法防御が増加する。

<!-- power-spike:start -->
## パワースパイク

- **区分：** 序盤
- **判定：** [[wiki/syntheses/champion-power-spikes-v16-18-1|パワースパイク分類 v16.18.1]] に基づく原典ベースの推論。
- **根拠：**
  - 基礎ステータス指数（体力・物理防御・攻撃力・移動速度を標準化して合算）が173件中3位（上位15%）。体力650、物理防御36、攻撃力68、移動速度350。
- **限界：** スキル基礎ダメージ・係数・アイテム完成時刻を全チャンピオンで統一比較できる原典値がないため、実戦の強さや購入優先度を断定しない。

<!-- power-spike:end -->

<!-- power-spike-match:start -->
## 試合時間別の観測

- **観測分類：** 明瞭な傾向なし
- **対象試合：** 393試合、全体勝率 51.9%
- **時間帯別勝率：** 〜20分 54.8%（n=62）、20〜25分 61.5%（n=52）、25〜30分 55.3%（n=114）、30〜35分 48.8%（n=84）、35分〜 42.0%（n=81）
- **最高帯：** 20〜25分（判定差 19.6ポイント）
- **判定根拠：** 5つの時間帯を比較できるが、最高帯と端点の差が8ポイント未満、または勝率が非単調だった。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-24|ジャックスの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### TOP（504試合）

- **実測ビルド候補：** [[wiki/entities/items/item-3053|ステラックの篭手]] + [[wiki/entities/items/item-3078|トリニティ フォース]]（該当n=44、61.4% / 非該当48.7%、差+12.7pt）；[[wiki/entities/items/item-3053|ステラックの篭手]] + [[wiki/entities/items/item-3078|トリニティ フォース]] + [[wiki/entities/items/item-6610|サンダード スカイ]]（該当n=38、60.5% / 非該当48.9%、差+11.6pt）
- **ステータス傾向：** 魔力（該当n=246、53.3% / 非該当46.5%、差+6.7pt）；移動速度（該当n=472、50.2% / 非該当43.8%、差+6.5pt）
- **理論仮説：** [[wiki/entities/items/item-3078|トリニティ フォース]] + [[wiki/entities/items/item-6631|ストライドブレイカー]]（n=9（15未満）；共通stats: 攻撃力・攻撃速度・体力／チャンピオン原典にも言及: 攻撃力・攻撃速度・体力）；[[wiki/entities/items/item-3073|実験的ヘクスプレート]] + [[wiki/entities/items/item-3078|トリニティ フォース]]（n=1（15未満）；共通stats: 攻撃力・攻撃速度・体力／チャンピオン原典にも言及: 攻撃力・攻撃速度・体力）

### JUNGLE（355試合）

- **実測ビルド候補：** [[wiki/entities/items/item-3157|ゾーニャの砂時計]] + [[wiki/entities/items/item-6610|サンダード スカイ]]（該当n=75、58.7% / 非該当48.2%、差+10.5pt）；[[wiki/entities/items/item-3078|トリニティ フォース]] + [[wiki/entities/items/item-3157|ゾーニャの砂時計]] + [[wiki/entities/items/item-6610|サンダード スカイ]]（該当n=68、58.8% / 非該当48.4%、差+10.4pt）
- **ステータス傾向：** 魔力（該当n=201、53.2% / 非該当46.8%、差+6.5pt）；物理防御（該当n=265、50.6% / 非該当50.0%、差+0.6pt）
- **理論仮説：** [[wiki/entities/items/item-3078|トリニティ フォース]] + [[wiki/entities/items/item-6631|ストライドブレイカー]]（n=2（15未満）；共通stats: 攻撃力・攻撃速度・体力／チャンピオン原典にも言及: 攻撃力・攻撃速度・体力）；[[wiki/entities/items/item-3073|実験的ヘクスプレート]] + [[wiki/entities/items/item-3078|トリニティ フォース]]（n=2（15未満）；共通stats: 攻撃力・攻撃速度・体力／チャンピオン原典にも言及: 攻撃力・攻撃速度・体力）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-24|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### TOP（対象n=645）

- **高勝率コンボ候補：** [[wiki/entities/champions/miss-fortune|ミス・フォーチュン（MissFortune）]] — 対象側勝率59.6%（34/57）、n=57（十分性の目安を満たす）。
- **カウンターピック候補：** [[wiki/entities/champions/mordekaiser|モルデカイザー（Mordekaiser）]] — 対象側勝率44.7%（21/47）、n=47（十分性の目安を満たす）。

### JUNGLE（対象n=447）

- **高勝率コンボ候補：** [[wiki/entities/champions/jinx|ジンクス（Jinx）]] — 対象側勝率67.7%（21/31）、n=31（十分性の目安を満たす）。
- **カウンターピック候補：** [[wiki/entities/champions/viego|ヴィエゴ（Viego）]] — 対象側勝率60.0%（18/30）、n=30（十分性の目安を満たす）。

> [!warning] 実測値の限界
> 味方ペアは同一試合・同一チームで同時に出場した組み合わせ、対面はMatch-v5の最終ロールから推定した同ロール候補である。パッチ、観測ランク帯、プレイヤー、試合展開、構成の交絡を調整していない。とくにサンプル不足の行は探索的な参考値に留める。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-matchups]]、[[wiki/syntheses/champion-combo-counter-ranked-matches|実測コンボ・カウンターピック分析]]
<!-- champion-matchup-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Jax` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Jax.png)
