---
title: "ライズ"
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
tags:
  - champion
  - role-mage
  - data-dragon
champion_id: "Ryze"
champion_key: "13"
data_version: "16.18.1"
roles:
  - "Mage"
resource_type: "マナ"
image_path: "raw/assets/champions/Ryze.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Ryze.png"
---

# ライズ

![[raw/assets/champions/Ryze.png|128]]

## 基本情報

- **英字ID：** `Ryze`
- **キー：** `13`
- **称号：** ルーンの魔導師
- **データversion：** `16.18.1`

## 紹介

ライズは類まれな能力を持つルーンテラ屈指の魔術師として知られ、古くから揺るぎない信念を持って活動している。その信念の裏に、彼は耐え難いほどの重荷を背負っている。ライズは計り知れない才能と神秘の力に関する膨大な知識を駆使し、ワールドルーン──無から世界を形成したとされる原始の魔法の断片──を探すことに人生を捧げる。古代文字が刻まれたルーンは、妄用される前に回収しなければならない。ルーンテラを創生した古代文字は、ルーンテラを破壊する力をも秘めているのだ。

## 分類

- **役割タグ：** `Mage`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 2 |
| `defense` | 2 |
| `magic` | 10 |
| `difficulty` | 7 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 620 |
| `hpperlevel` | 124 |
| `mp` | 300 |
| `mpperlevel` | 70 |
| `movespeed` | 340 |
| `armor` | 22 |
| `armorperlevel` | 4.2 |
| `spellblock` | 32 |
| `spellblockperlevel` | 1.3 |
| `attackrange` | 550 |
| `hpregen` | 8 |
| `hpregenperlevel` | 0.8 |
| `mpregen` | 8 |
| `mpregenperlevel` | 1 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 55 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 2.11 |
| `attackspeed` | 0.658 |

## アビリティ

- **パッシブ — 古代の呪術：** ライズのスキルは増加したマナに応じて追加ダメージを与え、魔力に応じて最大マナが一定割合増加する。

- **Q — オーバーロード：** 自動効果: 他の通常スキルを使うと「オーバーロード」のクールダウンがリセットされ、「ルーン」がチャージされる。「ルーン」が2つチャージされた状態で「オーバーロード」を使用すると、少しの間移動速度が増加する。 発動効果: 凝縮したエネルギー弾を直線上に発射して、最初に当たった敵にダメージを与える。すでに対象に「フラックス」が付与されていた場合、「オーバーロード」は追加ダメージを与え、周囲の敵に「フラックス」が波及する。
- **W — ルーンプリズン：** 対象をルーンの檻に捕らえ、ダメージとスロウ効果を与える。対象に「フラックス」が付与されている場合は、スロウの代わりにスネア状態にする。
- **E — スペルフラックス：** 純粋な魔力を凝縮したオーブを発射して対象にダメージを与え、対象とその周囲のすべての敵にデバフを与える。ライズのスキルはデバフを受けた敵には追加効果を与える。
- **R — ポータルワープ：** 自動効果: 「フラックス」が付与された対象に「オーバーロード」で与える追加ダメージが増加する。 発動効果: 近くにポータルを発生させる。数秒後、指定した場所にポータルの範囲内の味方をテレポートさせる。

<!-- power-spike:start -->
## パワースパイク

- **区分：** 終盤
- **判定：** [[wiki/syntheses/champion-power-spikes-v16-18-1|パワースパイク分類 v16.18.1]] に基づく原典ベースの推論。
- **根拠：**
  - 増加マナでスキルダメージが増え、魔力で最大マナも増加する。
- **限界：** スキル基礎ダメージ・係数・アイテム完成時刻を全チャンピオンで統一比較できる原典値がないため、実戦の強さや購入優先度を断定しない。

<!-- power-spike:end -->

<!-- power-spike-match:start -->
## 試合時間別の観測

