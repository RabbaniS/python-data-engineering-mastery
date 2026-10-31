# Day 08: Exceptions and Data Validation

## Topics
- Tracebacks and exception types
- `try`, `except`, `else`, and `finally`
- Raising clear exceptions
- Row-level validation and error reporting

## Quick theory
- Catch only exceptions you can handle meaningfully; broad catches can hide defects.
- Add context when raising an error so the user can locate the bad input.
- Validate data at system boundaries before relying on its types or values.
- For batch ingestion, distinguish rejected records from a failed pipeline and make the policy explicit.

## Practice
Validate required CSV fields, dates, quantities, and prices. Collect row-level issues and fail the run if the rejection threshold is exceeded.

## Quick check
1. Why is `except Exception` often too broad?
2. When should an error be raised instead of silently corrected?
3. How will your pipeline make rejected rows visible?