# AGENTS.md

This repository is the source of truth for my personal agent setup: the skills and
rules I install into every project I work on.

Authoring guidance is what every task here does, so the doctrine below applies
unconditionally and lives here rather than in a skill. Keep it under 275 lines.

## Portability

Skills follow the [Agent Skills spec](https://agentskills.io/specification): a
directory containing `SKILL.md` with YAML frontmatter. One `SKILL.md` serves every
harness, with no per-harness sidecars (`agents/openai.yaml`, `.claude/` variants).

**Cursor is the first-class harness.** Where a portable choice and a Cursor-specific
one conflict, take the portable one and note the Cursor behaviour beside it.

## Layout

```
skills/<skill-name>/SKILL.md   # one directory per skill, flat
rules/<rule-name>.mdc          # Cursor rules; see rules/AGENTS.md to write one
CONTEXT.md                     # leading-word glossary; read before naming a concept
```

Skills install by symlink into `~/.agents/skills/<name>`, rules into `~/.cursor/rules/`,
so a `git pull` updates everything installed. `~/.agents/skills/` is harness-neutral and
Cursor reads it, which is why it is the install root rather than `~/.cursor/skills/`.
The link script is not written yet; until it is, linking is manual.

## Where agent-authored files go

Everything an agent writes that is not source code goes under `.agents/` at the root of
whatever project it is working in:

```
.agents/tasks/todo.md      # working plan for the current task
.agents/tasks/lessons.md   # corrections from me, so a mistake stops recurring
.agents/<name>.md          # research notes, handoffs, scratch analysis
```

**Everything under `.agents/` is ephemeral** — scratch that dies with the task. Moving
an artifact somewhere durable (`docs/`, an ADR directory, a committed spec) is my
explicit call and never a default. Add `.agents/` to the project's `.gitignore` when it
is missing.

This holds even where the project already keeps plans or docs of its own, so a skill
behaves identically in every repo. A skill that produces an artifact names the full path
in its own body, since it travels to repos this file never reaches.

## Skill, rule, or AGENTS.md?

Pick by _what makes the guidance relevant_:

| Relevant when                                           | Home                |
| ------------------------------------------------------- | ------------------- |
| Every task in the repo, unconditionally                 | `AGENTS.md`         |
| Files matching a pattern are in play, whatever the task | A rule with `globs` |
| Doing a particular kind of work                         | A skill             |

Glob-scoped auto-attach is the one capability a rule has that the others lack, so
anything unconditional belongs in `AGENTS.md` instead.

## The two loads

Every line spends one of two budgets, and naming which one decides whether it stays:

- **Context load** — always-loaded tokens: every skill `description`, every line of
  this file, every `alwaysApply: true` rule. Paid every turn whether they fire or not.
- **Cognitive load** — what I have to remember: which skills exist and when to reach
  for each. Not a cost to minimise; it is the price of keeping my judgement in the loop.

## Invocation

**Default to user-invoked.** Model-invocation requires a reason: either the agent must
find the skill unprompted, or another skill must invoke it. Reuse alone is not a reason.

- **User-invoked** (`disable-model-invocation: true`) — only I can run it, by typing
  its name. Zero context load.
- **Model-invoked** (omit the key) — the agent fires it autonomously and other skills
  can reach it, at the cost of a permanently loaded description.

Design around one consequence: user-invoked skills cannot reach each other, since
neither has a description for the other to match. Shared reference two of them both
need lives outside the skill system — `CONTEXT.md`, or a doc either can point at.

## Frontmatter

Exactly these four keys, in this order:

```yaml
---
name:
  skill-name # lowercase alphanumeric and single hyphens, max 64
  # chars, no leading/trailing hyphen, matches directory
description: ... # max 1024 chars
disable-model-invocation: true # default for new skills; omit to allow auto-invocation
argument-hint: "..." # only when the skill takes an argument
---
```

`disable-model-invocation` and `argument-hint` are **not** in the spec; Cursor and
Claude Code honour them and no portable equivalent exists. That trade is why these two
stand while the spec's own optional keys (`license`, `compatibility`, `metadata`,
`allowed-tools`) stay out: those cost context without changing behaviour.

`argument-hint` is the prompt shown when the skill is invoked without an argument, so
phrase it as the question being asked: `"What will the next session be used for?"`. The
answer arrives as prose in the conversation, so the body reads it from context rather
than a positional variable.

## Descriptions

A description is a **context pointer**: it names material outside the agent's context
and encodes the condition for reaching it. The wording, not the target, decides whether
the agent gets there — so a skill that should have fired and didn't is a bug in the
description. Sharpen the wording before touching the body.

A model-facing description names the skill's job, then lists the triggers:

```yaml
description:
  Diagnosis loop for hard bugs and performance regressions. Use when the
  user says "debug this", or reports something throwing, failing, or slow.
```

The trigger clause is always loaded, so it earns harder pruning than the body:

- **Front-load the words that do the triggering.** Hold the opening job clause to a few
  words; it earns its place because the agent matches semantically against it, but it
  competes with the triggers for the strongest position.
- **One trigger per branch.** Synonyms renaming a single case are that case written
  twice; keep only genuinely distinct cases.
