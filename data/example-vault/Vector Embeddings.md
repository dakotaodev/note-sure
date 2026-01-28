---
tags: ml, embeddings, vectors
created: 2025-01-12
updated: 2025-01-24
---

# Vector Embeddings

## Definition
Vector embeddings are dense numerical representations of text, images, or other data. They capture semantic meaning in a high-dimensional space.

## Properties
- **Dimensionality**: Typically 384-1536 dimensions
- **Semantic Similarity**: Similar items have similar vectors
- **Distance Metrics**: Cosine similarity is most common
- **Composability**: Can be added/manipulated mathematically

## Common Models
- **Sentence Transformers**: BERT-based embeddings
- **OpenAI Embeddings**: High-quality proprietary embeddings
- **Cohere Embeddings**: Specialized for retrieval
- **Local Models**: ONNX-based self-hosted options

## Applications
- [[RAG Systems]] - Finding relevant documents
- Semantic search
- Clustering similar documents
- Anomaly detection

## Best Practices
1. Choose embedding model based on use case
2. Normalize vectors for consistency
3. Store in vector database for fast retrieval
4. Monitor embedding quality over time

## Related Notes
- [[Machine Learning]]
- [[Neural Networks]]
- [[Vector Databases]]
