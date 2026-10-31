# Day 05: Functions and Clean Interfaces

## Topics
- Defining and calling functions
- Parameters, return values, and defaults
- Local scope and pure functions
- Docstrings and small units of work

## Quick theory
- A function packages behavior behind a name and explicit inputs.
- `return` sends a result to the caller; `print` only writes output for a person to see.
- Prefer explicit parameters and return values over hidden global state.
- A pure function returns the same result for the same inputs and has no external side effects, making it easier to test.

## Practice
Refactor a sales summary into functions for parsing, validation, aggregation, and display. Keep file access outside the aggregation function.

## Quick check
1. What is the difference between returning and printing a value?
2. Why are mutable default arguments risky?
3. What makes a function easier to test?