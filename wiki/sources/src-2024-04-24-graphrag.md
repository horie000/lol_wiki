---
title: "GraphRAG：ローカルからグローバルへのクエリ指向要約"
type: source
status: active
source_path: raw/sources/graphrag-2404.16130.md
source_url: https://arxiv.org/abs/2404.16130
source_date: 2024-04-24
ingested: 2026-09-16
created: 2026-09-16
updated: 2026-09-16
tags:
  - local-llm
  - retrieval
  - graph-rag
---

# GraphRAG：ローカルからグローバルへのクエリ指向要約

## 要約

プライベートな文書集合に対する全体質問を扱うため、原文からエンティティ知識グラフを構築し、関連エンティティ群（コミュニティ）の要約を事前生成するGraphRAGを提案する。質問時には各コミュニティの部分回答を生成し、最後に全体要約へ統合する。

## 主要な主張

- 通常のRAGが得意な局所検索と、コーパス全体のテーマを問うクエリ指向要約を組み合わせる。
- 100万トークン規模のデータセットにおけるグローバルな意味把握質問で、通常RAGより回答の網羅性と多様性が向上したと報告している。
- エンティティとコミュニティ要約を中間表現にするため、毎回すべての文書をプロンプトへ送らない構成を設計できる。

## 根拠と限界

- 評価は原典のクラスのグローバル質問に限定され、ローカルLLM、Wikiの日本語、実測Riotデータへの直接検証ではない。
- グラフ抽出とコミュニティ要約にLLM呼び出しが必要で、初期構築・更新のトークン費用が発生する。
- 要約の誤りや古いインデックスが最終回答へ伝播するため、原文への出典リンクと更新管理が必要である。

## 関連ページ

- [[wiki/sources/src-2024-01-31-raptor|RAPTOR：木構造検索のための再帰的抽象処理]] — 階層要約・検索による別方式。
- [[wiki/sources/src-2023-07-06-lost-in-the-middle|Lost in the Middle：長文入力の位置バイアス]] — 全文投入を避ける根拠。
- [[wiki/syntheses/local-llm-large-scale-analysis|大量データ解析向けローカルLLM運用]] — 大規模データ分析の構成候補。

## 未解決の問い

- パッチ別・チャンピオン別の集計表を、グラフのノード・エッジ・属性としてどこまで自動抽出できるか。
- コミュニティ要約の更新と、元のCSV・JSON・レポートへの再現可能なリンクをどう管理するか。

## 出典

- 原典スナップショット：[[raw/sources/graphrag-2404.16130.md|graphrag-2404.16130.md]]
- 公開ページ：[From Local to Global: A Graph RAG Approach to Query-Focused Summarization](https://arxiv.org/abs/2404.16130)
