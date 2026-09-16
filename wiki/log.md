---
title: Wiki Log
type: log
---

# Wiki Log

This file is append-only. Newest entries are appended at the end.

## [2026-09-14] maintenance | Initial wiki scaffold

- Inputs: Karpathy's LLM Wiki pattern and the local Obsidian vault.
- Changes: Created the raw-source layer, generated-wiki layer, project schema, and repository-scoped Codex skill.
- Unresolved: No domain or source collection has been added yet.

## [2026-09-14] ingest | チャンピオンデータセット v16.18.1

- 入力：`raw/sources/champion.json.md`
- 変更：[[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1|原典要約]]、[[wiki/concepts/champion-dataset-schema|データスキーマ]]、[[wiki/syntheses/champion-roster-profile-v16-18-1|全体概況]]、[[wiki/overview|概要]]、[[wiki/index|索引]]
- 未解決：正式な配布元とフィールド定義、一律 `0` の値の意味、個別チャンピオンページを展開する粒度、参照画像の不足。

## [2026-09-14] maintenance | 個別チャンピオンページと画像を追加

- 入力：`raw/sources/champion.json.md`、Data Dragon CDNのversion `16.18.1` チャンピオン画像。
- 変更：`wiki/entities/` に173件の個別ページを作成し、[[wiki/index#エンティティ|索引]]へ登録した。`raw/assets/champions/` に173件のPNG画像を保存し、各ページへ埋め込んだ。[[wiki/overview|概要]]、[[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1|原典要約]]、[[wiki/syntheses/champion-roster-profile-v16-18-1|全体概況]]を更新した。
- 未解決：正式な配布元とフィールド定義、一律 `0` の値の意味。

## [2026-09-14] ingest | Data Dragon 配布アーカイブ v16.18.1

- 入力：`raw/sources/dragontail-16.18.1.tgz`
- 変更：[[wiki/sources/src-2026-09-14-dragontail-16-18-1|原典要約]]を作成し、[[wiki/concepts/champion-dataset-schema|データスキーマ]]、[[wiki/syntheses/champion-roster-profile-v16-18-1|全体概況]]、[[wiki/overview|概要]]、[[wiki/index|索引]]を更新した。173件の個別チャンピオンページへ、日本語のパッシブ1件とQ/W/E/Rの4スキル説明を統合した。
- 未解決：正式な配布元URLと公開日時、tooltipの数値プレースホルダーの仕様、アイテム・ルーン・TFT等の非チャンピオンデータを展開する粒度。

## [2026-09-14] ingest | アイテム・ルーン・サモナースペル個別ページ

- 入力：`raw/sources/dragontail-16.18.1.tgz` の `data/ja_JP/item.json`、`runesReforged.json`、`summoner.json`
- 変更：[[wiki/concepts/game-data-catalog|ゲームデータ個別ページのカタログ]]を作成し、アイテム868件、ルーン62件、サモナースペル34件を `wiki/entities/items/`、`wiki/entities/runes/`、`wiki/entities/spells/` に分担して作成した。[[wiki/sources/src-2026-09-14-dragontail-16-18-1|原典要約]]、[[wiki/overview|概要]]、[[wiki/index|索引]]を更新した。
- 未解決：`item-modifiers.json`、他ロケール、TFT等の周辺データを展開する粒度、ツールチップ内プレースホルダーの仕様。

## [2026-09-15] ingest | アイテムのゴールド効率について改めてまとめた

- 入力：`raw/sources/firstbloodstats-gold-efficiency.html`、`raw/sources/dragontail-16.18.1.tgz`
- 変更：[[wiki/sources/src-2017-11-26-firstbloodstats-gold-efficiency|原典要約]]、`scripts/gold_efficiency.py`、`scripts/lint.py`、868件のアイテム個別ページ、[[wiki/index|索引]]
- 未解決：記事にない現行ステータス単価（クリティカルダメージ、割合物理防御貫通、行動妨害耐性等）は対象外。スキルヘイストは記事のクールダウン短縮単価で暫定換算する。

## [2026-09-15] ingest | アイテムの金銭効率ランキング：ファイター編【LoL】

- 入力：`raw/sources/red-ff-lol-item-ft-ce.html`、`raw/sources/dragontail-16.18.1.tgz`
- 変更：[[wiki/sources/src-2026-02-28-red-ff-item-gold-efficiency|原典要約]]、`scripts/gold_efficiency.py`、868件のアイテム個別ページ、[[wiki/overview|概要]]、[[wiki/index|索引]]。行動妨害耐性10.33、割合物理防御貫通41.67、割合・固定魔法防御貫通46.15/46.67、ライフスティール53.57、割合移動速度62.5 gold/stat等を現行単価として反映した。
- 未解決：パッチ26.4の記事とData Dragon v16.18.1の差分、記事に単価がないオムニヴァンプ・アルティメットヘイスト・クリティカルダメージの扱い、FirstBloodStatsとの単価差を比較にどう用いるか。

## [2026-09-15] query | アイテム金銭効率の基準単価

- 入力：[[wiki/sources/src-2026-02-28-red-ff-item-gold-efficiency|レッド＆ふぉー記事]]、[[wiki/sources/src-2017-11-26-firstbloodstats-gold-efficiency|FirstBloodStats記事]]
- 変更：[[wiki/syntheses/gold-efficiency-stat-values|アイテム金銭効率の基準単価]]、[[wiki/index|索引]]、[[wiki/overview|概要]]、両原典要約の関連リンク
- 未解決：クリティカルダメージ、オムニヴァンプ、アルティメットヘイスト等の基準単価と、データ版の差分。

## [2026-09-15] maintenance | チャンピオン個別ページのディレクトリ整理

- 入力：`wiki/entities/` のチャンピオン個別ページ173件
- 変更：173件を `wiki/entities/champions/` へ移動し、[[wiki/index|索引]]の全チャンピオンリンク、[[wiki/concepts/game-data-catalog|ゲームデータ個別ページのカタログ]]、[[wiki/overview|概要]]を更新した。
- 未解決：Vault外から旧パスを参照しているブックマークやリンクは、このリポジトリ内では検出できない。

## [2026-09-15] lint | Wiki構造と金銭効率の検証

- 入力：`wiki/` 配下のMarkdown 1,148件、`scripts/lint.py`
- 変更：必須フロントマター、内部リンク、索引収録、孤立ページ、重複識別子を検証。構造上の修正は不要だった。
- 未解決：外部のObsidian Vaultやブックマークからの旧チャンピオンページパス参照は、このリポジトリ内では検証できない。

## [2026-09-15] query | アイテム金銭効率の高低例と総合評価

- 入力：`raw/sources/dragontail-16.18.1.tgz`、[[wiki/sources/src-2026-02-28-red-ff-item-gold-efficiency|レッド＆ふぉー記事]]、`scripts/gold_efficiency.py --ranking`
- 変更：[[wiki/syntheses/gold-efficiency-high-low-examples|アイテム金銭効率の高低例と総合評価]]、[[wiki/syntheses/gold-efficiency-stat-values|基準単価]]、[[wiki/index|索引]]、[[wiki/overview|概要]]。サモナーズリフトで購入可能な248レコードを同名同効果で241件に正規化し、上位・下位10例、効果、総合評価の推論を追加した。
- 未解決：時間限定効果・視界・クエスト・経験値の共通単価、Data Dragonの販売フラグとライブ環境の照合、チャンピオンや対戦相手を含む実戦価値の評価。

## [2026-09-15] query | チャンピオンのパワースパイク分類

- 入力：`raw/sources/champion.json.md`、`raw/sources/dragontail-16.18.1.tgz`、ユーザー指定の分類基準
- 変更：173件の `wiki/entities/champions/` 個別ページにパワースパイク（序盤・中盤・終盤）を追加し、[[wiki/syntheses/champion-power-spikes-v16-18-1|チャンピオンのパワースパイク分類 v16.18.1]]、[[wiki/index|索引]]、[[wiki/overview|概要]]を更新した。`scripts/power_spikes.py` を追加し、`scripts/lint.py` から検証する。
- 未解決：全チャンピオンを横断比較できるスキル基礎ダメージ・係数・アイテム完成時刻、役割別のゴールド・経験値獲得速度、試合時間別の実戦データ。

## [2026-09-15] query | パワースパイク分類基準の改訂

- 入力：ユーザーによる `Marksman` タグを終盤シグナルから外す指示、`raw/sources/champion.json.md`、`raw/sources/dragontail-16.18.1.tgz`
- 変更：`scripts/power_spikes.py` から役割タグの判定を削除し、173件の `wiki/entities/champions/` 個別ページを再生成した。[[wiki/syntheses/champion-power-spikes-v16-18-1|チャンピオンのパワースパイク分類 v16.18.1]]、[[wiki/overview|概要]]、関連する原典・概念ページも改訂後の基準に同期した。
- 未解決：全チャンピオンを横断比較できるスキル基礎ダメージ・係数・アイテム完成時刻、役割別のゴールド・経験値獲得速度、試合時間別の実戦データ。

## [2026-09-15] query | パワースパイク区分ごとのチャンピオン例

- 入力：改訂後の `scripts/power_spikes.py` による分類結果、`wiki/syntheses/champion-power-spikes-v16-18-1.md`
- 変更：同合成ページに、序盤・中盤・終盤から各10体のピックアップ表と選定根拠を追記した。中盤は暫定区分であり、勝率や実戦上の最適な時間帯を示さないことを明記した。
- 未解決：実戦データによる各ピックアップの時間帯別強さの検証、スキル基礎ダメージ・係数・アイテム完成時刻の横断比較。

## [2026-09-15] lint | パワースパイク表のリンク修正

- 入力：ユーザーによるパワースパイク表のリンク切れ報告、`wiki/syntheses/champion-power-spikes-v16-18-1.md`
- 変更：Markdown表内のWikilink表示名区切りをエスケープし、30件のチャンピオンリンクが列区切りに分割されないよう修正した。
- 未解決：なし。

## [2026-09-15] lint | パワースパイク統合結果表のリンク修正

- 入力：ユーザーによる統合結果表のリンク切れ報告、`wiki/syntheses/champion-power-spikes-v16-18-1.md`
- 変更：統合結果表の4行に残っていた未エスケープのWikilink表示名区切りを修正し、表の列構造とリンク先を再検証した。
- 未解決：なし。

## [2026-09-15] query | アイテムのチャンピオン相性タグ分類

- 入力：`raw/sources/dragontail-16.18.1.tgz` の `data/ja_JP/item.json`、チャンピオン役割語彙、ユーザー指定の「相性による分類」
- 変更：`scripts/item_synergy.py` を追加し、アイテム868件のフロントマターへ `champion-synergy-marksman`、`fighter`、`assassin`、`mage`、`tank`、`support`、`jungler`、`utility` の候補タグを同期した。`scripts/lint.py` からタグ検証を実行し、[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|分類合成ページ]]、[[wiki/concepts/game-data-catalog|カタログ]]、[[wiki/overview|概要]]、[[wiki/index|索引]]を更新した。
- 未解決：原典には個別チャンピオンの購入率・勝率・ビルド順序がないため、タグは役割・戦闘特性の候補であり、最適ビルドや個別チャンピオンとの相性を実証するものではない。

## [2026-09-15] query | アイテム相性タグ別の代表例

- 入力：[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテムのチャンピオン相性タグ分類 v16.18.1]]、`data/ja_JP/item.json` の分類タグと効果・ステータス
- 変更：`marksman`、`fighter`、`assassin`、`mage`、`tank`、`support`、`jungler`、`utility` の各タグについて、タグのシグナルが明確なアイテムを5件ずつ選び、個別ページへのリンクと代表効果を合成ページへ追記した。
- 未解決：代表例は原典シグナルに基づく選定であり、パッチごとの最適ビルド、購入率、勝率、個別チャンピオンへの適合度を示すものではない。

