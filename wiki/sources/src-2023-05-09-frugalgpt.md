---
title: "FrugalGPT：コスト削減と性能向上のLLM利用"
type: source
status: active
source_path: raw/sources/frugalgpt-2305.05176.md
source_url: https://arxiv.org/abs/2305.05176
source_date: 2023-05-09
ingested: 2026-09-16
created: 2026-09-16
updated: 2026-09-16
tags:
  - local-llm
  - model-routing
  - cost-efficiency
---

# FrugalGPT：コスト削減と性能向上のLLM利用

## 要約

LLM利用費を下げる方法を、プロンプト適応、LLM近似、LLMカスケードの3系統に整理した研究である。カスケードでは、安価なモデルの回答を信頼度で判定し、不十分な場合だけ高性能モデルへ順次切り替える。

## 主要な主張

- 大量のクエリ・テキスト処理ではモデルごとの価格差が大きく、単一モデル固定は費用面で不利になり得る。
- プロンプト例の選択、複数クエリの連結、回答キャッシュ、小型モデルのファインチューニング、モデルカスケードを候補として示している。
- 評価したFrugalGPTの一例では、最良の単一LLMと同等の性能を最大98%低い費用で得たと報告している。

## 根拠と限界

- 原典はGPT-4等の商用APIと当時の価格を用いた研究で、ローカルLLMの電力・メモリ・保守コストは含まれない。
- カスケードは信頼度判定器と複数回の呼び出しを必要とし、誤判定時の品質低下や遅延を伴う。
- 最大98%は特定データセット・モデル組み合わせの結果であり、現在の価格や本プロジェクトのデータへ一般化しない。

## 関連ページ

- [[wiki/sources/src-2024-06-26-routellm|RouteLLM：選好データによるLLMルーティング]] — 単一呼び出し先を事前選択する学習ルータ。
- [[wiki/sources/src-2024-03-18-routerbench|RouterBench：マルチLLMルーティング評価ベンチマーク]] — ルータの比較方法。
- [[wiki/syntheses/local-llm-large-scale-analysis|大量データ解析向けローカルLLM運用]] — モデル切り替えとトークン削減の統合案。

## 未解決の問い

- 軽量ローカルモデル→高性能ローカルモデルへの切り替え基準を、勝率分析・Lint判定のどの品質指標で定義するか。
- 解析単位をまとめるクエリ連結と、個別の出典追跡をどう両立するか。

## 出典

- 原典スナップショット：[[raw/sources/frugalgpt-2305.05176.md|frugalgpt-2305.05176.md]]
- 公開ページ：[FrugalGPT: How to Use Large Language Models While Reducing Cost and Improving Performance](https://arxiv.org/abs/2305.05176)
