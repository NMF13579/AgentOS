# Governance Claim Guard Report (Readiness Assertions)

**Task ID:** task-governance-claim-guard
**Date:** 2026-05-10
**Repository:** AgentOS
**Branch:** dev

## Goal
Prevent premature readiness claims in project documentation and reports by enforcing the presence of explicit completion review status tokens.

## Implementation Details
- **Validator Script:** `scripts/check-readiness-assertions.py`
- **Integrated into:** `scripts/agentos-validate.py` as a new check: `readiness-assertions`.

### Detection Patterns
The validator looks for positive assertions of readiness such as:
- "ready for use", "готов к использованию"
- "production-ready", "public MVP ready"
- "ready for pilot", "ready for deployment"

### Allowed Exceptions
Phrasing that indicates a candidate status or review readiness is allowed without a token:
- "ready for review", "готов к рассмотрению"
- "can be evaluated", "candidate for readiness decision"

### Valid Status Tokens
Readiness claims are only valid if one of these tokens is present in the file:
- `M37_PILOT_READY`
- `M38_PILOT_FEEDBACK_HARDENED`
- `M39_PUBLIC_MVP_READY`
- (and GAP variants)

## Current Findings
The rule identifies several legacy reports and current documentation as having premature claims:

### Critical Violations (ERROR)
| File | Line | Issue |
|---|---|---|
| `reports/execution-evidence-report.md` | 246 | Readiness claim without token / contradictions. |
| `reports/m37-pilot-readiness-evidence-report.md` | 60 | Premature mention of production-ready claims. |
| `reports/m33-hardening-evidence-report.md` | 145 | Assertion of "release-ready" without token. |
| `reports/milestone-11-completion-review.md` | 101 | Assertion of "Ready for Milestone 12". |
| `reports/task-health.md` | 37 | "Ready for Contract Generation" assertion. |

### Warnings (WARNING)
- `README.md`: Mentions of readiness in status definitions.
- `docs/quickstart.md`: Generic readiness phrasing.
- `docs/pilot-safety-boundaries.md`: Use of readiness terminology.

## Suggested Fixes
1. Replace "system is ready for..." with "system meets conditions for review...".
2. Add the required milestone token (e.g. `M37_PILOT_READY`) to the file if the claim is valid.
3. Polish definitions to use "Candidate for readiness" instead of "Ready".

## Final Result
`FAIL` (as expected: existing violations detected).

**Final Status:** `M37_GOVERNANCE_RULE_ENFORCED`
