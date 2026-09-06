# Skill mechanics

The skill-specific branch of `writing-for-agents`: frontmatter, invocation, and
descriptions. Everything else about writing it is the reference in `SKILL.md`.

## Frontmatter

Exactly these four keys, in this order:

```yaml
---
name: skill-name
description: ...
disable-model-invocation: true
argument-hint: "..."
---
```

`name` is lowercase alphanumeric and single hyphens, max 64 characters, no
leading or trailing hyphen, and matches the directory.

`disable-model-invocation` and `argument-hint` are not in the Agent Skills spec;
Cursor and Claude Code honour them. Omit `disable-model-invocation` to allow
model-invocation. Include `argument-hint` only when the skill takes an argument;
phrase it as the question being asked. The answer arrives as prose in the
conversation, so the body reads it from context rather than a positional variable.

One `SKILL.md` serves every harness. No per-harness sidecars. Cursor is the
first-class harness: where a portable choice and a Cursor-specific one conflict,
take the portable one and note the Cursor behaviour beside it.

## Invocation

Default to user-invoked. Model-invocation requires a reason: either the agent must
find the skill unprompted, or another skill must invoke it. Reuse alone is not a
reason.

- **User-invoked** (`disable-model-invocation: true`) — only the user can run it
  by name. Zero context load. The description is one line stating what it does,
  for a human list.
- **Model-invoked** (omit the key) — the agent can fire it and other skills can
  reach it. The description names the job, then lists the triggers. Front-load
  trigger words; one trigger per branch.

User-invoked skills cannot reach each other, since neither has a description for
the other to match. Shared reference two of them both need lives outside the
skill system — `CONTEXT.md`, or a doc either can point at.

A model-invoked skill whose content is all reference is a home for shared
reference: another skill can invoke it.

## Skill, rule, or AGENTS.md?

| Relevant when                                           | Home                |
| ------------------------------------------------------- | ------------------- |
| Every task in the repo, unconditionally                 | `AGENTS.md`         |
| Files matching a pattern are in play, whatever the task | A rule with `globs` |
| Doing a particular kind of work                         | A skill             |
