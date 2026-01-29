# Day 38 – K-Nearest Neighbors (KNN)

## Core Concept
KNN is a **non-parametric, lazy learning** algorithm.
- **Classification:** Predicts class via majority vote of $K$ neighbors.
- **Regression:** Predicts value via average (or weighted average) of $K$ neighbors.

## Distance Metrics
- **Euclidean:** $\sqrt{\sum(x_i - y_i)^2}$
- **Manhattan:** $\sum|x_i - y_i|$

## Choosing K (Hyperparameter Tuning)
- **Low K (e.g., 1):** High Variance, Low Bias (Captures noise).
- **High K:** Low Variance, High Bias (Oversimplifies).
- **Elbow Method:** Plot Error Rate vs K to find the optimal point.

## Pros & Cons [web:534]
- **Pros:** Simple, no training phase, effective for non-linear data.
- **Cons:** Slow prediction (O(N)), sensitive to outliers, struggles with high dimensions (Curse of Dimensionality).
