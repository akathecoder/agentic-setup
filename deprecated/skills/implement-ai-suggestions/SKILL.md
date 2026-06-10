---
name: implement-ai-suggestions
description: Deprecated Copilot-only feedback implementation skill preserved for reference. Use `apply-feedback` for current work.
---

# Deprecated: Implement AI Suggestions

This skill has been absorbed into `skills/apply-feedback`.

The original workflow fetched GitHub Copilot review comments, separated structured suggestions from prose feedback, applied acceptable suggestions, skipped bad suggestions, and left changes unstaged. The current `apply-feedback` skill broadens this to humans, Bugbot, Copilot, AI reviewers, GitHub comments, pasted findings, and Review output, with triage and user selection before any fix.
