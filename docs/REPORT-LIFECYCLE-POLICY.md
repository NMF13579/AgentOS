# Report Lifecycle Policy

## Purpose

This policy controls future report growth in AgentOS. It explains why reports exist, how to label them, and how to avoid creating unnecessary new reports.

## Scope

This policy applies to future AgentOS reports and to future review of existing reports. It does not delete, move, archive, compress, rename, rewrite, or consolidate any existing report.

## Non-Approval Boundary

Report lifecycle status is not approval.
Report lifecycle status is not task completion.
Report lifecycle status is not cleanup authorization.
Report lifecycle status is not milestone success.

## Report Lifecycle Statuses

- `ACTIVE_EVIDENCE`
  Current evidence for an open or recent milestone line.
- `HISTORICAL_EVIDENCE`
  Kept for traceability. Not used as current decision authority.
- `SUPERSEDED_EVIDENCE`
  Replaced by a later report, but not safe to delete without dependency review.
- `PROTECTED_DO_NOT_TOUCH`
  Must not be edited, moved, archived, compressed, or deleted without an explicit human checkpoint.
- `CANDIDATE_FOR_FUTURE_REVIEW`
  May be reviewed later, but no physical action is authorized.
- `UNKNOWN_BLOCKED`
  Status is unclear. No cleanup and no lifecycle claim are allowed.

## Active Evidence Rules

- Use `ACTIVE_EVIDENCE` only for reports that support an open or recent line of work.
- Active evidence may inform later review, but it does not approve action.
- Active evidence should stay specific to one task or milestone line where possible.

## Historical Evidence Rules

- Use `HISTORICAL_EVIDENCE` for traceability after a line is closed or no longer current.
- Historical evidence stays available for audit and explanation.
- Historical evidence is not current decision authority unless a later governed task says so.

## Superseded Evidence Rules

- Use `SUPERSEDED_EVIDENCE` when a later report clearly replaces an earlier report for current reading.
- Superseded evidence must still be preserved until dependency review confirms nothing relies on it.
- Superseded evidence is not automatically safe for cleanup.

## Unknown Status Rule

UNKNOWN_BLOCKED must be treated as blocked, not safe.

- If a report's role is unclear, default to `UNKNOWN_BLOCKED`.
- Unknown status stops cleanup claims and stops lifecycle claims.

## Cleanup Candidate Boundary

- A lifecycle label does not authorize cleanup.
- A lifecycle label does not authorize archive, deletion, move, compression, rename, rewrite, or consolidation.
- Exact cleanup decisions require a later registry review, dependency review, and human checkpoint.
- Existing reports must not be physically changed by this policy.

## Human Selection Requirement

- Human review remains required for any future cleanup line.
- An agent must not treat a lifecycle label as human approval.
- Reports marked for future review still require later human selection before any physical action.

## Registry Dependency

- Future cleanup review requires a registry and dependency check first.
- Dependency means links, references, validation use, context use, or any other reliance on a report.
- No report is safe to clean only because it looks old or duplicated.

## Forbidden Interpretations

- Do not read a lifecycle label as approval.
- Do not read a lifecycle label as task completion.
- Do not read a lifecycle label as milestone success.
- Do not read a lifecycle label as cleanup authorization.
- Do not read `SUPERSEDED_EVIDENCE` as safe to remove.
- Do not read `CANDIDATE_FOR_FUTURE_REVIEW` as permission to act.

## Future Report Creation Budget

- Every new milestone should prefer the minimum number of reports needed for traceability.
- Every new report must have a specific role.
- Duplicate evidence reports should be avoided.
- Completion review and evidence report must not be merged if that would blur evidence and decision boundaries.
- Creating a new report requires explaining why an existing report cannot hold the information.
- Report count reduction must not weaken auditability.

## Required Metadata for New Reports

Every new report should define:

- `report_id`
- `task_id`
- `report_role`
- `source_artifacts`
- `approval_boundary`
- `cleanup_authorization`
- `lifecycle_mutation`
- `supersedes`
- `superseded_by`
- `unknowns`

## Validation Checklist

- The report has a specific role.
- The report does not blur evidence and approval.
- The report does not claim cleanup authorization.
- The report includes the required metadata.
- The report does not silently create a new source of truth.
- If status is unclear, it is treated as `UNKNOWN_BLOCKED`.
