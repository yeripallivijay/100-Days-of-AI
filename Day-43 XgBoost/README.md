# Day 43 – XGBoost Classifier & Regressor

## Core Advantages [web:582]
XGBoost (Extreme Gradient Boosting) improves upon standard GBM by:
- **Parallelization:** Uses all CPU cores during training.
- **Regularization:** Includes L1 (Lasso) and L2 (Ridge) penalties in the objective function.
- **Tree Pruning:** Uses "max_depth" and creates trees backwards (pruning negative gain splits).
- **Missing Values:** Learns default directions for NaN values [web:584].

## Projects
1. **Travel Insurance Prediction:** `XGBClassifier`
   - Tuned `scale_pos_weight` for imbalanced classes.
2. **Car Price Prediction:** `XGBRegressor`
   - Tuned `reg_alpha` (L1) and `reg_lambda` (L2) to reduce variance.

## Key Hyperparameters
- `learning_rate` (eta): Step size shrinkage (0.01 - 0.3).
- `max_depth`: Depth of trees (3-10).
- `subsample`: Fraction of samples used per tree.
- `colsample_bytree`: Fraction of columns used per tree.
