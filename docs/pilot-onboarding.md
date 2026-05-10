# Pilot Onboarding Guide — M37 External Pilot

## Purpose
This guide helps eligible pilot users start using AgentOS safely, understand what they are testing, and provide structured feedback.

## Who This Guide Is For
Invited pilot users who have reviewed and accepted the [Pilot Scope](pilot-scope.md) and [Safety Boundaries](pilot-safety-boundaries.md).

## Before You Start
- Ensure your test project is under Git control.
- Verify that your environment has Bash and Python 3.
- Do not use a project with production secrets or protected data.

## What You Are Testing
- Installation and setup clarity.
- Documentation readability.
- Validation loop feedback.
- Basic task creation and verification.

## What You Are Not Testing
- Production deployments.
- Autonomous coding.
- Secret/credential handling.

## Safety Reminder
- **Non-critical repositories only.**
- **No production secrets.**
- **No automated deployment.**
- **Human review is required for every step.**
- **Stop immediately if behavior is unsafe or unclear.**

## Step 1 — Prepare a Safe Test Repository
Use a small, documented project that is easy to revert. Ensure it is fully committed to Git before you start.

## Step 2 — Add or Install AgentOS
Follow the [Installation Guide](../docs/installation.md) to copy the AgentOS templates and scripts into your test repository.

## Step 3 — Read the Starting Documents
Read these documents in order:
1. `README.md`
2. `docs/quickstart.md`
3. `docs/pilot-scope.md`
4. `docs/pilot-safety-boundaries.md`
5. `docs/pilot-eligibility-policy.md`

## Step 4 — Create a Simple Pilot Task
Open `tasks/active-task.md` and define a small, non-functional task such as:
- Improving a README sentence.
- Updating a configuration comment.
- Performing a validation-only check of your repo.

**Do not attempt code changes in your first pilot task.**

## Step 5 — Run Available Validation
Execute the validation suite:
```bash
python3 scripts/agentos-validate.py all
bash scripts/run-all.sh
```

## Step 6 — Review Results
Check the output for PASS, FAIL, or BLOCKED status. Inspect the reports in the `reports/` directory to understand the evidence provided.

## Step 7 — Record Feedback
Use the [Pilot Feedback Template](../templates/pilot-feedback.md) to record your experience.

## When to Stop
- If a command asks for credentials or secrets.
- If a destructive Git command is suggested.
- If validation fails and the recovery path is unclear.
- If AgentOS claims success without verifiable proof.

## What to Send Back
- The completed [Pilot Feedback Report](../templates/pilot-feedback.md).
- Any [Pilot Issue Reports](../templates/pilot-issue-report.md) for specific blockers.

## Final Onboarding Rule
Your safety and project integrity are the highest priority. If AgentOS documentation or tools suggest an action that feels risky, stop and report it.
