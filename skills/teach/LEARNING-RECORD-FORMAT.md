# Learning Record Format

Learning records live in `learning-records/` as `NNNN-slug.md`. Create the
directory when writing the first record. Scan for the highest existing number and
increment.

They capture non-obvious lessons, key insights, and stated prior knowledge that
steer future sessions and the zone of proximal development.

```md
# {Short title of what was learned or established}

{1-3 sentences: what was learned (or what prior knowledge was established), and
why it matters for future sessions.}
```

A learning record can be a single paragraph.

## Optional sections

Include these only when they add value:

- **Status** (`active` or `superseded by NNNN`): when an earlier understanding is
  replaced.
- **Evidence**: how the user demonstrated the understanding.
- **Implications**: what this unlocks or rules out next.

## When to write one

1. The user demonstrated genuine understanding of something non-trivial.
2. The user disclosed prior knowledge, including the depth claimed.
3. A misconception was corrected.
4. The mission shifted. Update `MISSION.md` and cross-link.

Coverage is not learning. Wait for evidence. Do not duplicate a glossary
definition. These are not session logs.

When a later record contradicts an earlier one, mark the old record superseded
rather than deleting it.
