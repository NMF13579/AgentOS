# M30 Required Check Policy

## Purpose
- Defines policy for making context pipeline check required.
- Required check policy is not approval.
- Required check policy does not authorize protected actions.

## Required check name
- Intended: `Context Pipeline / context-pipeline`
- exact check name shown by GitHub must be used in settings.
- observed GitHub check name is the source for repository settings.

## Target branches
- main
- dev

## Rules
- Workflow existence is not branch protection.
- Branch protection requires human/admin repository settings.
- Advisory CI is not required CI.
- CONTEXT_PIPELINE_READY_WITH_WARNINGS is non-pass in strict policy.
- skipped/cancelled/missing check is non-pass.
- Do not claim required-check enforcement without evidence.

## Source-of-truth boundary
- Markdown/YAML = meaning
- JSON = navigation
- SQLite = speed

## Non-Authorization
M30 required-check policy is not approval.
M30 required-check policy does not authorize commit, push, merge, release, deployment, or protected changes.
M30 required-check policy does not authorize bypassing AgentOS guardrails.
M30 required-check policy does not replace Human Gate.
M30 required-check policy does not weaken, disable, or reduce any guardrail.
M30 required-check policy must not weaken M27 runtime enforcement.
M30 required-check policy must not weaken M28 context control.
M30 required-check policy must not weaken M29 bypass resistance boundaries.
Human Gate remains approval authority.

- Branch protection requires human/admin repository settings.
