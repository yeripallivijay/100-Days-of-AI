# Day 42 – Gradient Boosting Regressor & Classifier

## Core Concept
Gradient Boosting builds an ensemble of trees sequentially.
- **Residuals:** Each new tree is trained to predict the *residual errors* ($y - \hat{y}$) of the previous ensemble.
- **Gradient Descent:** It minimizes a Loss Function (MSE for regression, Log Loss for classification) by moving in the negative gradient direction.
- **Learning Rate:** Scales the contribution of each new tree (usually 0.01 - 0.1) to prevent overfitting.

## Comparison vs AdaBoost
| Feature | AdaBoost | Gradient Boosting |
|---------|----------|-------------------|
| **Mistake Focus** | High weights on hard points | Fits residuals (errors) directly |
| **Loss Function** | Exponential Loss | Differentiable (MSE, Log Loss, etc.) |
| **Outliers** | Highly Sensitive | Robust (if loss function is robust) |

## Projects
- **Travel Dataset:** Classification with `GradientBoostingClassifier`.
- **CarDekho:** Regression with `GradientBoostingRegressor`.
