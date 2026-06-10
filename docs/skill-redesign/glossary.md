# Skill Redesign Glossary

## Language

**Active Skill**:
A user-facing skill that should be installed and invoked as part of the current workflow.
_Avoid_: Current skill, live skill

**Plan Skill**:
The active skill used to clarify, stress-test, and approve a feature or change before implementation.
_Avoid_: Grill skill, PRD skill

**Build Skill**:
The active skill used to implement an approved plan and verify the result.
_Avoid_: Dev skill, TDD skill

**Review Skill**:
The active skill used to review a pull request independently of the planning and build work that produced it.
_Avoid_: Reviewer agent

**Apply Feedback Skill**:
The active skill used to apply selected suggestions from AI reviewers, Bugbot, peer review, or similar feedback sources.
_Avoid_: Copilot-only fixer, Feedback Implementation Skill

**Work Packet**:
A folder that keeps the planning artifacts, references, and follow-up notes for one feature, ticket, or coherent change.
_Avoid_: Scratch folder, planning dump

**Reference Link**:
An online source such as a Jira ticket, Confluence page, pull request, design doc, or review thread that informs a **Work Packet**.
_Avoid_: External link

**Supporting Skill File**:
A markdown file next to `SKILL.md` that holds detailed workflow instructions, guardrails, examples, or reference material for one skill.
_Avoid_: Appendix, extra doc

**Git Write Operation**:
Any operation that changes git state, including staging, committing, pushing, amending, rebasing, resetting, checking out files, or changing branches.
_Avoid_: Git cleanup, git housekeeping

**Feedback Triage Category**:
One of the categories assigned to a review suggestion before any fix is attempted: genuine issue must fix, good issue but optional, or wrong issue ignore.
_Avoid_: Feedback status

## Relationships

- The **Plan Skill** produces the approved direction for the **Build Skill**.
- The **Review Skill** evaluates the resulting change independently of the **Plan Skill** and **Build Skill**.
- The **Apply Feedback Skill** applies selected findings from the **Review Skill** or external reviewers.
- A **Work Packet** belongs to one feature, ticket, or coherent change.
- A **Work Packet** contains **Reference Links** needed to revisit Jira, Confluence, pull requests, or review threads.
- A **Supporting Skill File** keeps detailed instructions out of a large monolithic `SKILL.md`.
- A **Git Write Operation** is always performed by the user, not by the skills.
- The **Apply Feedback Skill** assigns every suggestion a **Feedback Triage Category** before asking what to fix.

## Example dialogue

> **Dev:** "Should I use the **Build Skill** to respond to Bugbot comments?"
> **Domain expert:** "No - use the **Apply Feedback Skill** so review feedback is triaged and applied explicitly."

## Flagged ambiguities

- "Final result: 3 skills" listed four workflows - resolved: the active surface will contain four skills.
- "Plan output" could mean only discussion, only glossary updates, or a full implementation spec - resolved: the **Plan Skill** always creates a **Work Packet** with glossary, ADRs, and todo, and adds a higher-level implementation spec only when needed.
- "Build" could mean generic implementation or strict TDD - resolved: the **Build Skill** uses TDD by default for meaningful code changes, with an explicit escape hatch for trivial or mechanical edits.
- "Build input" could mean only approved plans or any chat request - resolved: the **Build Skill** requires a **Work Packet** for non-trivial work, but can handle trivial or mechanical edits directly.
- "Review input" could mean local diffs, GitHub PRs, or pasted patches - resolved: the **Review Skill** supports both local branch diffs and GitHub PR links or numbers.
- "Independent review" could mean merely trying to be objective or using an isolated context - resolved: the **Review Skill** should run in a fresh readonly subagent or session and avoid reading the **Work Packet** unless explicitly asked.
- "Feedback implementation" could mean only Copilot suggestions or all review feedback - resolved: the **Apply Feedback Skill** accepts GitHub review comments, Bugbot, Copilot or AI reviews, peer reviews, pasted findings, and **Review Skill** output.
- "Absorbed skills" could remain active as aliases or leave the core workflow surface - resolved: absorbed skills move to `deprecated/skills/` so `plan`, `build`, `review`, and `apply-feedback` become the core workflow skills.
- "Skill shape" could be one large `SKILL.md` or several focused files - resolved: each new skill should use **Supporting Skill Files** where possible.
- "Applying feedback" could mean directly implementing reviewer suggestions - resolved: **Apply Feedback Skill** first triages each item, asks the user which items to fix, and only fixes selected items.
- "Git safety" could allow routine staging or commits by the agent - resolved: all **Git Write Operations** are user-owned across all four skills.
