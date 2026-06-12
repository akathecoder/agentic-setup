# Publish Sequentially And Stop On First Failure

When multiple local source files are approved for publication, `publish-confluence` should publish them sequentially and stop on the first failure. The completion report should list completed pages, the failed operation, the MCP error, and the remaining unpublished files.

## Consequences

The skill avoids hiding partial failures behind parallel operations. The user can explicitly ask to continue after reviewing the failure.