## [2026-09-15] maintenance | Data Dragon由来ページの共通タグ付与

- 入力：`wiki/entities/champions/`、`wiki/entities/items/`、`wiki/entities/runes/`、`wiki/entities/spells/` の個別ページと、[[wiki/sources/src-2026-09-14-dragontail-16-18-1|Data Dragon 配布アーカイブ v16.18.1]]
- 変更：チャンピオン173件、アイテム868件、ルーン62件、サモナースペル34件の計1,137ページへ `data-dragon` タグを付与した。`scripts/data_dragon_tags.py` を追加し、`scripts/lint.py` からタグとData Dragon出典リンクを検証するようにした。[[wiki/concepts/game-data-catalog|カタログ]]と[[wiki/overview|概要]]も更新した。
- 未解決：Data Dragon以外の将来の補助原典を同じページへ追加する場合、共通タグをどの粒度で分けるか。

## [2026-09-15] lint | ゲームデータカタログ表のリンク修正

- 入力：ユーザーによる `wiki/concepts/game-data-catalog.md` の表リンク切れ報告
- 変更：チャンピオン、アイテム、ルーン、サモナースペルの4行について、Wikilinkの表示名区切りを `\|` としてエスケープした。全表の列数を確認し、4つのリンク先ファイルの存在も検証した。
- 未解決：なし。

