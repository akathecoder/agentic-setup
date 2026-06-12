# Default To Markdown Content Format

The `publish-confluence` skill should default to `contentFormat: markdown` for Markdown-heavy local documentation. Use `contentFormat: html` only when the user explicitly needs richer Confluence formatting or round-trip fidelity.

## Consequences

The skill should avoid inventing conversion logic for normal Markdown files. Approval previews must state the selected content format, especially when publishing HTML.
