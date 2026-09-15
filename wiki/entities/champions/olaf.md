---
title: "オラフ"
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
  - role-tank
  - data-dragon
champion_id: "Olaf"
champion_key: "2"
data_version: "16.18.1"
roles:
  - "Fighter"
  - "Tank"
resource_type: "マナ"
image_path: "raw/assets/champions/Olaf.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Olaf.png"
---

# オラフ

![[raw/assets/champions/Olaf.png|128]]

## 基本情報

- **英字ID：** `Olaf`
- **キー：** `2`
- **称号：** 狂戦士
- **データversion：** `16.18.1`

## 紹介

制止不能な破壊の力、斧を振りかざすオラフが求めているのは栄光にあふれる戦いの中での自らの死だ。過酷な環境のフレヨルドのロクファール半島出身の彼は、ある日、安らかな死を迎えるという予言を受けた──それは一族の間では臆病者の死を意味し、大いなる屈辱とされていた。怒りに燃えた彼は自らの死を求め、自分にとどめを刺してくれる相手を探して、偉大な戦士や伝説の野獣たちを打ち負かしながら国中を暴れまわった。今ではウィンタークロウの容赦なき用心棒となった彼は、やがて訪れる偉大な戦いの中で自らの死に場所を探そうとしている。

## 分類

- **役割タグ：** `Fighter`、`Tank`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 9 |
| `defense` | 5 |
| `magic` | 3 |
| `difficulty` | 3 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 645 |
| `hpperlevel` | 119 |
| `mp` | 316 |
| `mpperlevel` | 50 |
| `movespeed` | 350 |
| `armor` | 35 |
| `armorperlevel` | 4.2 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 125 |
| `hpregen` | 6.5 |
| `hpregenperlevel` | 0.6 |
| `mpregen` | 7.5 |
| `mpregenperlevel` | 0.6 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 68 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2.7 |
| `attackspeed` | 0.72 |

## アビリティ

- **パッシブ — 狂戦士の怒り：** 減少体力に応じて攻撃速度とライフスティールが増加する。

- **Q — 斧投げ：** 指定地点の地面をめがけて斧を投げ、命中した敵にダメージを与えて、物理防御と移動速度を低下させる。斧を拾うと、このスキルのクールダウンがリセットされる。
- **W — 根性比べ：** 攻撃速度が増加し、シールドを獲得する。
- **E — 捨て身切り：** 体力を消費して強烈な攻撃を繰り出し、対象に確定ダメージを与える。対象を倒した場合は消費した体力が回復する。
- **R — ラグナロク：** 自動効果で物理防御と魔法防御が増加する。このスキルを発動すると、通常攻撃を続けている限りは行動妨害効果を受けなくなる。

<!-- power-spike:start -->
## パワースパイク

- **区分：** 序盤
- **判定：** [[wiki/syntheses/champion-power-spikes-v16-18-1|パワースパイク分類 v16.18.1]] に基づく原典ベースの推論。
- **根拠：**
  - 基礎ステータス指数（体力・物理防御・攻撃力・移動速度を標準化して合算）が173件中4位（上位15%）。体力645、物理防御35、攻撃力68、移動速度350。
- **限界：** スキル基礎ダメージ・係数・アイテム完成時刻を全チャンピオンで統一比較できる原典値がないため、実戦の強さや購入優先度を断定しない。

<!-- power-spike:end -->

<!-- power-spike-match:start -->
## 試合時間別の観測

- **観測分類：** 判定保留（分母不足）
- **対象試合：** 95試合、全体勝率 40.0%
- **時間帯別勝率：** 〜20分 17.6%（n=17）、20〜25分 44.4%（n=9）、25〜30分 28.6%（n=21）、30〜35分 53.6%（n=28）、35分〜 50.0%（n=20）
- **最高帯：** 30〜35分（判定差 —）
- **判定根拠：** 5つの時間帯のいずれかで15試合未満のため、時間帯の比較を保留する。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-2|オラフの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### TOP（156試合）

- **実測ビルド候補：** [[wiki/entities/items/item-3073|実験的ヘクスプレート]] + [[wiki/entities/items/item-6631|ストライドブレイカー]]（該当n=49、65.3% / 非該当44.9%、差+20.4pt）
- **ステータス傾向：** ライフスティール（該当n=36、69.4% / 非該当45.8%、差+23.6pt）；物理防御（該当n=106、53.8% / 非該当46.0%、差+7.8pt）
- **理論仮説：** [[wiki/entities/items/item-3078|トリニティ フォース]] + [[wiki/entities/items/item-6631|ストライドブレイカー]]（n=1（15未満）；共通stats: 攻撃力・攻撃速度・体力／チャンピオン原典にも言及: 攻撃力・攻撃速度・体力）；[[wiki/entities/items/item-3073|実験的ヘクスプレート]] + [[wiki/entities/items/item-3078|トリニティ フォース]]（n=1（15未満）；共通stats: 攻撃力・攻撃速度・体力／チャンピオン原典にも言及: 攻撃力・攻撃速度・体力）

### JUNGLE（32試合）

- **実測ビルド候補：** 該当・非該当が各30試合以上で正の差を持つ候補なし。
- **ステータス傾向：** 該当・非該当が各30試合以上で正の差を持つ群なし。
- **理論仮説：** [[wiki/entities/items/item-3073|実験的ヘクスプレート]] + [[wiki/entities/items/item-6631|ストライドブレイカー]]（n=8（15未満）；共通stats: 攻撃力・攻撃速度・体力／チャンピオン原典にも言及: 攻撃力・攻撃速度・体力）；[[wiki/entities/items/item-3078|トリニティ フォース]] + [[wiki/entities/items/item-6631|ストライドブレイカー]]（未観測；共通stats: 攻撃力・攻撃速度・体力／チャンピオン原典にも言及: 攻撃力・攻撃速度・体力）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-2|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### TOP（対象n=210）

- **高勝率コンボ候補：** [[wiki/entities/champions/miss-fortune|ミス・フォーチュン（MissFortune）]] — 対象側勝率46.7%（14/30）、n=30（十分性の目安を満たす）。
- **カウンターピック候補：** [[wiki/entities/champions/mordekaiser|モルデカイザー（Mordekaiser）]] — 対象側勝率56.1%（23/41）、n=41（十分性の目安を満たす）。

### JUNGLE（対象n=50）

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

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Olaf` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Olaf.png)
