# Split Skills Into Supporting Files

The redesigned skills should use a small `SKILL.md` plus focused supporting markdown files wherever the workflow has reusable phases, guardrails, examples, or reference material. This keeps each skill easier to scan while preserving detailed instructions for agents that need them.

## Consequences

- `SKILL.md` should explain when to use the skill and the top-level workflow.
- Detailed material should move into files such as `workflow.md`, `subagents.md`, `triage.md`, `verification.md`, `artifacts.md`, or `guardrails.md`.
- Existing supporting files from `grill-with-docs` and `tdd` should be preserved or adapted instead of flattened.
