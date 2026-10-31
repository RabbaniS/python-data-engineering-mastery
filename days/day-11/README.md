# Day 11: Testing, Logging, and Configuration

## Topics
- Unit tests and assertions
- Test fixtures and temporary files
- Logging levels and useful context
- Environment-based configuration and secret handling

## Quick theory
- Tests check observable behavior; test outcomes and edge cases rather than private implementation details.
- A unit test isolates a small behavior; an integration test checks collaborating components.
- Logging records operational events with severity and context; it is more useful than scattered debug prints.
- Keep credentials outside source control and make required configuration fail clearly when missing.

## Practice
Add tests for valid and invalid records, replace diagnostic prints with logging, and read a configurable input path from a CLI argument.

## Quick check
1. What is one difference between a unit and integration test?
2. Which log level should represent an unrecoverable run failure?
3. Why should secrets not be committed to Git?