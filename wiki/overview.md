---
title: 概要
type: overview
status: active
created: 2026-09-14
updated: 2026-09-16
sources:
  - "[[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1]]"
  - "[[wiki/sources/src-2026-09-14-dragontail-16-18-1]]"
  - "[[wiki/sources/src-2017-11-26-firstbloodstats-gold-efficiency]]"
  - "[[wiki/sources/src-2026-02-28-red-ff-item-gold-efficiency]]"
  - "[[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate]]"
  - "[[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis]]"
  - "[[wiki/sources/src-2026-09-15-riot-ranked-match-champion-matchups]]"
  - "[[wiki/sources/src-2026-09-15-riot-ranked-match-champion-rune-selection]]"
  - "[[wiki/sources/src-2026-09-16-riot-ranked-match-tier-analysis]]"
  - "[[wiki/sources/src-2023-05-09-frugalgpt]]"
  - "[[wiki/sources/src-2023-05-23-qlora]]"
  - "[[wiki/sources/src-2023-07-06-lost-in-the-middle]]"
  - "[[wiki/sources/src-2023-09-12-pagedattention]]"
  - "[[wiki/sources/src-2023-10-09-llmlingua]]"
  - "[[wiki/sources/src-2023-10-10-longllmlingua]]"
  - "[[wiki/sources/src-2024-01-31-raptor]]"
  - "[[wiki/sources/src-2024-03-18-routerbench]]"
  - "[[wiki/sources/src-2024-03-19-llmlingua-2]]"
  - "[[wiki/sources/src-2024-04-24-graphrag]]"
  - "[[wiki/sources/src-2024-06-26-routellm]]"
  - "[[wiki/sources/src-2026-09-16-llama-cpp-readme]]"
tags:
  - overview
---

# 概要

この Vault は、原典を `raw/sources/` に保存し、そこから得た知識を継続的に統合する LLM 管理型 Wiki である。

## 現在の対象範囲

現在は、version `16.18.1` のチャンピオンデータセットとData Dragon配布アーカイブを収録している。基本原典には173件のレコードがあり、日本語の名前・称号・紹介文、役割タグ、リソース種別、画像参照、評価値、数値ステータスが含まれる。配布アーカイブの日本語個別レコードから、各チャンピオンのパッシブと4スキルの説明、868件のアイテム、62件のルーン、34件のサモナースペルを個別ページへ展開している。

これに加えて、2024-09-25〜2026-09-14に収集したキュー420のランク戦データを記述統計として扱っている。試合時間帯別スナップショットは4,672件、最新のアイテム・ビルド分析スナップショットは9,736件、ロール別ゴールド獲得率スナップショットは9,971件、コンボ・対面分析スナップショットは13,107件、チャンピオン別ルーン選択・完全セット分析スナップショットは20,010件の完全試合であり、各原典要約とレポートに解析時点を固定している。

また、ローカルLLMを大量データ解析へ適用するための原典群を収集している。プロンプト圧縮（LLMLingua系）、長文コーパスの階層・グラフ検索（RAPTOR、GraphRAG）、長文の位置バイアス評価、モデル切り替え（FrugalGPT、RouteLLM、RouterBench）、量子化・サービング（QLoRA、llama.cpp、PagedAttention）を、各原典の分析レポートと統合版で整理している。これらの評価値は外部ベンチマークに基づくため、日本語のRiot分析での再現値とは区別する。

蓄積したドメイン知識を別エージェントへ提供する場合は、制御層の `AGENTS.md`（編集者の共通ポリシー）、知識層の `wiki/`（変化する事実と分析）、呼び出し時の `llm-wiki-reader` 役割契約（参照専用・書き込みなし）を分離する。reader向けの短い契約と、編集者との境界は [[docs/agent-role-contracts.md|エージェント役割契約]] と統合版に記録している。

## 現在の知見

