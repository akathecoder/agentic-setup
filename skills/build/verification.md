# Build Verification

Never mark Build complete without proof.

## Verification Order

Run the narrowest useful check first, then broaden:

1. Focused test for the slice.
2. Related package or module tests.
3. Type-check, compile, lint, or format checks used by the repo.
4. Broader test suite when risk or blast radius justifies it.

If a command is unknown, inspect repo scripts, docs, CI config, or ask only when the answer cannot be discovered.

## Failure Handling

When a check fails:

- Read the failure carefully.
- Fix root causes, not symptoms.
- Re-run the failing check.
- If the failure is unrelated to your change, report it clearly and avoid masking it.

Use subagents for compiler/type-check investigations when failures are broad but separable.

## Reporting

Report:

- Commands run.
- Pass/fail result.
- Any checks not run and why.
- Residual risk.

Do not claim verification from unrun checks.
