# CONTEXT.md

The glossary of **leading words** shared across the skills and rules in this
repository. One term per concept: when a skill needs one of these meanings, it uses
the word below rather than a synonym, so the vocabulary compounds instead of
fragmenting.

Add a term here when a skill coins one. Where a term has near-synonyms that invite
drift, `Avoid:` names them.

## Authoring vocabulary

**Project**
A named workload under `<repository-root>/.agents/projects/<project>/`, possibly
narrower than the git repo. All agent-authored files for that workload live there,
including its own `CONTEXT.md` and `LINKS.md`; never in a global agent-installation
directory. The slug is kebab-case; I may name it, otherwise the agent chooses from
conversation context and stays consistent.
_Avoid_: workstream, initiative (when meaning this folder)

**Project context**
The uncommitted `<repository-root>/.agents/projects/<project>/CONTEXT.md` — working
memory for that workload so a later session can re-orient without re-asking. Distinct
from this file (the committed leading-word glossary at the authoring-repo root).

**Context pointer**
A reference held in the agent's context that names material outside it and encodes
the condition for reaching it. A skill's `description` is one; so is a line in
`AGENTS.md` naming a doc. The wording, not the target, decides whether the agent
reaches the material.
_Avoid_: hook

**Trigger**
The part of a model-facing `description` that states when to fire the skill, as
distinct from the **context pointer** as a whole. One trigger per **branch**.

**Context load**
The cost of always-loaded material on the agent's context window — skill
descriptions, `AGENTS.md`, `alwaysApply: true` rules. Paid every turn whether the
material fires or not.
_Avoid_: token cost, overhead

**Cognitive load**
The cost on me: which skills exist and when to reach for each. What a user-invoked
skill spends instead of context load.

**Invocation**
Who can reach a skill. **User-invoked** means only I can run it by name;
**model-invoked** means the agent can fire it and other skills can reach it.
_Avoid_: auto-invocation, discovery, activation

**Information hierarchy**
The three rungs content sits on, ranked by immediacy: in-file step, in-file
reference, disclosed reference.

**Reference**
Content consulted on demand rather than executed in order — the second and third
rungs of the **information hierarchy**, and the name of the skill shape that consists
entirely of it. Contrast **step**.

**Progressive disclosure**
The move down the information hierarchy — out of `SKILL.md` and behind a context
pointer — so the top of the file stays legible.

**Co-locate**
To keep a concept's definition, rules, and caveats under one heading rather than
scattered across a file. The within-file companion to progressive disclosure, which
decides how far down a piece sits rather than what sits beside it.

**Branching**
The test that decides disclosure: inline what every run needs, disclose what only
some runs reach. A **branch** is a distinct case a document handles, so different
runs take different paths through it.

**Completion criterion**
The condition telling the agent a step is done. Graded on **clarity** (can it tell
done from not-done?) and **demand** (how much it requires).
_Avoid_: acceptance criteria, exit condition, definition of done

**Legwork**
The digging an agent does inside a step, driven by the demand latent in the step's
wording rather than written as its own step.

**Leading word**
A compact concept the model already holds from pretraining, repeated as a token so
it accumulates meaning and anchors a region of behaviour cheaply.

**Gate**
A point where a skill stops and waits for me. Every gate names what unblocks it.
_Avoid_: checkpoint, approval step, HITL

**Done when**
The named list of completion criteria closing a multi-step skill.
_Avoid_: definition of done, acceptance criteria, exit checklist

## Skill shapes

**Delegator**
A skill of a few lines whose whole body hands off to another skill.

**Process**
A skill of numbered phases with **gates**. The longest shape.

**Reference skill**
A skill that is entirely **reference** — a glossary or rule set consulted rather than
run. The usual legitimate reason for a skill to be model-invoked, since other skills
must be able to reach it.

## Pruning failure modes

Each names a distinct way a document decays, with a detectable tell:

**No-op**
An instruction the model already obeys by default, paying context to say nothing.

**Duplication**
One meaning in two places. The deliberate opposite of a leading word, which repeats
the token and never the meaning.

**Cache**
A restatement of something the environment already says (`package.json`, `--help`,
the directory layout). Earns its load only when the lookup is expensive.

**Sprawl**
A document too long even when every line is live and unique.

**Sediment**
Guidance describing behaviour the repo no longer has. The tell is a claim that fails
when checked against the filesystem or a run.

## Relationships

- A **project** owns `<repository-root>/.agents/projects/<project>/`; its **project
  context** is not this glossary.
- A **context pointer** guards a **disclosed reference**; its wording decides how
  reliably the agent reaches it.
- **Invocation** decides which load a skill spends: model-invoked spends **context
  load**, user-invoked spends **cognitive load**.
- **Branching** is the test; **progressive disclosure** is the move it authorises.
- **Demand** in a **completion criterion** is what produces **legwork**.
