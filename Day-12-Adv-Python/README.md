# Day 12 – Advanced Python: Iterators, Generators, and Decorators

## Covered Concepts
- **Iterators:** Creating custom iterator classes with `__iter__` and `__next__`.
- **Generators:** Using `yield` for memory-efficient data processing (Lazy Evaluation).
- **Decorators:** Higher-order functions to modify behavior (e.g., logging, timing execution).

## Why it matters for AI?
- **Generators** are the backbone of data pipelines (e.g., TensorFlow Datasets), allowing us to train on datasets larger than RAM.
- **Decorators** are used for model inference (e.g., `@torch.no_grad`) and debugging pipelines.
