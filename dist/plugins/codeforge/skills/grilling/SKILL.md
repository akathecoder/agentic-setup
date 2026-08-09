---
name: grilling
description: Relentless decision interview. Use when a plan, design, or idea needs its unresolved decisions stress-tested, or when a planning skill needs to reach shared understanding before acting.
---

# Grilling

Interview the user until you reach a shared understanding. Map the topic as a
**design tree**: every decision branches into the decisions that hang off it.

## Process

1. Identify the active project. Read `.agents/projects/<project>/CONTEXT.md` and `LINKS.md`
   when they exist. Inspect the repository for facts; do not ask the user for facts
   that the environment can establish.

   Done when known facts and unresolved decisions are distinct.

2. Work the tree in **rounds**. The **frontier** is every decision whose prerequisites
   are settled. Ask the whole frontier in one numbered round, with a recommended
   answer for each question. Do not ask a question whose answer depends on another
   open question in the round.

   ```md
   **Q1 - Question title:** Question body and choices.

   Recommended: Recommended answer.
   ```

   Done when the user has answered the current frontier.

3. Recompute the frontier after each response. Record confirmed project facts,
   tracker choices, reusable non-secret configuration references, terminology, and
   links in the active project's context as they become known. Record durable
   technical decisions separately only when they meet the ADR test in
   `domain-modeling`.

   Done when every newly settled decision is captured in the appropriate project
   artifact.

4. End when the frontier is empty. Summarize the shared understanding and wait for
   the user's confirmation before taking action based on it.

   Done when the user confirms the understanding.
