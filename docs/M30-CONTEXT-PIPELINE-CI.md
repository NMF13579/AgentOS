# M30 Context Pipeline CI

## Purpose
- CI runs unified context pipeline checker in strict mode.
- Context Pipeline CI is not approval.
- Workflow existence is not branch protection.
- CI checks context readiness; CI does not approve protected actions.

## Workflow
- file: `.github/workflows/context-pipeline.yml`
- uses `actions/checkout@v4`
- uses `actions/setup-python@v5`
- permissions: `contents: read`
- checker command: `scripts/check-context-pipeline.py --json --strict`

## Strict validation
- Exit code alone is not readiness.
- CONTEXT_PIPELINE_READY_WITH_WARNINGS is non-ready in strict CI.
- workflow requires both:
  - exit code 0
  - JSON result `CONTEXT_PIPELINE_READY`

## Safety
- workflow must not hide required gate failures using `|| true`
- no auto-fix
- CI failure is a signal, not an auto-fix request.

## Advisory vs Required
- Workflow existence is not branch protection.
- Required status check is configured separately by human/admin.

## Source-of-truth
- Markdown/YAML = meaning
- JSON = navigation
- SQLite = speed

## CI Fixture Result Values
- CONTEXT_PIPELINE_CI_PASS means workflow accepts only exit 0 plus JSON result CONTEXT_PIPELINE_READY
- CONTEXT_PIPELINE_CI_FAIL
- CONTEXT_PIPELINE_CI_INVALID
- CONTEXT_PIPELINE_CI_BLOCKED
- CONTEXT_PIPELINE_CI_NEEDS_REVIEW

## Non-Authorization
Context Pipeline CI is not approval.
Context Pipeline CI does not authorize commit, push, merge, release, deployment, or protected changes.
Context Pipeline CI does not authorize bypassing AgentOS guardrails.
Context Pipeline CI does not replace Human Gate.
Context Pipeline CI does not weaken, disable, or reduce any guardrail.
Context Pipeline CI must not weaken M27 runtime enforcement.
Context Pipeline CI must not weaken M28 context control.
Context Pipeline CI must not weaken M29 bypass resistance boundaries.
Human Gate remains approval authority.

- workflow must not hide required gate failures using defensive shell patterns in required checker steps.
