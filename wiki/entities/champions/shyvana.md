---
title: "シヴァーナ"
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
  - "[[wiki/sources/src-2026-09-15-riot-ranked-match-champion-rune-selection]]"
tags:
  - champion
  - role-fighter
  - role-tank
  - data-dragon
champion_id: "Shyvana"
champion_key: "102"
data_version: "16.18.1"
roles:
  - "Fighter"
  - "Tank"
resource_type: "フューリー"
image_path: "raw/assets/champions/Shyvana.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Shyvana.png"
---

# シヴァーナ

![[raw/assets/champions/Shyvana.png|128]]

## 基本情報

- **英字ID：** `Shyvana`
- **キー：** `102`
- **称号：** 半龍人
- **データversion：** `16.18.1`

## 紹介

シヴァーナは恐るべき半龍の戦士だ。普段は人間の姿をしているが、ドラゴンに変身して空を飛び、炎を吐いて敵を焼き殺すこともできる。王子ジャーヴァンⅣの命を救ったことから、シヴァーナは不安を抱えながらも今や王国の近衛隊として仕え、疑念を向けるデマーシアの人々の中で受け入れられようともがいている。

## 分類

- **役割タグ：** `Fighter`、`Tank`
- **リソース種別：** フューリー

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 8 |
| `defense` | 6 |
| `magic` | 3 |
| `difficulty` | 4 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 625 |
| `hpperlevel` | 95 |
| `mp` | 100 |
| `mpperlevel` | 0 |
| `movespeed` | 350 |
| `armor` | 35 |
| `armorperlevel` | 4 |
| `spellblock` | 32 |
| `spellblockperlevel` | 2.05 |
| `attackrange` | 150 |
| `hpregen` | 7 |
| `hpregenperlevel` | 0.65 |
| `mpregen` | 0 |
| `mpregenperlevel` | 0 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 62 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2 |
| `attackspeed` | 0.638 |

## アビリティ

- **パッシブ — スケールメイル：** 敵チャンピオン、大型ミニオン、大型モンスターのキルかアシストで「スケールメイル」のスタックを獲得し、シヴァーナの防御力が向上する。

- **Q — エンバーストライク：** 次の通常攻撃で、対象とその周囲の両方を攻撃する。このスキルは再発動が可能。ドラゴンフォーム中は再発動が1回追加され、単体の敵に大ダメージを与える。
- **W — インフェルノイージス：** シールドと移動速度を獲得し、少ししてから周囲を爆発させる。ドラゴンフォーム中は、爆発が敵チャンピオンに命中すると自身の体力が回復する。
- **E — モルテンバースト：** 火球を放ち、大型の対象に命中すると爆発して、スロウ効果を付与する。ドラゴンフォーム中は敵を貫通し、大型の敵に命中すると爆発して、炎の軌跡を残す。
- **R — 龍の降臨：** ドラゴンに変身して前方にジャンプし、進路上の敵を逃走させる。ドラゴンフォーム中は巨大化し、通常スキルが強化される。

<!-- power-spike:start -->
## パワースパイク

- **区分：** 序盤、終盤
- **判定：** [[wiki/syntheses/champion-power-spikes-v16-18-1|パワースパイク分類 v16.18.1]] に基づく原典ベースの推論。
- **根拠：**
  - 基礎ステータス指数（体力・物理防御・攻撃力・移動速度を標準化して合算）が173件中22位（上位15%）。体力625、物理防御35、攻撃力62、移動速度350。
  - キルまたはアシストで「スケールメイル」のスタックを得て防御力が向上する。
- **限界：** スキル基礎ダメージ・係数・アイテム完成時刻を全チャンピオンで統一比較できる原典値がないため、実戦の強さや購入優先度を断定しない。

<!-- power-spike:end -->

<!-- power-spike-match:start -->
## 試合時間別の観測

- **観測分類：** 明瞭な傾向なし
- **対象試合：** 303試合、全体勝率 47.5%
- **時間帯別勝率：** 〜20分 50.0%（n=52）、20〜25分 47.2%（n=53）、25〜30分 53.0%（n=66）、30〜35分 42.2%（n=64）、35分〜 45.6%（n=68）
- **最高帯：** 25〜30分（判定差 10.8ポイント）
- **判定根拠：** 5つの時間帯を比較できるが、最高帯と端点の差が8ポイント未満、または勝率が非単調だった。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-102|シヴァーナの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### JUNGLE（521試合）

