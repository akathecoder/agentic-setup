# Add a catalog entry

Write new rows into `catalog.yaml` in this skill's directory. Write a **guide**
under `guides/` in the same directory exactly when `npx-skills` is false.

## Process

1. Fetch the source. Set `type` to the forms it publishes: `skill` when a
   `SKILL.md` or `skills/*/SKILL.md` exists; `plugin` when a Cursor, Claude, or
   Codex plugin manifest exists; `extension` when a Junie extension manifest
   exists.

   Done when `type` lists every published form.

2. If `type` is only `skill` and the source installs with `npx skills add`, set
   `npx-skills: true` and write no guide. Otherwise set `npx-skills: false` and
   write `guides/<id>.md` as deltas on the source's install docs:
   prerequisites, human gates, scope limits, and ids that differ by harness.
   Leave the commands in the source docs.

   Done when the YAML row is complete and a guide exists exactly when
   `npx-skills` is false.

3. Append the entry to `catalog.yaml`. Show the row and any guide path. Install
   only when the user also asked to install.

   Done when the catalog contains the entry and the user has the `id`.

Remove deletes the YAML row and its guide.

## catalog.yaml

```yaml
entries:
  - id: example
    name: Example
    type: [skill, plugin, extension]
    source: owner/repo
    npx-skills: false
    guide: example.md
```

`guide` is omitted when `npx-skills` is true. `id` is the picker key and the
guide filename stem. `source` is GitHub `owner/repo` or a URL. One entry per
source. `type` is the list of published forms.
