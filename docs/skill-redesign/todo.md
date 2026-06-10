# Skill Redesign Todo

## Discussion

- [x] Inventory current active and deprecated skills relevant to planning, building, reviewing, and applying feedback.
- [x] Decide the final target skill taxonomy and names.
- [x] Define the Plan skill scope and output artifact.
- [x] Define the Build skill scope and relationship to TDD.
- [x] Define the Review skill scope and independence guardrails.
- [x] Define the feedback-implementation skill scope and name.
- [x] Capture modular skill files, subagent strategy, feedback triage, and git-write restrictions.

## Implementation

- [x] Update or create skill directories and supporting reference files.
- [x] Move deprecated or absorbed skills out of the active surface as needed.
- [x] Update `README.md` to match the active skills.
- [x] Review the final diff for consistency, stale references, and install-surface accuracy.

## Review

- [x] Record final decisions and any follow-up questions after the redesign is complete.

Final review notes:

- Active core workflow skills are `plan`, `build`, `review`, and `apply-feedback`.
- Absorbed skills are no longer active under `skills/`.
- `README.md` reflects the active and deprecated surfaces.
- No stale references to active `grill-with-docs`, `implement-ai-suggestions`, or `tdd` paths remain under `skills/`.
- All four core workflow skills include no-git-write guardrails.
