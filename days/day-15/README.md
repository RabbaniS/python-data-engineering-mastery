# Day 15: PySpark DataFrames and Schemas

## Topics
- SparkSession and local execution
- DataFrames and explicit schemas
- Transformations versus actions
- Distributed data processing concepts

## Quick theory
- Spark DataFrames describe distributed data and operations; they are not ordinary in-memory pandas DataFrames.
- Transformations build a logical plan; actions such as `count` or `show` trigger execution.
- Explicit schemas make expected types clear and avoid unreliable inference on inconsistent inputs.
- Spark is useful when scale or distributed processing justifies its runtime and operational complexity.

## Practice
Start a local Spark session, load a small CSV with an explicit schema, inspect the plan, and count valid records.

## Quick check
1. What triggers Spark execution?
2. Why prefer an explicit schema for a production feed?
3. Does using Spark automatically make every job faster?