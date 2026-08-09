# Writing rules

Guidance for authoring the Cursor rules in this directory. The doctrine in the root
`AGENTS.md` applies here too — this file covers only what is specific to rules.

A rule is an `.mdc` file with this frontmatter:

```yaml
---
description: What the rule covers
globs: "**/*.ts" # attaches when matching files are in play
alwaysApply: false # true applies it to every session
---
```

Keep a rule under 50 lines and to one concern.

Prefer `globs` over `alwaysApply: true`. An always-applied rule costs context every
turn and is root-`AGENTS.md` content wearing a rule's frontmatter; glob scoping is the
one capability a rule has that `AGENTS.md` and skills do not, so it is the reason to
write a rule at all.

Give concrete before/after examples rather than describing the standard in prose — a
rule fires while the agent is editing matching files, so a worked example is what it
can act on directly.

Rules are Cursor-specific, which makes them the one deliberate exception to the
portability rule. Keep them to guidance that genuinely needs glob scoping, so a
different harness loses the least.

## Done when

- The rule names one concern and stays under 50 lines.
- `globs` scopes it, or `alwaysApply: true` is justified by guidance that truly
  applies to every session in the target repo.
- It carries at least one before/after example.
- Every line passes the no-op test.
