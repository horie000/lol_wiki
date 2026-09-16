---
title: "RAPTOR：木構造検索のための再帰的抽象処理"
type: source
status: active
source_path: raw/sources/raptor-2401.18059.md
source_url: https://arxiv.org/abs/2401.18059
source_date: 2024-01-31
ingested: 2026-09-16
created: 2026-09-16
updated: 2026-09-16
tags:
  - local-llm
  - retrieval
  - long-context
---

# RAPTOR：木構造検索のための再帰的抽象処理

## 要約

文書チャンクを埋め込み、クラスタリングし、要約する処理を下から上へ再帰的に行い、抽象度の異なる要約木を作る検索手法である。推論時には木の複数レベルから検索し、長い文書の局所情報と全体情報を組み合わせる。

## 主要な主張

- 短い連続チャンクだけを検索する従来RAGより、長い文書の全体的な理解を支援する。
- 複数段階の推論を要するQAで、GPT-4と組み合わせたQuALITY評価の最高精度を絶対20ポイント改善したと報告している。
- 事前に要約木を作ることで、問い合わせ時に原文全体を毎回コンテキストへ詰め込む必要を減らす設計候補になる。

## 根拠と限界

- 20ポイントという結果は原典が示す特定ベンチマークとGPT-4の組み合わせであり、ローカルLLMや日本語コーパスの結果ではない。
- 埋め込み・クラスタリング・要約の前処理コストと、要約による情報損失・更新遅延がある。
- 原典要旨にはトークン削減量の直接測定値がないため、削減効果は本プロジェクトでの検証課題として扱う。

## 関連ページ

- [[wiki/sources/src-2024-04-24-graphrag|GraphRAG：ローカルからグローバルへのクエリ指向要約]] — コミュニティ要約による全体質問への別アプローチ。
- [[wiki/sources/src-2023-07-06-lost-in-the-middle|Lost in the Middle：長文入力の位置バイアス]] — 長文を直接入力する場合の限界。
- [[wiki/syntheses/local-llm-large-scale-analysis|大量データ解析向けローカルLLM運用]] — 大規模コーパスの検索・要約候補。

## 未解決の問い

- Riot試合レポートのような構造化・時系列データを、どの粒度で要約木に分割すると再現性を保てるか。
- 新しいパッチや試合データを追加した際、要約木を差分更新できるか。

## 出典

- 原典スナップショット：[[raw/sources/raptor-2401.18059.md|raptor-2401.18059.md]]
- 公開ページ：[RAPTOR: Recursive Abstractive Processing for Tree-Organized Retrieval](https://arxiv.org/abs/2401.18059)
