# akathecoder's Agentic Setup

This repository is the source of truth for reusable agent skills, Cursor rules, and
installable plugins. It can contain multiple independent plugins; each plugin selects
the skills and client-specific extensions it needs.

## Contents

- `skills/` - Canonical portable skill sources.
- `rules/` - Canonical Cursor rule sources.
- `plugins/` - Source definitions that select skills and client extensions for a
  plugin.
- `dist/plugins/` - Generated self-contained packages for installation.

## Available Plugins

- [CodeForge](./plugins/codeforge/README.md) - Engineering planning, implementation,
  review, ticketing, and documentation workflows.

## Installing Individual Skills

Install selected skills into a supported coding agent with:

```bash
npx skills@latest add akathecoder/agentic-setup
```

The installer lets you choose skills and a target harness. Consult the target agent's
documentation for its installation and configuration steps.

## Development

Plugin packages are generated from explicit source selections. Build and validate them
before publishing changes:

```bash
python3 scripts/build_plugins.py
python3 scripts/build_plugins.py --check
git diff --check
```

`--check` fails when `dist/plugins/` does not match the canonical skill, rule, and
plugin sources. CI runs the same check.
