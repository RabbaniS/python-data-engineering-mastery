# Day 07: Files, Paths, CSV, and JSON

## Topics
- `pathlib.Path` and relative paths
- Reading and writing text with encodings
- `csv.DictReader` and `csv.DictWriter`
- JSON serialization and deserialization

## Quick theory
- Use `with` to close files reliably, including when an exception occurs.
- Specify `encoding="utf-8"` for portable text handling.
- `pathlib` expresses filesystem paths without manual separator handling.
- CSV represents tabular text; JSON represents nested values. Parsing does not guarantee that data is valid.

## Practice
Convert a CSV file to JSON records and back. Preserve column names and report malformed rows with their line numbers.

## Quick check
1. Why use a context manager for file access?
2. What does parsing JSON guarantee, and what does it not guarantee?
3. Why avoid hard-coded absolute paths in a project?