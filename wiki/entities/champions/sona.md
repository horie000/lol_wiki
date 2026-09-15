---
title: "ソナ"
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
  - role-support
  - role-mage
  - data-dragon
champion_id: "Sona"
champion_key: "37"
data_version: "16.18.1"
roles:
  - "Support"
  - "Mage"
resource_type: "マナ"
image_path: "raw/assets/champions/Sona.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Sona.png"
---

# ソナ

![[raw/assets/champions/Sona.png|128]]

## 基本情報

- **英字ID：** `Sona`
- **キー：** `37`
- **称号：** 沈黙の弦奏師
- **データversion：** `16.18.1`

## 紹介

ソナはデマーシアで随一の弦楽器エトワールの演奏家であり、その優雅な和音と活気あふれる旋律によってのみ自らの意思を伝えることができる。上品な態度で貴族たちの間で人気だが、彼女のうっとりするようなメロディーには実際に魔力が宿っており、デマーシアのタブーに触れるのではないかと考える者たちもいる。よそ者には何も聞こえないが親しい仲間だけはその旋律を理解することが可能で、彼女が爪弾くハーモニーは傷ついた味方を癒し、敵には予想もしないやり方でダメージを与える。

## 分類

- **役割タグ：** `Support`、`Mage`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 5 |
| `defense` | 2 |
| `magic` | 8 |
| `difficulty` | 4 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 550 |
| `hpperlevel` | 91 |
| `mp` | 340 |
| `mpperlevel` | 45 |
| `movespeed` | 325 |
| `armor` | 26 |
| `armorperlevel` | 4.2 |
| `spellblock` | 30 |
| `spellblockperlevel` | 1.3 |
| `attackrange` | 550 |
| `hpregen` | 5.5 |
| `hpregenperlevel` | 0.55 |
| `mpregen` | 11.5 |
| `mpregenperlevel` | 0.4 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 49 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2.3 |
| `attackspeed` | 0.644 |

## アビリティ

- **パッシブ — パワーコード：** アッチェレランド: 通常スキルを使用し条件を満たすたびに、恒久的に通常スキルヘイストを獲得する。獲得可能な上限を超えると、スキルの使用成功時にアルティメットの残りクールダウン時間が短縮されるようになる。 パワーコード: スキルを数回発動するたびに、次の通常攻撃で追加魔法ダメージを与え、さらに最後に発動した通常スキルに応じた追加効果が発生する。

- **Q — ヒム・オブ・ヴァロー：** ソナが「ヒム・オブ・ヴァロー」を演奏し、音波を放って周囲の敵2体(チャンピオンか中立モンスターを優先)に魔法ダメージを与え、さらに一時的にオーラをまとって、接触した味方の次の攻撃に追加ダメージを付与する。
- **W — パーセヴァランス：** ソナが「パーセヴァランス」を演奏し、癒しの旋律によって自身と周囲の味方の体力を回復する。さらにしばらくオーラをまとい、接触した味方に一時的なシールドを与える。
- **E — セレリティ：** ソナが「セレリティ」を演奏して周囲の味方の移動速度を増加させる。さらに一時的にオーラをまとって、接触した味方チャンピオンの移動速度を増加させる。
- **R — クレッシェンド：** ソナが究極の和音を演奏し、触れた敵チャンピオンに魔法ダメージを与え、強制的に踊らせてスタン効果を付与する。

<!-- power-spike:start -->
## パワースパイク

- **区分：** 終盤
- **判定：** [[wiki/syntheses/champion-power-spikes-v16-18-1|パワースパイク分類 v16.18.1]] に基づく原典ベースの推論。
- **根拠：**
  - 条件達成ごとに恒久的に通常スキルヘイストを獲得する。
- **限界：** スキル基礎ダメージ・係数・アイテム完成時刻を全チャンピオンで統一比較できる原典値がないため、実戦の強さや購入優先度を断定しない。

<!-- power-spike:end -->

<!-- power-spike-match:start -->
## 試合時間別の観測

