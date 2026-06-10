# Build Workflow

## 1. Intake

For non-trivial work, read the approved work packet under `docs/<jira-ticket-or-context>/`:

- `links.md`
- `glossary.md`
- `todo.md`
- `plan.md` when present
- relevant ADRs in `adr/`

If no work packet exists and the change is not trivial or mechanical, pause and ask the user to run Plan first.

Proceed directly only when:

- The edit is clearly trivial or mechanical.
- The target files are obvious.
- There is no meaningful product, architecture, or testing decision to make.

## 2. Slice The Work

Break the implementation into vertical slices:

- One user-visible or caller-visible behavior at a time.
- One failing test before implementation when TDD applies.
- One integration point at a time.

Avoid horizontal slicing such as writing all tests first, all types second, and all implementation last.

## 3. Implement

For each slice:

1. Identify the expected behavior.
2. Add or update the smallest useful behavior test unless using the explicit TDD escape hatch.
3. Run the focused test and confirm it fails for the expected reason.
4. Implement the smallest change that passes.
5. Run the focused test again.
6. Update `todo.md` only after the behavior is verified.

## 4. Integrate

The main agent owns integration:

- Resolve interactions between subagent work.
- Keep scope aligned with the approved plan.
- Read changed files before final reporting.
- Ensure tests and checks are run from the integrated working tree.

## 5. Report

Finish with:

- What changed.
- Which tests/checks ran and their result.
- Any work packet todo items completed.
- Any risks, skipped checks, or follow-up needed.

Do not stage or commit the result.
