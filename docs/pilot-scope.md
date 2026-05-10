# Pilot Scope — M37 External Pilot readiness

## Purpose
This document defines the scope of the M37 External Pilot for AgentOS. It specifies what the pilot is, who it is for, and the boundaries of allowed testing.

## Pilot Definition
The M37 pilot is a controlled, small-scale evaluation of AgentOS External MVP Usability. It is not a public release, not SaaS readiness, and not production readiness. It is an experimental stage to verify "First User Readiness" under strict human oversight.

## Pilot Audience
- M37 pilot is limited to 1–3 external pilot users.
- Pilot users must be invited and understand that AgentOS is still in an experimental stage.

## Allowed Pilot Scenarios
- Install or copy AgentOS into a small test repository.
- Read README, quickstart, and first-user guides.
- Create a simple documentation task using `tasks/active-task.md`.
- Run available validation commands (`agentos-validate.py all`, `run-all.sh`).
- Review generated reports in the `reports/` directory.
- Report confusion, blockers, and validation failures.

## Forbidden Pilot Scenarios
- Use AgentOS for production deployment.
- Autonomous coding without human review.
- High-risk code changes (auth, security, core logic).
- Credential or secret handling.
- Destructive Git operations (force push to protected branches, deleting history).
- Bypassing validation or ignoring FAIL results.
- Using AgentOS as a SaaS or cloud platform.
- Using AgentOS as a production sandbox.

## Supported Project Types
- Small or medium non-critical test repositories.
- Documentation-heavy projects.
- Projects using Git, Bash, and Python 3.

## Unsupported Project Types
- Production-critical repositories.
- Repositories containing secrets or protected production data.
- High-risk infrastructure or security systems.
- Legacy projects with non-standard structures that bypass AgentOS checks.

## Expected User Capabilities
- Basic knowledge of Git and terminal usage.
- Ability to read and follow Markdown-based instructions.
- Willingness to provide structured feedback and report issues.

## What Counts as Pilot Success
- A first external user can understand, install, and run AgentOS validation without the author's help.
- Confusions and blockers are identified and recorded honestly.
- The pilot user respects the safety boundaries.

## What Counts as Pilot Failure
- The pilot user cannot understand or install the framework.
- The pilot user attempts a forbidden scenario or bypasses a guardrail.
- AgentOS provides a false sense of security or autonomous safety.

## Out of Scope for M37
- Web UI, Cloud/Server backend, or Dashboard.
- Vector DB or multi-agent orchestration.
- Autonomous "self-heal" capabilities.

## Required Feedback from Pilot Users
- Confusing steps in installation or quickstart.
- Unclear error messages.
- Documentation gaps.
- Safety or boundary concerns.

## Safety Boundary
- AgentOS does not guarantee bug-free AI output.
- AgentOS does not replace human review.
- Risky operations must be stopped immediately for manual review.

## Final Rule
The M37 pilot must remain narrow and safe. Any action not explicitly allowed in this scope must be treated as forbidden until reviewed.
