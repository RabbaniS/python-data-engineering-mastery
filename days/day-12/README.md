# Day 12: SQL and SQLite from Python

## Topics
- Relational tables, keys, and constraints
- SQLite connections, cursors, and transactions
- Parameterized queries and bulk inserts
- Joins, grouping, and aggregations

## Quick theory
- A primary key identifies a row; constraints let the database enforce important invariants.
- Parameterized SQL separates query structure from values and prevents unsafe string interpolation.
- Transactions make a set of database changes commit together or roll back together.
- Use `executemany` for repeated inserts and indexes for measured lookup needs, not by default on every column.

## Practice
Load orders and customers into related tables, use a transaction, and write a join that reports customer totals. Make reruns predictable.

## Quick check
1. Why use placeholders for SQL values?
2. What does a transaction protect?
3. What does a foreign key represent?