# Day 45 – K-Means Clustering

## Core Concept
K-Means partitions $n$ observations into $k$ clusters where each observation belongs to the cluster with the nearest mean (centroid).

## Steps
1. Initialize $k$ centroids randomly.
2. **Assignment Step:** Assign each data point to the closest centroid.
3. **Update Step:** Recalculate centroids as the mean of all points in the cluster.
4. Repeat until convergence.

## The Elbow Method
Used to find optimal $K$.
- Plot **WCSS** (Within-Cluster Sum of Squares) vs Number of Clusters.
- Look for the "elbow" where the drop in WCSS slows down.

## Application
Customer Segmentation: Grouping customers based on 'Annual Income' and 'Spending Score'.
