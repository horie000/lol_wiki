---
title: "ブラッドミア"
type: entity
status: active
created: 2026-09-14
updated: 2026-09-16
sources:
  - "[[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]]"
  - "[[wiki/sources/src-2026-09-14-dragontail-16-18-1]]"
  - "[[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]"
  - "[[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis]]"
  - "[[wiki/sources/src-2026-09-15-riot-ranked-match-champion-matchups]]"
  - "[[wiki/sources/src-2026-09-15-riot-ranked-match-champion-rune-selection]]"
  - "[[wiki/sources/src-2026-09-16-riot-ranked-match-tier-analysis]]"
tags:
  - champion
  - role-mage
  - role-fighter
  - data-dragon
champion_id: "Vladimir"
champion_key: "8"
data_version: "16.18.1"
roles:
  - "Mage"
  - "Fighter"
resource_type: "真紅の衝動"
image_path: "raw/assets/champions/Vladimir.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Vladimir.png"
---

# ブラッドミア

![[raw/assets/champions/Vladimir.png|128]]

## 基本情報

- **英字ID：** `Vladimir`
- **キー：** `8`
- **称号：** 真紅の死神
- **データversion：** `16.18.1`

## 紹介

ブラッドミアは定命の者の血に飢えた悪魔であり、帝国の建国時代からずっとノクサスの政治に影響を与えてきている。彼は異常なやり方で自らの命を長らえているだけでなく、習得した血を操る魔術を使い、他者の肉体と精神を自分のものとして扱うこともできる。この能力を活かして、ノクサスの貴族たちが集まるきらびやかなサロンで自分を崇拝する熱狂的な信者たちを作り出し、粗末な路地裏では敵の血を最後の一滴まで搾り取っている。

## 分類

- **役割タグ：** `Mage`、`Fighter`
- **リソース種別：** 真紅の衝動

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 2 |
| `defense` | 6 |
| `magic` | 8 |
| `difficulty` | 7 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 600 |
| `hpperlevel` | 110 |
| `mp` | 2 |
| `mpperlevel` | 0 |
| `movespeed` | 330 |
| `armor` | 24 |
| `armorperlevel` | 4.5 |
| `spellblock` | 30 |
| `spellblockperlevel` | 1.3 |
| `attackrange` | 450 |
| `hpregen` | 7 |
| `hpregenperlevel` | 0.6 |
| `mpregen` | 0 |
| `mpregenperlevel` | 0 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 55 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2 |
| `attackspeed` | 0.658 |

## アビリティ

- **パッシブ — 真紅の盟約：** 増加体力を30得るたび魔力が1増加する。また、魔力1につき体力が1.6増加する(この固有スキル自身の効果とは重複しない)。

- **Q — 吸血：** 指定した敵ユニットから血を吸い取り、体力を吸収する。リソースが溜まっている状態の時、「吸血」のダメージと回復量が一定時間大幅に増加する。
- **W — 紅血の沼：** 2秒間血の池に潜り、敵に対象指定されなくなる。また、池に接触した敵にスロウとダメージを与え、与えたダメージに応じた体力を吸収する。
- **E — 血液奔流：** 自分の体力を消費して血液をチャージし、解放した時に自分の周囲にダメージを与える。この攻撃は敵ユニットを貫通せず、遮られる。
- **R — 呪血の渦：** 指定範囲に急速に進行する疫病をばら撒き、感染した敵は一定時間、あらゆる被ダメージが増加する。さらに数秒後爆発が起こり、感染した敵は魔法ダメージを受け、さらにブラッドミアは感染させた敵チャンピオンの数に応じて体力を回復する。

<!-- power-spike:start -->
## パワースパイク

- **区分：** 終盤
- **判定：** [[wiki/syntheses/champion-power-spikes-v16-18-1|パワースパイク分類 v16.18.1]] に基づく原典ベースの推論。
- **根拠：**
  - 増加体力と魔力を相互に増加させる。
- **限界：** スキル基礎ダメージ・係数・アイテム完成時刻を全チャンピオンで統一比較できる原典値がないため、実戦の強さや購入優先度を断定しない。

<!-- power-spike:end -->

