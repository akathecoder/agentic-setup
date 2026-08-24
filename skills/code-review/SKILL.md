---
name: code-review
description: Review a diff since a fixed point against repository standards and its originating project spec or ticket. Use for a branch, pull request, work-in-progress changes, or when an implementation workflow needs final review.
---

# Code Review

Review the diff between `HEAD` and a fixed point along two independent axes:

- **Standards**: does the change follow documented repository standards and the smell
  baseline below?
- **Spec**: does the change faithfully implement its originating local spec or tracker
  ticket?

Run the axes in parallel and preserve the separation when reporting results.

Resolve every `.agents/projects/` path from the repository root; never read or write
project artifacts in a global agent-installation directory.

## Process

1. Determine the fixed point from the user or the invoking implementation workflow.
   Validate it resolves, capture `git diff <fixed-point>...HEAD`, list its commits,
   and stop if the diff is empty.

   Done when a non-empty, merge-base diff is available.

2. Identify the active project and its source specification in this order: an issue
   reference in the commits, a supplied reference, `.agents/projects/<project>/spec.md`, then
   a matching project artifact. Fetch the full tracker body and comments when needed.
   If no spec exists, mark the Spec axis unavailable rather than inventing one.

   Done when the review has a spec source or an explicit no-spec status.

3. Identify repository standards in existing guidance such as `AGENTS.md`,
   `CLAUDE.md`, `CONTRIBUTING.md`, and coding-standard documents. Apply those before
   the smell baseline. The baseline is heuristic only and never overrides a documented
   repository decision or tooling that already enforces the rule.

   Baseline: mysterious names, duplicated code, feature envy, data clumps, primitive
   obsession, repeated switches, shotgun surgery, divergent change, speculative
   generality, message chains, middle man, and refused bequest.

   Done when standards sources and applicable heuristics are available to the review.

4. Launch two independent reviews in parallel:

   - **Standards**: report documented-standard violations with the source rule and
     file/hunk, then possible baseline smells with quoted evidence. Separate hard
     violations from judgement calls.
   - **Spec**: report missing or partial requirements, scope creep, and apparently
     implemented but incorrect behavior. Cite the relevant spec requirement.

   Done when each axis returns a concise, evidence-based report, or the Spec axis
   explicitly reports that no spec is available.

5. Write `.agents/projects/<project>/review.md` with `## Standards` and `## Spec` sections.
   Do not merge or rerank their findings. End with the number of findings and worst
   issue within each axis. If a tracker comment is needed, append `Written by Cursor`;
   do not add that line to the local review document.

   Done when the project has a two-axis review report and the user can distinguish
   standards findings from specification findings.
