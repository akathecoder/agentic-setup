# Keep `publish-confluence` In One Skill File

The `publish-confluence` skill should be implemented as a single `SKILL.md` rather than split into supporting files. The user explicitly chose this shape for the first version.

## Consequences

The implementation should keep the file concise despite covering workflow, target resolution, approval preview, publishing, subagents, and guardrails. Supporting files can be introduced later only if the skill grows too large or becomes difficult to maintain.
