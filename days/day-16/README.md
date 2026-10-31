# Day 16: Spark Transformations and Joins

## Topics
- `select`, `withColumn`, and `filter`
- DataFrame joins and join keys
- Null semantics and duplicate keys
- Avoiding unnecessary collection to the driver

## Quick theory
- Spark transformations are generally immutable: each operation returns a new DataFrame plan.
- A join can multiply rows when keys are not unique; check key cardinality and expected output counts.
- Nulls do not behave like ordinary values in comparisons and joins.
- `collect` brings all rows to the driver and can exhaust its memory; use it only for known-small results.

## Practice
Join order and customer DataFrames. Assert expected row counts, inspect unmatched records, and avoid collecting the full result.

## Quick check
1. What can duplicate join keys do to row counts?
2. Why can `collect()` be dangerous?
3. How should unmatched rows be inspected?