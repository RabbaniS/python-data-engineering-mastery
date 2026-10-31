# Day 17: Spark Aggregations and Windows

## Topics
- `groupBy` and aggregate functions
- Window specifications and ranking
- Partitioning within a window
- Choosing group aggregation versus row-preserving windows

## Quick theory
- A group aggregation reduces each group to one or more output rows.
- A window function computes values across related rows while retaining row-level output.
- Window definitions specify partitioning and ordering; incorrect ordering changes the meaning of rankings and running totals.
- Distributed shuffles can be expensive, so understand which operations require data movement.

## Practice
Calculate revenue per product and rank each customer's orders by date. Verify ties and deterministic ordering.

## Quick check
1. How does a window differ from a group aggregation?
2. Why does window ordering matter?
3. What is a shuffle in distributed processing?