---
title: "タロン"
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
  - data-dragon
champion_id: "Talon"
champion_key: "91"
data_version: "16.18.1"
roles:
  - "Assassin"
resource_type: "マナ"
image_path: "raw/assets/champions/Talon.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Talon.png"
---

# タロン

![[raw/assets/champions/Talon.png|128]]

## 基本情報

- **英字ID：** `Talon`
- **キー：** `91`
- **称号：** 将軍の懐刀
- **データversion：** `16.18.1`

## 紹介

タロンは闇を駆ける刃であり、誰にも悟られることなく攻撃し、気付かれる前に脱出することができる非情な殺し屋だ。暴力があふれる危険なノクサスの裏路地で育った彼は、生きるために戦い、殺し、盗みを余儀なくされて、優れたナイフの使い手として知られるようになった。現在は悪名高きデュ・クートウ家の養子となり、帝国の指揮のもとに殺しの仕事を請け負い、敵側の指導者、隊長、英雄…さらには支配者の軽蔑を勝った愚かなノクサス人たちまでも暗殺し続けている。

## 分類

- **役割タグ：** `Assassin`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 9 |
| `defense` | 3 |
| `magic` | 1 |
| `difficulty` | 7 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 658 |
| `hpperlevel` | 109 |
| `mp` | 400 |
| `mpperlevel` | 37 |
| `movespeed` | 335 |
| `armor` | 30 |
| `armorperlevel` | 4.7 |
| `spellblock` | 36 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 125 |
| `hpregen` | 8.5 |
| `hpregenperlevel` | 0.75 |
| `mpregen` | 7.6 |
| `mpregenperlevel` | 0.8 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 68 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2.9 |
| `attackspeed` | 0.625 |

## アビリティ

- **パッシブ — 血塗られし慈悲：** タロンのスキルは敵チャンピオンまたは大型モンスターに3回までスタックする「傷」を付与する。「傷」のスタックが3つになった敵チャンピオンに通常攻撃を行うと、そのチャンピオンは出血して継続的に大ダメージを受ける。

- **Q — ノクサスの刃：** タロンが対象を突き刺す。近接攻撃の射程内であれば、この攻撃はクリティカルダメージを与える。近接攻撃の射程外であれば、対象までジャンプしてから突き刺す。このスキルで対象を倒すと体力の一部が回復し、クールダウンの一部が解消する。
- **W — 飛燕手裏剣：** ブーメランのように戻ってくる刃を同時に複数投げる。刃は往路と復路で敵を貫通するたびに物理ダメージを与える。復路で刃が敵ユニットに命中すると、追加ダメージと短時間のスロウ効果を与える。
- **E — 暗殺者の跳躍：** タロンはどんな地形や建造物も最大距離まで飛び越えられる。このスキルのクールダウンは短いが、飛び越えた地形や建造物に対しては長いクールダウンに入る。
- **R — シャドウアサルト：** 複数の刃を全方向に投げ、インビジブル状態になって移動速度が増加する。インビジブル状態が解除されると、投げた刃がタロンのいる地点に一斉に戻ってくる。飛んでいった時と戻ってきた時のそれぞれで、刃が命中した敵に物理ダメージを与える。

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
- **対象試合：** 158試合、全体勝率 51.9%
- **時間帯別勝率：** 〜20分 58.1%（n=31）、20〜25分 36.0%（n=25）、25〜30分 52.9%（n=34）、30〜35分 58.5%（n=41）、35分〜 48.1%（n=27）
- **最高帯：** 30〜35分（判定差 22.5ポイント）
- **判定根拠：** 5つの時間帯を比較できるが、最高帯と端点の差が8ポイント未満、または勝率が非単調だった。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-91|タロンの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### JUNGLE（511試合）

- **実測ビルド候補：** [[wiki/entities/items/item-3170|スイフトマーチ]] + [[wiki/entities/items/item-6701|オポチュニティー]]（該当n=35、82.9% / 非該当48.5%、差+34.3pt）；[[wiki/entities/items/item-3170|スイフトマーチ]] + [[wiki/entities/items/item-3814|ナイト エッジ]] + [[wiki/entities/items/item-6701|オポチュニティー]]（該当n=33、81.8% / 非該当48.7%、差+33.1pt）
- **ステータス傾向：** 体力（該当n=299、54.8% / 非該当45.3%、差+9.6pt）；物理防御（該当n=58、51.7% / 非該当50.8%、差+1.0pt）
- **理論仮説：** [[wiki/entities/items/item-3071|ブラック クリーバー]] + [[wiki/entities/items/item-3814|ナイト エッジ]]（n=12（15未満）；共通stats: 攻撃力・体力／チャンピオン原典にも言及: 攻撃力・体力）；[[wiki/entities/items/item-3814|ナイト エッジ]] + [[wiki/entities/items/item-6609|ケミパンク チェーンソード]]（n=3（15未満）；共通stats: 攻撃力・体力／チャンピオン原典にも言及: 攻撃力・体力）

### MIDDLE（99試合）

- **実測ビルド候補：** 該当・非該当が各30試合以上で正の差を持つ候補なし。
- **ステータス傾向：** 該当・非該当が各30試合以上で正の差を持つ群なし。
- **理論仮説：** [[wiki/entities/items/item-3071|ブラック クリーバー]] + [[wiki/entities/items/item-6610|サンダード スカイ]]（n=5（15未満）；共通stats: 攻撃力・体力／チャンピオン原典にも言及: 攻撃力・体力）；[[wiki/entities/items/item-3071|ブラック クリーバー]] + [[wiki/entities/items/item-3814|ナイト エッジ]]（n=3（15未満）；共通stats: 攻撃力・体力／チャンピオン原典にも言及: 攻撃力・体力）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-91|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### JUNGLE（対象n=662）

- **高勝率コンボ候補：** [[wiki/entities/champions/jinx|ジンクス（Jinx）]] — 対象側勝率67.5%（27/40）、n=40（十分性の目安を満たす）。
- **カウンターピック候補：** [[wiki/entities/champions/viego|ヴィエゴ（Viego）]] — 対象側勝率64.9%（24/37）、n=37（十分性の目安を満たす）。

### MIDDLE（対象n=183）

- **高勝率コンボ候補：** [[wiki/entities/champions/mordekaiser|モルデカイザー（Mordekaiser）]] — 対象側勝率60.0%（9/15）、サンプル不足（n=15、十分性の目安30未満）。
- **カウンターピック候補：** [[wiki/entities/champions/ahri|アーリ（Ahri）]] — 対象側勝率53.3%（8/15）、サンプル不足（n=15、十分性の目安30未満）。

> [!warning] 実測値の限界
> 味方ペアは同一試合・同一チームで同時に出場した組み合わせ、対面はMatch-v5の最終ロールから推定した同ロール候補である。パッチ、観測ランク帯、プレイヤー、試合展開、構成の交絡を調整していない。とくにサンプル不足の行は探索的な参考値に留める。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-matchups]]、[[wiki/syntheses/champion-combo-counter-ranked-matches|実測コンボ・カウンターピック分析]]
<!-- champion-matchup-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Talon` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Talon.png)
