# Make `publish-confluence` Agent-Invoked And Internal

The `publish-confluence` skill is not intended to be invoked directly by the user. It should be invoked by an agent when that agent needs to publish local documentation to Confluence using a bounded publishing subagent.

## Consequences

README should classify `publish-confluence` as an internal skill. The trigger description should focus on agent invocation, local documentation publication, Atlassian MCP, and one Confluence page per source file.