<!-- power-spike-match:start -->
## 試合時間別の観測

- **スナップショット：** 2026-09-15生成、キュー420、完全試合4,672件、[[reports/riot-ranked-match-analysis/run-20260915T010911Z/report|詳細レポート]]。
- **観測分類：** 判定保留（分母不足）
- **対象試合：** 58試合、全体勝率 56.9%
- **時間帯別勝率：** 〜20分 57.1%（n=7）、20〜25分 28.6%（n=7）、25〜30分 30.0%（n=10）、30〜35分 62.5%（n=24）、35分〜 90.0%（n=10）
- **最高帯：** 35分〜（判定差 不明）
- **判定根拠：** 全5帯で各15試合未満の帯がある。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-8|ブラッドミアの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### MIDDLE（137試合）

- **実測ビルド候補：** [[wiki/entities/items/item-3089|ラバドン デスキャップ]] + [[wiki/entities/items/item-3171|真紅のアイオニア ブーツ]]（該当n=30、63.3% / 非該当43.9%、差+19.4pt）；[[wiki/entities/items/item-3089|ラバドン デスキャップ]] + [[wiki/entities/items/item-4633|リフトメーカー]]（該当n=32、59.4% / 非該当44.8%、差+14.6pt）
- **ステータス傾向：** 物理防御（該当n=34、50.0% / 非該当47.6%、差+2.4pt）
- **理論仮説：** [[wiki/entities/items/item-3041|メジャイ ソウルスティーラー]] + [[wiki/entities/items/item-4633|リフトメーカー]]（n=9（15未満）；共通stats: 魔力・体力／チャンピオン原典にも言及: 魔力・体力）；[[wiki/entities/items/item-3041|メジャイ ソウルスティーラー]] + [[wiki/entities/items/item-4629|コズミック ドライブ]]（n=6（15未満）；共通stats: 魔力・体力／チャンピオン原典にも言及: 魔力・体力）

### TOP（51試合）

- **実測ビルド候補：** 該当・非該当が各30試合以上で正の差を持つ候補なし。
- **ステータス傾向：** 該当・非該当が各30試合以上で正の差を持つ群なし。
- **理論仮説：** [[wiki/entities/items/item-4629|コズミック ドライブ]] + [[wiki/entities/items/item-4633|リフトメーカー]]（n=13（15未満）；共通stats: 魔力・体力／チャンピオン原典にも言及: 魔力・体力）；[[wiki/entities/items/item-3041|メジャイ ソウルスティーラー]] + [[wiki/entities/items/item-4629|コズミック ドライブ]]（n=5（15未満）；共通stats: 魔力・体力／チャンピオン原典にも言及: 魔力・体力）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-8|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### MIDDLE（対象n=225）

- **高勝率コンボ候補（最大3件）：**
  - [[wiki/entities/champions/ezreal|エズリアル（Ezreal）]] — 対象側勝率73.3%（11/15）、サンプル不足（n=15、十分性の目安30未満）。
  - [[wiki/entities/champions/miss-fortune|ミス・フォーチュン（MissFortune）]] — 対象側勝率66.7%（12/18）、サンプル不足（n=18、十分性の目安30未満）。
  - [[wiki/entities/champions/seraphine|セラフィーン（Seraphine）]] — 対象側勝率62.5%（10/16）、サンプル不足（n=16、十分性の目安30未満）。
- **低勝率カウンターピック候補（最大3件）：** n=15以上の同ロール対面なし。サンプル不足のため判断保留。

### TOP（対象n=98）

- **高勝率コンボ候補（最大3件）：** n=15以上の味方組み合わせなし。サンプル不足のため判断保留。
- **低勝率カウンターピック候補（最大3件）：** n=15以上の同ロール対面なし。サンプル不足のため判断保留。

> [!warning] 実測値の限界
> 味方ペアは同一試合・同一チームで同時に出場した組み合わせ、対面はMatch-v5の最終ロールから推定した同ロール候補である。パッチ、観測ランク帯、プレイヤー、試合展開、構成の交絡を調整していない。とくにサンプル不足の行は探索的な参考値に留める。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-matchups]]、[[wiki/syntheses/champion-combo-counter-ranked-matches|実測コンボ・カウンターピック分析]]
<!-- champion-matchup-analysis:end -->

