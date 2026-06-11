# CMR Tickets

Use this workflow for Change Management Review tickets under `CMR`. These tickets track release readiness after a feature is built and before production release approval.

## Purpose

CMR tickets should help stakeholders approve a production release by making the blast radius, rollout plan, monitoring, incident readiness, and unresolved risks explicit.

## Section Rule

Treat the template below as a candidate section list, not a fixed final description.

- Include a section only when it applies to the release.
- Omit a heading entirely when that point is not applicable.
- Ask the user when applicability is unclear.
- Do not write `NA` as filler unless the user explicitly asks for that wording.
- In the approval preview, show both sections to add and sections to omit.

## Information To Collect

Ask for missing facts that are not already present in the base ticket, linked feature tickets, docs, PRs, dashboards, comments, or user-provided context.

- Feature ticket links and PR links
- Release scope and services touched
- Customer touchpoints and expected impact
- Service, infra, database, queue, cache, config, and secret dependencies
- Downstream services and RED metrics to monitor
- Internet-exposed endpoint changes
- Rollout type and planned rollout dates
- Dashboard, alert, incident channel, and Slack channel links
- Critical application workflows and tech metrics to monitor
- New alert or logging needs
- Recent Sev0/Sev1 incident status and RCA status
- Known issues, scaling gaps, or accepted release risks

## Candidate Description Template

Assemble the final Jira description from only the applicable sections.

```markdown
## Change Summary

### Change Description / Scope

[Define the full scope of the CMR. Include feature ticket links, PR links, services touched, and what is being deployed.]

### Customer Touchpoints Impacted

**Positive impact:** [What improves for customers, internal users, ops, support, or other stakeholders.]

**Negative impact / risk:** [Possible degradation, behavior change, downtime, latency, user confusion, support impact, or release risk.]

### Critical Application Features To Monitor

- [Critical workflow or function]
- [Critical workflow or function]

## Dependencies And Blast Radius

### Service / Infra Dependencies

[Services, infrastructure, third-party systems, feature flags, queues, caches, databases, cron jobs, configs, secrets, or deployment dependencies.]

### Dependent Services That May Be Affected

[Services that may be impacted by this deployment and how they may be impacted.]

### Downstream Services To Monitor For RED Metrics

- [Service name]: [Rate, Errors, Duration metrics to monitor]
- [Service name]: [Rate, Errors, Duration metrics to monitor]

### Internet Exposure

**Is this deployment exposing any endpoints to the internet?** [Yes/No]

**Details:** [Endpoint names, auth, gateway, WAF, rate limits, or other exposure controls.]

## Data, Config, And Capacity Impact

### Database Migration / Config / Secret Changes

**Any database migration, config, or secret changes?** [Yes/No]

**Details:** [Migration name, config keys, secret names, deployment handling, rollback handling, and owner.]

### Expected Utilization Surge

**Any database, queue, or cache expected to see significant utilization surge?** [Yes/No]

**Details:** [Database, queue, or cache name, expected traffic or utilization change, capacity checks, and mitigation.]

### Key Tech Metrics To Monitor

- Infra metrics: [CPU, memory, pod restarts, saturation, queue depth, DB load, cache hit rate, or similar]
- Application metrics: [Latency, error rate, throughput, success/failure metrics, or business metrics]

## Rollout Plan

### Rollout Type

**Is this a gradual rollout or a 0-to-1 shift?** [Gradual rollout / 0-to-1 shift]

### Rollout Start

**Rollout date starting with 1% traffic:** [Date, time, and timezone]

### Planned Rollout Dates

- 1%: [Date, time, and timezone]
- 10%: [Date, time, and timezone]
- 50%: [Date, time, and timezone]
- 100%: [Date, time, and timezone]

### Rollback Plan

[Rollback trigger, rollback steps, owner, expected rollback time, feature flag/config revert, PR revert, or deployment rollback notes.]

## Post-Production Monitoring

### Dashboards

- [Dashboard name/link]
- [Dashboard name/link]

### Alerts

- [Alert name/link]
- [Alert name/link]

### Incident Channel

[Incident channel link or channel name.]

### Release / Team Slack Channel

[Slack channel link or channel name.]

## Alerts And Logging

### Alert Coverage

**Are all necessary alerts available to monitor the metrics?** [Yes/No]

**Details:** [Existing alerts, alert coverage, and known alerting gaps.]

### New Alerts Required

**Are any new alerts needed after this feature deployment?** [Yes/No]

**Details:** [Alert name, metric, threshold, owner, and ETA.]

### New Logs

**Any new logs added?** [Yes/No]

**Estimated daily volume of logs:** [Volume estimate]

**Details:** [Log source, retention/indexing concern, PII/security concern, or expected operational use.]

## Incident Readiness

### Recent Sev0 / Sev1 Incidents

**Was there any Sev0/Sev1 incident in the last 24 hours?** [Yes/No]

**Details:** [Incident link, summary, affected service, and release relevance.]

### RCA Status

**Is RCA for the last incident published?** [Yes/No]

**Details / next steps:** [RCA link if published. Owner and ETA if not published.]

### Incident Reporting Plan

[Who monitors, where issues are reported, escalation path, and post-deploy reporting expectations.]

## Known Risks And Open Items

### Known Issues / Scaling Work Not Yet Done

[Known limitations, deferred scaling work, unresolved risks, or accepted trade-offs.]

### Approval Notes

[Anything approvers should explicitly review before approving this CMR.]
```

## CMR Preview Requirements

Before writing a CMR ticket, the approval preview must include:

- Final rendered description assembled from applicable sections
- Sections omitted as not applicable
- Unknowns that still need user answers
- Linked feature tickets, PRs, docs, dashboards, alerts, and channels
- Any comments, field edits, issue links, or sub-tickets that will be created

Do not update the CMR ticket until the user approves this preview.
