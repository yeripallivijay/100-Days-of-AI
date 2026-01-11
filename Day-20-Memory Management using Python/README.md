# Day 20 – Python Memory Management

## Covered Concepts
- **Reference Counting:** Python tracks object references automatically.
- **Garbage Collection:** Automatic cleanup of unused objects.
- **Generators:** `yield` keyword for memory-efficient iteration.
- **Memory Profiling:** Using `sys.getsizeof()` to measure object memory usage.

## Why it matters for AI?
- **Large Datasets:** Generators prevent memory crashes when processing millions of samples.
- **Production:** Memory leaks kill deployed models. Proper management ensures stability.
