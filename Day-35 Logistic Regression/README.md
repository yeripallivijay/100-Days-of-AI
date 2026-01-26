# Day 35 – Evaluation Metrics & Assumptions for Linear Regression

## Performance Metrics
- **Mean Absolute Error (MAE):** $\frac{1}{n}\sum|y - \hat{y}|$
- **Mean Squared Error (MSE):** $\frac{1}{n}\sum(y - \hat{y})^2$
- **R-Squared ($R^2$):** $1 - \frac{SSR}{SST}$ (Coefficient of Determination)
- **Adjusted $R^2$:** $1 - (1-R^2)\frac{n-1}{n-p-1}$
  - *Why use Adj-$R^2$?* It decreases if you add a feature that doesn't improve the model significantly.

## Key Assumptions Validation
1. **Linearity:** Scatter plot of y vs X.
2. **Homoscedasticity:** Scatter plot of Residuals vs Predictions (should look like random noise).
3. **Normality:** Q-Q Plot or Distplot of residuals.
4. **Multicollinearity:** Variance Inflation Factor (VIF) < 5.
