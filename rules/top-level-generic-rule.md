# agents.md

This file provides guidance to the AI coding agent when working with code in this repository.

## Planning

Enter plan mode for any non-trivial task (3+ steps or architectural decisions). Write detailed specs upfront to reduce ambiguity. If something goes wrong, stop and re-plan immediately — don't keep pushing. Use plan mode for verification steps, not just building.

## Subagents

Use subagents to keep the main context window clean. Offload research, exploration, and parallel analysis to subagents. For complex problems, use more subagents. Assign one focused task per subagent.

## Task Management

1. Write the plan in `tasks/todo.md` with checkable items before starting
2. Confirm the plan before implementing
3. Mark items complete as you go
4. Provide a high-level summary at each step
5. Add a review section to `tasks/todo.md` when done
6. After any correction from the user, update `tasks/lessons.md` with the pattern — write a rule to prevent repeating the same mistake

## Verification

Never mark a task complete without proving it works. Run tests, check logs, and demonstrate correctness. Diff behavior between main and your changes when relevant.

## Bug Fixing

When given a bug report: just fix it. Use logs, errors, and failing tests to diagnose. Fix failing CI automatically. Require zero context switching from the user.

## Code Quality

For non-trivial changes, ask: "Is there a more elegant solution?" If a fix feels hacky, step back and implement the right solution. Skip for simple fixes — don't over-engineer. Make every change as simple as possible and minimize code impact. Find root causes; avoid temporary fixes.
