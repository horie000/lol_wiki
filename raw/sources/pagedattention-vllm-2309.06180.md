---
title: "Efficient Memory Management for Large Language Model Serving with PagedAttention"
source_type: research-paper
source_url: https://arxiv.org/abs/2309.06180
source_date: 2023-09-12
retrieved: 2026-09-16
capture_type: abstract-and-metadata
---

# Efficient Memory Management for Large Language Model Serving with PagedAttention

## Metadata

- Authors: Woosuk Kwon, Zhuohan Li, Siyuan Zhuang, Ying Sheng, Lianmin Zheng, Cody Hao Yu, Joseph E. Gonzalez, Hao Zhang, Ion Stoica
- arXiv: 2309.06180
- Implementation: https://github.com/vllm-project/vllm

## Abstract（原文）

High throughput serving of large language models (LLMs) requires batching sufficiently many requests at a time. However, existing systems struggle because the key-value cache (KV cache) memory for each request is huge and grows and shrinks dynamically. When managed inefficiently, this memory can be significantly wasted by fragmentation and redundant duplication, limiting the batch size. To address this problem, we propose PagedAttention, an attention algorithm inspired by the classical virtual memory and paging techniques in operating systems. On top of it, we build vLLM, an LLM serving system that achieves (1) near-zero waste in KV cache memory and (2) flexible sharing of KV cache within and across requests to further reduce memory usage. Our evaluations show that vLLM improves the throughput of popular LLMs by 2-4x with the same level of latency compared to the state-of-the-art systems, such as FasterTransformer and Orca. The improvement is more pronounced with longer sequences, larger models, and more complex decoding algorithms.

## Capture note

- 本ファイルは原典の書誌情報と公開要旨を保存したスナップショットであり、本文全体の代替ではない。
