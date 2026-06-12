# Use Contextual Target Resolution

The `publish-confluence` skill should interpret a user-provided Confluence ID based on context. If the ID resolves as an existing page and the user asked to update, update that page. If the ID represents a folder, parent, or container and the user asked to publish under it, create exactly one new page under that target. If the target role is ambiguous, stop and ask before writing.

## Consequences

The skill must fetch or inspect target metadata before write approval when needed. Approval previews must state whether the operation will update an existing page or create one new page under a parent/container.
