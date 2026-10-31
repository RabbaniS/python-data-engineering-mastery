# Day 19: Performance, Partitions, and File Formats

## Topics
- CSV, JSON, and Parquet tradeoffs
- Partitioning and file sizing
- Predicate and column pushdown
- Reading execution plans and measuring performance

## Quick theory
- Parquet is a columnar format that can reduce I/O when queries select a subset of columns.
- Partitioning can help filter common query dimensions, but excessive tiny partitions create overhead.
- Predicate pushdown can filter data closer to storage; verify the plan and actual workload.
- Measure representative jobs before tuning. Avoid caching data that is not reused or too large for available memory.

## Practice
Write a sample dataset as Parquet partitioned by a sensible date field. Compare file size and filtered read behavior with CSV.

## Quick check
1. Why can Parquet improve analytical reads?
2. What is the small-files problem?
3. Why benchmark with a representative query?