- **スナップショット：** 2026-09-15生成、キュー420、完全試合4,672件、[[reports/riot-ranked-match-analysis/run-20260915T010911Z/report|詳細レポート]]。
- **観測分類：** 判定保留（分母不足）
- **対象試合：** 75試合、全体勝率 42.7%
- **時間帯別勝率：** 〜20分 50.0%（n=10）、20〜25分 33.3%（n=9）、25〜30分 31.6%（n=19）、30〜35分 52.2%（n=23）、35分〜 42.9%（n=14）
- **最高帯：** 30〜35分（判定差 不明）
- **判定根拠：** 全5帯で各15試合未満の帯がある。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-13|ライズの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### MIDDLE（192試合）

- **実測ビルド候補：** [[wiki/entities/items/item-2522|アクチュアライザー]] + [[wiki/entities/items/item-3040|セラフ エンブレイス]]（該当n=57、64.9% / 非該当39.3%、差+25.7pt）；[[wiki/entities/items/item-3040|セラフ エンブレイス]] + [[wiki/entities/items/item-3173|チェインレースド クラッシャー]]（該当n=37、64.9% / 非該当42.6%、差+22.3pt）
- **ステータス傾向：** 魔法防御（該当n=60、53.3% / 非該当43.9%、差+9.4pt）；物理防御（該当n=81、49.4% / 非該当45.0%、差+4.3pt）
- **理論仮説：** [[wiki/entities/items/item-3003|アークエンジェル スタッフ]] + [[wiki/entities/items/item-6657|ロッド オブ エイジス]]（n=4（15未満）；共通stats: 魔力・マナ／チャンピオン原典にも言及: 魔力・マナ）；[[wiki/entities/items/item-3040|セラフ エンブレイス]] + [[wiki/entities/items/item-6655|ルーデン エコー]]（n=3（15未満）；共通stats: 魔力・マナ／チャンピオン原典にも言及: 魔力・マナ）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-13|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### MIDDLE（対象n=320）

- **高勝率コンボ候補（最大3件）：**
  - [[wiki/entities/champions/ashe|アッシュ（Ashe）]] — 対象側勝率44.4%（16/36）、n=36（十分性の目安を満たす）。
- **低勝率カウンターピック候補（最大3件）：**
  - [[wiki/entities/champions/hwei|フェイ（Hwei）]] — 対象側勝率45.0%（9/20）、サンプル不足（n=20、十分性の目安30未満）。
  - [[wiki/entities/champions/ahri|アーリ（Ahri）]] — 対象側勝率50.0%（11/22）、サンプル不足（n=22、十分性の目安30未満）。
  - [[wiki/entities/champions/sylas|サイラス（Sylas）]] — 対象側勝率50.0%（9/18）、サンプル不足（n=18、十分性の目安30未満）。

### TOP（対象n=50）

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

### MIDDLE（対象169試合、全体勝率45.6%）

| 順位 | 完全ルーンセット | 選択数 | 選択率 | 選択時勝率 |
| ---: | --- | ---: | ---: | ---: |
| 1 | 主系魔道：死神の残り火／マナフローバンド・追い風・追火；副系不滅：ボーンアーマー・超成長；シャードUNKNOWN(5005)・UNKNOWN(5010)・UNKNOWN(5011) | 26/169 | 15.4% | 38.5% |
| 2 | 主系魔道：嵐乗りの勇躍／マナフローバンド・至高・強まる嵐；副系不滅：ボーンアーマー・超成長；シャードUNKNOWN(5005)・UNKNOWN(5008)・UNKNOWN(5001) | 22/169 | 13.0% | 40.9% |
| 3 | 主系魔道：死神の残り火／マナフローバンド・追い風・追火；副系不滅：超成長・ボーンアーマー；シャードUNKNOWN(5005)・UNKNOWN(5010)・UNKNOWN(5011) | 9/169 | 5.3% | 44.4% |

- **選定ロール：** チャンピオン・ロール別の完全試合数が最も多いロールを1つ選んだ。別ロールや全候補は詳細レポートで確認できる。
- **シャード表示：** Data Dragonで表示名を解決できない場合は`UNKNOWN(<ID>)`としてIDを保持する。

- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-rune-selection|Riotランク戦試合データ：チャンピオン別ルーン選択]]、[[wiki/syntheses/champion-rune-selection-ranked-matches|実測チャンピオン別ルーン選択分析]]。
<!-- champion-rune-set-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Ryze` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Ryze.png)