- **観測分類：** 判定保留（分母不足）
- **対象試合：** 86試合、全体勝率 46.5%
- **時間帯別勝率：** 〜20分 25.0%（n=12）、20〜25分 30.8%（n=13）、25〜30分 50.0%（n=18）、30〜35分 59.1%（n=22）、35分〜 52.4%（n=21）
- **最高帯：** 30〜35分（判定差 —）
- **判定根拠：** 5つの時間帯のいずれかで15試合未満のため、時間帯の比較を保留する。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-37|ソナの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### UTILITY（204試合）

- **実測ビルド候補：** [[wiki/entities/items/item-6617|ムーンストーンの再生]] + [[wiki/entities/items/item-6620|ヘリアの残響]]（該当n=45、55.6% / 非該当49.7%、差+5.9pt）
- **ステータス傾向：** マナ（該当n=160、51.2% / 非該当50.0%、差+1.2pt）
- **理論仮説：** [[wiki/entities/items/item-3040|セラフ エンブレイス]] + [[wiki/entities/items/item-6655|ルーデン エコー]]（n=1（15未満）；共通stats: 魔力・マナ／チャンピオン原典にも言及: 魔力・マナ）；[[wiki/entities/items/item-6617|ムーンストーンの再生]] + [[wiki/entities/items/item-6653|ライアンドリーの仮面]]（n=1（15未満）；共通stats: 魔力・体力／チャンピオン原典にも言及: 魔力・体力）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-37|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### UTILITY（対象n=365）

- **高勝率コンボ候補（最大3件）：**
  - [[wiki/entities/champions/akali|アカリ（Akali）]] — 対象側勝率68.8%（11/16）、サンプル不足（n=16、十分性の目安30未満）。
  - [[wiki/entities/champions/yone|ヨネ（Yone）]] — 対象側勝率68.8%（11/16）、サンプル不足（n=16、十分性の目安30未満）。
  - [[wiki/entities/champions/smolder|スモルダー（Smolder）]] — 対象側勝率62.5%（15/24）、サンプル不足（n=24、十分性の目安30未満）。
- **低勝率カウンターピック候補（最大3件）：**
  - [[wiki/entities/champions/leona|レオナ（Leona）]] — 対象側勝率23.1%（6/26）、サンプル不足（n=26、十分性の目安30未満）。
  - [[wiki/entities/champions/nautilus|ノーチラス（Nautilus）]] — 対象側勝率36.8%（7/19）、サンプル不足（n=19、十分性の目安30未満）。
  - [[wiki/entities/champions/thresh|スレッシュ（Thresh）]] — 対象側勝率43.8%（7/16）、サンプル不足（n=16、十分性の目安30未満）。

### TOP（対象n=1）

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

### UTILITY（対象379試合、全体勝率49.1%）

| 順位 | 完全ルーンセット | 選択数 | 選択率 | 選択時勝率 |
| ---: | --- | ---: | ---: | ---: |
| 1 | 主系魔道：エアリー召喚／マナフローバンド・至高・強まる嵐；副系不滅：心身調整・生気付与；シャードUNKNOWN(5008)・UNKNOWN(5008)・UNKNOWN(5001) | 174/379 | 45.9% | 43.1% |
| 2 | 主系魔道：エアリー召喚／マナフローバンド・至高・追火；副系栄華：切り崩し・冷静沈着；シャードUNKNOWN(5008)・UNKNOWN(5008)・UNKNOWN(5001) | 26/379 | 6.9% | 46.2% |
| 3 | 主系魔道：エアリー召喚／マナフローバンド・追い風・強まる嵐；副系天啓：魔法の靴・なんでも屋；シャードUNKNOWN(5007)・UNKNOWN(5010)・UNKNOWN(5011) | 14/379 | 3.7% | 78.6% |

- **選定ロール：** チャンピオン・ロール別の完全試合数が最も多いロールを1つ選んだ。別ロールや全候補は詳細レポートで確認できる。
- **シャード表示：** Data Dragonで表示名を解決できない場合は`UNKNOWN(<ID>)`としてIDを保持する。

- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-rune-selection|Riotランク戦試合データ：チャンピオン別ルーン選択]]、[[wiki/syntheses/champion-rune-selection-ranked-matches|実測チャンピオン別ルーン選択分析]]。
<!-- champion-rune-set-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Sona` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Sona.png)
