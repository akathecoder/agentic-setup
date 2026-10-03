---
name: grill-with-docs
description: Relentlessly interview a change or design while maintaining project docs.
disable-model-invocation: true
---

Run a `grilling` session using `domain-modeling` for the active project.

Maintain all artifacts under `<workspace-root>/.agents/projects/<project>/`. Resolve
the opened workspace root from session context; in a single-repository workspace it
is the repository root. Keep this root fixed when changing directories; never use
sub-repositories or global agent-installation directories. Capture confirmed facts,
terminology, tracker choice, relevant links, and reusable non-secret configuration
references in `CONTEXT.md` and `LINKS.md`; record qualifying architectural decisions
as project ADRs. Do not begin
implementation or create tickets during this skill.

Done when the user confirms that the design tree is resolved and the active project's
facts and decisions are captured.
