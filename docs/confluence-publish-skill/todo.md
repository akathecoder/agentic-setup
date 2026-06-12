# Confluence Publish Skill Todo

## Discussion

- [x] Identify the planning packet location.
- [x] Gather existing Atlassian MCP and skill-writing context.
- [x] Confirm the active skill name.
- [x] Confirm the skill is internal and agent-invoked, not directly user-invoked.
- [x] Confirm the trigger description.
- [x] Confirm whether "attestation MCP" means Atlassian MCP.
- [x] Define the local source document input rules.
- [x] Define the Confluence target-resolution rules for page IDs and folder/container IDs.
- [x] Define the single-page publishing invariant.
- [x] Define the preview-before-write approval flow.
- [x] Define the Composer 2.5 publishing subagent boundary.
- [x] Define failure handling, retries, and completion reporting.
- [x] Define supporting skill files.

## Implementation

- [x] Create the skill directory and `SKILL.md`.
- [x] Update `README.md` with the active skill entry.

## Verification

- [x] Check skill frontmatter and trigger description.
- [x] Review single-file skill shape.
- [x] Verify README active skill table accuracy.
- [x] Check for stale or conflicting Atlassian publishing guidance.

## Review

- [x] Record final decisions and remaining follow-up questions.

Final review notes:

- Added internal `publish-confluence` skill under `skills/publish-confluence/SKILL.md`.
- Kept v1 as a single-file skill per user direction.
- README lists `publish-confluence` as an internal skill.
- Verified frontmatter, trigger wording, stale-name references, README entry, lints, and markdown whitespace.
