---
tags: rag, llm, ai
created: 2025-01-20
updated: 2025-01-26
---

# RAG Systems (Retrieval-Augmented Generation)

## Overview
RAG combines retrieval of relevant documents with generative language models. Instead of relying solely on a model's training data, RAG augments prompts with contextual documents.

## Architecture Components

### 1. Document Processing
- Split documents into chunks
- Create [[Vector Embeddings]] for each chunk
- Store in a [[Vector Databases|vector database]]

### 2. Retrieval
- Convert user query to embedding
- Perform similarity search
- Retrieve top-k relevant documents

### 3. Generation
- Combine retrieved documents with user query
- Feed to LLM as context
- Generate response grounded in retrieved documents

## Advantages
- Up-to-date information (not limited to training data)
- Reduced hallucinations
- Transparent source citations
- Cost-effective vs fine-tuning

## Disadvantages
- Additional latency from retrieval
- Quality depends on document quality
- Requires maintaining document store

## Implementation Tools
- **LangChain** - Python framework for LLM apps
- **LlamaIndex** - Document indexing and retrieval
- **Vespa** - Vector search platform
- **Weaviate** - Vector database

## Key Decisions
1. Chunk size and overlap strategy
2. Embedding model selection
3. Vector database choice
4. Retrieval strategy (BM25, semantic, hybrid)

## Current Project
Building an agentic RAG solution that integrates with Obsidian vaults for personal knowledge base retrieval.

## Resources
- [[Machine Learning]]
- [[Vector Embeddings]]
- [[LLM Applications]]
