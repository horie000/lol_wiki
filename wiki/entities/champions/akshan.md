---
title: "アクシャン"
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
  - role-marksman
  - role-assassin
  - data-dragon
champion_id: "Akshan"
champion_key: "166"
data_version: "16.18.1"
roles:
  - "Marksman"
  - "Assassin"
resource_type: "マナ"
image_path: "raw/assets/champions/Akshan.png"
image_url: "https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Akshan.png"
---

# アクシャン

![[raw/assets/champions/Akshan.png|128]]

## 基本情報

- **英字ID：** `Akshan`
- **キー：** `166`
- **称号：** 流浪の番人
- **データversion：** `16.18.1`

## 紹介

危機を前にしても片眉を少し上げるだけ。飄々とした伊達男のアクシャンは、正しき復讐を果たすべく、露出度高く、今日も颯爽と悪に立ち向かう。隠密戦闘に熟達している彼は敵の目から自由自在に姿をくらまし、もっとも予想外のタイミングで奇襲に転じることができる。アクシャンは、強い正義感と死を覆す伝説の武器を携え、ルーンテラの多くの悪党たちにけじめをつけさせている。「自分を許せないことはするな」という自分なりの道徳観に基づいて。

## 分類

- **役割タグ：** `Marksman`、`Assassin`
- **リソース種別：** マナ

## 評価値

| フィールド | 値 |
| --- | ---: |
| `attack` | 0 |
| `defense` | 0 |
| `magic` | 0 |
| `difficulty` | 0 |

## 数値ステータス

| フィールド | 値 |
| --- | ---: |
| `hp` | 610 |
| `hpperlevel` | 107 |
| `mp` | 350 |
| `mpperlevel` | 40 |
| `movespeed` | 330 |
| `armor` | 26 |
| `armorperlevel` | 4.7 |
| `spellblock` | 33 |
| `spellblockperlevel` | 1.1 |
| `attackrange` | 500 |
| `hpregen` | 3.75 |
| `hpregenperlevel` | 0.65 |
| `mpregen` | 8.2 |
| `mpregenperlevel` | 0.7 |
| `crit` | 0 |
| `critperlevel` | 0 |
| `attackdamage` | 52 |
| `attackdamageperlevel` | 0 |
| `attackspeedperlevel` | 4 |
| `attackspeed` | 0.638 |

## データ品質上の注意

- `info` の4項目がすべて `0` である。未収録値か実値かは原典だけでは判定できない。

## アビリティ

- **パッシブ — ダーティーファイト：** 通常攻撃かスキルを3回使用するごとに追加ダメージを与え、対象がチャンピオンだった場合はシールドを獲得する。 通常攻撃時に追加で通常攻撃を行う。ただし、その際のダメージは低下する。追加の通常攻撃をキャンセルすると、代わりに移動速度が増加する。

- **Q — 報復のブーメラン：** ブーメランを投げる。ブーメランは往路と復路でダメージを与え、敵に命中するたびに射程が増加する。
- **W — 義賊の流儀：** 自動効果で味方チャンピオンを倒した敵チャンピオンを「悪党」としてマークする。自分が「悪党」をキルすると、その「悪党」にキルされていた味方が復活し、追加ゴールドを獲得する。その際、すべてのマークが除去される。 発動するとカモフラージュ状態になり、「悪党」に向かっている間は移動速度とマナ自動回復が増加する。茂みの外に出るか地形から離れると、カモフラージュ状態がすぐに解除される。
- **E — ヒーロースイング：** 地形に向けてグラップルフックを発射し、その周囲をスイングしながら最も近い敵に繰り返し射撃を行う。チャンピオンか地形に衝突すると、その時点で飛び降りる。自ら早めに飛び降りることもできる。
- **R — 当然の報い：** 敵チャンピオンをロックオンして弾丸のチャージを開始する。チャージ終了時にすべての弾丸を発射し、最初に命中したチャンピオン、ミニオン、または建造物に減少体力に応じたダメージを与える。

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

- **スナップショット：** 2026-09-15生成、キュー420、完全試合4,672件、[[reports/riot-ranked-match-analysis/run-20260915T010911Z/report|詳細レポート]]。
- **観測分類：** 判定保留（分母不足）
- **対象試合：** 55試合、全体勝率 56.4%
- **時間帯別勝率：** 〜20分 50.0%（n=8）、20〜25分 55.6%（n=9）、25〜30分 66.7%（n=15）、30〜35分 55.6%（n=9）、35分〜 50.0%（n=14）
- **最高帯：** 25〜30分（判定差 不明）
- **判定根拠：** 全5帯で各15試合未満の帯がある。
- **解釈上の限界：** [[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別勝率の見直し]] に基づく記述統計。試合時間は勝敗後に確定するため、因果的なパワースパイク、推奨ビルド、特定時点での強さを示さない。
- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]

<!-- power-spike-match:end -->

<!-- champion-build-analysis:start -->
## 実試合ビルド分析

- **スナップショット：** 2026-09-15生成、キュー420、ユニーク試合9,736件、[[reports/riot-champion-item-synergy/run-20260915T060638Z/champions/champion-166|アクシャンの詳細レポート]]。
- **根拠と方法：** [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテム相性タグ分類の実試合再評価]]。
- **読み方：** 最終所持状態の記述的な相関であり、購入順・因果効果・最適ビルドを確定しない。理論仮説は共通ステータスとチャンピオン原典の語彙から優先表示した未検証候補。

