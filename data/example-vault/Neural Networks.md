---
tags: neural-networks, deep-learning, ml
created: 2025-01-11
updated: 2025-01-24
---

# Neural Networks

## Fundamentals
A neural network is a computational model inspired by biological neural networks. It consists of interconnected nodes (neurons) that process information.

## Architecture
- **Input Layer** - Receives data
- **Hidden Layers** - Process information (can be many layers)
- **Output Layer** - Produces prediction
- **Weights & Biases** - Learnable parameters

## Activation Functions
- **ReLU** - Rectified Linear Unit (most common)
- **Sigmoid** - Outputs between 0 and 1
- **Tanh** - Outputs between -1 and 1
- **Softmax** - Multiclass classification

## Training Process
1. Forward pass - compute predictions
2. Calculate loss - measure error
3. Backward pass - compute gradients
4. Update weights - gradient descent
5. Repeat until convergence

## Loss Functions
- **MSE** - Mean Squared Error (regression)
- **Cross Entropy** - Classification
- **KL Divergence** - Distribution matching

## Optimization Algorithms
- **SGD** - Stochastic Gradient Descent
- **Adam** - Adaptive learning rates
- **RMSprop** - Root Mean Square Propagation
- **Momentum** - Accelerate convergence

## Common Architectures
- **Fully Connected** - Simple feedforward networks
- **CNN** - Convolutional (vision tasks)
- **RNN/LSTM** - Recurrent (sequences)
- **[[Transformer Architecture]]** - Modern NLP

## Regularization Techniques
- Dropout - Randomly disable neurons
- L1/L2 regularization - Penalize large weights
- Early stopping - Stop before overfitting
- Batch normalization - Normalize layer inputs

## Related
- [[Machine Learning]]
- [[Linear Algebra Fundamentals]]
- [[LLM Applications]]
