# Day 19 – Parallel Computing in Python

## Covered Concepts
- **Multithreading:** Using the `threading` module for I/O-bound concurrency.
- **Multiprocessing:** Using the `multiprocessing` module for CPU-bound parallelism.
- **Concurrent Futures:** Using `ThreadPoolExecutor` and `ProcessPoolExecutor` for modern, scalable task management.

## Why it matters for AI?
- **Data Loading:** We use Multiprocessing in PyTorch `DataLoader` to fetch and augment batches of images in parallel while the GPU trains on the previous batch.
