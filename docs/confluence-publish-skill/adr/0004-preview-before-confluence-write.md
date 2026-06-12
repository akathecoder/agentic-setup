# Require Preview Before Confluence Writes

The `publish-confluence` skill must show a Confluence approval preview before any write-capable Atlassian MCP call. The preview should list each local file, target operation, target ID/title/space/parent, selected content format, single-page invariant, body summary or diff, version message, and unresolved questions.

Only an explicit publish approval authorizes the publishing subagent to write to Confluence.

## Consequences

Reviewing the local file, draft body, or target summary is not approval to publish. If the user asks for revisions, the skill must update the preview and ask again.
