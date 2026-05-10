# Pilot Support and Escalation Guide — M37 External Pilot

## Purpose
This guide defines how pilot feedback, technical issues, and safety concerns are triaged and escalated during the M37 External Pilot.

## Support Model
Triage is performed by the project maintainers. Pilot users should report all findings using the provided templates.

## Severity Reference
All pilot findings must be classified using these levels:

### P0 — Stop Pilot Immediately
- Possible data loss or unsafe destructive action attempted.
- Secret exposure or credential handling request detected.
- Protected production data exposure.
- Validation bypass or suspected false PASS in a safety-critical check.
- Production deployment attempted or suggested.
- Risk to protected Git branches.

### P1 — Pilot Blocked or Unsafe to Continue
- Installation or setup is blocked.
- Core validation suite cannot run.
- Unclear safety boundary preventing user from making a safe decision.
- Required pilot documentation is missing or unreadable.
- A command is unavailable and no workaround exists.

### P2 — Confusing or Degraded Experience
- Confusing documentation or terminology.
- Unclear error messages or validation output.
- Missing troubleshooting paths.
- Onboarding step is incomplete but a workaround is known.

### P3 — Minor Issue or Improvement
- Typos or formatting issues.
- Minor wording improvements.
- Convenience or feature requests for future milestones.

## Escalation Triggers
The maintainers must be notified immediately if any P0 or P1 issue occurs.

## Validation Failure Handling
Validation issues must be recorded with one of these classes:
- **COMMAND_NOT_AVAILABLE:** The script is missing from the repo.
- **VALIDATION_FAILED:** The check ran and returned a non-zero exit code.
- **VALIDATION_SKIPPED:** A required check was bypassed.
- **VALIDATION_INCONCLUSIVE:** The result is ambiguous or the tool crashed.
- **VALIDATION_OUTPUT_UNCLEAR:** The user cannot determine what failed.
- **VALIDATION_FALSE_PASS_SUSPECTED:** The system claims success but evidence is missing.

**Rules:**
- Missing command is **not** PASS.
- Skipped validation is **not** PASS.
- False PASS must be escalated as P0 if safety-critical.

## Safety Concern Handling
Any action that feels risky, even if AgentOS claims it is safe, must be treated as a P0 safety concern until reviewed.

## Documentation Gap Handling
If a pilot user cannot find instructions for a required step, it must be recorded as a P1/P2 documentation gap.

## Required Records
Maintainers will record every escalation with:
- Issue summary and severity.
- Affected pilot user and project type.
- Steps to reproduce and actual results.
- Whether the pilot was stopped, paused, or continued.
- M38 action recommendation.

## Continue / Pause / Stop Rules
- **P0:** Stop the pilot immediately for all users until resolved.
- **P1:** Pause the affected pilot path; user may continue other safe tasks.
- **P2/P3:** Pilot may continue while the issue is tracked for M38.

## M38 Feedback Handoff
M37 records will be used in Milestone 38 to harden documentation, fix validation gaps, and update the pilot onboarding pack.

## Final Escalation Rule
When in doubt, stop. Treating uncertainty as a PASS is a violation of the M37 safety boundary.
