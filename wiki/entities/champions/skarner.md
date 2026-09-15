---
title: "スカーナー"
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
  - role-tank
  - role-fighter
  - data-dragon
champion_id: "Skarner"
champion_key: "72"
data_version: "16.18.1"
roles:
  - "Tank"
  - "Fighter"
resource_type: "マナ"
image_path: "raw/assets/champions/Skarner.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Skarner.png"
---

# スカーナー

![[raw/assets/champions/Skarner.png|128]]

## 基本情報

- **英字ID：** `Skarner`
- **キー：** `72`
- **称号：** 原始の守護者
- **データversion：** `16.18.1`

## 紹介

古代の巨大生物種ブラカーンであるスカーナーは、イシュタルの支配層“ユン・タル”初代メンバーのひとりとして崇拝されている。自らの国家を外敵から守ることにすべてを捧げたスカーナーは、イシャオカン地下の居室で大地の震動に耳を澄ませ、脅威を察知しようとしている。イシュタルが外界から隔絶されていることに対し、ユン・タルの面々が疑問を呈せば呈すほど、スカーナーはますます偏執的に、頑なになり、是が非でもイシュタルとその民を守ろうとするのだった──それがいかなる代償を伴おうとも。

## 分類

- **役割タグ：** `Tank`、`Fighter`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 7 |
| `defense` | 8 |
| `magic` | 5 |
| `difficulty` | 5 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 630 |
| `hpperlevel` | 110 |
| `mp` | 320 |
| `mpperlevel` | 40 |
| `movespeed` | 335 |
| `armor` | 33 |
| `armorperlevel` | 4.5 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 150 |
| `hpregen` | 7.5 |
| `hpregenperlevel` | 0.75 |
| `mpregen` | 7.2 |
| `mpregenperlevel` | 0.75 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 63 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2 |
| `attackspeed` | 0.625 |

## アビリティ

- **パッシブ — 響振動：** スカーナーの通常攻撃、「砕けし大地」、「大地の怒り」、「インペイル」は、敵に「振動」を付与する。「振動」が最大スタックになると、その効果時間をかけて敵に最大体力に応じた魔法ダメージを与える。

- **Q — 砕けし大地/大地の怒り：** 地面から通常攻撃を強化する巨大な岩を掘り起こす。岩は強力な飛翔物として投げることができる。
- **W — 激震の砦：** シールドを獲得して地震を発生させ、衝撃波で敵にダメージとスロウ効果を与える。
- **E — イシュタルの衝動：** 前方に突撃して地形を通り抜ける。チャンピオンか大型モンスターに衝突すると、対象を次にぶつかった壁に叩きつけ、ダメージを与えてスタンさせる。
- **R — インペイル：** 尻尾で前方を貫き、敵チャンピオンにサプレッション効果を与える。サプレッション効果を受けた犠牲者は、スカーナーの動きに追従して引きずられる。

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
- **対象試合：** 129試合、全体勝率 50.4%
- **時間帯別勝率：** 〜20分 55.0%（n=20）、20〜25分 54.5%（n=11）、25〜30分 51.6%（n=31）、30〜35分 44.1%（n=34）、35分〜 51.5%（n=33）
- **最高帯：** 〜20分（判定差 —）
- **判定根拠：** 5つの時間帯のいずれかで15試合未満のため、時間帯の比較を保留する。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-72|スカーナーの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### JUNGLE（210試合）

- **実測ビルド候補：** [[wiki/entities/items/item-2502|終わりなき絶望]] + [[wiki/entities/items/item-3075|ソーンメイル]]（該当n=31、71.0% / 非該当45.3%、差+25.7pt）；[[wiki/entities/items/item-3075|ソーンメイル]] + [[wiki/entities/items/item-3084|心の鋼]]（該当n=41、61.0% / 非該当46.2%、差+14.8pt）
- **ステータス傾向：** 魔法防御（該当n=127、51.2% / 非該当45.8%、差+5.4pt）
- **理論仮説：** [[wiki/entities/items/item-6610|サンダード スカイ]] + [[wiki/entities/items/item-6631|ストライドブレイカー]]（n=1（15未満）；共通stats: 攻撃力・体力／チャンピオン原典にも言及: 攻撃力・体力）；[[wiki/entities/items/item-3161|ショウジンの矛]] + [[wiki/entities/items/item-6610|サンダード スカイ]]（未観測；共通stats: 攻撃力・体力／チャンピオン原典にも言及: 攻撃力・体力）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-72|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### JUNGLE（対象n=246）

- **高勝率コンボ候補：** [[wiki/entities/champions/jhin|ジン（Jhin）]] — 対象側勝率61.9%（13/21）、サンプル不足（n=21、十分性の目安30未満）。
- **カウンターピック候補：** [[wiki/entities/champions/nocturne|ノクターン（Nocturne）]] — 対象側勝率46.7%（7/15）、サンプル不足（n=15、十分性の目安30未満）。

### UTILITY（対象n=28）

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

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Skarner` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Skarner.png)
