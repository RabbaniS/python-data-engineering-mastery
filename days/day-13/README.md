# Day 13: pandas for Data Transformation

## Topics
- Series and DataFrames
- Reading CSV and inspecting schemas
- Filtering, null handling, joins, and `groupby`
- Choosing between pandas and SQL

## Quick theory
- A DataFrame is a labeled, in-memory table; its full dataset generally needs to fit in available memory.
- Inspect types and missing values before transforming data.
- Vectorized operations are usually clearer and faster than Python loops over rows.
- SQL is often a better fit when data already resides in a database; pandas is useful for in-memory analysis and transformations.

## Practice
Recreate a customer revenue report from Day 12 in pandas. Compare row counts, null behavior, and final totals with the SQL result.

## Quick check
1. What is a DataFrame?
2. Why should null behavior be checked during a join?
3. When might pandas not be the right tool for a dataset?