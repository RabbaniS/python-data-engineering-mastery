# Day 02: Operators, Strings, and Formatting

## Topics
- Arithmetic, comparison, and Boolean operators
- String indexing, slicing, and common methods
- f-strings and readable output
- Truthiness and explicit comparisons

## Quick theory
- `and` and `or` short-circuit: the second operand may not be evaluated.
- Strings are immutable; methods return new strings instead of changing the original.
- Use f-strings for readable interpolation, and format numbers deliberately for reports.
- Prefer explicit checks such as `value is None` when testing for missing values.

## Practice
Normalize customer names by trimming whitespace and applying consistent casing. Print a compact, aligned order summary.

## Quick check
1. What does slicing `text[:3]` return?
2. Are strings mutable?
3. How do `and` and `or` evaluate when the first operand determines the result?