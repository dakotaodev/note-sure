---
tags: ml, supervised-learning, algorithms
created: 2025-01-09
---

# Supervised Learning

## Definition
Learning from labeled data where both inputs and desired outputs are provided. The goal is to learn a mapping from inputs to outputs.

## Regression
- Predict continuous values
- Examples: house prices, temperature
- Common algorithms: Linear Regression, SVMs, Neural Networks

## Classification
- Predict discrete categories
- Examples: email spam detection, image classification
- Common algorithms: Logistic Regression, Decision Trees, Random Forests

## Key Algorithms

### Tree-Based
- **Decision Trees** - Interpretable, prone to overfitting
- **Random Forests** - Ensemble of trees, more robust
- **Gradient Boosting** - Sequential tree building
- **XGBoost** - Optimized gradient boosting

### Distance-Based
- **KNN** - K-Nearest Neighbors
- **SVM** - Support Vector Machines
- **Kernel Methods** - Non-linear classification

### Probabilistic
- **Naive Bayes** - Probability-based
- **Logistic Regression** - Linear decision boundary
- **Gaussian Processes** - Uncertainty quantification

## Model Selection
1. Define problem (regression vs classification)
2. Choose algorithm family
3. Tune hyperparameters
4. Cross-validate on test set
5. Compare metrics

## Evaluation Metrics
- **Regression**: MSE, MAE, R²
- **Classification**: Accuracy, Precision, Recall, F1
- **General**: Cross-validation, confusion matrix

## Common Pitfalls
- Overfitting on training data
- Data leakage between train/test
- Imbalanced datasets
- Not scaling features
- Wrong metric for the problem

## Related
- [[Machine Learning]]
- [[Linear Algebra Fundamentals]]
- [[Design Patterns]]
