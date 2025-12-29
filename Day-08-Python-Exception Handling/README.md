# Day 8 – Python Exception Handling

## Covered
- **Blocks:** `try`, `except`, `else`, `finally`.
- **Built-in Exceptions:** Understanding the hierarchy (`BaseException` -> `Exception` -> `ValueError`, etc.).
- **Best Practices:**
  - Always clean up resources (closing files) in the `finally` block.
  - Avoid bare `except:` clauses; catch specific errors.

## Why it matters
- **Robustness:** Ensures long-running training jobs don't crash unexpectedly.
- **Debugging:** Proper error messages make fixing pipelines 10x faster.
