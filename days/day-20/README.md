# Day 20: Reliable End-to-End Pipeline Design

## Topics
- Extract, transform, and load boundaries
- Idempotency and safe reruns
- Checkpoints, retries, and observability
- Configuration and reproducibility

## Quick theory
- A reliable pipeline makes inputs, outputs, and side effects explicit.
- Idempotency means rerunning the same work does not create unintended additional effects.
- Retries work best for transient failures and require bounded policies; idempotency protects against repeated writes.
- Track run IDs, source ranges, row counts, duration, and failure context to make operations diagnosable.

## Practice
Combine API or file extraction, validation, Spark transformation, and a database or Parquet sink. Add a run manifest and prove a rerun is safe.

## Quick check
1. What does idempotency protect against?
2. Why should retries be bounded?
3. Which run metrics would help diagnose missing output?