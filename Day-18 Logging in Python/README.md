# Day 18 – Logging in Python

## Covered Concepts
- **The Logging Module:** Replacing `print()` with `logging`.
- **Log Levels:** DEBUG, INFO, WARNING, ERROR, CRITICAL.
- **Handlers:** Saving logs to files (`FileHandler`) and displaying them in the console (`StreamHandler`).
- **Formatting:** Customizing log messages with timestamps (`asctime`) and log levels (`levelname`).

## Why it matters for AI?
- **Debugging Long Runs:** AI training jobs can run for days. If they crash, logs are the only way to diagnose the failure.
- **Monitoring:** In production, logs help track model performance and inference latency.