- レコードのフィールド集合と version は統一され、主要な識別子に重複はない。
- 役割タグでは `Mage` と `Fighter` の所属件数が多い。
- 複数の一律 `0` フィールドと一部の空値があり、性能比較では欠損の可能性を考慮する必要がある。
- 173件すべてに `wiki/entities/champions/` 配下の個別エンティティページがあり、指定CDNから取得・検証した128×128ピクセルのPNG画像を表示する。
- 173件すべての個別ページに、日本語のパッシブ1件とQ/W/E/Rの4スキル説明を掲載している。チャンピオンのtooltip数値、スキン、TFT等は未展開である。
- 173件すべてのチャンピオンページに、基礎ステータス・能力の蓄積成長・明示的なアイテム連動を根拠としたパワースパイク（序盤・中盤・終盤）を記録している。役割タグは判定に使わない。これは実戦の強さを断定しない再現可能な分類である。
- 収集済みランク戦では、試合時間を5帯に分けたチャンピオン勝率の観測を原典ベース分類と別層で記録している。序盤寄り11、中盤寄り22、終盤寄り14、明瞭な傾向なし75、分母不足51であり、試合時間は勝敗後に確定するため因果的なパワースパイクや推奨ビルドを示さない。
- ロール別の最終ゴールド/分は、BOTTOM 423.4、JUNGLE 405.1、MIDDLE 384.1、TOP 384.0、UTILITY 291.2だった。チーム内の最終ゴールド比率もBOTTOM 22.4%、UTILITY 15.5%などの差を示すため、時間帯別勝率はロール構成を固定しない限り能力上のパワースパイクへ直結させない。
- アイテム868件、ルーン62件、サモナースペル34件を、それぞれ `wiki/entities/items/`、`wiki/entities/runes/`、`wiki/entities/spells/` に原典のID単位で個別ページ化している。名称空欄のアイテム4件やモード別スペルも、推測で統合せず保持している。
- アイテム868件には、レッド＆ふぉー記事の単価表を適用したゴールド効率、理論価格、算定対象外の効果を個別に記録している。行動妨害耐性、割合物理防御貫通、割合・固定魔法防御貫通、ライフスティール、割合移動速度などを算定し、固定通常攻撃時追加ダメージだけはFirstBloodStats記事の補助単価を使う。記事に単価のないステータスや条件付き効果は対象外である。
- アイテム868件には、効果・ステータスから相性のよいチャンピオン系統を推定した `champion-synergy-*` タグを付与している。複数タグを許し、`marksman`、`fighter`、`assassin`、`mage`、`tank`、`support`、`jungler`、`utility` の検索で絞り込める。これはData Dragon原典からの候補分類であり、個別チャンピオンの最適ビルドや勝率を断定しない。
- 収集済みの実試合データから、`scripts/riot_champion_item_synergy.py` でチャンピオン・ロール・個別アイテムに加え、Data Dragon `stats` の同一ステータス群（クリティカル率など）と完成アイテム中核の所持時／非所持時勝率差を集計できる。173件のチャンピオンentityには最大2ロール・各2候補の短い生成ブロックを置き、全候補と詳細表は同じスナップショットの `reports/` へリンクする。これは原典タグや最適ビルドを自動確定するものではなく、パッチ差、試合時間、勝敗後の完成、生存者バイアスを含む探索レポートである。
- 収集済みの実試合データから、味方コンボと同ロール対面候補も集計している。173件すべてのチャンピオンentityに、実測勝率・分子分母・n<30のサンプル不足表示・詳細レポートへのリンクを追加した。Wilson区間で小標本の極端値を抑えた選定だが、パッチ、構成、プレイヤー、実際のレーン対面を調整した因果推定ではない。
- 収集済みの実試合データから、チャンピオン・ロール別の個別ルーンと完全セットの選択率も集計している。20,010件の完全試合では、各チャンピオンの観測数最多ロールについて、主系・副系・全選択枠・3シャードが一致する完全セット上位3件を各entityへ表示する。選択数と選択時勝率は実測の記述統計であり、最適ルーンや因果効果を示さない。
- 収集済みランク戦を観測ランク帯別にも比較している。IRON〜CHALLENGER各1,000試合では、上位観測帯ほど試合時間中央値が短く、最終GPM・CS/分・視界スコアが高い傾向と、全帯でBOTTOMの最終GPMが最高・UTILITYが最低という構造を確認した。ただし `observed_tier` は試合発見者の収集時点の帯であり、10人全員の試合時ランクや因果的な技能差ではない。
- 大量データ解析向けローカルLLMの原典を、トークン削減、階層検索、モデル切り替え、量子化・サービングの4層で比較している。圧縮率や費用削減率は各論文の条件に依存し、導入時は入力トークン、出典リンク率、正確性、遅延、ピークメモリ、フォールバック率を同一スナップショットで測定する。
- モデル切り替えについては、軽量モデルを既定にし、難易度・信頼度・出典不足時だけ高性能モデルへエスカレーションする案を統合版に記録している。ルータの誤判定、追加遅延、ローカルモデルへの再校正が未検証のため、現時点では運用提案であり実測結論ではない。
- チャンピオン173件、アイテム868件、ルーン62件、サモナースペル34件の全個別ページに、Data Dragon由来であることを示す共通タグ `data-dragon` を付与している。
- サモナーズリフトで購入できるアイテムの高低10例を比較し、消耗品・視界・ジャングル用品・時間限定効果の0%を「弱い」と結論付けられないことを整理した。
- 個別ページの説明ではHTML風の表示タグを除去しているが、サモナースペル等のツールチップ内プレースホルダーは追加仕様なしに数値化していない。