- **実測ビルド候補：** [[wiki/entities/items/item-2510|黄昏と暁]] + [[wiki/entities/items/item-6672|クラーケン スレイヤー]]（該当n=104、66.3% / 非該当48.7%、差+17.7pt）；[[wiki/entities/items/item-6333|デス ダンス]] + [[wiki/entities/items/item-6672|クラーケン スレイヤー]]（該当n=39、64.1% / 非該当51.2%、差+12.9pt）
- **ステータス傾向：** 魔力（該当n=241、58.5% / 非該当46.8%、差+11.7pt）；体力（該当n=485、52.8% / 非該当44.4%、差+8.3pt）
- **理論仮説：** [[wiki/entities/items/item-3073|実験的ヘクスプレート]] + [[wiki/entities/items/item-3078|トリニティ フォース]]（n=9（15未満）；共通stats: 攻撃力・攻撃速度・体力／チャンピオン原典にも言及: 攻撃力・体力）；[[wiki/entities/items/item-3050|ジーク コンバージェンス]] + [[wiki/entities/items/item-6665|変幻自在のジャック＝ショー]]（未観測；共通stats: 物理防御・体力・魔法防御／チャンピオン原典にも言及: 物理防御・体力）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-102|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### JUNGLE（対象n=612）

- **高勝率コンボ候補（最大3件）：**
  - [[wiki/entities/champions/smolder|スモルダー（Smolder）]] — 対象側勝率70.3%（26/37）、n=37（十分性の目安を満たす）。
  - [[wiki/entities/champions/seraphine|セラフィーン（Seraphine）]] — 対象側勝率63.8%（30/47）、n=47（十分性の目安を満たす）。
  - [[wiki/entities/champions/leona|レオナ（Leona）]] — 対象側勝率62.1%（36/58）、n=58（十分性の目安を満たす）。
- **低勝率カウンターピック候補（最大3件）：**
  - [[wiki/entities/champions/viego|ヴィエゴ（Viego）]] — 対象側勝率61.5%（24/39）、n=39（十分性の目安を満たす）。
  - [[wiki/entities/champions/lee-sin|リー・シン（LeeSin）]] — 対象側勝率72.7%（24/33）、n=33（十分性の目安を満たす）。

### TOP（対象n=32）

- **高勝率コンボ候補（最大3件）：** n=15以上の味方組み合わせなし。サンプル不足のため判断保留。
- **低勝率カウンターピック候補（最大3件）：** n=15以上の同ロール対面なし。サンプル不足のため判断保留。

> [!warning] 実測値の限界
> 味方ペアは同一試合・同一チームで同時に出場した組み合わせ、対面はMatch-v5の最終ロールから推定した同ロール候補である。パッチ、観測ランク帯、プレイヤー、試合展開、構成の交絡を調整していない。とくにサンプル不足の行は探索的な参考値に留める。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-matchups]]、[[wiki/syntheses/champion-combo-counter-ranked-matches|実測コンボ・カウンターピック分析]]
<!-- champion-matchup-analysis:end -->

<!-- champion-rune-set-analysis:start -->
## よく選ばれるルーンセット（実測）

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合20,010件、[[reports/riot-ranked-match-analysis/run-20260915T103154Z/report|ルーンセットの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-rune-selection|Riotランク戦試合データ：チャンピオン別ルーン選択]]、[[wiki/syntheses/champion-rune-selection-ranked-matches|実測チャンピオン別ルーン選択分析]]。
- **読み方：** 主系・キーストーン・主系3枠・副系2枠・3シャードが完全一致する組み合わせを、同じチャンピオン・正規化ロールの参加者を分母に集計した。選択時勝率は記述統計であり、因果効果や推奨を示さない。

### JUNGLE（対象695試合、全体勝率52.4%）

| 順位 | 完全ルーンセット | 選択数 | 選択率 | 選択時勝率 |
| ---: | --- | ---: | ---: | ---: |
| 1 | 主系栄華：プレスアタック／凱旋・レジェンド: ヘイスト・背水の陣；副系天啓：宇宙の英知・魔法の靴；シャードUNKNOWN(5005)・UNKNOWN(5008)・UNKNOWN(5001) | 161/695 | 23.2% | 59.0% |
| 2 | 主系栄華：征服者／凱旋・レジェンド: 迅速・背水の陣；副系天啓：宇宙の英知・魔法の靴；シャードUNKNOWN(5005)・UNKNOWN(5008)・UNKNOWN(5001) | 123/695 | 17.7% | 49.6% |
| 3 | 主系栄華：プレスアタック／凱旋・レジェンド: ヘイスト・背水の陣；副系天啓：魔法の靴・宇宙の英知；シャードUNKNOWN(5005)・UNKNOWN(5008)・UNKNOWN(5001) | 55/695 | 7.9% | 41.8% |

- **選定ロール：** チャンピオン・ロール別の完全試合数が最も多いロールを1つ選んだ。別ロールや全候補は詳細レポートで確認できる。
- **シャード表示：** Data Dragonで表示名を解決できない場合は`UNKNOWN(<ID>)`としてIDを保持する。

- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-rune-selection|Riotランク戦試合データ：チャンピオン別ルーン選択]]、[[wiki/syntheses/champion-rune-selection-ranked-matches|実測チャンピオン別ルーン選択分析]]。
<!-- champion-rune-set-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Shyvana` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Shyvana.png)
