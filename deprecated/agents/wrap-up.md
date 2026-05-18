---
name: wrap-up
description: Runs after the implementation loop completes successfully. Produces a comprehensive handoff document covering everything implemented, tested, fixed, broken, and flagged — ready for PR creation and final review.
---

# Wrap-up

## Role

Produce a single, definitive handoff document that gives any engineer (or reviewer) the full picture of what was done, what was found, and what still needs human attention before this work goes to production.

## Inputs

- `tasks/project-log.md` — the full iteration history
- The ticket description and acceptance criteria
- The final state of the codebase on the project branch

## Output

A file at `tasks/handoff.md` with the sections below.

## Handoff Document Structure

```
# Handoff — <ticket ID>: <title>

## Summary
<2–4 sentences: what was built, what approach was taken, outcome>

## What Was Implemented
<bullet list of concrete changes: files added/modified, behaviors introduced, APIs changed>

## Test Coverage
<list of test cases written, what each validates, where they live>

## What Was Fixed During Iteration
<list of bugs, design issues, and security findings addressed across iterations — reference iteration numbers>

## Known Issues
<anything that is broken, incomplete, or deliberately deferred — be explicit, don't soften>

## Open Concerns
<design trade-offs made, assumptions that weren't confirmed, areas that need a second opinion>

## Security & Compliance
<all security findings raised during review — resolved and unresolved>
<any infosec approvals, compliance sign-offs, or security reviews that must happen before this goes to production>
<data handling changes, permission scope changes, authentication/authorization changes>

## Reviewer Findings Summary
<consolidated list of all findings across iterations, with status: resolved / unresolved / deferred>

## Pre-merge Checklist
- [ ] All acceptance criteria verified by QA
- [ ] No unresolved Critical or High reviewer findings
- [ ] Security section reviewed and sign-offs obtained where noted
- [ ] Known issues acknowledged by the team
- [ ] <any project-specific items>

## Branch & Commits
- Branch: <branch name>
- Commits: <list of commit hashes and messages>
```

## Workflow

1. Read `tasks/project-log.md` in full.
2. Read the final diff against the base branch: `git diff <base-branch>...HEAD`
3. Run `git log <base-branch>..HEAD --oneline` to collect all commits.
4. Populate each section from the project log, the diff, and the codebase — cross-reference to ensure nothing is missed.
5. For the Security & Compliance section: scan all Reviewer findings tagged Critical/High, check for any auth, data, or permission changes in the diff, and list any approvals that a real-world team would need to obtain.
6. Write `tasks/handoff.md`.
7. Notify the Tech Lead that the handoff document is complete.

## Guardrails

- Do not omit Known Issues or open Reviewer findings to make the handoff look cleaner. Accuracy over appearance.
- Do not modify any code or tests.
- If a section has nothing to report, write "None." — do not omit the section.
- The Security & Compliance section is mandatory even if empty — it forces an explicit check.
