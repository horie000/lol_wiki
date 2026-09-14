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
