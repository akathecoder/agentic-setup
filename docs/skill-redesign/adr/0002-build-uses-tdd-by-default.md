# Build Uses TDD By Default

The Build skill should use test-driven development by default for meaningful code changes, while allowing an explicit escape hatch for trivial or mechanical edits. This preserves the existing TDD discipline for behavior-bearing work without forcing red-green-refactor ceremony onto changes where tests would add little signal.

## Consequences

- Non-trivial Build work should begin from an approved work packet produced by Plan.
- Trivial or mechanical edits may proceed directly without creating a work packet first.
- Build should prefer behavior-focused tests through public interfaces.
- Build may skip test-first work only when the change is trivial, mechanical, or explicitly approved as not needing tests.
- When Build skips TDD, it should still verify the change through the project’s appropriate checks.