### MIDDLE（274試合）

- **実測ビルド候補：** [[wiki/entities/items/item-3036|ドミニク リガード]] + [[wiki/entities/items/item-6676|コレクター]]（該当n=53、71.7% / 非該当46.6%、差+25.1pt）；[[wiki/entities/items/item-3031|インフィニティ エッジ]] + [[wiki/entities/items/item-3036|ドミニク リガード]] + [[wiki/entities/items/item-6676|コレクター]]（該当n=38、71.1% / 非該当48.3%、差+22.7pt）
- **ステータス傾向：** 魔力（該当n=104、51.9% / 非該当51.2%、差+0.7pt）
- **理論仮説：** [[wiki/entities/items/item-3087|スタティック シヴ]] + [[wiki/entities/items/item-6672|クラーケン スレイヤー]]（未観測；共通stats: 攻撃力・攻撃速度・移動速度／チャンピオン原典にも言及: 攻撃力・移動速度）；[[wiki/entities/items/item-3748|タイタン ハイドラ]] + [[wiki/entities/items/item-6609|ケミパンク チェーンソード]]（未観測；共通stats: 攻撃力・体力／チャンピオン原典にも言及: 攻撃力・体力）

<!-- champion-build-analysis:end -->

<!-- champion-matchup-analysis:start -->
## 実測コンボ・カウンターピック

- **スナップショット：** キュー420、`tier-mode=all`、完全試合13,107件（入力13,120ファイル・19,107レコード、重複統合後13,107試合）。
- **選定方法：** 実測の同一チーム味方ペアと、正規化ロールが同じ相手を対象に、最小n=15以上を集計。候補の順位は勝率だけでなく95% Wilson区間（コンボは下限、対面は上限）と試合数を加味した。n<30はサンプル不足として扱う。
- **読み方：** [[reports/riot-champion-matchups/run-20260915T071824Z/champions/champion-166|詳細な候補表]]。実測の記述統計であり、因果的なシナジー、確定カウンター、推奨編成を意味しない。

### MIDDLE（対象n=344）

- **高勝率コンボ候補（最大3件）：**
  - [[wiki/entities/champions/zyra|ザイラ（Zyra）]] — 対象側勝率55.4%（46/83）、n=83（十分性の目安を満たす）。
  - [[wiki/entities/champions/nautilus|ノーチラス（Nautilus）]] — 対象側勝率46.3%（19/41）、n=41（十分性の目安を満たす）。
- **低勝率カウンターピック候補（最大3件）：**
  - [[wiki/entities/champions/vex|ヴェックス（Vex）]] — 対象側勝率37.5%（6/16）、サンプル不足（n=16、十分性の目安30未満）。
  - [[wiki/entities/champions/viktor|ビクター（Viktor）]] — 対象側勝率45.0%（9/20）、サンプル不足（n=20、十分性の目安30未満）。
  - [[wiki/entities/champions/ahri|アーリ（Ahri）]] — 対象側勝率48.1%（13/27）、サンプル不足（n=27、十分性の目安30未満）。

### BOTTOM（対象n=10）

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

### MIDDLE（対象305試合、全体勝率50.8%）

| 順位 | 完全ルーンセット | 選択数 | 選択率 | 選択時勝率 |
| ---: | --- | ---: | ---: | ---: |
| 1 | 主系栄華：プレスアタック／冷静沈着・レジェンド: 迅速・最期の慈悲；副系不滅：ボーンアーマー・超成長；シャードUNKNOWN(5005)・UNKNOWN(5008)・UNKNOWN(5001) | 122/305 | 40.0% | 43.4% |
| 2 | 主系栄華：プレスアタック／冷静沈着・レジェンド: 迅速・切り崩し；副系魔道：英気集中・強まる嵐；シャードUNKNOWN(5005)・UNKNOWN(5008)・UNKNOWN(5011) | 36/305 | 11.8% | 69.4% |
| 3 | 主系栄華：プレスアタック／冷静沈着・レジェンド: 迅速・切り崩し；副系不滅：ボーンアーマー・シールドバッシュ；シャードUNKNOWN(5005)・UNKNOWN(5008)・UNKNOWN(5011) | 18/305 | 5.9% | 66.7% |

- **選定ロール：** チャンピオン・ロール別の完全試合数が最も多いロールを1つ選んだ。別ロールや全候補は詳細レポートで確認できる。
- **シャード表示：** Data Dragonで表示名を解決できない場合は`UNKNOWN(<ID>)`としてIDを保持する。

- **出典：** [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-rune-selection|Riotランク戦試合データ：チャンピオン別ルーン選択]]、[[wiki/syntheses/champion-rune-selection-ranked-matches|実測チャンピオン別ルーン選択分析]]。
<!-- champion-rune-set-analysis:end -->

## 関連ページ

- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]] — `data.Akshan` のレコード。
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1]] — `ja_JP` 個別レコードのパッシブと4スキル。
- 原典：[[raw/sources/champion.json.md|champion.json.md]]
- 原典：[[raw/sources/dragontail-16.18.1.tgz|dragontail-16.18.1.tgz]]
- 画像：[Data Dragon CDN](https://ddragon.leagueoflegends.com/cdn/16.18.1/img/champion/Akshan.png)
