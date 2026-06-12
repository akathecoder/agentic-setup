# Use Composer 2.5 As A Bounded Publishing Executor

The main agent owns high-level thinking, user interaction, target reasoning, approval previews, and final reporting. After explicit approval, a Composer 2.5 publishing subagent may read MCP schemas, fetch current Confluence state, perform only the approved Confluence create or update operations, and return URLs, results, and errors.

The subagent must not change scope, ask user questions, split documents, choose targets, or write unapproved content.

## Consequences

Approval context must be complete before launching the publishing subagent. The subagent prompt must include the exact approved operation list and must forbid any extra writes.
