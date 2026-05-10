# M37 Pilot Smoke Scenario

## Purpose
This fixture describes a minimal smoke scenario to verify that the M37 pilot path is coherent and safe for a first external pilot user.

## Simulated Pilot User
A technical user who has just joined the M37 pilot. They want to test AgentOS by making a non-functional change to their project's README.

## Simulated safe repository type
A small, non-critical documentation repository under Git control.

## First pilot task type
Simple documentation update (e.g., improving a wording or fixing a typo).

## Documents to read
- `README.md`
- `docs/pilot-onboarding.md`
- `docs/pilot-scope.md`
- `docs/pilot-safety-boundaries.md`

## Commands to attempt
```bash
python3 scripts/agentos-validate.py all
bash scripts/run-all.sh
```

## Feedback templates to fill
- `templates/pilot-feedback.md`

## Escalation condition to check
The user should check if a `BLOCKED` status correctly instructs them to stop according to `docs/pilot-support-escalation.md`.

## Expected smoke result
The user successfully completes a validation cycle for their documentation task, understands the results, and knows how to record feedback.

## Forbidden Actions
- Use on production code.
- Destructive commands.
- Handling secrets or API keys.
- Direct push to protected branches.
- Bypassing validation.
