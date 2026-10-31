# Day 10: Classes, Dataclasses, and Type Hints

## Topics
- Classes, instances, and methods
- `dataclass` for record-like objects
- Function and variable type annotations
- Composition and simple domain models

## Quick theory
- A class defines behavior and state; an instance is a particular object created from that definition.
- A dataclass generates common methods for data-focused classes.
- Type hints document expected shapes and help static tools find mistakes; Python does not enforce them automatically at runtime.
- Prefer simple functions and data structures until a class makes shared state or behavior clearer.

## Practice
Represent an order as a typed dataclass. Add validation at construction or at the ingestion boundary and test invalid values.

## Quick check
1. What does a type annotation do at runtime by default?
2. When is a dataclass useful?
3. What is the difference between a class and an instance?