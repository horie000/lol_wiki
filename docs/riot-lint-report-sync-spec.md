# Riotレポート連動Lint仕様書

- 仕様バージョン：1.0
- 作成日：2026-09-16
- 対象実装：`scripts/lint.py`
- 関連実装：`scripts/riot_champion_duration_wiki_sync.py`、`scripts/riot_champion_build_wiki_sync.py`、`scripts/riot_champion_matchup_wiki_sync.py`、`scripts/riot_champion_rune_wiki_sync.py`、`scripts/riot_champion_tier_wiki_sync.py`

## 1. 目的

`lint.py` を実行した時点で最新の完了済みRiot解析レポートを選び、チャンピオンentityの生成ブロックへ反映してから、生成物の再現性とWikiの整合性を検証する。これにより、レポート更新後に同期スクリプトを個別に実行し忘れても、パワースパイク、ビルド、コンボ・カウンターピック、ルーン、観測ランク帯候補が古いまま残ることを防ぐ。

同期は機械的な候補表示であり、勝率から因果効果、最適ビルド、確定カウンターを自動的に推薦するものではない。質的な採用判断は別途行う。

## 2. 最新レポートの選択

次の各レポート系列を独立に探索する。

| entityへ反映する情報 | 探索するディレクトリ | 同期入力 | 必須条件 |
| --- | --- | --- | --- |
| 試合時間帯別の観測／実測パワースパイク | `reports/riot-ranked-match-analysis/run-*` | `champion-duration-winrate.json` | `analysis.json`、`quality.json`、`report.md`、時間帯JSON、manifestの全outputs |
| チャンピオン別ビルド | `reports/riot-champion-item-synergy/run-*` | `analysis.json` | `quality.json`、`report.md`、`champions/`、manifestの全outputs |
| 味方コンボ・同ロール対面 | `reports/riot-champion-matchups/run-*` | `analysis.json` | `quality.json`、`report.md`、`champions/`、manifestの全outputs |
| チャンピオン別完全ルーンセット | `reports/riot-ranked-match-analysis/run-*` | `analysis.json` | `results.rune_sets`、`quality.json`、`report.md`、manifestの全outputs |
| 観測ランク帯別候補 | `reports/riot-ranked-tier-analysis/run-*` | `analysis.json` | `tier_mode=observed`、`quality.json`、`report.md`、manifestの全outputs |

選択基準はファイル更新時刻やディレクトリ名ではなく、`manifest.json` の `generated_at` のUTC時刻とする。次をすべて満たさない実行は未完了として候補から除外する。

1. `manifest.json`、同期入力、`analysis.json`、`quality.json`、`report.md` が存在する。
2. manifestの `outputs` が配列であり、列挙されたファイルまたはディレクトリがすべて存在する。
3. 同期スクリプトが期待する最小スキーマを満たす。たとえば、ビルドは `results`、`status_group_results`、`build_results`、`theoretical_build_results`、対面は `candidates`、ルーンは `results.rune_sets` を要求する。
4. 時間帯分析は `champion-duration-winrate.json` の `method`、`duration`、`rows` を満たす。

同一系列で条件を満たす実行が複数ある場合は、`generated_at` が最も新しいものを1件だけ使用する。該当レポートがない場合は同期をスキップし、他のLintを継続する。

## 3. 実行モード

### 3.1 通常実行

```bash
python3 scripts/lint.py
```

通常実行は次の順序で行う。

1. 選択した各レポートに対して `--dry-run` を実行し、入力とentity差分を検証する。
2. 既存の静的生成物（ゴールド効率、アイテム分類、原典ベースのパワースパイク）を必要に応じて更新する。
3. 選択したレポートごとに対応する同期スクリプトを `--write` で実行する。
4. Data Dragonタグ、ゴールド効率、アイテム分類、原典ベースのパワースパイクを `--check` で検証する。
5. 全レポート同期を `--check` で再実行し、entityが選択レポートから再現できることを確認する。

通常のLintはrawやレポート本文を再生成せず、既存レポートを入力にWikiの生成ブロックだけを更新する。Data DragonタグはLintの自動書き込み対象にせず、欠落検出のみ行う。

### 3.2 検証だけの実行

```bash
python3 scripts/lint.py --check-only
```

`--check-only` はファイルを書き換えず、静的生成物と最新レポートから得られるentity内容の一致だけを確認する。更新を取り込む通常運用では `--check-only` を使わない。

## 4. entity同期の扱い

- 試合時間帯別のブロックは `<!-- power-spike-match:start -->` から `<!-- power-spike-match:end -->` の範囲を置換する。
- ビルド、コンボ・カウンターピック、ルーン、観測ランク帯のブロックは、それぞれの同期スクリプトが定義する専用マーカー範囲だけを置換する。
- レポート由来の `updated` は、entityに既に記録された日付より古い場合に巻き戻さない。複数系列を同じLintで同期しても、最後に古いレポートを処理したことで更新日が後退しない。
- entityの `sources` には対応する原典要約を重複なく保持し、詳細レポートは派生物としてWikilinkで案内する。
- 同期対象に分析結果の行がないチャンピオンでも既存の生成ブロックを空結果へ更新し、過去スナップショットの候補を残さない。

## 5. 失敗時の扱い

- dry-run、write、checkのいずれかが失敗した時点で終了コードを返す。
- 未完了またはスキーマ不一致のレポートは「最新」として採用しない。最新レポートがない場合はその系列だけをスキップする。
- 対応するchampion entityやアイテムentityを解決できない場合は同期スクリプトのエラーとしてLintを失敗させる。
- 解析レポートの候補をWikiの質的な推奨へ昇格させることは、この自動処理の責務に含めない。

## 6. 再利用コマンド

Lintと同じ入力選択を手動で再現したい場合は、出力された実行ディレクトリの入力を明示する。

```bash
python3 scripts/riot_champion_duration_wiki_sync.py \
  --analysis reports/riot-ranked-match-analysis/run-YYYYMMDDTHHMMSSZ/champion-duration-winrate.json \
  --dry-run

python3 scripts/riot_champion_build_wiki_sync.py \
  --analysis reports/riot-champion-item-synergy/run-YYYYMMDDTHHMMSSZ/analysis.json \
  --dry-run

python3 scripts/riot_champion_matchup_wiki_sync.py \
  --analysis reports/riot-champion-matchups/run-YYYYMMDDTHHMMSSZ/analysis.json \
  --dry-run
```

各同期スクリプトは `--dry-run`、`--write`、`--check` を備え、rawを変更しない。

## 7. 受け入れ条件

- 完了条件を満たす系列ごとに、manifestの `generated_at` が最大の実行を選択できる。
- manifestの `outputs` 欠落や期待スキーマ不一致の実行を選択しない。
- 通常の `lint.py` がレポート同期のdry-run、write、checkを順に実行できる。
- `lint.py --check-only` がファイルを変更せずに検証できる。
- 既存の生成ブロック外の本文を変更せず、複数系列の同期でentityの `updated` を巻き戻さない。
- 同期後に従来の静的Lint（リンク・効率・分類・原典ベースのパワースパイク）が成功する。
