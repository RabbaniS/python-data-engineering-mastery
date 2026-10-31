# Day 14: APIs and Reliable Ingestion

## Topics
- HTTP methods, status codes, and JSON responses
- Timeouts, pagination, retries, and rate limits
- Raw versus normalized data
- Incremental extraction and watermarks

## Quick theory
- A successful network call is not guaranteed; set timeouts and handle status codes explicitly.
- Retry transient failures with bounded backoff; do not retry permanent client errors indefinitely.
- Preserve raw responses when practical so transformations can be rerun and audited.
- A watermark tracks extraction progress; design updates so reruns do not lose or duplicate records.

## Practice
Ingest one public paginated API into timestamped raw JSON files, then normalize records into SQLite. Record request metadata and handle retries.

## Quick check
1. Why must HTTP requests have a timeout?
2. What is the purpose of a watermark?
3. Which failures are reasonable retry candidates?