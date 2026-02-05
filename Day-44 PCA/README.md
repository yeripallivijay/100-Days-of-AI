# Day 44 – Principal Component Analysis (PCA)

## Core Concept
PCA is a dimensionality reduction technique that:
1. Finds the directions (Principal Components) of maximum variance.
2. Projects data onto these directions.
3. Discards the noise (lower variance components).

## Project: Breast Cancer Visualization
- **Dataset:** sklearn `load_breast_cancer` (30 features).
- **Process:**
  1. Standardize data (StandardScaler is mandatory for PCA).
  2. Apply `PCA(n_components=2)`.
  3. Visualize the new 2D projection.
- **Result:** The two classes (Malignant/Benign) are clearly separable in just 2 dimensions.

## Why Use PCA?
- Speeds up ML algorithms (XGBoost, SVM).
- Removes multicollinearity.
- Enables visualization of high-dimensional data.
