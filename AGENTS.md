# AGENTS.md

This repository is the source of truth for my personal agent setup: the skills and
rules I install into every project I work on.

Authoring guidance is what every task here does, so the doctrine below applies
unconditionally and lives here rather than in a skill. Keep it under 275 lines.

## Portability

Skills follow the [Agent Skills spec](https://agentskills.io/specification): a
directory containing `SKILL.md` with YAML frontmatter. One `SKILL.md` serves every
harness, with no per-harness sidecars (`agents/openai.yaml`, `.claude/` variants).

**Plugins follow [Agent Plugins](https://agent-plugins.org/specification) 1.0.0.** A
plugin definition composes canonical skills (and optional MCP) without duplicating their
authorship. Build it into a self-contained distributable plugin: every packaged path,
including symlinks, resolves within that plugin root. Client-only behaviour lives under
reverse-domain namespaces (`extensions` and/or a top-level directory of that name), never
as portable top-level fields. MCP, when needed, is root `mcp.json` at the same schema
version as `plugin.json`.

**Cursor is the first-class harness.** Where a portable choice and a Cursor-specific
one conflict, take the portable one and note the Cursor behaviour beside it.

## Layout

```
skills/<skill-name>/SKILL.md   # canonical skill source; one directory per skill, flat
rules/<rule-name>.mdc          # canonical rules; see rules/AGENTS.md to write one
plugins/<plugin-name>/
  plugin.json                  # source manifest; $schema + name at minimum
  skills/<skill-name> -> …     # source selection symlink into skills/<skill-name>
  mcp.json                     # only when the plugin ships MCP
  <reverse-domain>/            # client extension sources, including client rules
dist/plugins/<plugin-name>/    # generated self-contained installable plugin
CONTEXT.md                     # leading-word glossary; read before naming a concept
```

Author skills and rules in their canonical trees. A plugin definition selects them by
symlink — never copy. The build copies selected content into `dist/plugins/`; do not
install a source definition. Plugin `name` matches its directory and the Agent Plugins
name constraints. Split plugins when install or enablement should be independent.

Skills still install by symlink into `~/.agents/skills/<name>`, rules into
`~/.cursor/rules/`, and plugins into the client's plugin root (prefer a harness-neutral
path under `~/.agents/` when allowed). The link script is not written yet; link manually.

## Where agent-authored files go

Everything an agent writes that is not source code goes under
`<repository-root>/.agents/projects/`, nested by **project** — a named workload that
may be narrower than the repo. Resolve the repository root before creating an artifact;
never create or read project artifacts from a global agent-installation directory such
as `~/.agents/`:

```
.agents/projects/<project>/
  CONTEXT.md           # what this project is; enough to re-orient next session
  LINKS.md             # Jira, Confluence, repos, and other refs for this project
  tasks/todo.md        # working plan for the current task
  tasks/lessons.md     # corrections from me, so a mistake stops recurring
  <name>.md            # research notes, handoffs, scratch analysis
```

Pick `<project>` from conversation context (ticket keys, Confluence links, what I said).
If I name one, use that; otherwise choose a short kebab-case slug and stay consistent.
When several project folders could fit and context does not settle it, ask me once.

**Local to the repository, not to the task.** Files under
`<repository-root>/.agents/projects/` persist across sessions so the next agent can
read `CONTEXT.md` and `LINKS.md` instead of re-asking. They are gitignored — they do
not travel through git history or onto other developers' machines. Do not delete them
when a task finishes; I remove a project folder when I am done with it. Moving an
artifact somewhere durable (`docs/`, an ADR directory, a committed spec) is my explicit
call and never a default. Add `.agents/` to the repo's `.gitignore` when it is missing.

The repo-root `CONTEXT.md` in _this_ authoring repo is a different file: the committed
leading-word glossary. A project's `CONTEXT.md` is uncommitted working memory for that
workload only.

This layout holds even where the repo already keeps plans or docs of its own, so a
skill behaves identically in every repo. A skill that produces an artifact names the
path shape `.agents/projects/<project>/…` in its own body, since it travels to repos
this file never reaches.

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
and encodes the condition for reaching it. The wording decides whether the agent gets
there — a miss is a bug in the description. Sharpen wording before touching the body.

A model-facing description names the skill's job, then lists the triggers:

```yaml
description:
  Diagnosis loop for hard bugs and performance regressions. Use when the
  user says "debug this", or reports something throwing, failing, or slow.
```

The trigger clause is always loaded, so prune it harder than the body:

- **Front-load the words that do the triggering.** Hold the job clause to a few words.
- **One trigger per branch.** Keep only genuinely distinct cases, not synonym renames.
- **Name the job, not the contents.** When to load is the description; what is the body.

A user-invoked skill's description is one line stating what it does, for a human list.

## Information hierarchy

Content sits on one of three rungs, ranked by how immediately the agent needs it:

1. **In-file step** — what the agent does, in order. The primary tier.
2. **In-file reference** — definitions and rules consulted on demand. A flat set of
   peers is a fine arrangement, not a smell.
3. **Disclosed reference** — a sibling file reached by a pointer, loaded only when the
   pointer fires.

**Progressive disclosure** is the move down that ladder; the test is **branching**:
inline what every run needs, disclose what only some runs reach. A skill forking between
two modes gives each mode its own file. The same test governs templates.

Sibling files are `UPPERCASE-KEBAB.md`, one level deep from `SKILL.md`, always pointed
at with the condition for reading them: `When the document is a skill, read
SKILL-MECHANICS.md for invocation choice.` A pointer without its condition cannot fire.

Flat siblings win over nesting under `references/` — one-word filenames stay one level
deep. Executables still go in `scripts/`, static templates in `assets/`.

**Co-locate** within a file: definition, rules, and caveats under one heading.

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

A **leading word** is a compact concept the model already holds from pretraining —
`seam`, `tight` loop, `red`, `tracer bullet`, `blast radius`. Repeat it as a token; it
anchors behaviour cheaply and improves triggering, since the word already lives in how
I phrase prompts. Prefer ordinary technical English; a coined word buys nothing until
defined. Record coined terms in `CONTEXT.md`; hunt for restatements one word would retire.

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

- **No-op** — an instruction the model already obeys by default. Test: _does this change
  behaviour versus the default?_ Settled by running the skill. Delete the sentence.
- **Duplication** — one meaning in two places. Single source of truth. Repeating a
  leading word is the deliberate opposite: token repeats, meaning stated once.
- **Cache** — restating what the environment already says (`package.json`, `--help`).
  Cache unwritten conventions and gotchas; leave one-command lookups to the environment.
- **Sprawl** — too long even when every line is live; hold `SKILL.md` under 500 lines.
  Cure with the ladder, not word-trimming.
- **Sediment** — guidance for behaviour the repo no longer has. Tell: claim fails against
  the filesystem or a run.

## Done when

A skill is finished when:

- The frontmatter carries nothing beyond the four allowed keys, and `name` matches the
  directory.
- A plugin that ships it has valid `plugin.json` (Agent Plugins 1.0.0) and a
  self-contained built package containing the skill under `skills/`.
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
