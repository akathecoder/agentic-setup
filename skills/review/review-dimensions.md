# Review Dimensions

Prioritize findings by user impact and merge risk.

## Critical

Must address before merge:

- Correctness bugs.
- Security vulnerabilities.
- Data loss or corruption.
- Broken authorization or permissions.
- Race conditions or concurrency bugs.
- Unhandled failure modes in important paths.

## Suggestions

Should address when meaningful:

- Missing behavior tests for important paths.
- Design issues that increase coupling or make future changes risky.
- Performance issues such as N+1 queries, unbounded loops, missing pagination, or avoidable large allocations.
- Error handling that is incomplete but not immediately dangerous.
- Readability issues that obscure important behavior.

## Nitpicks

Optional:

- Naming or style issues that conflict with local conventions.
- Minor simplifications.
- Small consistency issues.

Do not pad the review with nitpicks. If the PR is clean, say so.

## Review Heuristics

For each changed area, ask:

- Can this break an existing caller or user flow?
- Are edge cases handled?
- Are errors observable and recoverable?
- Are permissions and trust boundaries preserved?
- Are tests checking behavior rather than implementation?
- Does the change fit the surrounding code's patterns?
- Is complexity hidden behind an appropriate interface?
