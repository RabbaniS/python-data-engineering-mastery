# Day 09: Comprehensions, Iterators, and Generators

## Topics
- List, set, and dictionary comprehensions
- Iterable versus iterator
- Generator expressions and `yield`
- Lazy processing of large inputs

## Quick theory
- A comprehension is a concise transformation or filter; keep it readable rather than nesting many conditions.
- An iterable can provide an iterator; an iterator produces values one at a time.
- A generator is lazy, so it can process a stream of records without storing the entire result in memory.
- Laziness reduces memory use but does not remove the need to handle errors or close resources.

## Practice
Create a generator that reads valid order records one at a time and yields normalized values. Compare it with loading all rows into a list.

## Quick check
1. What is the memory advantage of a generator?
2. Can a generator usually be traversed repeatedly after it is exhausted?
3. When is a regular loop clearer than a comprehension?