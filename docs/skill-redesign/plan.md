# Skill Redesign Plan

## Target Active Skills

The active user-facing skill surface should become:

- `plan` - clarify, stress-test, and approve a feature or change before implementation.
- `build` - implement an approved plan, using TDD by default for meaningful code changes.
- `review` - independently review a local branch diff or GitHub PR from a fresh readonly context.
- `apply-feedback` - triage and implement selected feedback from AI reviewers, Bugbot, peers, GitHub comments, pasted findings, or Review output.

## Shared Design Rules

- Split each skill into a small `SKILL.md` plus supporting `.md` files wherever the workflow has reusable phases, guardrails, or reference material.
- Keep `SKILL.md` focused on when to use the skill and the top-level workflow.
- Put detailed instructions in supporting files such as `workflow.md`, `subagents.md`, `artifacts.md`, `triage.md`, `verification.md`, and `guardrails.md`.
- Never stage, commit, push, amend, reset, checkout, rebase, or otherwise perform git write operations in any of the four skills. Git writes are user-owned.
- Prefer subagents whenever they reduce main-context pressure without losing important judgment.

## Plan Skill

Use deprecated `grill-with-docs` as the base, but change the artifact model.

Expected behavior:

- Ask one focused question at a time, with a recommended answer.
- Explore the codebase instead of asking when the answer is discoverable.
- Create a work packet under `docs/<jira-ticket-or-context>/`.
- Use a Jira ticket folder such as `docs/pmntc-1234/` when a ticket is provided.
- Use a concise context folder such as `docs/skill-redesign/` when no Jira ticket exists.
- Always maintain `links.md`, `glossary.md`, `todo.md`, and `adr/`.
- Create `plan.md` only when the work needs high-level interfaces, test intent, risks, or implementation guardrails.
- Keep actual implementation code out of the Plan stage.
- Use subagents for bounded exploration where the final answer matters more than preserving all intermediate context, such as mapping ownership, finding existing patterns, checking similar implementations, listing affected files, or summarizing test conventions.
- Keep core trade-off decisions, terminology choices, and user-facing grilling in the main conversation.

Suggested supporting files:

- `artifacts.md` - work packet layout and naming rules.
- `questioning.md` - one-question-at-a-time grilling, recommendations, and AskQuestion usage.
- `documentation.md` - glossary and ADR rules.
- `subagents.md` - when Plan should delegate exploration.
- `handoff.md` - what Build needs from the Plan packet.

## Build Skill

Use deprecated `tdd` as the base, but broaden it from pure TDD into the implementation skill.

Expected behavior:

- Require an approved work packet for non-trivial work.
- Allow direct implementation for trivial or mechanical edits.
- Use TDD by default for meaningful behavior changes.
- Permit an explicit escape hatch for trivial/mechanical edits or user-approved non-TDD work.
- Preserve behavior-focused testing through public interfaces.
- Run appropriate verification before marking work complete.
- Keep changes scoped to the approved plan unless the user approves scope expansion.
- Rely heavily on subagents for implementation slices, research, test writing, verification, compiler/typecheck investigation, UI design, and cleanup when the work can be split safely.
- Keep orchestration, scope control, user decisions, and final integration in the main conversation.
- Never ask subagents to stage, commit, push, or perform other git write operations.

Suggested supporting files:

- `workflow.md` - plan intake, implementation loop, integration, and reporting.
- `tdd.md` - red-green-refactor default and escape hatch.
- `subagents.md` - delegation strategy and merge-back expectations.
- `testing.md` - behavior-focused tests and mocking guidance.
- `verification.md` - checks before marking work complete.
- `guardrails.md` - scope, quality, and git write restrictions.

## Review Skill

Use `deprecated/skills/review-pr` as the base, but update it for independent review.

Expected behavior:

- Review both local branch diffs and GitHub PR links or numbers.
- Run from a fresh readonly context or subagent by default.
- Do not read the work packet, Plan history, or Build session context unless explicitly asked.
- Gather context from the diff, nearby code, tests, PR metadata, and existing review comments.
- Prioritize correctness, security, test coverage, design, performance, readability, and consistency.
- Report findings by severity and avoid duplicating existing review comments.
- Do not fix issues during Review.
- Never stage, commit, push, or apply patches during Review.

Suggested supporting files:

- `inputs.md` - local diff and GitHub PR input handling.
- `independence.md` - fresh readonly context and bias guardrails.
- `review-dimensions.md` - correctness, security, design, tests, performance, readability, consistency.
- `output.md` - severity tiers, verdict logic, and reporting format.

## Apply Feedback Skill

Use deprecated `implement-ai-suggestions` as the base, but broaden the source model.

Expected behavior:

- Accept GitHub review comments, Bugbot output, Copilot or AI review comments, peer review comments, pasted findings, and Review-skill output.
- Classify feedback as structured suggestions or prose findings.
- Triage every item before editing into one of three categories:
  - Genuine issue, must fix.
  - Good issue, but not high priority and can be ignored.
  - Wrong issue, ignore.
- Think independently about every suggestion. Do not assume a reviewer, AI reviewer, Bugbot, or peer is correct.
- Present the triaged list to the user and ask which items to fix.
- Fix only the items the user selects.
- Use a subagent with the Build skill to fix selected issues when the fix is non-trivial or separable.
- Skip invalid, low-value, out-of-scope, or risky feedback with an explicit reason.
- Process same-file feedback sequentially and independent files in parallel when useful.
- Leave changes unstaged and uncommitted.

Suggested supporting files:

- `inputs.md` - GitHub comments, Bugbot output, AI review, peer review, pasted findings, Review output.
- `triage.md` - the three feedback categories and independent judgment rules.
- `selection.md` - user confirmation before fixing anything.
- `implementation.md` - delegating selected fixes to Build subagents.
- `reporting.md` - applied/skipped output.
- `guardrails.md` - scope and git write restrictions.

## Migration Notes

- `grill-with-docs` is absorbed into `plan`.
- `tdd` is absorbed into `build`.
- `implement-ai-suggestions` is absorbed into `apply-feedback`.
- `deprecated/skills/review-pr` is revived and updated as `review`.
- Absorbed active skills should move to `deprecated/skills/` so the core Plan/Build/Review/Apply Feedback workflow is represented by the four new skills.
- Supporting reference files should move with the skills that use them.
- New skills should keep detailed instructions in supporting files instead of monolithic `SKILL.md` files.
- `README.md` must be updated to reflect the active skill surface.

## Verification

- Check every `SKILL.md` has frontmatter with `name` and a `description` beginning with "Use when...".
- Search for stale references to absorbed skill names.
- Search the four active skills for prohibited git write commands.
- Verify `README.md` active skills and deprecated skills are accurate.
- Review the final diff for accidental changes outside the skill redesign.

## Risks

- Renaming active skills can break installed muscle memory unless README and deprecated notes are clear.
- Moving legacy glossary and ADR format guidance can break references from adjacent skills.
- Review independence can be weakened if the skill accidentally reads the Plan packet by default.
- `apply-feedback` can grow too broad unless it keeps strict triage and scope boundaries.
- Subagent-heavy Build can fragment work unless the main agent keeps ownership of integration and verification.
- Apply Feedback can accidentally implement bad reviewer advice unless triage and user selection happen before edits.
