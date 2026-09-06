---
name: prototype
description: Throwaway prototype that answers a design question. Use when the user wants to sanity-check a state model or logic, or explore what a UI should look like.
argument-hint: "What design question should this prototype answer?"
---

# Prototype

A prototype is throwaway code that answers one design question. The question
decides the shape.

Resolve every `.agents/projects/` path from the repository root; never read or write
project artifacts in a global agent-installation directory.

## Pick a branch

Identify the question from the user's prompt, the surrounding code, or by asking:

- When the question is whether logic or a state model feels right, read `LOGIC.md`.
- When the question is what something should look like, read `UI.md`.

The two branches produce different artifacts. If the question is ambiguous and the
user is away, default from the surrounding code (a backend module → logic; a page or
component → UI) and state the assumption at the top of the prototype.

## Rules

1. **Throwaway and marked.** Put the prototype next to the module or page it is
   answering for. Name it so a casual reader can see it is a prototype. For a
   throwaway route, follow the project's existing routing convention.
2. **Trivial to run.** A UI prototype starts from one command in the project's task
   runner. A logic demo is a single HTML file the user opens.
3. **In-memory state.** Persistence is what a prototype checks, not what it depends
   on. When the question is about a database, use a scratch store named so it is
   obviously disposable.
4. **Runnable, not polished.** Skip tests, extra error handling, and abstractions.
5. **Surface the state.** After every action (logic) or on every variant switch (UI),
   show the full relevant state.
6. **Capture the answer.** Record the question and verdict in the active project's
   context, and on the tracker ticket when one exists. Fold the validated decision
   into the real code. Leave the prototype in the working tree; commit it to a
   `prototype/<name>` branch only when the user asks, so it remains a **primary
   source** off main.

## Done when

- The prototype answers the stated question and is trivial to run.
- When a verdict exists, it is recorded in project artifacts.
