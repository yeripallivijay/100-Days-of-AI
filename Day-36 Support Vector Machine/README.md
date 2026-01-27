# Day 36 – Support Vector Machines (SVM)

## Core Concepts
- **Support Vectors:** The critical data points that define the boundary.
- **Margin:** Distance between the hyperplane and support vectors (SVM maximizes this).
- **Kernel Trick:** Maps data to higher dimensions without computing them explicitly.

## Kernel Comparison
| Kernel | Best For | Decision Boundary |
|--------|----------|-------------------|
| **Linear** | Linearly separable data | Straight line |
| **Polynomial** | Moderate curves | Curves/polynomials |
| **RBF** | Complex, non-linear patterns | Smooth, wiggly boundaries [web:509] |

## SVC vs SVR [web:511]
- **SVC:** Predicts classes (0/1)
- **SVR:** Predicts continuous values within an ε-margin

## Key Parameters
- `C`: Penalty for misclassification (small=wide margin, large=hard margin)
- `gamma`: Kernel coefficient (influences decision boundary curvature)
