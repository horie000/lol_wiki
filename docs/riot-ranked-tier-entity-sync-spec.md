# 観測ランク帯別チャンピオン候補 entity 同期仕様書

- 仕様バージョン：1.0
- 作成日：2026-09-16
- 対象ゲーム：League of Legends
- 実装：`scripts/riot_champion_tier_wiki_sync.py`
- 入力生成：`scripts/riot_ranked_tier_analyzer.py`
- 関連仕様：[Riot API ランク戦試合結果解析スクリプト仕様書](riot-ranked-match-analysis-spec.md)

## 1. 目的

観測ランク帯別分析レポートに含まれるチャンピオンのピック数上位、高勝率候補、低勝率候補を、各チャンピオンの entity ページから参照できる短い生成ブロックとして同期する。詳細な表、全候補、品質情報は `reports/` の実行成果物に残し、entity は検索と導線の入口とする。

この同期はレポートの機械的な候補を表示する工程であり、推奨、カウンターの確定、因果効果、有意差の判定を行わない。

## 2. 入力と前提

### 2.1 入力ファイル

`--analysis` には、`riot_ranked_tier_analyzer.py` が生成した次の `analysis.json` を指定する。

```text
reports/riot-ranked-tier-analysis/run-YYYYMMDDTHHMMSSZ/analysis.json
```

同じ実行ディレクトリに `report.md` が存在することを必須とする。入力は読み取り専用で扱い、`raw/` 配下へ書き込まない。

### 2.2 必須条件

- `filters.tier_mode` は `observed` であること。
- `filters.min_games` が正の整数であること。今回の分析は15。
- `results.champion_tier` と `results.champion_extremes` が存在すること。
- すべての候補 `champion_id` が `wiki/entities/champions/` の frontmatter にある `champion_key` と対応すること。
- `observed_tier` は `IRON`、`BRONZE`、`SILVER`、`GOLD`、`PLATINUM`、`EMERALD`、`DIAMOND`、`MASTER`、`GRANDMASTER`、`CHALLENGER` のいずれかであること。

entity のファイル名や英字表記から推測せず、`champion_key` でページを解決する。これにより、`Kai'Sa` のような特殊なファイル名にも依存しない。

## 3. 候補の選定

既定の `--selection-limit` は5とする。

1. `results.champion_tier` を観測帯ごとに `games` の降順、`win_rate` の降順、チャンピオン名の昇順で並べ、上位5件をピック数上位として選ぶ。
2. `results.champion_extremes` の `direction=high` を観測帯ごとに候補順位順で取り、上位5件を高勝率候補として選ぶ。
3. `direction=low` を同様に取り、下位5件を低勝率候補として選ぶ。
4. 各帯・各分類の内部では `champion_id` をキーに重複排除する。重複が入力にあっても、同じチャンピオンを同じ表へ二度掲載しない。
5. `games < filters.min_games` の行は候補表示から除外する。今回の閾値は15ゲームである。
6. 候補に一度でも登場するチャンピオンのページだけを既定の同期対象とする。以前の生成マーカーが残るページは、候補から外れた場合も更新して古いブロックを残さない。

`--champions` を指定した場合は、指定した entity のみを検証・同期する。候補の全体集合を変更するオプションではない。

## 4. entity 生成ブロック

各対象ページへ次のマーカーで囲んだブロックを一つだけ置く。

```text
<!-- champion-tier-analysis:start -->
...
<!-- champion-tier-analysis:end -->
```

ブロックには次を記録する。

- 生成日、キュー、観測帯数、帯別試合数、統合後試合数、`min-games`
- 観測ランク帯の意味と、候補が探索的な記述統計であること
- ピック数上位候補の帯内順位、試合数、ピック率、勝敗、勝率
- 高勝率・低勝率候補の帯内順位、試合数、勝敗、勝率
- 対応する source summary、synthesis、詳細 `report.md` への Wikilink

生成ブロック以外の本文、既存の関連ページ、既存の出典記述は変更しない。entity の frontmatter には対応する source summary を `sources` へ一度だけ追加し、`updated` を解析結果の生成日へ更新する。

## 5. CLI

```bash
python3 scripts/riot_champion_tier_wiki_sync.py \
  --analysis reports/riot-ranked-tier-analysis/run-20260916T083219Z/analysis.json \
  --dry-run

python3 scripts/riot_champion_tier_wiki_sync.py \
  --analysis reports/riot-ranked-tier-analysis/run-20260916T083219Z/analysis.json \
  --write

python3 scripts/riot_champion_tier_wiki_sync.py \
  --analysis reports/riot-ranked-tier-analysis/run-20260916T083219Z/analysis.json \
  --check
```

| オプション | 既定値 | 説明 |
| --- | --- | --- |
| `--analysis PATH` | 必須 | 観測ランク帯分析の `analysis.json` |
| `--entity-root PATH` | `wiki/entities/champions` | チャンピオン entity のディレクトリ |
| `--champions LIST` | 全候補ページ | champion key、英字ID、タイトル、ファイル名で対象を限定 |
| `--selection-limit N` | `5` | 各帯・各分類の掲載上限 |
| `--source-ref WIKILINK` | 観測帯分析の source summary | frontmatter に追加する出典 |
| `--dry-run` | 既定 | 差分件数を表示し、書き込まない |
| `--write` | — | 生成ブロックと frontmatter を書き込む |
| `--check` | — | 期待状態と一致しなければ終了コード1 |

新しい分析結果を同期するときは、同じ `analysis.json` に対して `--dry-run`、`--write`、`--check` の順に実行する。生成ブロックを手編集せず、内容変更は入力レポートから再同期する。

## 6. 解釈上の限界

- `observed_tier` は試合を発見したプレイヤーの収集時点の所属帯であり、参加者10人全員の試合時ランクではない。
- 同じ試合が複数の観測帯へ現れるため、帯別候補を合算して全体傾向を作らない。
- ピック数上位、高低勝率候補は未調整の記述統計であり、パッチ、期間、ロール、構成、プレイヤー、対面を調整していない。
- `min-games=15` は表示上のフィルターであって、統計的有意性、信頼区間、多重比較補正を保証しない。
- 高勝率候補を推奨、低勝率候補をチャンピオン固有の弱点やカウンターと解釈しない。検証にはパッチ・ロールをそろえた十分な標本と、必要に応じたTimelineや試合時ランク情報が必要である。

## 7. 受け入れ条件

- `--dry-run` が entity を変更せず、対象件数と候補行数を表示できる。
- `--write` が候補に登場する entity だけへブロックを追加し、source summary を重複なく frontmatter に追加できる。
- `--check` が同じ入力に対する同期後の entity で成功する。
- 同じ観測帯・分類に同一 `champion_id` が複数あっても、表中に一度だけ表示する。
- 生成ブロック外の本文を保持し、詳細レポートへのリンクを作成できる。
- `scripts/lint.py` と `git diff --check` が成功する。
