---
tags: transformers, nlp, deep-learning
created: 2025-01-14
updated: 2025-01-25
---

# Transformer Architecture

## Overview
Introduced in "Attention is All You Need" (Vaswani et al., 2017), transformers revolutionized NLP by enabling parallel processing of sequences.

## Key Components

### Self-Attention
- Query, Key, Value computations
- Allows each token to attend to all other tokens
- Captures long-range dependencies
- Parallelizable unlike RNNs

### Multi-Head Attention
- Multiple attention heads in parallel
- Each head learns different representations
- Concatenate and project results
- More expressive than single head

### Feed-Forward Networks
- Position-wise dense layers
- Applied to each position independently
- Non-linearity for learning complex patterns

### Positional Encoding
- Add position information to embeddings
- Enables model to understand token positions
- Sinusoidal encoding is common
- Allows handling variable length sequences

## Architecture Layers
1. Embedding layer
2. Positional encoding
3. Stacked encoder layers (in encoder)
4. Stacked decoder layers (in decoder)
5. Output projection

## Advantages
- Parallelizable training (vs RNNs)
- Captures long-range dependencies
- Pre-trainable on large corpora
- Transfer learning to downstream tasks

## Modern Variants
- **BERT** - Bidirectional encoder
- **GPT** - Decoder-only (autoregressive)
- **Vision Transformer** - Apply to images
- **T5** - Text-to-text framework

## How It Powers LLMs
- All modern language models are transformer-based
- Pre-trained on large text corpora
- Fine-tuned for specific tasks
- Foundation for [[LLM Applications]]

## Training Tips
- Use warm-up learning rate schedule
- Gradient accumulation for large batches
- Mixed precision training for efficiency
- Regular validation on hold-out set

## Related
- [[Neural Networks]]
- [[Machine Learning]]
- [[LLM Applications]]
