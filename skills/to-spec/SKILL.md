---
name: to-spec
description: Turn the current project discussion into a local and tracker-published spec.
disable-model-invocation: true
---

# To Spec

Synthesize the current conversation, active project artifacts, and codebase
understanding into a specification. Do not interview the user; use `grill-with-docs`
when decisions remain unresolved.

Resolve every `.agents/projects/` path from the repository root; never read or write
project artifacts in a global agent-installation directory.

## Process

1. Identify the active project and read `.agents/projects/<project>/CONTEXT.md`, `LINKS.md`,
   relevant ADRs, and existing specs. Explore the current codebase where necessary.

   Done when the spec uses confirmed project language and respects relevant decisions.

2. Sketch the seams at which the feature will be tested. Prefer the highest existing
   seam; propose a new seam only when necessary. Check that the seams meet the user's
   expectations before proceeding.

   Done when the user has confirmed the test seams.

3. Write `.agents/projects/<project>/spec.md` using this structure. Do not include source
   paths or ordinary code snippets, which become stale; a trimmed prototype-derived
   state machine, reducer, schema, or type shape is allowed when it captures a
   decision more precisely than prose.

   ```md
   # Spec Title

   ## Problem Statement
   ## Solution
   ## User Stories
   ## Implementation Decisions
   ## Testing Decisions
   ## Out of Scope
   ## Further Notes
   ```

   User stories are an extensive numbered list in the form: "As an <actor>, I want
   <feature>, so that <benefit>."

   Done when the local spec fully captures the agreed problem, behavior, decisions,
   tests, and boundaries.

4. Publish the same spec to the tracker recorded in project context: Jira by default,
   or GitHub Issues when the user requested it or Jira is unavailable. Use available
   authenticated tooling; otherwise produce a ready-to-paste version and record the
   limitation. Update `CONTEXT.md` and `LINKS.md` with the tracker identifier and URL.
   Add `Written by Cursor` only if publishing also creates a conversational comment.

   Done when both the local spec and its tracker representation are available, or the
   ready-to-paste fallback and limitation are recorded.
