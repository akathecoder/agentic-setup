---
name: writing-for-agents
description: Reference for writing skills, AGENTS.md, and other documents an agent will consume.
disable-model-invocation: true
---

# Writing For Agents

Reference for writing any document an agent consumes: a skill, an `AGENTS.md`, a
doc reached by a pointer. The packaging differs; the writing does not: the same
levers make each one predictable, because the agent takes the same process every
run rather than producing the same output.

When the document is a skill, read `SKILL-MECHANICS.md` for frontmatter, invocation,
and descriptions.

## Context pointers

A **context pointer** is a reference held in the agent's context that names
material outside it and encodes the condition for reaching it. A skill's
`description` is one; so is a line in `AGENTS.md` naming a doc. The pointer's
wording, not the target, decides whether the agent reaches the material.

A pointer states what the material is and lists the **branches** that should
trigger reaching it. Every word of an always-loaded pointer is **context load**,
so prune it harder than the body:

- Front-load the words that do the triggering.
- One **trigger** per branch. Synonym renames are one branch written twice.
- Name the job, not the contents.

A pointer without its condition cannot fire.

## The two loads

- **Context load** — always-loaded tokens: skill descriptions, `AGENTS.md`,
  `alwaysApply: true` rules. Paid every turn whether they fire or not.
- **Cognitive load** — which documents exist and when to reach for each. A
  user-invoked skill spends this instead of context load.

Material reached only through a pointer escapes context load at the price of the
pointer's own line.

## Information hierarchy

Content sits on one of three rungs:

1. **In-file step** — what the agent does, in order.
2. **In-file reference** — definitions and rules consulted on demand.
3. **Disclosed reference** — a sibling file reached by a context pointer.

**Progressive disclosure** is the move down that ladder. The test is **branching**:
inline what every run needs, disclose what only some runs reach. A skill forking
between two modes gives each mode its own file.

Sibling files are `UPPERCASE-KEBAB.md`, one level deep from `SKILL.md`. Flat
siblings win over nesting under `references/`. Executables go in `scripts/`, static
templates in `assets/`.

**Co-locate** a concept's definition, rules, and caveats under one heading.

Split only when the cut earns a load: by sequence, when later steps tempt the
agent to rush the one in front; by invocation, when `SKILL-MECHANICS.md` applies.

## Steps and completion criteria

Every step ends on a **completion criterion**. Two properties:

- **Clarity** — can the agent tell done from not-done?
- **Demand** — how much it requires, which is what drives **legwork**.

The strongest criteria are both checkable and exhaustive. End multi-step skills
with an explicit `Done when` list.

## Leading words

A **leading word** is a compact concept the model already holds from pretraining,
repeated as a token so it anchors behaviour. Prefer ordinary technical English; a
coined word buys nothing until defined. Record coined terms in `CONTEXT.md`.

Prompt the positive: state the target behaviour so the unwanted one is never
named. Reserve prohibition for hard guardrails, paired with the positive target.

## Human gates

Where the skill must not run ahead of the user, say so in the imperative and name
what unblocks it.

## Durability

Anything an agent will read later describes the code by its types and behaviours,
never by source paths or line numbers. Pointing at conventional files
(`.agents/projects/<project>/…`) is a context pointer, not a code reference.

Cloud and repository comments stand alone. They do not refer to local ADRs,
project artifacts, or other uncommitted documents.

## Artifact paths

Everything an agent writes that is not source code goes under
`<repository-root>/.agents/projects/<project>/`. Resolve the repository root
before creating an artifact; never use a global agent-installation directory.
A skill that produces an artifact names that path shape in its own body.

## Pruning

- **No-op** — an instruction the model already obeys by default. Delete it.
- **Duplication** — one meaning in two places. Single source of truth.
- **Cache** — a restatement of something the environment already says. Cache
  unwritten conventions; leave one-command lookups to the environment.
- **Sprawl** — too long even when every line is live. Hold `SKILL.md` under 500
  lines. Cure with the ladder.
- **Sediment** — guidance for behaviour the repo no longer has.

## Done when

A skill is finished when:

- The frontmatter carries nothing beyond the four allowed keys, and `name`
  matches the directory.
- A model-invoked skill either carries trigger phrasing or is named by another
  skill that invokes it; otherwise it is user-invoked.
- The description matches the invocation mode.
- Every sibling file's pointer states the condition for reading it.
- Every step has a checkable completion criterion, and every gate names what
  unblocks it.
- Coined vocabulary appears in `CONTEXT.md`.
- Every line passes the no-op test.
- It has been run against a real task and what the run exposed is folded back in.
  A skill that has never executed is a draft.
