# Design Skill Todo

## Discussion

- [x] Choose the planning packet location for this skill design.
- [x] Decide the active skill name.
- [x] Decide the trigger description.
- [x] Define what inputs the skill must gather before any design work starts.
- [x] Define the design packet artifact structure the skill should maintain.
- [x] Define the questioning and confirmation loop.
- [x] Define how HLD, LLD, schemas, flows, ADRs, open questions, and todos relate.
- [x] Define guardrails for what the skill must not decide without user approval.
- [x] Define handoff boundaries.
- [x] Define supporting skill files.
- [x] Decide Confluence-compatible Markdown artifact policy.
- [x] Decide Mermaid diagrams need prose or table fallbacks.

## Implementation

- [x] Create the skill directory and `SKILL.md`.
- [x] Add supporting skill files for workflow, artifacts, questioning, guardrails, and templates as needed.
- [x] Update `README.md` with the active skill entry.
- [x] Update design artifact guidance for Confluence-safe Markdown.
- [x] Update design documentation guidance to avoid incompatible Markdown structures.
- [x] Update diagram guidance to require Mermaid fallback summaries.

## Verification

- [x] Check skill frontmatter and trigger description.
- [x] Review supporting file links and progressive disclosure.
- [x] Verify the README active skill table is accurate.
- [x] Verify Confluence compatibility guidance appears in the relevant design skill files.

## Review

- [x] Record final decisions and remaining follow-up questions.

Final review notes:

- Added active `design` skill under `skills/design/`.
- Kept `SKILL.md` small and split detailed guidance into `artifacts.md`, `intake.md`, `questioning.md`, `documentation.md`, `diagrams.md`, and `guardrails.md`.
- Updated `README.md` to list `design` as an active generic skill.
- Verified frontmatter, trigger wording, supporting links, README entry, markdown whitespace, and lints.
- Updated `design` guidance so generated artifacts use conservative Confluence-compatible Markdown and Mermaid diagrams include prose or table fallback summaries.
