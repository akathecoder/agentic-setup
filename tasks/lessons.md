# Lessons

- When planning a Confluence-writing skill, ask for and record the destination space/folder/page parent and required page-title convention before implementation.
- When planning skill work in this repo, create planning artifacts under `docs/<jira-ticket-or-context>/` with `links.md`, `glossary.md`, `todo.md`, optional `plan.md`, and `adr/` instead of scattering them across root-level `CONTEXT.md`, `tasks/todo.md`, and `docs/adr/`.
- When designing a design-only skill, do not assume it should proactively hand off to `plan`, `prototype`, or `build`; record that follow-on work happens only when the user explicitly asks.
- When the user explicitly renames a planned skill, update the planned skill folder, trigger wording, ADR, glossary, and supporting docs to match the user's chosen name even if an earlier name seemed less ambiguous.
- When a planned skill is intended for agent invocation rather than direct user use, record it as an internal skill and phrase the trigger around when an agent should invoke it.
