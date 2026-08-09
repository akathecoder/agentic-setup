# CodeForge

CodeForge is an engineering skill set for deliberate planning, implementation, review,
ticket communication, and documentation. It includes adapted Matt Pocock workflows and
companion skills for Jira, GitHub, Confluence, Cursor Canvas, and long-running project
context.

All project artifacts created by these skills live locally under
`.agents/projects/<project>/`.

## Installation

CodeForge is distributed from:

```text
https://github.com/akathecoder/agentic-setup
```

Use your AI agent's plugin documentation to install CodeForge from that distribution
source. The portable Agent Plugin is supported by compatible harnesses, but each
harness owns its installation flow.

## Cursor

Use the Cursor-specific CodeForge package when you want the `update-ticket` rule to
prompt the agent after meaningful implementation or review progress.

1. Open **Customize** from the Cursor sidebar.
2. Open **Plugins**.
3. Add the CodeForge marketplace or repository URL above when Cursor asks for a plugin
   source, then select `cursor-codeforge`.
4. Select **Install** and choose a user or workspace scope.

Manage installed skills and rules from **Customize**. Install only `cursor-codeforge`
in Cursor; installing both CodeForge package formats duplicates the skills.

## Installing Individual Skills

Install selected skills directly into a supported coding agent with:

```bash
npx skills@latest add akathecoder/agentic-setup
```

The installer lets you choose the skills and target harness. This is useful when you
want only part of CodeForge instead of the complete plugin. The Cursor-only
`update-ticket.mdc` rule is included only by `cursor-codeforge`; install it separately
from `rules/` when using individual skills in Cursor.

## Included Skills

### Main Flow

- `grill-with-docs` - Interview a change or design while maintaining project facts,
  terminology, links, and ADRs.
- `to-spec` - Turn the current project discussion into a local and tracker-published
  specification.
- `to-tickets` - Break approved work into Jira-first or GitHub ticket drafts, then
  publish them after approval.
- `implement` - Build approved work with tests, changed-code coverage, and final review.
- `code-review` - Review a diff against repository standards and its originating spec.

### Planning And Design

- `wayfinder` - Plan large, uncertain work as a decision-ticket map until the route is
  clear.
- `improve-codebase-architecture` - Find deepening opportunities and present them in a
  Cursor Canvas or local visual report.
- `codebase-design` - Shared vocabulary and discipline for deep modules, seams,
  leverage, and locality.
- `grilling` - Model-invoked decision interview primitive used by planning skills.
- `domain-modeling` - Model-invoked project terminology and durable-decision discipline.

### Implementation And Review

- `tdd` - Model-invoked red-green testing discipline for behavior-focused vertical slices.
- `triage-pr-feedback` - Evaluate human and bot GitHub PR feedback, fix valid findings,
  reply, and resolve open review threads without committing or pushing.
- `update-ticket` - Model-invoked Jira/GitHub progress-update workflow that drafts
  comments for approval and never changes ticket metadata.

### Documentation And Clarity

- `to-confluence` - Draft concise, standalone Confluence pages from project knowledge,
  then publish only after approval.
- `bro-what` - Re-explain the previous response in plain, easy-to-follow language.
