# Design Intake

## Intake Rule

Before proposing architecture, gather the required context. First extract everything available from the user's prompt into `context.md`, then ask one focused follow-up question at a time for missing required context.

Do not force the user to fill a rigid form when the initial prompt already contains usable information.

## Required Before Design

The skill must know:

- Service intent.
- Service responsibilities.
- Where the service is used in the larger system.
- What is in scope for this service.
- What is out of scope because another service owns it.
- What is in scope for this design discussion.
- What is out of scope for this design discussion.
- Existing constraints.
- Must-haves.
- Must-avoids.

If one of these is unknown, ask about it before making design proposals.

## Optional But Valuable

Capture these when available, but do not block forever on them:

- Initial user ideas and plans.
- Basic designs or sketches.
- Good-to-haves.
- Known risks.
- Expected traffic, scale, latency, availability, consistency, compliance, security, or operational needs.
- Existing systems, APIs, events, tables, queues, or clients that may interact with the new service.

## `context.md` Structure

Use this structure and keep it current:

```md
# <System Name> Context

## Intent

## Responsibilities

## Larger System Context

## Service Scope

### In Scope

### Out of Scope

## Design Discussion Scope

### In Scope

### Out of Scope

## Existing Constraints

## Must-Haves

## Must-Avoids

## Good-to-Haves

## User Ideas And Early Sketches

## Notes
```

Use `Unknown` for a required section only temporarily, and add a matching question to `open_questions.md`.
