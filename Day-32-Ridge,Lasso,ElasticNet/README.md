# Day 32 – Regularized Linear Regression

## Covered Concepts
- **Overfitting vs Underfitting:** The Bias-Variance Tradeoff.
- **Ridge (L2):** $\sum (y - \hat{y})^2 + \lambda \sum \beta^2$
- **Lasso (L1):** $\sum (y - \hat{y})^2 + \lambda \sum |\beta|$
- **ElasticNet:** Combination of L1 and L2.

## Project: Algerian Forest Fire Prediction
Predicting the **Fire Weather Index (FWI)** using weather data.
- **Ridge** performed best due to high correlation between 'Temp' and 'FFMC'.
- **Lasso** successfully reduced feature count by zeroing out 'Rain' in some iterations.

## Why Regularization?
Standard Linear Regression fails when:
1. Features > Observations (p > n)
2. High Multicollinearity exists (Features are twins).
Regularization solves both.
