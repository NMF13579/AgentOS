# Public MVP Limitations

## Purpose
This document states what AgentOS does not claim in the public MVP candidate.

## Status
AgentOS is being evaluated as a public MVP candidate. This document does not declare public release completion.

## Non-Claims
AgentOS does **not** claim:
- Production readiness or production-scale security.
- Production-grade sandboxing or execution isolation.
- Guaranteed safe or bug-free AI output.
- Automatic approval of risky actions.
- Destructive workflow support or safety.
- SaaS readiness or hosted runner capabilities.
- Full autonomy without human oversight.
- Replacement for human engineering judgment or review.
- Replacement for standard repository security controls (e.g., branch protection).

## Current Boundaries
AgentOS is a **repository-based guardrail framework** for AI coding workflows.
It depends on:
- Honest and explicit task contracts.
- Mandatory human review of all AI changes.
- Validation evidence and audit logs.
- Explicit safety boundaries defined in policy.
- Documented limitations.

## What Users Must Not Do
Users must not treat AgentOS as authorization to:
- Bypass human gates or approval checkpoints.
- Bypass or ignore validation results.
- Ignore `BLOCKED` results or `FAIL` markers.
- Ignore warnings without careful manual review.
- Run destructive workflows or test production-critical repositories.
- Use AgentOS as a production-grade execution sandbox.
- Assume AI output is correct or optimal without independent verification.

## Known Limitation References
- **Internal known limitations:** [docs/known-limitations.md](known-limitations.md)
- **Pilot hardening evidence:** [reports/m38-pilot-feedback-evidence-report.md](../reports/m38-pilot-feedback-evidence-report.md)
- **M39 freeze scope:** [reports/m39-release-candidate-freeze-scope.md](../reports/m39-release-candidate-freeze-scope.md)

## Public MVP Candidate Boundary
Public MVP readiness, if later approved, means AgentOS is suitable for limited public evaluation by experienced developers. It does **not** mean production readiness or a stable commercial release.
