---
title: "ヴァイ"
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
champion_id: "Vi"
champion_key: "254"
data_version: "16.18.1"
roles:
  - "Fighter"
  - "Assassin"
resource_type: "マナ"
image_path: "raw/assets/champions/Vi.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Vi.png"
---

# ヴァイ

![[raw/assets/champions/Vi.png|128]]

## 基本情報

- **英字ID：** `Vi`
- **キー：** `254`
- **称号：** ピルトーヴァーの用心棒
- **データversion：** `16.18.1`

## 紹介

ゾウンの貧民街で育ったヴァイは、直情的で頭に血が上りやすく、権力者などというものをほとんど意にも介さない、恐るべき女だ。またかつては若さゆえにしばしば問題を引き起こし、スティルウォーター刑務所で過ごした時間も長いため、生き延びるための知恵に長けた存在でもある。そんな彼女だが、現在はピルトーヴァーの執行官たちと組んで、治安を乱す側ではなく維持する側に立っている。その腕に装着されたヘクステック式パワーグラブは、犯罪者だろうが頑丈な壁だろうが簡単にぶち抜いてしまうだろう。

## 分類

- **役割タグ：** `Fighter`、`Assassin`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 8 |
| `defense` | 5 |
| `magic` | 3 |
| `difficulty` | 4 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 655 |
| `hpperlevel` | 105 |
| `mp` | 295 |
| `mpperlevel` | 65 |
| `movespeed` | 340 |
| `armor` | 30 |
| `armorperlevel` | 4.7 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 125 |
| `hpregen` | 10 |
| `hpregenperlevel` | 1 |
| `mpregen` | 8 |
| `mpregenperlevel` | 0.65 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 63 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2 |
| `attackspeed` | 0.644 |

## アビリティ

- **パッシブ — ケンカの作法：** 一定時間ごとにシールドをチャージし、スキルが敵に命中した瞬間に発動する。

- **Q — 真っすぐいってぶっとばす：** ガントレットにエネルギーをチャージした後、指定方向に猛ダッシュしながらパンチを繰り出す。敵ユニットに命中するとダメージとノックバックを与える。これは「メッタ打ち」の連続攻撃回数にもカウントされる。
- **W — メッタ打ち：** ヴァイのパンチが敵の物理防御を破って追加ダメージを与え、さらに自身の攻撃速度が増加する。
- **E — 無慈悲な連撃：** ヴァイが次の通常攻撃と同時に、衝撃波を放つ。衝撃波は通常攻撃をした対象の背後に広がり、触れた敵にダメージを与える。
- **R — 突入捜査：** 進路にいる敵を跳ね飛ばしながら指定した対象に向かって突撃し、接触と同時に対象をノックアップさせ、追いかけるように自身もジャンプしてから、地面に叩きつけてフィニッシュする。

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
- **対象試合：** 351試合、全体勝率 50.4%
- **時間帯別勝率：** 〜20分 44.2%（n=52）、20〜25分 52.8%（n=53）、25〜30分 54.3%（n=81）、30〜35分 48.6%（n=74）、35分〜 50.5%（n=91）
- **最高帯：** 25〜30分（判定差 10.1ポイント）
- **判定根拠：** 5つの時間帯を比較できるが、最高帯と端点の差が8ポイント未満、または勝率が非単調だった。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-254|ヴァイの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### JUNGLE（598試合）

- **実測ビルド候補：** [[wiki/entities/items/item-3026|ガーディアン エンジェル]] + [[wiki/entities/items/item-3071|ブラック クリーバー]]（該当n=70、64.3% / 非該当47.5%、差+16.7pt）；[[wiki/entities/items/item-3053|ステラックの篭手]] + [[wiki/entities/items/item-6610|サンダード スカイ]]（該当n=63、63.5% / 非該当47.9%、差+15.6pt）
- **ステータス傾向：** クリティカル率（該当n=91、54.9% / 非該当48.5%、差+6.4pt）；物理防御（該当n=425、50.1% / 非該当48.0%、差+2.1pt）
- **理論仮説：** [[wiki/entities/items/item-3073|実験的ヘクスプレート]] + [[wiki/entities/items/item-3078|トリニティ フォース]]（未観測；共通stats: 攻撃力・攻撃速度・体力／チャンピオン原典にも言及: 攻撃力・攻撃速度・体力）；[[wiki/entities/items/item-3050|ジーク コンバージェンス]] + [[wiki/entities/items/item-6665|変幻自在のジャック＝ショー]]（n=1（15未満）；共通stats: 物理防御・体力・魔法防御／チャンピオン原典にも言及: 物理防御・体力）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-254|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### JUNGLE（対象n=735）

- **高勝率コンボ候補：** [[wiki/entities/champions/akali|アカリ（Akali）]] — 対象側勝率61.0%（25/41）、n=41（十分性の目安を満たす）。
- **カウンターピック候補：** [[wiki/entities/champions/master-yi|マスター・イー（MasterYi）]] — 対象側勝率43.2%（16/37）、n=37（十分性の目安を満たす）。

### MIDDLE（対象n=14）

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

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Vi` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Vi.png)
