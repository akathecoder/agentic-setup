---
name: handoff
description: Use when the user wants to compact the current conversation into a handoff document for another agent to pick up.
argument-hint: "What will the next session be used for?"
---

Write a handoff document summarising the current conversation so a fresh agent can continue the work. Save it to a path produced by a context-driven `mktemp` prefix: first derive a short lowercase hyphenated slug from the user's focus or current task, then run `mktemp -t "handoff-${slug}.md"` (read the file before you write to it). Do not use a literal placeholder like `handoff-XXXXXX.md` as the human-readable part of the filename.

Suggest the skills to be used, if any, by the next session.

Do not duplicate content already captured in other artifacts (PRDs, plans, ADRs, issues, commits, diffs). Reference them by path or URL instead.

If the user passed arguments, treat them as a description of what the next session will focus on and tailor the doc accordingly.
