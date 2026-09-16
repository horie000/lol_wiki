---
title: "QLoRA: Efficient Finetuning of Quantized LLMs"
source_type: research-paper
source_url: https://arxiv.org/abs/2305.14314
source_date: 2023-05-23
retrieved: 2026-09-16
capture_type: abstract-and-metadata
---

# QLoRA: Efficient Finetuning of Quantized LLMs

## Metadata

- Authors: Tim Dettmers, Artidoro Pagnoni, Ari Holtzman, Luke Zettlemoyer
- arXiv: 2305.14314（NeurIPS submission）

## Abstract（原文）

We present QLoRA, an efficient finetuning approach that reduces memory usage enough to finetune a 65B parameter model on a single 48GB GPU while preserving full 16-bit finetuning task performance. QLoRA backpropagates gradients through a frozen, 4-bit quantized pretrained language model into Low Rank Adapters (LoRA). Our best model family, which we name Guanaco, outperforms all previous openly released models on the Vicuna benchmark, reaching 99.3% of the performance level of ChatGPT while only requiring 24 hours of finetuning on a single GPU. QLoRA introduces a number of innovations to save memory without sacrificing performance: (a) 4-bit NormalFloat (NF4), a new data type that is information theoretically optimal for normally distributed weights (b) double quantization to reduce the average memory footprint by quantizing the quantization constants, and (c) paged optimizers to manage memory spikes. We use QLoRA to finetune more than 1,000 models, providing a detailed analysis of instruction following and chatbot performance across 8 instruction datasets, multiple model types (LLaMA, T5), and model scales that would be infeasible to run with regular finetuning (e.g. 33B and 65B parameter models). Our results show that QLoRA finetuning on a small high-quality dataset leads to state-of-the-art results, even when using smaller models than the previous SoTA.

## Capture note

- 本ファイルは原典の書誌情報と公開要旨を保存したスナップショットであり、本文全体の代替ではない。
