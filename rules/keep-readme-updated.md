# Rule: Keep README Up to Date

## Purpose

The README is the canonical entry point for any developer working in this project. It must always reflect the current state of the codebase — not aspirational docs, not stale instructions.

## When This Rule Applies

Update the README whenever you make a change that affects:

- **Setup / installation**: new dependencies, changed env vars, updated prerequisites, Docker/container changes
- **Running the project**: changed commands, scripts, entrypoints, or dev server config
- **Architecture**: new modules, services, or major structural changes
- **APIs or interfaces**: new CLI flags, HTTP endpoints, exported functions, config file formats
- **Tooling**: new linters, formatters, build tools, CI steps, or test runners
- **Contributing workflow**: branching strategy, PR process, code style enforcement changes

Do NOT update the README for:
- Internal refactors that don't change the developer-facing surface
- Bug fixes that don't change behavior observable from outside the code
- Test-only changes

## Required Behavior

1. **Read the current README first** before modifying it. Never overwrite content blindly.

2. **Update the relevant section only** — don't restructure the whole file unless the user asks. Surgical edits over wholesale rewrites.

3. **Keep it developer-focused**:
   - Lead with how to get the project running (`clone → install → run`)
   - Document commands, not concepts — show the actual shell commands
   - Prefer code blocks over prose for anything a dev would copy-paste
   - Skip marketing language, mission statements, and business context unless the user explicitly includes them
   - No "Why we built this" sections unless asked

4. **Accuracy over completeness**: A short, correct README is better than a long, outdated one. Remove stale instructions rather than leaving them.

5. **Format conventions**:
   - Use fenced code blocks with language tags for all commands and config samples
   - Use `##` sections (not `###`) for top-level groupings: Setup, Usage, Configuration, Development, Testing, Deployment
   - Keep the Getting Started / Quick Start section as the first substantive section after any one-liner description

## Example Triggers

| Change made | README update needed |
|---|---|
| Added `REDIS_URL` env var | Add to Configuration / Environment Variables section |
| Renamed `npm run dev` to `npm run start:dev` | Update the run command in Usage/Setup |
| Extracted auth into a separate service | Update Architecture section (or add one) |
| Added Prettier + lint-on-commit hook | Add to Development / Contributing section |
| Refactored internals with no interface change | No update needed |

## Exceptions

- Skip if the user explicitly says not to update the README for the current change.
- Skip if there is no README in the project and the change is minor — but consider creating one if the project is substantive enough.
- If the README is auto-generated (e.g., from a doc tool), update the source instead and note that to the user.
