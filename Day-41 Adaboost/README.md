# Day 41 – AdaBoost Classifier & Regressor

## Core Concept
AdaBoost (Adaptive Boosting) is a sequential ensemble method.
- **Weights:** Misclassified samples get higher weights.
- **Stumps:** Uses "Decision Stumps" (trees with depth=1) as weak learners.
- **Voting:** Final prediction is a weighted sum of all weak learners.

## Projects
1. **Travel Insurance Prediction** (Classification)
   - *Challenge:* Imbalanced dataset (fewer people buy insurance).
   - *Solution:* AdaBoost focuses heavily on the minority class errors.

2. **CarDekho Price Prediction** (Regression)
   - *Challenge:* High variance in car prices.
   - *Solution:* Sequential correction of residual errors.

## Pros & Cons [web:564]
- **Pros:** High accuracy, less prone to overfitting than complex trees.
- **Cons:** Sensitive to noisy data and outliers (it tries too hard to fit them).
