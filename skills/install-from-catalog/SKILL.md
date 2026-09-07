---
name: install-from-catalog
description: Install a catalogued third-party skill, plugin, or extension, or add a source to the catalog.
disable-model-invocation: true
argument-hint: "Which catalog entry to install, or a source URL to add?"
---

# Install From Catalog

Install a **catalog entry** into the current workspace or the user's agent dirs,
or add a **source** to the catalog. Read `catalog.yaml` in this skill's
directory (the directory that contains this file). When an entry names a
**guide**, read `guides/<guide>` in the same directory. Install through the
source's published path for this harness.

When the conversation names a catalog `id` or `name`, install that entry. When
it names a source URL absent from the catalog, or asks to add, read `ADD.md`.
Otherwise list the catalog (`id`, `name`, `type`, npx-skills or guide) and wait
for a pick.

**Scope** is project or global. Use it when this conversation already named one;
otherwise ask. Do not install until scope is known.

## Process

1. Read `catalog.yaml` and resolve the entry.

   Done when `id`, `name`, `type`, `source`, and `npx-skills` are known, and
   `guide` is known when `npx-skills` is false.

2. Resolve **scope**. Detect the current harness from the running agent and its
   CLIs (`cursor-agent`, `claude`, `codex`, Junie). When none match, the
   harness is skills.sh. Choose the form in `type` this harness understands:
   plugin for Cursor, Claude Code, or Codex; extension for Junie; skill for
   skills.sh. If `type` has no form for this harness, say so and stop.

   Done when scope and the install form are known, or the harness is unsupported
   for this entry.

3. If `npx-skills` is true, run `npx skills add <source>` with `-y`. Add `-g`
   when scope is global; project is the installer default. Add `--skill <name>`
   when the catalog or source names one skill in a multi-skill repo.

   Done when the installer has finished and the skill is listed for that scope.

4. If `npx-skills` is false, fetch the source's current install docs for this
   harness and read `guides/<guide>`. Follow the docs; apply the guide's
   deltas (prerequisites, human gates, scope limits, ids that differ by
   harness). Run every step this agent can run. For a step only the user can
   perform, stop and name the command or UI action. Do not proceed until the
   user confirms it is done.

   Done when every step on this harness's path has been run or confirmed.

5. Check that the capability is present: the harness's list command, the
   installer's output, or the user's confirmation of a gate. Tell the user what
   landed and where.

   Done when presence is confirmed or the failure is reported with the next
   action.

If the chosen form cannot honour **scope**, say so and ask again. Offer a form
from `type` that can, when one exists.

## Done when

The chosen entry is present for this harness and scope, or a named gate is
waiting on the user.
