---
title: Riotランク戦試合データ：チャンピオン別ルーン選択
type: source
status: active
source_path: raw/sources/riot-ranked-matches
ingested: 2026-09-15
created: 2026-09-15
updated: 2026-09-15
tags:
  - league-of-legends
  - ranked-match
  - champion
  - rune
  - descriptive-statistics
---

# Riotランク戦試合データ：チャンピオン別ルーン選択

## 要約

`raw/sources/riot-ranked-matches/` のMatch-v5データをキュー420に限定し、チャンピオン・正規化ロールごとに、よく選択されるキーストーン、通常ルーン、ステータスシャードを集計した。選択率は同じチャンピオン・ロールの参加者を分母とし、選択時勝率とチャンピオン全体勝率を併記する。

採用した固定スナップショットは `reports/riot-ranked-match-analysis/run-20260915T082512Z/` である。入力15,589ファイル・22,574レコードを試合IDで統合し、15,574ユニーク試合から、キュー420の15,572件の完全試合を `tier_mode=all` で選択した。重複7,000件、競合0件、不完全試合2件、キュー不一致2件、非試合JSON 8件を品質情報へ残している。

## 解析条件

| 項目 | 条件 |
| --- | --- |
| 入力 | `raw/sources/riot-ranked-matches/`（読み取り専用） |
| キュー | `420` |
| tier mode | `all`（同一試合IDは1回だけ） |
| 完全試合 | 15,572件 |
| パッチ | 14.19〜16.18、48パッチ |
| 最小ゲーム数 | 15（チャンピオン・ロールの母数とルーン選択数） |
| ルーンの単位 | キーストーン、通常ルーン、ステータスシャードを別集計 |
| 分母 | 同じチャンピオン・正規化ロールの参加者 |

同一参加者の同一ルーンは一度だけ数えた。キーストーンと通常ルーンは通常1つの選択として扱い、シャードは3枠を別々に扱うため、シャードの選択率は種類内で合計100%にならない。正規化ロールはMatch-v5最終スコアの `teamPosition`、`individualPosition`、`lane` から解決したものである。

## 代表的な観測

以下は、複数パッチを合算したキーストーンのうち、母数100件以上で選択率が高い組み合わせの例である。全行は `champion-rune-summary.csv` と `analysis.json` の `results.champion_runes` に保存した。

| チャンピオン | ロール | キーストーン | 選択／チャンピオン | 選択率 | 選択時勝率 | 全体勝率 | 差 |
| --- | --- | --- | ---: | ---: | ---: | ---: |
| [[wiki/entities/champions/mordekaiser\|モルデカイザー]]（Mordekaiser） | TOP | 征服者 | 1,692/1,707 | 99.1% | 51.8% | 51.6% | +0.2pp |
| [[wiki/entities/champions/jinx\|ジンクス]]（Jinx） | BOTTOM | リーサルテンポ | 1,910/2,024 | 94.4% | 51.7% | 51.1% | +0.6pp |
| [[wiki/entities/champions/leona\|レオナ]]（Leona） | UTILITY | アフターショック | 1,934/2,055 | 94.1% | 54.1% | 54.0% | +0.1pp |
| [[wiki/entities/champions/nautilus\|ノーチラス]]（Nautilus） | UTILITY | アフターショック | 2,199/2,359 | 93.2% | 50.0% | 49.9% | +0.1pp |
| [[wiki/entities/champions/ashe\|アッシュ]]（Ashe） | BOTTOM | リーサルテンポ | 2,082/2,292 | 90.8% | 50.0% | 49.7% | +0.3pp |
| [[wiki/entities/champions/ahri\|アーリ]]（Ahri） | MIDDLE | 電撃 | 1,592/1,762 | 90.4% | 47.7% | 48.4% | −0.7pp |
| [[wiki/entities/champions/viego\|ヴィエゴ]]（Viego） | JUNGLE | 征服者 | 1,376/1,595 | 86.3% | 49.3% | 48.7% | +0.6pp |
| [[wiki/entities/champions/jhin\|ジン]]（Jhin） | BOTTOM | フリートフットワーク | 1,759/2,377 | 74.0% | 50.7% | 50.4% | +0.2pp |

選択率が高い組み合わせでも、選択時勝率とチャンピオン全体勝率の差は多くが1ポイント未満だった。この表は「そのチャンピオン・ロールで何が選ばれたか」を示す証拠であり、「選ぶと勝率が上がる」ことを示す比較ではない。

## データ品質と制約

- 解析は48パッチを横断するため、ルーンの採用傾向にはパッチ変更と環境変化が混ざる。現在パッチの判断にはパッチを固定した再集計が必要である。
- `tier_mode=all` は同じ試合の観測帯重複を除くが、観測ランク帯は試合時点の10人全員のランクではない。標本はランク帯の全試合を無作為抽出したものでもない。
- `min_games=15` は表示下限であり、統計的有意性の検定ではない。少数ロール・少数キーストーンは追加標本で変わり得る。
- Match-v5の最終ルーンと勝敗だけを使い、プレイヤー、対面、アイテム、試合時間、味方構成、選択前の状態を調整していない。選択時勝率との差から因果効果や最適性は推定できない。
- `perks.statPerks` のステータスシャードはData Dragonの `runesReforged.json` に表示名がないため、`UNKNOWN(5001)` などのIDで残る。これは試合データの欠損ではない。

## 関連ページ

- [[wiki/syntheses/champion-rune-selection-ranked-matches|実測チャンピオン別ルーン選択分析]] — 選択傾向をロール差と因果解釈の制約とともに統合する。
- [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-matchups|Riotランク戦試合データ：チャンピオン別コンボ・カウンターピック分析]] — 同じ収集データからの構成・対面候補。
- [[wiki/syntheses/role-gold-acquisition-rate|ロール別ゴールド獲得率：ランク戦最終スコアの集計]] — ロール混合値を読む際の資源配分の補助情報。

## 未解決の問い

- 同一パッチ・同一ロールで、上記の選択傾向が再現するか。
- パッチ、プレイヤー、対面、アイテム、試合時間を調整したとき、選択時勝率の差が残るか。
- ステータスシャードIDを、対応するパッチのデータ辞書で表示名へ解決できるか。

## 出典

- 原典：[[raw/sources/riot-ranked-matches|riot-ranked-matches]]
- ローカル表示名：`raw/sources/dragontail-16.18.1.tgz`
- 解析レポート：`reports/riot-ranked-match-analysis/run-20260915T082512Z/report.md`
- 解析条件：`reports/riot-ranked-match-analysis/run-20260915T082512Z/manifest.json`
- 品質情報：`reports/riot-ranked-match-analysis/run-20260915T082512Z/quality.json`
- 構造化結果：`reports/riot-ranked-match-analysis/run-20260915T082512Z/analysis.json`、`champion-rune-summary.csv`