## ナビゲーション

- [[wiki/index|Wiki 索引]]
- [[wiki/index#エンティティ|個別エンティティ一覧]]
- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1|チャンピオンデータセット v16.18.1]]
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1|Data Dragon 配布アーカイブ v16.18.1]]
- [[wiki/sources/src-2017-11-26-firstbloodstats-gold-efficiency|アイテムのゴールド効率について改めてまとめた]]
- [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate|Riotランク戦試合データ：試合時間帯別チャンピオン勝率]]
- [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]
- [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-matchups|Riotランク戦試合データ：チャンピオン別コンボ・カウンターピック分析]]
- [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-rune-selection|Riotランク戦試合データ：チャンピオン別ルーン選択]]
- [[wiki/syntheses/local-llm-large-scale-analysis|大量データ解析向けローカルLLM運用：トークン削減・検索・モデル切り替え]]
- [[wiki/sources/src-2023-10-09-llmlingua|LLMLingua：LLM推論を高速化するプロンプト圧縮]]
- [[wiki/sources/src-2023-10-10-longllmlingua|LongLLMLingua：長文コンテキスト向けプロンプト圧縮]]
- [[wiki/sources/src-2024-03-19-llmlingua-2|LLMLingua-2：タスク非依存プロンプト圧縮]]
- [[wiki/sources/src-2024-01-31-raptor|RAPTOR：木構造検索のための再帰的抽象処理]]
- [[wiki/sources/src-2024-04-24-graphrag|GraphRAG：ローカルからグローバルへのクエリ指向要約]]
- [[wiki/sources/src-2023-07-06-lost-in-the-middle|Lost in the Middle：長文入力の位置バイアス]]
- [[wiki/sources/src-2023-05-09-frugalgpt|FrugalGPT：コスト削減と性能向上のLLM利用]]
- [[wiki/sources/src-2024-06-26-routellm|RouteLLM：選好データによるLLMルーティング]]
- [[wiki/sources/src-2024-03-18-routerbench|RouterBench：マルチLLMルーティング評価ベンチマーク]]
- [[wiki/sources/src-2023-09-12-pagedattention|PagedAttention：LLMサービングの効率的メモリ管理]]
- [[wiki/sources/src-2023-05-23-qlora|QLoRA：量子化LLMの効率的ファインチューニング]]
- [[wiki/sources/src-2026-09-16-llama-cpp-readme|llama.cpp README：ローカルLLM推論ランタイム]]
- [[wiki/syntheses/local-llm-large-scale-analysis#llm-wikiのドメイン知識を別エージェントへ渡す設計（内部設計案）|別エージェントへのドメイン知識提供と役割境界]]
- [[docs/agent-role-contracts.md|エージェント役割契約]]
- [[wiki/sources/src-2026-02-28-red-ff-item-gold-efficiency|アイテムの金銭効率ランキング：ファイター編【LoL】]]
- [[wiki/concepts/champion-dataset-schema|チャンピオンデータのスキーマ]]
- [[wiki/concepts/game-data-catalog|ゲームデータ個別ページのカタログ]]
- [[wiki/syntheses/gold-efficiency-stat-values|アイテム金銭効率の基準単価]]
- [[wiki/syntheses/gold-efficiency-high-low-examples|アイテム金銭効率の高低例と総合評価]]
- [[wiki/syntheses/item-champion-synergy-tags-v16-18-1|アイテムのチャンピオン相性タグ分類 v16.18.1]]
- [[wiki/syntheses/champion-roster-profile-v16-18-1|チャンピオンデータ概況 v16.18.1]]
- [[wiki/syntheses/champion-power-spikes-v16-18-1|チャンピオンのパワースパイク分類 v16.18.1]]
- [[wiki/syntheses/champion-power-spikes-match-duration|チャンピオンのパワースパイク：試合時間帯別勝率の見直し]]
- [[wiki/syntheses/role-gold-acquisition-rate|ロール別ゴールド獲得率：ランク戦最終スコアの集計]]
- [[wiki/syntheses/champion-combo-counter-ranked-matches|実測チャンピオン・コンボ／カウンターピック分析]]
- [[wiki/syntheses/champion-rune-selection-ranked-matches|実測チャンピオン別ルーン選択分析]]
- [[wiki/syntheses/ranked-tier-characteristics|ランク帯別の試合特徴と全帯共通傾向]]
- [[wiki/log|Wiki ログ]]

## 未解決の問い

- データの正式な配布元とフィールド定義は何か。
- tooltipの数値プレースホルダーを検証できる仕様資料は何か。
- `item-modifiers.json`、他ロケール、TFT等の周辺データをどの粒度で取り込むか。
- パッチ・ロール・観測ランク帯を固定した時間帯別勝率の傾向が、全体集計でも再現するか。
- ロール別GPMの差をパッチ・チャンピオン・試合時間で調整した場合、チャンピオンの時間帯別勝率の観測はどの程度変わるか。
- コンボ・対面候補をパッチ・ロール・試合時間・プレイヤー構成で調整した場合、どの候補が再現するか。
- チャンピオン別ルーン選択の定番が、同一パッチ・同一ロールの層別集計でも再現するか。

## 出典

- [[wiki/sources/src-2026-09-14-champion-dataset-v16-18-1|チャンピオンデータセット v16.18.1]]
- [[wiki/sources/src-2026-09-14-dragontail-16-18-1|Data Dragon 配布アーカイブ v16.18.1]]
- [[wiki/sources/src-2017-11-26-firstbloodstats-gold-efficiency|アイテムのゴールド効率について改めてまとめた]]
- [[wiki/sources/src-2026-09-15-riot-ranked-match-duration-winrate|Riotランク戦試合データ：試合時間帯別チャンピオン勝率]]
- [[wiki/sources/src-2026-09-15-riot-ranked-match-item-build-analysis|Riotランク戦試合データ：チャンピオン別アイテム・ビルド分析]]
- [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-matchups|Riotランク戦試合データ：チャンピオン別コンボ・カウンターピック分析]]
- [[wiki/sources/src-2026-09-15-riot-ranked-match-champion-rune-selection|Riotランク戦試合データ：チャンピオン別ルーン選択]]
