# RCA Template

Source template: https://coindcx.atlassian.net/wiki/spaces/OnRampOffR/pages/4150427667/RCA+Template+2025

## Ownership

| **Created By** | **Reviewed By** | **Approved By** |
| -------------- | --------------- | --------------- |
|                |                 |                 |

## Problem Statement and Impact Assessment

| **Question**                       | **Answer**                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **What went wrong?**               | Example: A server crash caused a 1-hour system downtime, affecting 100,000 customers                                                                                                                                                                                                                                                                                                                                                                                           |
| **Where and when did it occur?**   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| **Who detected the issue?**        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| **Primary Responding Team**        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| **Incident Reporting time**        |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| **Incident Reported on**           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| **Time to take corrective action** |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| **Who/what was affected**          | Customers, systems, revenue, compliance, etc.                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| **Quantify the impact**            | e.g., X% downtime, Y failed transactions, Z hours of delay, legal consequences                                                                                                                                                                                                                                                                                                                                                                                                 |
| **How severe is the issue?**       | Sev1/Critical: Severe impact on business operations, causing major service disruptions, legal implications, or significant financial loss. Sev2/High: Substantial impact on business functions, affecting multiple users or systems but with workarounds available. Sev3/Medium: Moderate impact, causing inconvenience or partial disruption with a manageable resolution. Sev4/Low: Minimal impact with no major consequences, easily resolvable without significant effort. |

## Timeline

| **Time** | **Description** |
| -------- | --------------- |
|          |                 |

Capture detection, acknowledgement, investigation start, diagnosis, mitigation, recovery, customer communication, and closure timestamps where available.

## RCA Using Fault Tree Analysis (FTA) and 5 Whys

### [FTA]

Use this section to structure the failure analysis:

1. Write down the main failure: what was the observed issue?
2. Identify all direct causes that contributed to the failure.
3. Break each direct cause into at least two levels of contributing factors where the information is available.
4. Once the deepest identifiable cause is reached, apply 5 Whys to uncover the true root cause.
5. Present the breakdown as a structured list showing how different factors led to the failure.

Example structure:

1. **Main Failure:** Server crash
   1. **Cause 1:** High CPU usage
      1. **Sub-Cause 1.1:** Unoptimized database query
         1. **Sub-Cause 1.1.1:** Query executed with no index optimization
         2. **Sub-Cause 1.1.2:** Large data retrieval without pagination
   2. **Cause 2:** Disk space full
      1. **Sub-Cause 2.1:** Log files not purged
         1. **Sub-Cause 2.1.1:** No automated log rotation policy
         2. **Sub-Cause 2.1.2:** Debug logging enabled in production

Using Fault Tree Analysis, identify all failure paths contributing to the issue. Then apply 5 Whys to each lowest-level contributing factor to uncover deeper systemic problems.

### [5 Whys]

Apply 5 Whys to every lowest-level contributing factor.

Example for `Sub-Cause 1.1.1 - Query executed with no index optimization`:

- **Why 1?** The query lacked an index.
  - **Because** the developer did not follow optimization guidelines.
- **Why 2?** The developer did not follow optimization guidelines.
  - **Because** there was no mandatory review process for database queries.
- **Why 3?** There was no mandatory review process for database queries.
  - **Because** database performance was not formally integrated into the deployment workflow.
- **Why 4?** Database performance was not integrated into the workflow.
  - **Because** no governance policy enforced database optimization.
- **Why 5?** No governance policy enforced database optimization.
  - **Because** the team lacked clear ownership and accountability for database performance.

**Root Cause:** Lack of ownership and governance for database performance, leading to unoptimized queries in production.

## Root Cause Description

| **Root Cause Description** | **Supporting Example** |
| -------------------------- | ---------------------- |
|                            |                        |

## Questions

### How can we reduce the time-to-detect in half?

Answer with concrete monitoring, alerting, ownership, and signal-quality improvements.

### How can we reduce the time-to-diagnose in half?

Answer with concrete observability, runbook, dashboard, logging, tracing, escalation, and knowledge improvements.

### How can we reduce the time-to-mitigate in half?

Answer with concrete rollback, feature flag, automation, operational tooling, access, and decision-making improvements.

## Corrective Action (Short Term Fixes)

| **Corrective Action** | **Responsible Person** | **ETA** | **Jira Ref** |
| --------------------- | ---------------------- | ------- | ------------ |
|                       |                        |         |              |

Corrective actions should address the immediate failure mode and be achievable in the short term.

## Preventive Action (Long Term Solutions)

| **Preventive Action** | **Responsible Person** | **ETA** | **Jira Ref** |
| --------------------- | ---------------------- | ------- | ------------ |
|                       |                        |         |              |

Preventive actions should address systemic root causes and reduce recurrence risk.

## Lessons Learned

-
