# Day 18: Data Quality and Spark SQL

## Topics
- Required fields, uniqueness, ranges, and freshness
- Spark SQL temporary views
- Data contracts and rejected records
- Quality metrics and actionable failures

## Quick theory
- A data contract describes expected schema and important business rules.
- Quality checks should produce measurable results and identify affected data, not only a pass/fail message.
- A temporary view lets SQL query a DataFrame within a Spark session.
- Decide explicitly whether a failed check rejects a row, warns, or fails the whole pipeline.

## Practice
Define checks for a daily orders feed, report invalid rows and freshness, then query the valid view with Spark SQL.

## Quick check
1. What belongs in a data contract?
2. How is a view useful in a Spark workflow?
3. What should happen when a critical quality check fails?