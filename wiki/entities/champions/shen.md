---
title: "シェン"
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
  - data-dragon
champion_id: "Shen"
champion_key: "98"
data_version: "16.18.1"
roles:
  - "Tank"
resource_type: "気"
image_path: "raw/assets/champions/Shen.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Shen.png"
---

# シェン

![[raw/assets/champions/Shen.png|128]]

## 基本情報

- **英字ID：** `Shen`
- **キー：** `98`
- **称号：** 黄昏の瞳
- **データversion：** `16.18.1`

## 紹介

シェンは「均衡の守人」として知られるアイオニアの秘密の戦士たちの長「黄昏の瞳」であり、全ての感情、偏見、自尊心などの迷いから逃れるため、霊的領域と物質世界の間に存在する見えざる道を、感情に左右されることなく歩み続けている。彼は二つの世界の均衡を保つという任務を託されており、それを脅かそうとする者には鋼の刀と魔術の力で挑む。

## 分類

- **役割タグ：** `Tank`
- **リソース種別：** 気

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 3 |
| `defense` | 9 |
| `magic` | 3 |
| `difficulty` | 4 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 610 |
| `hpperlevel` | 99 |
| `mp` | 400 |
| `mpperlevel` | 0 |
| `movespeed` | 340 |
| `armor` | 34 |
| `armorperlevel` | 4.2 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 125 |
| `hpregen` | 8.5 |
| `hpregenperlevel` | 0.75 |
| `mpregen` | 50 |
| `mpregenperlevel` | 0 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 64 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 3 |
| `attackspeed` | 0.751 |

## アビリティ

- **パッシブ — 内気功：** スキルを使用すると、自身にシールドを展開する。また味方、もしくは敵チャンピオンに対してスキルを使用すると、この効果のクールダウンが短縮される。

- **Q — 護刃招来：** 「スピリットブレード」を自身のもとへ呼び寄せ、通常攻撃に対象の最大体力に応じた追加ダメージを付与する。移動中の「スピリットブレード」が敵チャンピオンを斬りつけると追加ダメージが強化され、斬りつけられた敵はシェンから逃げる際にスロウ状態になる。
- **W — 防人の帳：** 「スピリットブレード」を中心に、敵チャンピオンの通常攻撃をブロックするフィールドを展開する。
- **E — 殺気駆け：** 指定方向にダッシュし、触れた敵チャンピオンにタウント効果を与える。
- **R — 瞬身護法：** 指定した味方チャンピオンにシールドを展開し、印を結んだあと「スピリットブレード」と共にそのチャンピオンのもとへワープする。

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
- **対象試合：** 110試合、全体勝率 58.2%
- **時間帯別勝率：** 〜20分 66.7%（n=24）、20〜25分 40.0%（n=15）、25〜30分 66.7%（n=27）、30〜35分 43.8%（n=16）、35分〜 60.7%（n=28）
- **最高帯：** 〜20分（判定差 26.7ポイント）
- **判定根拠：** 5つの時間帯を比較できるが、最高帯と端点の差が8ポイント未満、または勝率が非単調だった。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-98|シェンの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### TOP（205試合）

- **実測ビルド候補：** [[wiki/entities/items/item-3075|ソーンメイル]] + [[wiki/entities/items/item-3748|タイタン ハイドラ]]（該当n=32、65.6% / 非該当50.9%、差+14.8pt）；[[wiki/entities/items/item-3084|心の鋼]] + [[wiki/entities/items/item-3748|タイタン ハイドラ]]（該当n=33、54.5% / 非該当52.9%、差+1.6pt）
- **ステータス傾向：** 物理防御（該当n=173、56.1% / 非該当37.5%、差+18.6pt）；攻撃速度（該当n=37、59.5% / 非該当51.8%、差+7.7pt）
- **理論仮説：** [[wiki/entities/items/item-2501|覇王のブラッドメイル]] + [[wiki/entities/items/item-3748|タイタン ハイドラ]]（n=1（15未満）；共通stats: 攻撃力・体力／チャンピオン原典にも言及: 攻撃力・体力）；[[wiki/entities/items/item-2524|バンドルパイプ]] + [[wiki/entities/items/item-6665|変幻自在のジャック＝ショー]]（n=1（15未満）；共通stats: 物理防御・体力・魔法防御／チャンピオン原典にも言及: 体力）

### JUNGLE（107試合）

- **実測ビルド候補：** 該当・非該当が各30試合以上で正の差を持つ候補なし。
- **ステータス傾向：** 該当・非該当が各30試合以上で正の差を持つ群なし。
- **理論仮説：** [[wiki/entities/items/item-3073|実験的ヘクスプレート]] + [[wiki/entities/items/item-6631|ストライドブレイカー]]（未観測；共通stats: 攻撃力・攻撃速度・体力／チャンピオン原典にも言及: 攻撃力・体力）；[[wiki/entities/items/item-3071|ブラック クリーバー]] + [[wiki/entities/items/item-3073|実験的ヘクスプレート]]（n=1（15未満）；共通stats: 攻撃力・体力／チャンピオン原典にも言及: 攻撃力・体力）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-98|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### TOP（対象n=301）

- **高勝率コンボ候補：** [[wiki/entities/champions/jhin|ジン（Jhin）]] — 対象側勝率86.7%（13/15）、サンプル不足（n=15、十分性の目安30未満）。
- **カウンターピック候補：** [[wiki/entities/champions/aatrox|エイトロックス（Aatrox）]] — 対象側勝率35.3%（6/17）、サンプル不足（n=17、十分性の目安30未満）。

### JUNGLE（対象n=142）

- **高勝率コンボ候補：** [[wiki/entities/champions/akshan|アクシャン（Akshan）]] — 対象側勝率48.0%（12/25）、サンプル不足（n=25、十分性の目安30未満）。
- **カウンターピック候補：** n=15以上の同ロール対面なし。サンプル不足のため判断保留。

> [!warning] 実測値の限界
> 味方ペアは同一試合・同一チームで同時に出場した組み合わせ、対面はMatch-v5の最終ロールから推定した同ロール候補である。パッチ、観測ランク帯、プレイヤー、試合展開、構成の交絡を調整していない。とくにサンプル不足の行は探索的な参考値に留める。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-matchups]]、[[wiki/syntheses/champion-combo-counter-ranked-matches|実測コンボ・カウンターピック分析]]
<!-- champion-matchup-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Shen` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Shen.png)
