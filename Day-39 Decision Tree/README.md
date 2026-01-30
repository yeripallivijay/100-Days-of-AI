# Day 39 – Decision Tree Classifier

## Datasets
1. **Iris:** Multiclass classification (Setosa, Versicolor, Virginica).
2. **Diabetes:** Binary classification (Positive, Negative).

## Core Concepts
- **Root Node:** The feature that splits the data best (Highest Information Gain).
- **Gini Impurity:** Measure of chaos (0 = pure node, 0.5 = mixed).
- **Overfitting:** When the tree grows deep enough to memorize single samples.
- **Pruning:**
  - **Pre-Pruning:** `max_depth=3`, `min_samples_leaf=5`.
  - **Post-Pruning:** `ccp_alpha` (Cost Complexity Pruning).

