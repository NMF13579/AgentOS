---
type: template
module: m25
status: draft
authority: supporting
created: 2026-05-06
last_validated: unknown
---

# Enforcement Review

## Review Record
Review ID:
Related PR / branch:
AgentOS result:
WARN present: YES | NO
Blocking result present: YES | NO
Human reviewer:
Review decision: APPROVED_FOR_MERGE | APPROVED_WITH_WARNINGS | BLOCKED | NEEDS_REVIEW
Reason:
Evidence links / artifacts:
Override used: YES | NO
Override record path:
Next reviewer:
Deadline:
Final statement:

## Required Checks Observed
| Required check | Observed result | Notes |
|---|---|---|
| scope |  |  |
| scope-fixtures |  |  |
| execution-audit |  |  |
| ci-evidence |  |  |
| m24-evidence-report |  |  |
| m24-completion-review |  |  |

## Decision Rules
- APPROVED_FOR_MERGE can be used only when AgentOS result is PASS and no blocking result is present.
- APPROVED_WITH_WARNINGS can be used only when WARN is present and human reviewer accepts the documented risk.
- BLOCKED must be used when FAIL, ERROR, NOT_RUN, or INCOMPLETE is present.
- NEEDS_REVIEW must include next reviewer name and deadline.

## Review Boundaries
This review is a human review record.
This review does not authorize automatic approval.
This review does not authorize auto-merge.
Evidence report is not approval.
CI PASS is not human approval.
Required checks do not replace owner review.
Skipped / neutral / missing AgentOS validation must not be treated as PASS.
PASS does not prove implementation correctness.
NOT_RUN is not PASS.
INCOMPLETE is not PASS.
ERROR requires human review.
FAIL requires human review.

## Notes
- This template records review evidence for M25 merge-gate enforcement.
- It does not configure GitHub branch protection.
- It does not change repository automation behavior.