## [2026-09-15] lint | Wiki全体の表内Wikilink修正

- 入力：`wiki/` 配下のMarkdown表を横断確認
- 変更：表セル内のWikilink表示名区切りを `\|` に統一し、カタログ以外の合成表（パワースパイク2行、金銭効率のステータス単価21行、金銭効率の高効率・低効率例20行）も修正した。全表の列構造とリンク先を再検証した。
- 未解決：なし。

## [2026-09-15] maintenance | Riot APIランク戦データ収集スクリプトと仕様書

- 入力：Riot Games公式League of Legends API仕様、ユーザー指定の「ランク帯ごとに直近1,000試合」要件
- 変更：`scripts/riot_ranked_match_collector.py` と `docs/riot-ranked-match-collector-spec.md` を追加した。League-v4でランク帯所属者を取得し、Match-v5の試合ID・詳細を収集、重複除去と `gameStartTimestamp` 順で帯ごとに1,000件をJSONLへ保存する。ルート別レート制限、429の`Retry-After`、5xx再試行、キャッシュ、Manifest、途中再実行、キュー・地域・対象帯のCLI指定を実装した。
- 未解決：Riot APIキー未設定のため実データ収集は未実行。収集時点のランク帯を観測値として扱うため、試合実施時点のランクを厳密には復元しない。

## [2026-09-15] maintenance | Riot API収集先をraw配下へ固定

- 入力：ユーザーによる収集データ保存先の指定
- 変更：収集スクリプトの既定出力を `raw/sources/riot-ranked-matches/` とし、`--output` に指定できるパスもリポジトリ内の `raw/` 配下に限定した。仕様書へ保存先制約を追記した。
- 未解決：なし。

## [2026-09-15] maintenance | Riot API収集の進捗バーと所要時間表示

- 入力：ユーザーによる収集進捗と完了時間の標準出力表示要件
- 変更：`scripts/riot_ranked_match_collector.py` に全体・ランク帯別処理のシーケンスバーを追加し、PUUID解決、試合ID候補取得、試合詳細取得の進捗を標準出力へ即時表示するようにした。全ランク帯の収集完了時に日本語の所要時間を表示し、仕様書へ出力形式を追記した。
- 未解決：なし。

## [2026-09-15] maintenance | ランク戦試合結果解析の仕様確定

- 入力：ユーザー確認済みの「取得した試合結果を解析する」要件と、チャンピオン指定の組み合わせ・対面クエリ要件。
- 変更：`docs/riot-ranked-match-analysis-spec.md` を作成し、ローカル入力・`raw/` 読み取り専用・共通正規化・集計項目・品質情報・レポート形式・受け入れ条件を定義した。通常集計と専用クエリの最小ゲーム数は `15` とした。
- 未解決：Timeline APIを用いた時系列解析、試合時点の厳密なランク復元、勝率から因果関係や絶対的な相性を断定すること。

## [2026-09-15] maintenance | ランク戦解析リソースをLLM Wikiスキルへ登録

- 入力：確定した `docs/riot-ranked-match-analysis-spec.md` と解析スクリプトの再利用要件。
- 変更：`.agents/skills/llm-wiki/SKILL.md` に Match analysis のルート、仕様書、共通モジュール、集計CLI、チャンピオン指定CLI、`--dry-run`、`raw/` 読み取り専用、個人識別情報を出力しない運用を追記した。
- 未解決：実データを用いた解析結果の検証は、API収集済みデータの品質確認後に行う。

## [2026-09-15] maintenance | Riotランク戦解析スクリプトを追加

- 入力：`docs/riot-ranked-match-analysis-spec.md`、`raw/sources/riot-ranked-matches/` の収集形式、ローカルData Dragonアーカイブ。
- 変更：`scripts/riot_match_analysis.py`（共通ローダー・正規化）、`scripts/riot_ranked_match_analyzer.py`（チャンピオン・アイテム・ルーン・スペル・性能・時間・任意の構成分析）、`scripts/riot_champion_query.py`（チャンピオン指定の味方組み合わせ・相手別低勝率）を追加した。既定の最小ゲーム数は `15`、専用クエリは味方上位20件・相手下位20件とし、出力先を `raw/` 外へ限定した。
- 未解決：実データに対する集計レポートは未生成。`scripts/riot_match_analysis.py` の共有ロジックを利用し、APIキーなしで `--help`、`--dry-run`、構文チェックを実行できる設計とした。

## [2026-09-15] lint | 直近のランク戦解析変更とWiki全体の検証

- 入力：直近のGit変更（解析仕様書、再利用リソース案内、解析スクリプト3本）、`wiki/` 配下のMarkdown 1,148件、`scripts/lint.py`。
- 変更：`wiki/log.md` に直近3コミットの作業記録を追記した。必須フロントマター、出典リンク、Wikilink、索引収録、孤立ページ、重複識別子を再検証し、構造上の修正は不要だった。
- 未解決：6件の警告Calloutは原典の制約・解釈上の注意を明示した既存記録であり、矛盾とは判定していない。実データを用いたランク戦解析レポートは未生成。

## [2026-09-15] query | ランク戦試合結果の解析レポート生成

