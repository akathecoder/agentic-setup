---
name: implement-ai-suggestions
description: Implement suggestions from a GitHub Copilot AI review comment or review on a pull request. Applies structured code suggestions and triages prose feedback. Use when the user provides a link to a Copilot review or comment and asks to implement, apply, or act on AI suggestions.
---

# Implement AI Suggestions

Take a link to a GitHub Copilot review or comment, fetch the suggestions, and implement the good ones locally. Skip suggestions that are invalid, low-quality, or would degrade the code.

## Input Parsing

Accept two URL formats:

1. **Individual comment**: `https://github.com/{owner}/{repo}/pull/{number}#discussion_r{comment_id}`
   - Extract `owner`, `repo`, `number`, and `comment_id` from the URL.
2. **Full review**: `https://github.com/{owner}/{repo}/pull/{number}#pullrequestreview-{review_id}`
   - Extract `owner`, `repo`, `number`, and `review_id` from the URL.

If the URL doesn't match either pattern, request a valid link in normal chat. This is free-form input, so do not force it through AskQuestion.

## Workflow

### Step 1: Verify Branch

Check that the current branch matches the PR's head branch:

```bash
gh pr view <number> -R {owner}/{repo} --json headRefName -q '.headRefName'
```

Compare against `git branch --show-current`. If they don't match, use the AskQuestion tool to warn the user and ask whether to continue:

> "Your local branch `<local branch>` doesn't match the PR branch `<pr branch>`. Do you still want to apply suggestions to your current branch?"

- **Yes**: Proceed with the implementation on the current local branch. Ignore the branch mismatch.
- **No**: Stop and tell the user: "Switch to the PR branch and try again."

### Step 2: Fetch Suggestions

**For an individual comment** (`discussion_r{comment_id}`):

```bash
gh api repos/{owner}/{repo}/pulls/comments/{comment_id}
```

This returns a single review comment object.

**For a full review** (`pullrequestreview-{review_id}`):

```bash
gh api repos/{owner}/{repo}/pulls/{number}/reviews/{review_id}/comments --paginate
```

This returns all inline comments belonging to that review.

### Step 3: Classify Each Comment

For each comment, examine the `body` field and classify:

**Structured suggestion**: The body contains a GitHub suggestion block:

````
```suggestion
replacement code here
```
````

These have exact replacement code. The suggestion replaces the lines the comment is attached to (from `start_line` to `line` in the file on the PR's HEAD, identified by `path`).

**Prose feedback**: The body contains a recommendation in natural language without a `suggestion` block (e.g., "Consider extracting this into a helper function" or "This could cause a null pointer dereference").

### Step 4: Triage

For each comment, decide: **implement** or **skip**.

**Structured suggestions** — default to implement. Skip only if:
- The suggestion introduces a clear bug or regression
- The suggestion contradicts established codebase patterns (read surrounding code to verify)
- The suggested code doesn't compile/parse (obvious syntax errors)

**Prose feedback** — evaluate each on merit by reading the relevant file and surrounding context:
- **Implement** if the feedback identifies a real issue (bug, security flaw, meaningful design improvement) and you can produce a concrete fix.
- **Skip** if the feedback is vague, purely stylistic with no codebase convention to anchor it, would require a large refactor beyond the PR's scope, or is simply wrong.

### Step 5: Implement

Process suggestions **one at a time**. For each suggestion you're implementing:

1. Read the target file at the relevant lines (use `path`, `start_line`, `line` from the comment).
2. Read surrounding context (imports, callers, related functions) to understand the impact.
3. Apply the change:
   - **Structured suggestion**: Replace lines `start_line` through `line` with the suggestion code.
   - **Prose feedback**: Write the fix using your judgment, keeping changes minimal and focused.
4. Verify the edit didn't break the file (no syntax errors in the immediate vicinity).

**Parallelism**: When multiple suggestions target **different files**, use subagents (Task tool) to implement them in parallel. When multiple suggestions target the **same file**, process them sequentially (later suggestions' line numbers may shift after earlier edits).

**Do not** stage or commit changes. Leave everything in the working tree.

### Step 6: Report

Present the results:

```
## Copilot Suggestions — PR #<number>

### Applied (<N>)

1. **`path/to/file.ts:L42`** — <brief description of the change>
2. **`path/to/other.ts:L17-L23`** — <brief description>

### Skipped (<N>)

1. **`path/to/file.ts:L88`** — "<original suggestion summary>" → **Reason**: <why it was skipped>
2. **`path/to/file.ts:L102`** — "<original suggestion summary>" → **Reason**: <why>
```

If all suggestions were applied, omit the Skipped section. If all were skipped, omit the Applied section and explain why.

## Guardrails

- Never auto-commit or auto-push. Changes stay unstaged in the working tree.
- Never modify files outside the paths referenced by the suggestions.
- When implementing prose feedback, keep changes minimal — fix the identified issue, don't refactor the neighborhood.
- Always report what was skipped and why. The user needs to see what was left on the table.
- If `gh` is not authenticated or fails, surface the error and suggest `gh auth login`.
- If no suggestions are found in the linked comment/review, say so and stop.
