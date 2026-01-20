# Day 28 – Exploratory Data Analysis (EDA)

## Projects Completed
1. **Red Wine Quality Prediction** [wine.csv]
   - Univariate: Distribution of quality scores (skewed)
   - Bivariate: Alcohol content strongly correlates with quality
   - Feature Engineering: Created 'total acidity' feature

2. **Flight Ticket Price Prediction**
   - Univariate: Highly skewed ticket prices
   - Bivariate: Distance vs Price shows strong positive correlation
   - Feature Engineering: 'price_per_km' ratio

## EDA Checklist Used
- Data Summary (`describe()`, `info()`)
- Missing Values (`isnull().sum()`)
- Distributions (Histograms, Boxplots)
- Correlations (Heatmap)
- Outlier Detection (IQR method)