- 入力：`raw/sources/riot-ranked-matches/` の実行時スナップショット、`raw/sources/dragontail-16.18.1.tgz`、`--queue-id 420`、`--tier-mode observed`、`--min-games 15`。
- 変更：`scripts/riot_ranked_match_analyzer.py --include-matchups --format markdown,csv,json` を実行し、`reports/riot-ranked-match-analysis/run-20260915T003112Z/report.md` と品質・マニフェスト・集計CSV/JSONを生成した。入力4,236レコードから重複除去後3,236試合を集計し、味方・対面ペアも出力した。
- 未解決：取得処理中のスナップショットのため、後続データは今回のレポートに含まれない。重複レコード1,000件、観測帯UNKNOWN 2,236試合があり、収集時点の観測帯を試合時ランクと解釈しない。Timelineがないため購入時刻・15分時点の差分は未解析。

## [2026-09-15] maintenance | ランク戦解析レポートの表示仕様改訂

- 入力：ユーザーによるレポート表示の修正要件、`docs/riot-ranked-match-analysis-spec.md`、前回レポートの確認結果。
- 変更：人間向けMarkdownからアイテム上位表を削除し、アイテム集計はCSV/JSONへ保持した。ルーンの `UNKNOWN(<ID>)` が `perks.statPerks` のステータスシャードとData Dragon表示名辞書の範囲差によるものだと説明し、ルーン・スペルを全パッチのID単位で合算した。試合時間の中央値・P10・P90の読み方、全パッチ行、具体的な解釈上の注意を追加した。味方シナジーと同ロール対面を別表に分け、味方ペアは順不同の重複を集計段階から排除した。
- 未解決：取得継続中のスナップショットで、今回の再生成は3,964試合。入力にはキャッシュとの重複1,000件がある。対面表の逆方向（例：Aを対象にBを見る、Bを対象にAを見る）は対象側が異なるため別結果として残している。

## [2026-09-15] maintenance | チャンピオン上位の重複表示修正

- 入力：ユーザーによる `Yone` の複数表示報告、`scripts/riot_ranked_match_analyzer.py`、前回の解析レポート。
- 変更：チャンピオン上位のMarkdown表を、全パッチの `overall`・`role=ALL` 行をチャンピオンID単位で合算して表示するよう修正した。パッチ別・ロール別の詳細行は `champion-summary.csv` と `analysis.json` に保持する。
- 未解決：取得処理中のスナップショットのため、今回の再生成はユニーク試合4,100件。後続取得分は別の実行で反映する必要がある。

## [2026-09-15] query | 実試合データからチャンピオン・アイテム相性を再評価

- 入力：`raw/sources/riot-ranked-matches/`、`raw/sources/dragontail-16.18.1.tgz`、queue `420`、`tier-mode all`、`min-games 15`。
- 変更：`scripts/riot_champion_item_synergy.py` を追加し、通常スロット `item0`〜`item5` の参加者単位の所持を、同じチャンピオン・正規化ロールの非所持時と比較する集計を実装した。`--patch`、`--include-utility`、チャンピオン・ロール絞り込み、CSV/JSON/Markdown、`--dry-run` を提供し、個人情報補助キャッシュのパスをmanifestから除外する安全策も加えた。Markdownのプラス・マイナス差と頻出表は、所持・非所持の双方が30ゲーム以上のペアに限定した。`.agents/skills/llm-wiki/SKILL.md` の再利用資源へ登録し、仕様書をv0.5へ更新した。[[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテムのチャンピオン相性タグ分類]]、[[wiki/concepts/game-data-catalog|ゲームデータ個別ページのカタログ]]、[[wiki/overview|概要]]、索引へ実測値の位置付けを追記した。全体レポートは `reports/riot-champion-item-synergy/run-20260915T013050Z/`、`16.18`限定確認は `reports/riot-champion-item-synergy-patch-16-18/run-20260915T013049Z/` に出力した。
- 結果：全体スナップショットは入力7,961レコード、重複除去後5,961試合、完全試合5,961件、utility除外後の最小15ゲーム以上ペア3,516件。現在のData Dragonで解決できない過去アイテムIDの所持観測は297件。`16.18`限定は179試合、最小15ゲーム以上のペア57件だった。
- 未解決：収集キャッシュが解析中も増加していたため、レポートは取得途中のスナップショットである。全パッチ合算はアイテムIDの再利用・定義差を含み、最終所持による生存者バイアス、試合時間、購入時刻、対面、構成を調整していない。所持時／非所持時差から既存タグを自動変更せず、パッチ・ロール・Timeline等を揃えた追加検証を残した。

## [2026-09-15] query | 試合時間と勝率によるパワースパイクの見直し

- 入力：`raw/sources/riot-ranked-matches/` のスナップショット、`raw/sources/dragontail-16.18.1.tgz`、キュー420、`tier-mode=all`。
- 変更：4,672件の完全試合を5時間帯に分け、チャンピオンごとの勝率を集計した。序盤寄り11、中盤寄り22、終盤寄り14、明瞭な傾向なし75、分母不足51として、[[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate|原典要約]]、[[wiki/syntheses/champion-power-spikes-match-duration|統合分析]]、173件の個別チャンピオンページへ観測ブロックを追加した。解析成果物は `reports/riot-ranked-match-analysis/run-20260915T010911Z/` に保存した。
- 未解決：48パッチ、複数ロール・観測帯の混合集計であり、時間帯別勝率は因果的なパワースパイクを示さない。パッチ・ロール固定、Timelineによるゴールド・経験値・購入時刻の分析が必要である。

## [2026-09-15] query | ステータス群とチャンピオン別ビルドの実試合分析

- 入力：`raw/sources/riot-ranked-matches/` の解析時点スナップショット、`raw/sources/dragontail-16.18.1.tgz`、queue `420`、`tier-mode all`、`min-games 15`、ビルド中核 `2,3`。
- 変更：`scripts/riot_champion_item_synergy.py` を再利用可能なCLIとして拡張し、Data Dragon `item.json` の `stats` に基づくステータス群（`FlatCritChanceMod` を含む）、完成アイテムの順不同2個・3個中核、実測候補と統計不足の理論仮説を集計した。`--status-groups` と `--build-sizes` を追加し、`docs/riot-ranked-match-analysis-spec.md` をv0.6へ更新、`.agents/skills/llm-wiki/SKILL.md` の再利用資源説明も更新した。全体レポートに加えて `champions/champion-<champion_id>.md` を生成する。
- 結果：`reports/riot-champion-item-synergy/run-20260915T021003Z/` に、ユニーク完全試合7,589件、個別アイテム4,117行、ステータス群1,731行、完成アイテム中核4,653行、理論仮説候補23,696行を出力した。クリティカル率群の例は Jinx BOTTOM 1,107試合で該当時52.0%・非該当30.0%、Ashe BOTTOM 1,293試合で51.4%・33.1%、Yone MIDDLE 833試合で50.7%・36.4%だった。Wikiの統合分析、概要、ゲームデータカタログ、索引へ方法と限界を反映した。
- 未解決：ステータス群はData Dragonの静的`stats`だけで、合計値、発動効果、スキル相互作用を含まない。ビルドは最終所持状態の順不同組み合わせで、購入順・完成時刻・因果効果を示さない。理論仮説は共通ステータスによる候補生成に限られ、最適ビルドを確定しない。収集キャッシュは取得継続中のため、今回のレポートもスナップショットである。

