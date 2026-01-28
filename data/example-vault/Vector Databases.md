---
tags: databases, vectors, tools
created: 2025-01-18
---

# Vector Databases

## Overview
Vector databases are specialized data stores optimized for storing and searching high-dimensional vector data. Essential for [[RAG Systems]].

## Popular Options

### Weaviate
- Open source vector database
- GraphQL API
- Multiple embedding models supported
- Good community support

### Pinecone
- Managed vector database service
- Serverless infrastructure
- Built-in filtering and metadata
- Easy integration with LangChain

### Milvus
- Open source distributed vector database
- Scalable to billions of vectors
- Flexible indexing algorithms
- SQL-like query interface

### Qdrant
- Modern vector database
- Written in Rust
- Strong performance metrics
- Self-hosted or cloud options

## Key Features to Evaluate
- Scalability - Handle billions of vectors?
- Latency - Query response time
- Filtering - Support metadata filtering
- Integration - Works with your tech stack
- Cost - Managed vs self-hosted

## Search Algorithms
- HNSW (Hierarchical Navigable Small World)
- IVF (Inverted File Index)
- LSH (Locality-Sensitive Hashing)
- Flat search (for small datasets)

## Best Practices
1. Choose appropriate index type for scale
2. Batch insert operations
3. Implement retry logic for resilience
4. Monitor storage and query performance
5. Regular backups for important data

## Related
- [[Vector Embeddings]]
- [[RAG Systems]]
- [[Machine Learning]]
