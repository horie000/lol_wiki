---
title: "RAPTOR: Recursive Abstractive Processing for Tree-Organized Retrieval"
source_type: research-paper
source_url: https://arxiv.org/abs/2401.18059
source_date: 2024-01-31
retrieved: 2026-09-16
capture_type: abstract-and-metadata
---

# RAPTOR: Recursive Abstractive Processing for Tree-Organized Retrieval

## Metadata

- Authors: Parth Sarthi, Salman Abdullah, Aditi Tuli, Shubh Khanna, Anna Goldie, Christopher D. Manning
- arXiv: 2401.18059

## Abstract（原文）

Retrieval-augmented language models can better adapt to changes in world state and incorporate long-tail knowledge. However, most existing methods retrieve only short contiguous chunks from a retrieval corpus, limiting holistic understanding of the overall document context. We introduce the novel approach of recursively embedding, clustering, and summarizing chunks of text, constructing a tree with differing levels of summarization from the bottom up. At inference time, our RAPTOR model retrieves from this tree, integrating information across lengthy documents at different levels of abstraction. Controlled experiments show that retrieval with recursive summaries offers significant improvements over traditional retrieval-augmented LMs on several tasks. On question-answering tasks that involve complex, multi-step reasoning, we show state-of-the-art results; for example, by coupling RAPTOR retrieval with the use of GPT-4, we can improve the best performance on the QuALITY benchmark by 20% in absolute accuracy.

## Capture note

- 本ファイルは原典の書誌情報と公開要旨を保存したスナップショットであり、本文全体の代替ではない。
