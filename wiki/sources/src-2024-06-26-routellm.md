---
title: "RouteLLM：選好データによるLLMルーティング"
type: source
status: active
source_path: raw/sources/routellm-2406.18665.md
source_url: https://arxiv.org/abs/2406.18665
source_date: 2024-06-26
ingested: 2026-09-16
created: 2026-09-16
updated: 2026-09-16
tags:
  - local-llm
  - model-routing
  - cost-efficiency
---

# RouteLLM：選好データによるLLMルーティング

## 要約

強いモデルと弱いモデルのどちらへ問い合わせを送るかを、モデル間の選好データから学習するルータ群を提案する研究である。クエリの勝率予測とコスト閾値を分け、閾値を変えて品質と強モデル呼び出し率の曲線を調整する。

## 主要な主張

- Chatbot Arena等の選好データを使い、クエリごとに強モデル・弱モデルを動的に選択する。
- ベンチマークで品質を大きく損なわず2倍超のコスト削減を報告し、強弱モデルを変更したテストでも転移性能を示した。
- ルータの評価指標として、強モデル呼び出し率、性能ギャップ回復率、所望性能に必要な強モデル呼び出し率を定義している。

## 根拠と限界

- 選好データは主にチャット・ベンチマーク由来であり、構造化されたRiot分析の正確性や出典遵守を直接測っていない。
- ルータ自体の推論コストと誤った低品質モデル選択のリスクを含めて運用する必要がある。
- 原典の強弱モデルには外部APIと公開モデルが混在するため、ローカルモデル群では選好データを作り直し、閾値を再校正する必要がある。

## 関連ページ

- [[wiki/sources/src-2023-05-09-frugalgpt|FrugalGPT：コスト削減と性能向上のLLM利用]] — 信頼度判定付きカスケード。
- [[wiki/sources/src-2024-03-18-routerbench|RouterBench：マルチLLMルーティング評価ベンチマーク]] — コスト・品質曲線の評価基盤。
- [[wiki/syntheses/local-llm-large-scale-analysis|大量データ解析向けローカルLLM運用]] — 軽量モデルを既定にする切り替え案。

## 未解決の問い

- 実測レポートの難易度（行数、候補数、矛盾数、出典不足）からルータ入力特徴をどう作るか。
- ルータの選択結果を固定スナップショットへ記録し、同じデータで再現できるようにする方法は何か。

## 出典

- 原典スナップショット：[[raw/sources/routellm-2406.18665.md|routellm-2406.18665.md]]
- 公開ページ：[RouteLLM: Learning to Route LLMs with Preference Data](https://arxiv.org/abs/2406.18665)
