---
title: "RouterBench：マルチLLMルーティング評価ベンチマーク"
type: source
status: active
source_path: raw/sources/routerbench-2403.12031.md
source_url: https://arxiv.org/abs/2403.12031
source_date: 2024-03-18
ingested: 2026-09-16
created: 2026-09-16
updated: 2026-09-16
tags:
  - local-llm
  - model-routing
  - evaluation
---

# RouterBench：マルチLLMルーティング評価ベンチマーク

## 要約

複数のLLMを性能・費用の制約下で選ぶルータを比較するため、評価指標、理論枠組み、データセットを整備した研究である。8データセット、11モデル、64タスクを含む40万件超の推論結果を使い、予測ルータとカスケードルータを評価する。

## 主要な主張

- 初期データセットは405,467サンプルで、オープンモデルと商用モデルを含む。
- コスト制約下の性能を評価し、KNN・MLP等の予測ルータや、判定器を用いるカスケードを比較している。
- RAGデータセットでは、時間依存の質問をオンラインモデルへ送るなど、クエリ属性に応じた切り替えの可能性を示している。

## 根拠と限界

- 原典自身が、性能と経済的コスト中心で、遅延・スループットなどを十分に含まないことを限界としている。
- 掲載モデル・タスクは一部であり、現在のローカルモデルの能力差や本プロジェクトの日本語分析を代表しない。
- カスケードは判定器の誤り率に敏感で、誤判定が増えると性能が急速に低下し得る。

## 関連ページ

- [[wiki/sources/src-2024-06-26-routellm|RouteLLM：選好データによるLLMルーティング]] — 選好データを用いるルータ学習。
- [[wiki/sources/src-2023-05-09-frugalgpt|FrugalGPT：コスト削減と性能向上のLLM利用]] — カスケードとキャッシュの運用案。
- [[wiki/syntheses/local-llm-large-scale-analysis|大量データ解析向けローカルLLM運用]] — 切り替え評価の設計。

## 未解決の問い

- 本プロジェクト向けに、正確性、出典完全性、トークン数、遅延、メモリを一つの評価曲線へ統合できるか。
- 分析対象のパッチ・ロール・データ量が異なるとき、どの特徴でルータを学習・検証するか。

## 出典

- 原典スナップショット：[[raw/sources/routerbench-2403.12031.md|routerbench-2403.12031.md]]
- 公開ページ：[RouterBench: A Benchmark for Multi-LLM Routing System](https://arxiv.org/abs/2403.12031)
