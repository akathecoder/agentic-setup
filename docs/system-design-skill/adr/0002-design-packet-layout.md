# Use Packet-Local `designs/<system-slug>/` Artifacts

The `design` skill should create and maintain design artifacts under `designs/<system-slug>/`. This preserves the user's requested design-oriented structure while avoiding a global root `CONTEXT.md` that becomes ambiguous when a repository has multiple active designs.

## Design Packet Shape

```text
designs/<system-slug>/
├── context.md
├── design_plan.md
├── adr/
├── flows/
├── hld.md
├── lld/
├── schemas/
├── open_questions.md
└── todo.md
```

## Consequences

The skill should treat `designs/<system-slug>/design_plan.md` as the primary file the user references most often. Supporting files should hold details that would make the primary plan too large or too noisy.

The skill should create core tracking files at the start of a design session and create detailed HLD, LLD, schema, flow, and ADR files only when there is real design material to record.
