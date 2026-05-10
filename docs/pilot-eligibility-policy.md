# Pilot Eligibility Policy — M37 External Pilot

## Purpose
This document defines who is allowed to participate in the M37 External Pilot and what types of projects are suitable for testing.

## Eligibility Summary
The M37 pilot is reserved for 1–3 invited users who understand the experimental nature of AgentOS and are committed to safe, documented testing.

## Eligible Pilot Users
- Technical users comfortable with Git, terminal usage, and Markdown.
- Users who accept that AgentOS is in an experimental state.
- Users committed to providing structured feedback and reporting confusions.
- Users who understand and accept the [Safety Boundaries](pilot-safety-boundaries.md).

## Ineligible Pilot Users
- Users expecting production readiness or an autonomous agent platform.
- Users expecting a web UI, cloud runner, or SaaS-like dashboard.
- Users unwilling to follow structured validation or report feedback.
- Users intending to test on production-critical repositories.

## Eligible Pilot Projects
- Small or medium non-critical test repositories.
- Project types suitable for documentation or low-risk configuration testing.
- Projects that are fully recoverable from Git history or local backup.
- Repositories free from production secrets and protected data.

## Ineligible Pilot Projects
- Production-critical repositories where a failure would cause business harm.
- Repositories with credentials, secrets, or API keys committed in history.
- Infrastructure-as-code repos controlling production systems.
- High-risk or regulated systems (financial, medical, etc.).

## Required User Understanding
Participants must explicitly accept that:
- M37 is **not** a public release.
- AgentOS does **not** guarantee correct AI output.
- Human review is required for all changes.

## Required Project Conditions
- The project must be under Git version control.
- The project root must be safe to modify with templates and scripts.
- The project must not require direct automated deployment.

## Required Git Conditions
- Users must be able to inspect diffs and revert changes.
- Direct push to protected branches is forbidden during the pilot.
- Destructive operations (force push) are forbidden.

## Required Safety Conditions
- Project must not involve production secrets.
- Project must not involve protected customer data.

## Required Feedback Commitment
- Reporting any P0/P1 blockers immediately.
- Completing a pilot feedback report after initial trial.

## Disqualification Criteria
A pilot candidate is disqualified if they:
- Request production deployment or infrastructure changes.
- Request secret/credential handling capabilities.
- Request autonomous execution without human review.
- Fail to follow the safety boundaries defined for M37.
- Cannot provide structured feedback.

## Final Eligibility Rule
Eligibility is determined by the project owner. Any deviation from these criteria must be reviewed and approved before the pilot user receives AgentOS artifacts.