## [2026-09-15] maintenance | ステータス群・チャンピオン別ビルド分析の最新スナップショット

- 入力：同じ `raw/sources/riot-ranked-matches/` と `raw/sources/dragontail-16.18.1.tgz`。収集中キャッシュの増分を反映した再実行。
- 変更：開始アイテム・素材を人間向けの個別アイテム候補から除外し、完成アイテムの順不同2個・3個中核とData Dragon `stats` 群をチャンピオン別Markdownへ出力する最終版を生成した。個人識別情報は出力せず、既存のWiki統合分析を最新レポートへ同期した。
- 結果：`reports/riot-champion-item-synergy/run-20260915T051714Z/` にユニーク完全試合7,994件、個別アイテム4,262行、ステータス群1,757行、完成アイテム中核4,897行、理論仮説候補24,039行、チャンピオン別173ファイルを出力した。クリティカル率群は Jinx BOTTOM 1,169試合で52.6%対30.3%、Ashe BOTTOM 1,347試合で50.9%対32.9%、Yone MIDDLE 871試合で50.9%対36.5%だった。
- 未解決：解析中も収集キャッシュが増え得るため、レポートは実行時点のスナップショットである。ステータス群は静的`stats`の有無、理論仮説は共有ステータスだけを根拠とし、ゲーム内の強さ・最適ビルド・因果効果を確定しない。

## [2026-09-15] maintenance | Lintでのレポート知見選別運用

- 入力：ユーザーによる、Lint時にレポート内の優れた内容を分析へ反映する運用要件、`AGENTS.md`、`.agents/skills/llm-wiki/SKILL.md`。
- 変更：Lintの対象に `reports/` の確認を加え、原典追跡、再現可能性、方法・条件・母数・品質・制約、非重複性、再利用価値を満たす知見だけを原則 `wiki/syntheses/` へ統合する運用を定義した。派生レポートを原典扱いせず、極端値や肯定的結果だけを採用しないこと、重要な反証・差がない結果・矛盾・限界も保持すること、採否と理由をLintログへ残すことを明記した。レポート生成・entity同期スクリプトの機械的な順位や生成ブロックは、それだけでは選別済み知見とみなさない。
- 未解決：既存レポートの知見を個別に再選別する作業は、次回のLint対象とする。

## [2026-09-15] maintenance | チャンピオンentityへのビルド分析同期

- 入力：`raw/sources/riot-ranked-matches/` の解析時点スナップショット、`raw/sources/dragontail-16.18.1.tgz`、ユーザー指定の「entityへの短い生成ブロック＋reportsの詳細」。
- 変更：`scripts/riot_champion_item_synergy.py` のステータス群・ビルド中核をData Dragonで `maps["11"]` が真のアイテムへ限定した。`scripts/riot_champion_build_wiki_sync.py` を追加し、選択した `analysis.json` から173件のチャンピオンentityへ、最大2ロール・実測ビルド2件・ステータス群2件・理論仮説2件の生成ブロックを同期した。各ブロックは同一実行の詳細レポートへリンクする。[[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|専用原典要約]]を作成し、仕様書をv0.7、LLM Wikiスキル、統合分析、概要、カタログ、索引を更新した。
- 結果：`reports/riot-champion-item-synergy/run-20260915T060638Z/` にユニーク完全試合9,736件、個別アイテム4,908行、ステータス群1,908行、完成アイテム中核5,988行、理論仮説25,426行、チャンピオン別173ファイルを生成した。entity同期の `--check` は差分0件、詳細レポート欠落0件で、ビルド・理論候補のマップ11対象外アイテムIDは0件だった。
- 未解決：複数パッチ、最終所持状態、生存者バイアス、試合時間、対面、構成、購入順・購入時刻を調整していない。理論仮説は共通statsと原典語彙による表示優先度であり、ゲーム内の強さや最適ビルドを確定しない。収集継続後のデータを反映するには、新しい実行結果を明示的に選んで再同期する必要がある。

## [2026-09-15] query | ロール別ゴールド獲得シェア

- 入力：`raw/sources/riot-ranked-matches/**/matches.jsonl` の完成済み4本、キュー420、`tier_mode=all`。IRON、BRONZE、SILVER、GOLDを各1,000レコード含む。
- 変更：共通正規化を再利用する `scripts/riot_role_gold_share.py` を追加し、チーム内 `goldEarned` シェアを全体、勝敗、試合時間帯、観測ランク帯別に集計した。主成果物を `reports/riot-role-gold-share/run-20260915T061525Z/`、キャッシュ込み感度確認を `reports/riot-role-gold-share/run-20260915T061335Z/` に保存し、[[wiki/sources/src-2026-09-15-riot-ranked-match-role-gold-share|原典要約]]、[[wiki/syntheses/role-gold-share-ranked-matches|統合レポート]]、[[wiki/index|索引]]を更新した。
- 結果：4,000入力レコードから重複1件とロール構成不正8件を除き、3,991試合・7,982チームを分析した。平均シェアはボット22.69%、ジャングル21.49%、ミッド20.17%、トップ20.12%、サポート15.53%。20分未満から35分以上ではボット+1.47ポイント、サポート-1.33ポイントだった。キャッシュ込み9,938試合でも順位は同じで、主分析との差は最大0.31ポイントだった。
- 未解決：最終スコアの `goldEarned` は現在ゴールドではなく累積獲得額である。固定時点のシェア、獲得経路、購入時刻はTimelineデータが必要。勝敗・時間帯・観測帯の差は未調整の記述統計で、資源配分の因果効果を示さない。