<!-- champion-rune-set-analysis:start -->
## よく選ばれるルーンセット（実測）

- **スナップショット：** 2026-09-16生成、キュー420、ユニーク試合10,000件、[[reports/riot-ranked-match-analysis/run-20260916T081004Z/report|ルーンセットの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-rune-selection|Riotランク戦試合データ：チャンピオン別ルーン選択]]、[[wiki/syntheses/champion-rune-selection-ranked-matches|実測チャンピオン別ルーン選択分析]]。
- **読み方：** 主系・キーストーン・主系3枠・副系2枠・3シャードが完全一致する組み合わせを、同じチャンピオン・正規化ロールの参加者を分母に集計した。選択時勝率は記述統計であり、因果効果や推奨を示さない。

### MIDDLE（対象197試合、全体勝率53.8%）

| 順位 | 完全ルーンセット | 選択数 | 選択率 | 選択時勝率 |
| ---: | --- | ---: | ---: | ---: |
| 1 | 主系魔道：嵐乗りの勇躍／ニンバスクローク・至高・強まる嵐；副系栄華：背水の陣・レジェンド: ヘイスト；シャードUNKNOWN(5007)・UNKNOWN(5008)・UNKNOWN(5001) | 34/197 | 17.3% | 41.2% |
| 2 | 主系魔道：嵐乗りの勇躍／ニンバスクローク・至高・強まる嵐；副系栄華：レジェンド: ヘイスト・背水の陣；シャードUNKNOWN(5007)・UNKNOWN(5008)・UNKNOWN(5011) | 24/197 | 12.2% | 66.7% |
| 3 | 主系魔道：死神の残り火／ニンバスクローク・至高・強まる嵐；副系栄華：背水の陣・レジェンド: ヘイスト；シャードUNKNOWN(5007)・UNKNOWN(5008)・UNKNOWN(5001) | 16/197 | 8.1% | 31.2% |

- **選定ロール：** チャンピオン・ロール別の完全試合数が最も多いロールを1つ選んだ。別ロールや全候補は詳細レポートで確認できる。
- **シャード表示：** Data Dragonで表示名を解決できない場合は`UNKNOWN(<ID>)`としてIDを保持する。

- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-rune-selection|Riotランク戦試合データ：チャンピオン別ルーン選択]]、[[wiki/syntheses/champion-rune-selection-ranked-matches|実測チャンピオン別ルーン選択分析]]。
<!-- champion-rune-set-analysis:end -->

<!-- champion-tier-analysis:start -->
## 観測ランク帯別チャンピオン候補

- **スナップショット：** 2026-09-16生成、キュー420、観測10帯、各1,000試合、統合後9,761試合、min-games 15、[[reports/riot-ranked-tier-analysis/run-20260916T083219Z/report|ランク帯別詳細レポート]]。
- **根拠：** [[wiki/sources/src-2026-09-16-riot-ranked-match-tier-analysis|Riotランク戦試合データ：観測ランク帯別特徴]]、[[wiki/syntheses/ranked-tier-characteristics|ランク帯別の試合特徴と全帯共通傾向]]。
- **読み方：** `observed_tier` はその試合を発見したプレイヤーの収集時点の所属帯であり、10人全員の試合時ランクではない。以下は各帯の上位選択と、min-games以上で機械的に抽出した高低勝率の探索候補で、推奨・因果効果・有意差を示さない。

### 高勝率候補（上位5）

| 観測帯 | 候補順位 | 試合数 | 勝敗 | 勝率 |
| --- | ---: | ---: | --- | ---: |
| SILVER | 4 | 15 | 10勝/5敗 | 66.7% |
| EMERALD | 2 | 36 | 26勝/10敗 | 72.2% |

### 低勝率候補（下位5）

| 観測帯 | 候補順位 | 試合数 | 勝敗 | 勝率 |
| --- | ---: | ---: | --- | ---: |
| GOLD | 1 | 25 | 6勝/19敗 | 24.0% |

<!-- champion-tier-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Vladimir` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Vladimir.png)
