---
name: improve-codebase-architecture
description: Scan a codebase for deepening opportunities, present a visual architecture report, then grill through a selected candidate.
disable-model-invocation: true
---

# Improve Codebase Architecture

Surface architectural friction as **deepening opportunities**: refactors that turn
shallow modules into deep ones. Use the `codebase-design` vocabulary throughout and
respect the active project's domain language and ADRs.

## Process

1. Scope before scanning. Use a direction named by the user, or inspect a useful span
   of commit history to identify recently changing hot spots. Read
   `.agents/projects/<project>/CONTEXT.md` and relevant project ADRs, then explore the selected
   area for shallow modules, leaking seams, poor locality, and interfaces that resist
   behavior-focused tests. Apply the deletion test to every candidate.

   Done when candidates are grounded in real friction in the selected code area.

2. Read `HTML-REPORT.md` before presenting candidates. Record the candidate data in
   `.agents/projects/<project>/architecture-review.md`. When running in Cursor with its visual
   Canvas capability available, create a Canvas using the same report structure,
   candidate cards, diagrams, and recommendation strengths. Prefer Canvas over HTML.
   Otherwise create a self-contained HTML report at
   `.agents/projects/<project>/architecture-review-<timestamp>.html` and tell the user its
   absolute path. Do not propose interfaces yet.

   Done when the user can compare a visual report whose candidate data is preserved in
   the active project artifacts.

3. Ask the user which candidate to explore. Run `grilling` and `domain-modeling` to
   work through its constraints, dependencies, module shape, seam, hidden behavior,
   and surviving tests. Update project context inline as language or facts crystallize.
   Offer a project ADR only for a durable, surprising trade-off. When the user wants to
   compare interfaces, use `codebase-design` and its `DESIGN-IT-TWICE.md` process.

   Done when the selected candidate has a shared design understanding or a recorded
   reason not to pursue it.