## [2026-09-15] query | ロール別ゴールド獲得率の集計とパワースパイク分析への反映

- 入力：`raw/sources/riot-ranked-matches/` の読み取り専用スナップショット、queue `420`、`tier-mode all`、`min-games 15`。入力9,980ファイル・13,971レコードを試合IDで統合し、9,971件の完全試合を集計した。
- 変更：`scripts/riot_ranked_match_analyzer.py` に `role_gold` 集計と `role-gold.csv` 出力を追加し、仕様書をv0.8へ更新した。平均GPM、中央値・P10・P90、加重GPM、チーム内最終ゴールド比率、分母・勝率をロール別に記録し、解析レポートを `reports/riot-ranked-match-analysis/run-20260915T061543Z/` に保存した。[[wiki/syntheses/role-gold-acquisition-rate|ロール別ゴールド獲得率の統合分析]]、既存の[[wiki/syntheses/champion-power-spikes-match-duration|試合時間帯別パワースパイク分析]]、概要、索引、既存ランク戦出典要約へ結果と解釈上の注意を反映した。
- 結果：平均GPMはBOTTOM 423.4、JUNGLE 405.1、MIDDLE 384.1、TOP 384.0、UTILITY 291.2。チーム内最終ゴールド比率はBOTTOM 22.4%、JUNGLE 21.5%、MIDDLE 20.4%、TOP 20.3%、UTILITY 15.5%だった。
- 未解決：最終ゴールドは勝敗後の状態であり、15分時点の収入、購入時刻、実際のレーン収入、因果的なロール優劣を示さない。時間帯別パワースパイクの再分析では、パッチ・ロール・チャンピオンを固定し、可能ならTimelineを用いる必要がある。

## [2026-09-15] maintenance | ロール別ゴールド分析の重複統合

- 入力：同時進行で作成された[[wiki/syntheses/role-gold-acquisition-rate|ロール別ゴールド獲得率]]と[[wiki/syntheses/role-gold-share-ranked-matches|ロール別ゴールド獲得シェア]]の2ページ、および完成済み標本・キャッシュ込み標本の解析成果物。
- 変更：`role-gold-acquisition-rate.md` を正本とし、完成済み3,991試合の分布、勝敗別、試合時間帯別、観測ランク帯別、キャッシュ込み9,938試合との感度比較を統合した。`role-gold-share-ranked-matches.md` は履歴リンクを保つ `superseded` の案内ページへ変更し、原典要約と索引のリンクを正本へ揃えた。
- 未解決：固定時点のゴールドシェアにはTimelineデータが必要。パッチ、チャンピオン、試合時間、参加者の実際のランクを調整した因果比較は未実施。

## [2026-09-15] lint | Wiki・レポート整合性確認

- 入力：`wiki/`、`reports/` の22実行manifest、最新のチャンピオン・アイテム分析、ロール別ゴールド分析、`scripts/lint.py`、`scripts/item_synergy.py`。
- 変更：Wiki 1,154コンテンツページの索引掲載を確認し、正規化したWikilink 2,045ファイルを検査した。欠落リンク、重複索引項目、manifestの未生成出力は検出されなかった。`scripts/lint.py`、アイテム分類check、チャンピオンentity同期check、`git diff --check` はすべて成功した。
- レポート確認：`run-20260915T060638Z` のアイテム・ビルド分析、および `run-20260915T061543Z` のロール別ゴールド分析は、対応する原典要約・統合ページ・索引・過去ログへ反映済みと確認した。機械的なランキング、極端な勝率差、最終所持状態、最終ゴールドだけから新しい因果的推奨は昇格しなかった。
- 未解決：Timelineがないため、購入時刻、固定時点のゴールド、ビルド完成時刻、途中経過の因果比較は未実施。複数パッチ、チャンピオン、対面、構成、プレイヤーを調整した推定も未実施。

## [2026-09-15] lint | チャンピオンentityのアイテムWikilinkと分析成果物の再検証

- 入力：`wiki/`、`reports/` の22実行manifest、既存の `reports/riot-champion-item-synergy/run-20260915T060638Z/analysis.json`、`scripts/lint.py`、`scripts/item_synergy.py`、`scripts/riot_champion_build_wiki_sync.py`。
- 変更：Lint記録を追記し、Wiki 1,154コンテンツページの索引掲載、内部Wikilink 11,606件、frontmatterと出典追跡、22 manifestの出力存在を確認した。173件のチャンピオンentityにある1,843件のアイテムWikilinkは既存868件のアイテムentityと表示名・IDを照合し、欠落を検出しなかった。entity同期check、通常Lint、アイテム分類check、`git diff --check` は成功し、entity・レポート自体は変更していない。新しい試合レポートも生成していない。
- レポート確認：最新のチャンピオン・アイテム分析とロール別ゴールド分析の主要結果は、対応する原典要約・統合分析・索引へ反映済みと確認した。機械的なランキング、極端な勝率差、最終所持状態、最終ゴールドだけから新しい因果的推奨は昇格しなかった。
- 未解決：Timelineがないため、購入時刻、固定時点のゴールド、ビルド完成時刻、途中経過の因果比較は未実施。複数パッチ、チャンピオン、対面、構成、プレイヤーを調整した推定も未実施。

## [2026-09-15] query | 実測コンボ・カウンターピックのentity反映

- 入力：`raw/sources/riot-ranked-matches/`、キュー420、`tier-mode=all`、完全試合13,107件、入力13,120ファイル・19,107レコード。
- 変更：既存の共通ローダーと`riot_champion_query.py`の正規化を再利用する `scripts/riot_champion_matchup_wiki_sync.py` を追加し、味方コンボ9,532候補、同ロール対面2,264候補を集計した。95% Wilson区間でサンプル数を加味し、n≥30を十分性の目安、n=15–29をサンプル不足として、173件すべてのチャンピオンentityへ各ロールの候補を同期した。[[wiki/sources/src-2026-09-15-riot-ranked-match-champion-matchups|原典要約]]、[[wiki/syntheses/champion-combo-counter-ranked-matches|統合分析]]、索引、概要も更新した。
- 結果：entity掲載の選定394行のうち、n≥30は262行、n<30は132行。カイ＝サ BOTTOMはレオナ（91/154、59.1%）をコンボ候補、ルシアン（16/46、34.8%）を同ロール対面候補として掲載した。詳細は `reports/riot-champion-matchups/run-20260915T071824Z/` に保存した。
- 未解決：正規化ロールは最終スコアからの推定で、実際のレーン対面を保証しない。パッチ、プレイヤー、試合時間、味方構成を調整した再現性・因果比較、多重比較への対応は未実施。n<30の候補はentityに残したが、探索的な参考値として扱う。

