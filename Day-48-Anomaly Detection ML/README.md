
# Day 48 – Isolation Forest for Anomaly Detection

## Core Concept
Isolation Forest uses **random partitioning** to isolate anomalies:
- **Path Length:** Number of splits to isolate a point.
- **Normal Points:** Long paths (dense regions).
- **Anomalies:** Short paths (easy to isolate) .

## Algorithm
```python
from sklearn.ensemble import IsolationForest
iso_forest = IsolationForest(contamination=0.1, random_state=42)
iso_forest.fit(X)
anomaly_labels = iso_forest.predict(X)  # -1 = Anomaly, 1 = Normal
anomaly_scores = iso_forest.decision_function(X)  # Lower = More Anomalous
