# Modern Go Guidelines

Source: https://github.com/JetBrains/go-modern-guidelines

Read the README **Instructions** section for the current harness. Commands live
there. This file is the rest.

## Prerequisite

Marketplace and plugin installs run a CLI via `go install` into
`~/.cache/go-modern-guidelines`. Need Go 1.25+ on `PATH`, or an older Go with
`GOTOOLCHAIN=auto`. The skills.sh skill `use-modern-go` uses the same CLI when
it runs.

## Form by harness

| Harness | Form | Agent can finish? |
| --- | --- | --- |
| Cursor | plugin `modern-go-guidelines` on `goland-cursor-marketplace` | No. After marketplace add, the user runs `/plugins` in a Cursor session and installs it. |
| Claude Code | plugin `modern-go-guidelines@goland-claude-marketplace` | `/plugin` is in-session. Use the `claude plugin` CLI from the README when it covers the same install; otherwise gate. |
| Codex | plugin on `goland-codex-marketplace` via `codex plugin` | Yes. |
| Junie | extension `modern-go-guidelines` | `/extensions` is in-session. Gate. |
| skills.sh (Grok, OpenCode, others) | skill `use-modern-go` | Yes. `--skill use-modern-go`; project is default, `-g` for global, `-y` once scope is known. |

Cursor marketplace add takes the GitHub URL, not `owner/repo`.

## Gates

Name the command and wait. Unblocks when the user confirms it ran.

- Cursor: `/plugins` → install `modern-go-guidelines`
- Claude Code: `/plugin marketplace add` and `/plugin install`, unless the CLI path was used
- Junie: `/extensions marketplace add` and `/extensions install`

## Scope

Cursor, Claude Code, and Junie marketplace installs are user-global. If scope
is project, say so and offer the skills.sh skill `use-modern-go` (project is
the default) or switch scope to global.