## [2026-09-15] query | 実測チャンピオン別ルーン選択の分析

- 入力：`raw/sources/riot-ranked-matches/`、`raw/sources/dragontail-16.18.1.tgz`、キュー420、`tier_mode=all`、`min-games=15`。固定スナップショットは `reports/riot-ranked-match-analysis/run-20260915T082512Z/`。
- 変更：共通Match-v5ローダーを再利用して `champion_id × role × rune_kind × rune_id` の選択率、選択時勝率、チャンピオン全体勝率を追加した。パッチ別の分母重複を除くレポート集約、`champion-rune-summary.csv`、仕様書v0.9、原典要約、統合分析、概要、索引を更新した。
- 結果：15,572件の完全試合（48パッチ）で、TOPモルデカイザーの征服者は1,692/1,707（99.1%）、BOTTOMジンクスのリーサルテンポは1,910/2,024（94.4%）、UTILITYレオナのアフターショックは1,934/2,055（94.1%）だった。ロールを固定すると定番が明瞭だが、選択時勝率と全体勝率の差は代表例で−0.7〜+0.6ポイントだった。
- 未解決：48パッチ横断、最終スコア由来のロール、観測ランク帯混合、選択前状態・対面・構成・プレイヤー未調整であり、ルーンの因果効果や推奨は導かない。パッチ・ロール固定とTimelineを用いた再検証、ステータスシャード表示名の補完が必要である。

## [2026-09-15] maintenance | コンボ・カウンターピックのentity掲載件数拡張

- 入力：既存の `reports/riot-champion-matchups/run-20260915T071824Z/analysis.json` と対応する `quality.json`、173件のチャンピオンentity。
- 変更：`scripts/riot_champion_matchup_wiki_sync.py` に既存analysisからentityだけを更新する `--analysis` モードと `--selection-limit` を追加した。各チャンピオンの最大2ロールについて、高勝率コンボを最大3件、対象側の低勝率カウンターピックを最大3件、実測勝敗数・分母・サンプル不足表示付きで記載した。rawの再集計や新規レポート生成は行っていない。
- 結果：候補全体11,796行から、entity表示は1,014行（コンボ561、カウンター453）となった。n≥30は699行、n<30は315行で、n<30の候補は探索的な参考値として残した。仕様書をv1.0へ更新し、原典要約・統合分析の説明も同期した。
- 未解決：Wilson区間を用いた候補の安定化は未調整の記述統計であり、パッチ、プレイヤー、試合時間、構成、実際のレーン対面、多重比較を調整した因果比較ではない。

## [2026-09-15] query | チャンピオンページへのルーンセット上位3件反映

- 入力：`raw/sources/riot-ranked-matches/`、`raw/sources/dragontail-16.18.1.tgz`、キュー420、`tier_mode=all`、`min-games=15`。固定スナップショットは `reports/riot-ranked-match-analysis/run-20260915T103154Z/`。
- 変更：Match-v5 `perks` の主系・キーストーン・主系3枠・副系2枠・3シャードを完全一致セットとして `riot_ranked_match_analyzer.py` に追加し、`champion-rune-set-summary.csv` と `results.rune_sets` へ保存した。`riot_champion_rune_wiki_sync.py` の `--dry-run` → `--write` → `--check` を実行し、173件のチャンピオンentityへ、観測数最多ロールの選択数上位3セット、選択率、選択時勝率を同期した。ソース要約、統合分析、仕様書v1.1、概要、スキル説明を更新した。
- 結果：入力20,034ファイル・30,013レコードを試合IDで統合し、20,013ユニーク試合からキュー420の完全試合20,010件を分析した。完全セット行は137,667件（ロール別62,675件）、172チャンピオンに実測セット行があり、1チャンピオンは分母不足のためページ上で掲載保留とした。例としてエイトロックスTOPの上位3セットは607/1,635（選択時勝率50.1%）、94/1,635（57.4%）、68/1,635（44.1%）である。
- 未解決：47パッチを横断し、ロールは最終スコアから正規化している。シャード表示名はData Dragonに辞書がなく`UNKNOWN(<ID>)`を残す。選択時勝率は未調整の記述統計で、因果効果、最適セット、推奨を示さない。ページには観測数最多ロールだけを表示し、別ロールと全候補はレポートで確認する。

## [2026-09-16] ingest | 大量データ解析向けローカルLLM運用の原典群

- 入力：ユーザー指定の「ローカルLLMの運用・利用」、追加指定の「大量データ解析・トークン利用量削減・モデル切り替え」。arXivの研究論文11件と、ggml-org/llama.cpp公式READMEの取得時点スナップショットを `raw/sources/` に保存した。
- 変更：プロンプト圧縮（LLMLingua、LongLLMLingua、LLMLingua-2）、階層・グラフ検索（RAPTOR、GraphRAG）、長文位置バイアス（Lost in the Middle）、推論サービング（PagedAttention/vLLM、llama.cpp）、量子化適応（QLoRA）、モデル切り替え（FrugalGPT、RouteLLM、RouterBench）の各原典分析レポートを `wiki/sources/` に作成した。[[wiki/syntheses/local-llm-large-scale-analysis|大量データ解析向けローカルLLM運用：トークン削減・検索・モデル切り替え]] に統合し、概要と索引を更新した。
- 結果：各原典の要旨・メタデータを保持し、トークン削減率・コスト削減率・速度・メモリの数値を、外部ベンチマークの結果として本プロジェクトの実測値と区別した。統合版には、構造化前処理→検索／階層要約→品質ゲート付き圧縮→軽量モデル既定・高性能モデルへのエスカレーションという運用仮説と、トークン数・出典リンク率・正確性・遅延・ピークメモリ・フォールバック率の計測項目を記録した。
- 未解決：圧縮器の日本語・表・JSONでの忠実性、要約インデックスの差分更新、ローカルモデルのルータ校正、Apple SiliconとGPUサーバの費用・電力・スループット比較は未検証である。原典の最大値をそのまま運用保証や推奨へ昇格させない。

