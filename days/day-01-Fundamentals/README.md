# Day 01: Python Fundamentals

## Topics
- Variables
- Data types
- Type conversion
- Arithmetic operators
- Comparison operators
- Logical operators
- Input and output

## Definitions and examples

| Topic | Definition | Example |
| --- | --- | --- |
| Variables | Names that refer to values. Python determines the value's type at runtime; assigning a new value can change the type. | `customer = "Asha"` |
| Data types | Categories that describe what values are and which operations they support. Common built-in types include `int`, `float`, `str`, `bool`, and `NoneType`. | `count = 3`, `price = 2.5`, `active = True` |
| Type conversion | Changing a value from one type to another with a constructor or conversion function. Conversion may fail if the text is not valid for the target type. | `count = int("12")` |
| Arithmetic operators | Symbols that perform numeric calculations: `+`, `-`, `*`, `/`, `//`, `%`, and `**`. | `total = 7 * 3`; `remainder = 7 % 3` |
| Comparison operators | Operators that compare values and produce a Boolean result: `==`, `!=`, `<`, `<=`, `>`, and `>=`. | `is_large = total >= 20` |
| Logical operators | `and`, `or`, and `not` combine or invert Boolean conditions. | `is_valid = count > 0 and active` |
| Input and output | Input receives data from a user or another source; output presents or stores a result. `input()` reads a line as text, while `print()` displays values. | `name = input("Name: ")`; `print(name)` |

## Quick theory
- `input()` always returns a string, so convert numeric input before doing arithmetic.
- `/` performs true division; `//` performs floor division; `%` gives the remainder.
- `==` compares values, while `=` assigns a value to a variable.
- Use `and` when all conditions must be true; use `or` when at least one must be true.
- `float` can have small binary precision errors. Use `Decimal` for exact decimal currency calculations.

## Practice
Create a script that asks for a product name, quantity, and unit price. Convert the numeric inputs, calculate the total, compare it with a minimum order amount, and print a clear summary. Try valid and invalid input.

## Quick check
1. What type does `input()` return, and why might conversion be needed?
2. What is the difference between `=` and `==`?
3. What is the difference between `/`, `//`, and `%`?
4. When would you use `and` instead of `or`?