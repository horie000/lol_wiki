---
title: "ヤスオ"
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
  - role-assassin
  - data-dragon
champion_id: "Yasuo"
champion_key: "157"
data_version: "16.18.1"
roles:
  - "Fighter"
  - "Assassin"
resource_type: "つむじ風"
image_path: "raw/assets/champions/Yasuo.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Yasuo.png"
---

# ヤスオ

![[raw/assets/champions/Yasuo.png|128]]

## 基本情報

- **英字ID：** `Yasuo`
- **キー：** `157`
- **称号：** 赦されざる者
- **データversion：** `16.18.1`

## 紹介

固い信念を持つアイオニア人のヤスオは風を操って戦う俊敏な剣士だ。高慢な若者だった彼は師匠殺しの濡れ衣を着せられ、無実を証明できぬまま、身を守るために兄を殺めることを余儀なくされた。師匠の死にまつわる真実が明らかとなってもなお、ヤスオが自らの過ちを赦すことはできなかった。自分の剣を導く風だけを頼りに、彼は今も祖国の地を放浪し続けている。

## 分類

- **役割タグ：** `Fighter`、`Assassin`
- **リソース種別：** つむじ風

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 8 |
| `defense` | 4 |
| `magic` | 4 |
| `difficulty` | 10 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 590 |
| `hpperlevel` | 110 |
| `mp` | 100 |
| `mpperlevel` | 0 |
| `movespeed` | 345 |
| `armor` | 32 |
| `armorperlevel` | 4.6 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 175 |
| `hpregen` | 6.5 |
| `hpregenperlevel` | 0.9 |
| `mpregen` | 0 |
| `mpregenperlevel` | 0 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 60 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 3.5 |
| `attackspeed` | 0.697 |

## アビリティ

- **パッシブ — 浪人道：** クリティカル率が増加する。また、移動距離に応じてシールドがチャージされ、敵チャンピオンおよび中立モンスターからダメージを受けると発動する。

- **Q — 抜刀：** 指定方向に突きを放ち、直線上の敵すべてにダメージを与える。 このスキルが命中するとヤスオは「つむじ風」のスタックを数秒間得る。スタックが2つたまるとヤスオは風を身にまとい、次の「抜刀」と同時に「つむじ風」を放つ。「つむじ風」は指定方向に吹き抜け、触れた敵ユニットをノックアップさせる。 「抜刀」は通常攻撃扱いのため、通常攻撃と同じように強化される。
- **W — 風殺の壁：** 4秒間持続し、少しずつ前進する風の壁を生み出す。敵のあらゆる発射物は、この壁に触れると消滅する。
- **E — 風薙ぎ：** 指定した敵を通り過ぎるようにダッシュし、魔法ダメージを与える。発動ごとに、その後のダッシュで与えるダメージが増加する(上限あり)。 同一の敵に対しては数秒間、このスキルを再発動できない。 このスキルのダッシュ中に「抜刀」を発動すると、円状に斬撃を繰り出す。
- **R — 鬼哭啾々：** ノックアップ状態の敵チャンピオンのもとへブリンクし、空中で斬撃を繰り出して物理ダメージを与える。また、範囲内のノックアップ中の敵をさらにノックアップさせる。発動と同時に波動ゲージが満タンになるが「つむじ風」のスタックをすべて消費する。 少しの間、クリティカル時に対象の物理防御増加分を大きく貫通する。

<!-- power-spike:start -->
## パワースパイク

- **区分：** 終盤
- **判定：** [[wiki/syntheses/champion-power-spikes-v16-18-1|パワースパイク分類 v16.18.1]] に基づく原典ベースの推論。
- **根拠：**
  - パッシブでクリティカル率が増加し、Qは通常攻撃扱いである。
- **限界：** スキル基礎ダメージ・係数・アイテム完成時刻を全チャンピオンで統一比較できる原典値がないため、実戦の強さや購入優先度を断定しない。

<!-- power-spike:end -->

<!-- power-spike-match:start -->
## 試合時間別の観測

- **観測分類：** 明瞭な傾向なし
- **対象試合：** 337試合、全体勝率 51.3%
- **時間帯別勝率：** 〜20分 56.7%（n=60）、20〜25分 50.9%（n=53）、25〜30分 54.8%（n=84）、30〜35分 45.1%（n=71）、35分〜 49.3%（n=69）
- **最高帯：** 〜20分（判定差 11.6ポイント）
- **判定根拠：** 5つの時間帯を比較できるが、最高帯と端点の差が8ポイント未満、または勝率が非単調だった。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-157|ヤスオの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### MIDDLE（637試合）

