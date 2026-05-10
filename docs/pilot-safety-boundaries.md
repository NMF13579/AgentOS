# Pilot Safety Boundaries — M37 External Pilot

## Purpose
This document defines the safety boundaries for the AgentOS M37 External Pilot. It specifies what must not be assumed, promised, or allowed during this experimental stage.

## Safety Boundary Summary
The M37 pilot is an evaluation of workflow and usability, not a production-grade security system. Safety depends on strict adherence to these boundaries and mandatory human review.

## Non-Claims
- AgentOS does **not** guarantee bug-free AI output.
- AgentOS does **not** replace human review or engineer responsibility.
- AgentOS is **not** in a state of production readiness.
- AgentOS is **not** a production deployment or orchestration system.
- AgentOS is **not** a production-grade sandbox.

## Forbidden Pilot Uses
- Use AgentOS for production deployment.
- Direct push to protected branches.
- Force push to any branch.
- Destructive Git operations (e.g., `git reset --hard` on important work).
- Handling or storing credentials, API keys, or secrets.
- Deleting or migrating production databases.
- Infrastructure changes against production environments.
- Autonomous execution without human checkpoints.
- Using pilot results as proof of production security certification.

## Human Review Requirement
Any action that is risky, unclear, or touches production-like systems must stop and require immediate human review. No AgentOS validation PASS overrides the need for human engineering judgment.

## Production Use Boundary
The pilot is strictly limited to non-critical test repositories. Any use on production codebases is forbidden.

## Data and Secrets Boundary
Do not use AgentOS with protected production data or secrets. Pilot projects must use dummy data or public data only.

## Git and Deployment Boundary
The pilot must not involve any automated deployment pipeline. Git operations must be reviewed by a human before being pushed to a remote repository.

## Sandbox Boundary
AgentOS does not provide a secure sandbox. It provides a governance layer. Pilot users are responsible for their own environment security.

## Failure Handling
If a command fails or a safety gate triggers:
- Stop immediately.
- Do not attempt to bypass the guardrail.
- Record the error and the report from the `reports/` directory.
- Follow the [Troubleshooting Guide](../docs/troubleshooting.md).

## Escalation Triggers
Report these issues immediately as P0/P1:
- **P0:** Possible data loss or unsafe destructive action.
- **P0:** Secret exposure or credential handling request.
- **P0:** Validation bypass or false PASS in a safety check.
- **P1:** Installation blocked or validation cannot run.
- **P1:** Unclear safety boundary blocking a user decision.
- **P2:** Confusing documentation or error messages.

## Final Safety Rule
When in doubt, stop. AgentOS is designed to fail-closed. Treating a missing marker or a crash as a PASS is a critical safety violation.
