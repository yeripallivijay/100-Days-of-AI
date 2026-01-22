# Day 31 – Linear Regression & ML Pipelines

## Covered Concepts

### Linear Regression Variants
- **Simple:** `y = b₀ + b₁x`
- **Multiple:** `y = b₀ + b₁x₁ + b₂x₂ + ... + bₙxₙ`
- **Polynomial:** `y = b₀ + b₁x + b₂x² + b₃x³ + ...`

### ML Pipeline (sklearn)
```python
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('poly', PolynomialFeatures(degree=2)),
    ('model', LinearRegression())
])