- **実測ビルド候補：** [[wiki/entities/items/item-3031|インフィニティ エッジ]] + [[wiki/entities/items/item-3172|ガンメタル ブーツ]]（該当n=156、66.0% / 非該当47.0%、差+19.0pt）；[[wiki/entities/items/item-3031|インフィニティ エッジ]] + [[wiki/entities/items/item-3153|ルインドキング ブレード]] + [[wiki/entities/items/item-3172|ガンメタル ブーツ]]（該当n=116、66.4% / 非該当48.4%、差+18.0pt）
- **ステータス傾向：** クリティカル率（該当n=558、53.4% / 非該当39.2%、差+14.2pt）；物理防御（該当n=179、60.9% / 非該当48.0%、差+12.9pt）
- **理論仮説：** [[wiki/entities/items/item-3050|ジーク コンバージェンス]] + [[wiki/entities/items/item-6665|変幻自在のジャック＝ショー]]（未観測；共通stats: 物理防御・体力・魔法防御／チャンピオン原典にも言及: 物理防御・体力）；[[wiki/entities/items/item-3073|実験的ヘクスプレート]] + [[wiki/entities/items/item-6631|ストライドブレイカー]]（未観測；共通stats: 攻撃力・攻撃速度・体力／チャンピオン原典にも言及: 攻撃力・体力）

### TOP（131試合）

- **実測ビルド候補：** [[wiki/entities/items/item-3153|ルインドキング ブレード]] + [[wiki/entities/items/item-6673|イモータル シールドボウ]]（該当n=59、47.5% / 非該当38.9%、差+8.6pt）；[[wiki/entities/items/item-3031|インフィニティ エッジ]] + [[wiki/entities/items/item-3153|ルインドキング ブレード]] + [[wiki/entities/items/item-6673|イモータル シールドボウ]]（該当n=30、46.7% / 非該当41.6%、差+5.1pt）
- **ステータス傾向：** 物理防御（該当n=40、47.5% / 非該当40.7%、差+6.8pt）
- **理論仮説：** [[wiki/entities/items/item-3036|ドミニク リガード]] + [[wiki/entities/items/item-6673|イモータル シールドボウ]]（n=9（15未満）；共通stats: 攻撃力・クリティカル率／チャンピオン原典にも言及: 攻撃力・クリティカル率）；[[wiki/entities/items/item-3033|モータル リマインダー]] + [[wiki/entities/items/item-6673|イモータル シールドボウ]]（n=9（15未満）；共通stats: 攻撃力・クリティカル率／チャンピオン原典にも言及: 攻撃力・クリティカル率）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-157|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### MIDDLE（対象n=811）

- **高勝率コンボ候補：** [[wiki/entities/champions/mordekaiser|モルデカイザー（Mordekaiser）]] — 対象側勝率62.2%（51/82）、n=82（十分性の目安を満たす）。
- **カウンターピック候補：** [[wiki/entities/champions/malzahar|マルザハール（Malzahar）]] — 対象側勝率44.4%（20/45）、n=45（十分性の目安を満たす）。

### TOP（対象n=224）

- **高勝率コンボ候補：** [[wiki/entities/champions/miss-fortune|ミス・フォーチュン（MissFortune）]] — 対象側勝率60.0%（12/20）、サンプル不足（n=20、十分性の目安30未満）。
- **カウンターピック候補：** [[wiki/entities/champions/yorick|ヨリック（Yorick）]] — 対象側勝率58.8%（10/17）、サンプル不足（n=17、十分性の目安30未満）。

> [!warning] 実測値の限界
> 味方ペアは同一試合・同一チームで同時に出場した組み合わせ、対面はMatch-v5の最終ロールから推定した同ロール候補である。パッチ、観測ランク帯、プレイヤー、試合展開、構成の交絡を調整していない。とくにサンプル不足の行は探索的な参考値に留める。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-matchups]]、[[wiki/syntheses/champion-combo-counter-ranked-matches|実測コンボ・カウンターピック分析]]
<!-- champion-matchup-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Yasuo` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Yasuo.png)
