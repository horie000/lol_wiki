---
title: "ヴェル＝コズ"
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
  - role-mage
  - role-support
  - data-dragon
champion_id: "Velkoz"
champion_key: "161"
data_version: "16.18.1"
roles:
  - "Mage"
  - "Support"
resource_type: "マナ"
image_path: "raw/assets/champions/Velkoz.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Velkoz.png"
---

# ヴェル＝コズ

![[raw/assets/champions/Velkoz.png|128]]

## 基本情報

- **英字ID：** `Velkoz`
- **キー：** `161`
- **称号：** ヴォイドの瞳
- **データversion：** `16.18.1`

## 紹介

ルーンテラに現れた最初のヴォイドの生物がヴェル＝コズであるかどうかは定かではないが、彼の残酷さと計算された知性にかなうヴォイドの生物は他に存在しない。彼の同族たちは周囲のあらゆるものを貪り食うか破滅させるかのどちらかだが、ヴェル＝コズは物質世界とそこに住む戦争好きの奇妙な生き物たちをを詳細に調べて研究し、ヴォイドが利用できる弱点がないか探そうとしている。ただし、ヴェル＝コズは受動的な観察者などからは程遠い存在であり、襲ってくる者がいれば恐怖のプラズマで反撃し、この世界の構造そのものを破壊しようとする。

## 分類

- **役割タグ：** `Mage`、`Support`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 2 |
| `defense` | 2 |
| `magic` | 10 |
| `difficulty` | 8 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 590 |
| `hpperlevel` | 102 |
| `mp` | 469 |
| `mpperlevel` | 21 |
| `movespeed` | 340 |
| `armor` | 22 |
| `armorperlevel` | 4.7 |
| `spellblock` | 30 |
| `spellblockperlevel` | 1.3 |
| `attackrange` | 525 |
| `hpregen` | 5.5 |
| `hpregenperlevel` | 0.55 |
| `mpregen` | 8 |
| `mpregenperlevel` | 0.8 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 55 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 1.59 |
| `attackspeed` | 0.643 |

## アビリティ

- **パッシブ — 有機分解：** スキルが命中するたびに対象の「有機分解」が進行していき、3スタックすると確定ダメージを与える。

- **Q — 電離炸裂弾：** 再発動させるか敵に命中するとT字に分裂するプラズマ弾を発射する。この弾は命中した敵にスロウ効果とダメージを与える。
- **W — ヴォイドの裂谷：** ヴォイドへ通じる裂け目を大地に呼び出し、触れた敵にダメージを与える。裂け目は少ししてから爆発し、再度ダメージを与える。
- **E — 地殻砕裂：** 指定したエリアを爆発させ、範囲内の敵にダメージを与えてノックアップさせる。 至近距離にいる敵は、わずかにふき飛ばされる。
- **R — 生体破壊光線：** 指定方向へ2.5秒間、強力なビームを発射し、触れた敵に魔法ダメージを与える。このスキルによって「有機分解」されて解析が完了したチャンピオンは確定ダメージを代わりに受ける。

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
- **対象試合：** 178試合、全体勝率 56.2%
- **時間帯別勝率：** 〜20分 57.7%（n=26）、20〜25分 47.6%（n=21）、25〜30分 50.0%（n=36）、30〜35分 62.2%（n=45）、35分〜 58.0%（n=50）
- **最高帯：** 30〜35分（判定差 14.6ポイント）
- **判定根拠：** 5つの時間帯を比較できるが、最高帯と端点の差が8ポイント未満、または勝率が非単調だった。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-161|ヴェル＝コズの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### UTILITY（261試合）

- **実測ビルド候補：** [[wiki/entities/items/item-4628|ホライゾン フォーカス]] + [[wiki/entities/items/item-6655|ルーデン エコー]]（該当n=48、58.3% / 非該当54.0%、差+4.3pt）；[[wiki/entities/items/item-4645|シャドウフレイム]] + [[wiki/entities/items/item-6655|ルーデン エコー]]（該当n=43、58.1% / 非該当54.1%、差+4.0pt）
- **ステータス傾向：** 物理防御（該当n=47、63.8% / 非該当52.8%、差+11.0pt）；体力（該当n=92、59.8% / 非該当52.1%、差+7.7pt）
- **理論仮説：** [[wiki/entities/items/item-3118|マリグナンス]] + [[wiki/entities/items/item-6655|ルーデン エコー]]（n=9（15未満）；共通stats: 魔力・マナ／チャンピオン原典にも言及: マナ）；[[wiki/entities/items/item-2503|黒炎のトーチ]] + [[wiki/entities/items/item-6655|ルーデン エコー]]（n=4（15未満）；共通stats: 魔力・マナ／チャンピオン原典にも言及: マナ）

### MIDDLE（73試合）

- **実測ビルド候補：** 該当・非該当が各30試合以上で正の差を持つ候補なし。
- **ステータス傾向：** 該当・非該当が各30試合以上で正の差を持つ群なし。
- **理論仮説：** [[wiki/entities/items/item-3118|マリグナンス]] + [[wiki/entities/items/item-6655|ルーデン エコー]]（n=1（15未満）；共通stats: 魔力・マナ／チャンピオン原典にも言及: マナ）；[[wiki/entities/items/item-2503|黒炎のトーチ]] + [[wiki/entities/items/item-3118|マリグナンス]]（未観測；共通stats: 魔力・マナ／チャンピオン原典にも言及: マナ）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-161|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### UTILITY（対象n=349）

- **高勝率コンボ候補：** [[wiki/entities/champions/caitlyn|ケイトリン（Caitlyn）]] — 対象側勝率67.7%（21/31）、n=31（十分性の目安を満たす）。
- **カウンターピック候補：** [[wiki/entities/champions/nautilus|ノーチラス（Nautilus）]] — 対象側勝率50.0%（17/34）、n=34（十分性の目安を満たす）。

### MIDDLE（対象n=98）

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

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Velkoz` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Velkoz.png)
