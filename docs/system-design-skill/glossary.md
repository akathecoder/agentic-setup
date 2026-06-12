# Design Skill Glossary

## Language

**Design Skill**:
A user-facing skill for collaboratively designing a new software system or service before implementation begins.
_Avoid_: System design skill, architecture skill, design-system skill

**Design Packet**:
The packet-local `designs/<system-slug>/` folder of living design documents produced while using the **Design Skill**.
_Avoid_: Scratch docs, planning dump

**High Level Design**:
A system-level description of responsibilities, boundaries, external interactions, major components, and key flows.
_Avoid_: HLD-only spec

**Low Level Design**:
A focused design for one internal component, API contract, data model, algorithm, or operational behavior.
_Avoid_: Implementation notes

**Flow Document**:
A focused design document that uses Mermaid diagrams to explain a user journey, API interaction, sequence, state transition, or async workflow.
_Avoid_: Diagram dump

## Relationships

- The **Design Skill** produces a **Design Packet** before a new service is implemented.
- A **Design Packet** keeps context, plan, HLD, LLDs, schemas, flows, ADRs, open questions, and todos under one system-specific folder.
- A **High Level Design** describes the service in the larger system context.
- A **Low Level Design** details one part of the approved system direction.
- A **Flow Document** may support the **High Level Design** or a specific **Low Level Design**.

## Flagged ambiguities

- "Design doc" may mean the repo planning packet for this skill, or the design documents produced by the eventual skill. Resolved: this planning work lives in `docs/system-design-skill/`; the skill's own output structure is `designs/<system-slug>/`.
