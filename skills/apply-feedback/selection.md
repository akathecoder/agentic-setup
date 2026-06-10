# User Selection

After triage, ask the user which items to fix. Do not edit before this step.

Use `AskQuestion` when the list can be represented as structured choices. Allow multiple selections.

Recommended default:

- Preselect or recommend all **Genuine issue, must fix** items.
- Include **Good issue, optional** items as selectable.
- Do not recommend **Wrong issue, ignore** items.

If there are many items, group them by category and file before asking.

## Selection Prompt

Ask:

```text
Which feedback items should I fix now?
```

Options should include item number, category, file, and short summary.

If the user selects an item categorized as wrong, confirm before implementing and explain the risk.

## After Selection

Fix only selected items. Report all unselected items as skipped with their category and reason.
