# Day 40 – Random Forest Classifier & Regressor

## Datasets
1. **Travel Dataset** (Classification): Customer segmentation [web:553].
2. **CarDekho Dataset** (Regression): Car price prediction [web:551].

## Key Hyperparameters
- `n_estimators`: Number of trees (100-500 works well).
- `max_depth`: Tree depth (Prevents overfitting).
- `max_features`: Features considered per split ('sqrt' or 'log2').
- `oob_score=True`: Out-of-bag validation score [web:552].

## Results Summary
| Dataset | Task | Single Tree | Random Forest | Improvement |
|---------|------|-------------|---------------|-------------|
| Travel  | Class | ~85%        | **92%**       | +7%         |
| CarDekho| Reg   | RMSE: 2.1   | **RMSE: 1.8** | -15%        |

## Feature Importance (Random Forest Magic)
Automatically ranks features by how much they reduce impurity.
