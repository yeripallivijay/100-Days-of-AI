
# Day 47 – DBSCAN (Density-Based Clustering)

## Core Concept
DBSCAN finds clusters based on density rather than distance to a centroid.

## Parameters
- **eps (ε):** Max distance between two points to be neighbors.
- **min_samples:** Min points to form a core point.

## Labels
- **0, 1, 2...:** Cluster IDs.
- **-1:** Noise/Outliers.

## make_moons Dataset
```python
X, y = make_moons(n_samples=200, noise=None,random_sample=42)

