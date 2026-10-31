# Day 06: Modules, Imports, and Project Layout

## Topics
- Modules and packages
- Imports and the `if __name__ == "__main__"` guard
- Separating reusable code from command-line entry points
- Basic repository organization

## Quick theory
- A module is a Python file that can be imported; a package groups related modules.
- Importing a module executes its top-level statements, so keep side effects inside functions or an entry-point guard.
- The `__name__` guard lets a file work both as an importable module and as a script.
- Organize code around responsibilities, not one enormous script or one file per tiny expression.

## Practice
Split a CSV report into a parsing module and a small CLI script. Import the parser without triggering the report run.

## Quick check
1. What happens to top-level statements when a module is imported?
2. Why use the `__main__` guard?
3. What belongs in a reusable module rather than a CLI entry point?