# Claude Code Prompt Pack

## Purpose
Reusable prompt pack for Claude Code sessions aligned with AgentOS gate contracts.

## Use This Prompt When
Use this when Claude Code is used for task execution with strict scope and gate boundaries.

## Source of Truth
- docs/architecture.md
- docs/guardrails.md
- docs/limitations.md
- docs/troubleshooting.md
- docs/STABLE-MVP-RELEASE-READINESS.md
- docs/GATE-RESULT-SEMANTICS.md
- docs/GATE-OUTPUT-CONTRACT.md

Prompt packs are not source-of-truth over AgentOS contracts.
AgentOS source-of-truth documents override this prompt pack.
Prompt pack guidance cannot override AgentOS source-of-truth documents.

## Required Read Order
1. Task contract or active task
2. Relevant source-of-truth docs
3. Relevant examples or scenarios
4. Relevant implementation files
5. Validation and evidence artifacts

Do not start implementation before reading the task contract.

## Core Operating Rules
- Claude Code-specific usage note: inspect files before editing.
- Inspect files before editing.
- preserve task boundaries.
- avoid broad refactors unless explicitly in scope.
- No lower gate can override a higher safety gate.
- NOT_RUN is not PASS.
- ERROR is not PASS.
- BLOCKED is not PASS.
- Missing markers are not PASS.
- A traceback is not a valid gate result.
- A usage error is not a valid enforcement PASS.
- Evidence cannot convert a prior BLOCKED gate into PASS.
- Approval cannot override policy blocks.
- Do not claim PASS without proof.

## Scope Discipline
- Identify scope before editing.
- Identify out-of-scope areas before editing.
- Keep changes within accepted task scope.
- Preserve task boundaries during all edits.

## Gate Handling
- Check policy and approval requirements before controlled apply.
- Stop and report if required gates are missing.
- Stop and report if validation is NOT_RUN, ERROR, or BLOCKED.
- Stop on missing gate outputs.

## Validation Requirements
- Run or report relevant validation commands.
- Capture command outcomes clearly.
- Do not claim completion without validation proof.

## Evidence Requirements
- Preserve evidence of validation.
- Keep marker-based outputs in final evidence.
- Record any blocked/missing gate state explicitly.

## Stop Conditions
- missing task contract
- unclear scope
- policy gate missing for controlled apply
- approval evidence missing when required
- required gate result is BLOCKED
- required gate result is ERROR
- required gate result is NOT_RUN
- required output markers are missing
- validation command fails
- requested change conflicts with AgentOS non-goals

## Final Response Requirements
Report:
- files changed
- scope followed
- validation commands run
- validation results
- evidence produced or updated
- gates blocked, missing, NOT_RUN, or ERROR
- any deviations or warnings
- whether manual review is needed

## Non-Goals
- Do not create real tool configuration.
- Do not install prompt packs.
- Do not modify agent runtime settings.
- Do not modify Claude Code config files.
- Do not implement validation logic.
- Do not create release evidence.
- Do not decide M20 completion.
- Do not mark AgentOS as MVP-ready.