## [2026-09-16] maintenance | 非編集エージェントへのWiki知識提供契約

- 入力：ユーザー指定の「llm-wikiのドメイン知識を別エージェントが参照する観点」、「AGENTS.mdの利用」、「編集者ではないことの明示」。既存の `AGENTS.md`、`.agents/skills/llm-wiki/SKILL.md`、ローカルLLM運用統合版を確認した。
- 変更：`docs/agent-role-contracts.md` に `llm-wiki-reader` の最小役割契約、読み取り範囲、`write_scope: []`、禁止操作、出力形式、editorとの差分、呼び出しフローを追加した。ルート `AGENTS.md` にeditor／readerの役割境界を追記し、ローカルLLM統合版、概要、索引への導線を更新した。
- 結果：readerには「`llm-wiki-editor`ではない」という否定形のidentity、read-only権限、空の書き込み範囲をsystem/developerメッセージで渡し、`wiki/index.md`から必要ページだけを参照させる設計を記録した。更新候補は編集提案として返し、実編集は明示的なeditorタスクに限定する。
- 未解決：実際の別エージェント実行で、契約の遵守率、コンテキスト削減量、回答の出典リンク率・数値一致率を測定していない。reader契約をVault内の別 `AGENTS.md` へ置く場合の階層探索挙動も、呼び出し環境ごとに確認が必要である。

## [2026-09-16] maintenance | Riot Match-v5 Timeline取得スクリプトを追加

- 入力：既存の`raw/sources/riot-ranked-matches/**/matches.jsonl`、Riot Match-v5 Timeline API仕様、既存の`riot_ranked_match_collector.py`のHTTPクライアント。
- 変更：`scripts/riot_match_timeline_collector.py`を追加し、試合IDの重複排除、キュー・パッチ・UTC日付・件数フィルター、地域ルート解決、Timelineキャッシュ、429/5xx再試行、個人識別情報の除去、`timelines.jsonl`・`errors.jsonl`・`manifest.json`の出力を実装した。仕様を`docs/riot-match-timeline-collector-spec.md`へ記録し、収集仕様とLLM Wikiスキルから参照できるようにした。
- 結果：`--help`、Python構文チェック、GOLD 1,000件を入力にした`--limit 10 --dry-run`、個人識別情報除去テストは成功した。実取得コマンドも実行したが、環境に`RIOT_API_KEY`がないためAPI接続前に終了し、Timelineレポートはまだ生成していない。
- 未解決：実APIキーを環境変数へ設定した後、少数件で実取得し、404件数、Timelineフレーム完全性、取得時間、後続の固定時点ゴールド・購入イベント分析への利用可能性を確認する必要がある。

## [2026-09-16] maintenance | reader契約の実行境界を補強

- 入力：`llm-wiki-reader` を別エージェントへ渡す際の役割混同防止と、`write_scope: []` の実効性に関する設計確認。
- 変更：`AGENTS.md` にプロンプト契約とOS・ツール権限の違い、Vault外起動・read-only公開・書き込みツール無効化の方針を追記した。`docs/agent-role-contracts.md` に実行時の強制境界と短縮呼び出しテンプレートを追加し、統合版にも二重化の注意を反映した。
- 結果：readerのidentity、読み取り範囲、空の書き込み範囲、禁止操作を短い固定契約で渡し、質問固有の参照候補だけを後置する運用を明文化した。
- 未解決：実際の実行基盤でread-onlyマウント、ツール許可リスト、終了後の変更検査を設定した際の遵守率とコンテキスト削減量は未測定である。

## [2026-09-16] query | 実施内容と評価の内部分析を統合版へ追記

- 入力：これまでに収集・分析したローカルLLM原典群と、別エージェント向け `llm-wiki-reader` 役割契約の実装結果。
- 変更：[[wiki/syntheses/local-llm-large-scale-analysis|大量データ解析向けローカルLLM運用：トークン削減・検索・モデル切り替え]] に、実施事実、知識鮮度・コンテキスト効率・安全性・追跡可能性の評価、未検証事項を「内部分析」として追記した。
- 結果：外部原典の実証結果、本プロジェクトの構造検査、運用上の推論を分離し、現段階を「境界と評価計画を整えた段階」と明記した。
- 未解決：reader遵守率、入力トークン削減量、出典リンク率・数値一致率、圧縮・ルーティング・量子化の日本語データでの再現値は未測定である。

## [2026-09-16] query | 取得済みランク戦の観測ランク帯別分析

- 入力：`raw/sources/riot-ranked-matches/jp1/ranked-solo-5x5/**/matches.jsonl`、キュー420、IRON〜CHALLENGERの10観測帯、各1,000試合。既存の共通Match-v5ローダーで試合IDを統合した。
- 変更：`scripts/riot_ranked_tier_analyzer.py` を追加し、観測帯別の試合時間、最終GPM・DPM・CS/分・視界・KDA、ロール別ゴールド比率、チャンピオン、キーストーン、順不同サモナースペル構成、高低勝率の探索候補、全帯共通性を再利用可能なCSV/JSON/Markdown出力として実装した。`docs/riot-ranked-match-analysis-spec.md`をv1.2へ更新し、入力要約と統合分析を `wiki/sources/src-2026-09-16-riot-ranked-match-tier-analysis.md`、`wiki/syntheses/ranked-tier-characteristics.md` に追加し、索引を更新した。
- 結果：10,000観測スコープ、9,761ユニーク試合、完全試合9,761件、不完全・競合本体0件を確認した。観測帯をまたぐ重複試合は229件、重複レコードは239件だった。すべての帯でBOTTOMの最終GPMが最高、UTILITYが最低で、共通上位キーストーン4種とサモナースペル構成5種を確認した。生成先は `reports/riot-ranked-tier-analysis/run-20260916T083219Z/`。
- 未解決：`observed_tier` は試合時点の10人全員のランクではなく、帯別標本の取得期間・パッチも一致しない。GPM等は最終スコア由来で、因果効果、固定時点の資源差、ランク母集団の推定を示さない。TimelineはAPIキー未設定のため未取得で、10分・15分・20分時点の比較は未実施である。