- **Name the job, not the contents.** The description says when to load the skill; what
  it contains is the body's work.

A user-invoked skill's description is instead one line stating what the skill does,
read by a human browsing a list.

## Information hierarchy

Content sits on one of three rungs, ranked by how immediately the agent needs it:

1. **In-file step** — what the agent does, in order. The primary tier.
2. **In-file reference** — definitions and rules consulted on demand. A flat set of
   peers is a fine arrangement, not a smell.
3. **Disclosed reference** — a sibling file reached by a pointer, loaded only when the
   pointer fires.

**Progressive disclosure** is the move down that ladder, and the test is **branching**:
inline what every run needs, disclose what only some runs reach. A skill forking between
two modes gives each mode its own file, so a given run loads one. The same test governs
templates.

Sibling files are `UPPERCASE-KEBAB.md`, one level deep from `SKILL.md`, and always
pointed at with the condition for reading them: `When the document is a skill, read
SKILL-MECHANICS.md for invocation choice.` A pointer naming a target without its
condition leaves the agent unable to tell when to follow it.

The spec suggests nesting reference material under `references/`; flat siblings win here
because a one-word filename is easier to point at and keep one level deep. Executable
helpers still go in `scripts/` and static templates in `assets/`.

**Co-locate** within a file: keep a concept's definition, rules, and caveats under one
heading rather than scattered.

## Steps and completion criteria

Every step ends on a condition telling the agent the work is done. Two independent
properties make it work:

- **Clarity** — can the agent tell done from not-done? A vague bound ("understanding
  reached") invites stopping early, especially when later steps are visible and pulling
  at attention. Sharpen the bound; that fixes almost every case.
- **Demand** — how much it requires, which is what drives **legwork**. "Every modified
  model accounted for" forces legwork where "produce a change list" does not.

The strongest criteria are both checkable and exhaustive. End multi-step skills with an
explicit `Done when` list.

## Leading words

A **leading word** is a compact concept the model already holds from pretraining that
the agent thinks with while running the skill — `seam`, `tight` loop, `red`, `tracer
bullet`, `blast radius`. Repeat it as a token; it accumulates meaning across uses and
anchors a region of behaviour in very few tokens. It pays off twice, steering behaviour
in the body and improving triggering in the description, since the word already lives in
how I phrase my prompts.

Prefer a word already carrying the meaning in ordinary technical English, since a coined
word buys nothing until you spend tokens defining it. Record coined terms in
`CONTEXT.md`; hunt for restatements a single word would retire.

## Prompt the positive

Steering by prohibition drags the forbidden behaviour into context and makes it more
available — the ban half-reads as an instruction. State the target behaviour so the
unwanted one is never named: "write one-line comments" rather than "don't write long
comments". Reserve prohibition for hard guardrails, paired with the positive target.

## Human gates

Where the skill must not run ahead of me, say so in the imperative and name what
unblocks it:

- `Do not proceed until you have reproduced and minimised the failure.`
- `Show the ranked list before testing. Proceed with your own ranking if I am away.`

## Durability

Anything an agent will read later — a spec, a ticket, a handoff, a plan — describes the
code by its types and behaviours, never by source paths or line numbers, which rot between
the write and the read. Pointing at this repo's own conventional files is a context
pointer rather than a code reference, and is unaffected.

## Pruning

Skills degrade by accumulation, so removal is a standing task rather than a cleanup
phase. Each failure mode has a detectable tell:

- **No-op** — an instruction the model already obeys by default. The test is _does this
  change behaviour versus the default?_, which is model-relative: a disagreement about it
  is a disagreement about the default, settled by running the skill. Delete the whole
  sentence rather than trimming words from it.
- **Duplication** — one meaning in two places. Keep a single source of truth per
  meaning. Repeating a leading word is the deliberate opposite: the token repeats, the
  meaning is stated once.
- **Cache** — restating what the environment already says: `package.json` scripts,
  config files, `--help` output. Cache the unwritten convention, the reason behind a
  choice, the gotcha no config confesses; leave one-command lookups to the environment,
  where they cannot go stale.
- **Sprawl** — too long even when every line is live; hold `SKILL.md` under 500 lines.
  Cure it with the ladder rather than by trimming words.
- **Sediment** — guidance describing behaviour the repo no longer has. The tell is a
  claim that fails when checked against the filesystem or a run.

## Done when

A skill is finished when:

- The frontmatter carries nothing beyond the four allowed keys, and `name` matches the
  directory.
- A model-invoked skill either carries trigger phrasing for the agent or is named by
  another skill that invokes it; otherwise it is user-invoked.
- The description matches the invocation mode.
- Every sibling file's pointer states the condition for reading it.
- Every step has a checkable completion criterion, and every gate names what unblocks it.
- Coined vocabulary appears in `CONTEXT.md`.
- Every line passes the no-op test.
- It has been run against a real task and what the run exposed is folded back in. A
  skill that has never executed is a draft; say so rather than calling it done.

## Working agreements

- Plan before non-trivial work as checkable items, confirm the plan with me, and tick
  items off as they land.
- Discuss the reasoning behind guidance you add here before it becomes doctrine.
- Never commit or push unless I ask. Leave changes unstaged.
