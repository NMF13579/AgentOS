# Compact Task Brief Standard

## Purpose

This standard defines the minimum safe structure for future AgentOS task briefs. It reduces repeated text without weakening boundaries, checks, or human approval separation.

## Scope

This standard applies to future task briefs. It does not rewrite old task briefs and does not override canonical documents.

## Non-Weakening Boundary

Compact task briefs must preserve explicit scope, forbidden changes, validation, expected final report, and final boundary rule.
A compact task brief must not weaken AgentOS safety invariants.
A compact task brief must not hide approval, evidence, PASS, lifecycle, cleanup, or protected artifact boundaries.

## Source-of-Truth Precedence

Task brief is a thin task interface, not a source-of-truth override.
If a task brief conflicts with canonical docs, canonical docs take precedence.
A task brief must not change canonical behavior without a separate human-approved canonical change.
Compact task brief standard must not become a hidden source of truth.

- Task brief may narrow execution scope for a task.
- Task brief may define allowed and forbidden changes for a task.
- Task brief may define validation required for a task.
- Task brief must not redefine canonical behavior.
- Task brief must not weaken canonical safety rules.
- Task brief must not override protected artifact rules.
- Task brief must not override validation authority.
- Task brief must not create new approval semantics.
- Task brief must not create new lifecycle semantics.
- Task brief must not create new cleanup authorization semantics.
- If a task needs canonical behavior changed, that change must be a separate explicit task with human checkpoint requirements.

## Required Minimal Structure

Every safe compact task brief must include:

- Task ID / Name
- Mode
- Repository
- Branch
- Context
- Goal
- Scope
- Rules
- Allowed Changes
- Forbidden Changes
- Required Behavior / Content
- Non-Goals
- Validation
- Expected Final Report
- Final Boundary Rule

## Required Safety Blocks

Explicit safety blocks are required for tasks involving:

- approval
- evidence
- PASS / FAIL / BLOCKED semantics
- lifecycle mutation
- task status changes
- cleanup
- archive
- delete
- move
- compress
- registry
- dependency map
- source of truth
- protected artifact
- canonical artifact
- scripts
- schemas
- workflows
- validation authority
- privacy or sensitive data
- destructive operations

For these tasks, compact wording may be shorter but boundaries must stay explicit.

## Compression Rules

Compression is allowed only by:

- removing repeated background text
- referencing already-created canonical docs
- merging duplicate explanatory paragraphs
- replacing long rationale with exact boundary statements
- keeping validation commands short but sufficient
- using structured YAML-like fields where clearer
- moving reusable rules to docs instead of repeating them in every prompt

Prompt = thin task interface. Docs, scripts, schemas, and templates remain source of truth.

## Prohibited Compression

Do not compress by:

- removing forbidden changes
- removing allowed changes
- removing validation
- removing expected final report
- removing final boundary rule
- replacing specific paths with vague categories when paths are known
- replacing fail-closed behavior with best-effort behavior
- treating UNKNOWN as acceptable
- treating NOT_RUN as PASS
- treating evidence as approval
- treating PASS as approval
- allowing next milestone start implicitly
- allowing physical cleanup without exact candidate admission and human selection
- allowing protected/canonical changes without human checkpoint
- using task brief text to override canonical docs
- hiding canonical changes inside task-specific instructions
- replacing exact paths with broad categories in HIGH_RISK_EXPANDED tasks when exact paths are known
- omitting explicit fail-closed preconditions in HIGH_RISK_EXPANDED tasks

Shorter is acceptable only when safer or equally safe.
Ambiguous compactness is forbidden.
No task may authorize the next milestone implicitly.

## Risk-Based Expansion Rules

- `LOW_RISK_COMPACT`: documentation-only or report-only tasks with narrow paths.
- `MEDIUM_RISK_STANDARD`: policy, registry, validator, or workflow-adjacent tasks.
- `HIGH_RISK_EXPANDED`: cleanup, lifecycle, protected/canonical, approval, validation authority, scripts, schemas, workflows, source-of-truth, privacy, or destructive tasks.

Rules:

- LOW risk may use compact brief.
- MEDIUM risk must include full allowed and forbidden changes plus validation.
- HIGH risk must include expanded boundary rules.
- HIGH risk must include exact allowed paths when known.
- HIGH risk must include exact forbidden paths when known.
- HIGH risk must include explicit fail-closed preconditions.
- HIGH risk must include exact validation commands.
- HIGH risk must include explicit human checkpoint requirements where applicable.
- HIGH risk must block if exact paths are required but unknown.
- HIGH risk must block if source-of-truth impact is unknown.
- HIGH risk must block if protected/canonical impact is unknown.

HIGH_RISK_EXPANDED tasks must include exact allowed paths, exact forbidden paths, explicit fail-closed preconditions, exact validation commands, and explicit human checkpoint requirements where applicable.
For HIGH_RISK_EXPANDED tasks, vague categories are not sufficient when exact paths are known.

## Required Validation Block

Every compact task brief must still define:

- what to check
- how to check it
- what blocked state looks like
- what successful state looks like

Validation may be shorter, but not weaker.

## Required Expected Final Report Block

Every compact task brief must define what the final answer must include, so results stay comparable and reviewable.

## Required Final Boundary Rule

Every compact task brief must end with a clear boundary that states what the task may create or update and what it must not start, approve, or authorize.

## Examples

Safe short example:

```text
Task X1 — Report Update
Mode: report-only
Repository: owner/repo
Branch: dev
Goal: create reports/x1-report.md
Allowed Changes: reports/x1-report.md
Forbidden Changes: docs/, scripts/, schemas/, workflows/, source files
Validation: test -f reports/x1-report.md
Expected Final Report: final status, created file, validation result
Final Boundary Rule: Task X1 may only create reports/x1-report.md
```

Unsafe compressed example:

```text
Task Y1 — Cleanup
Goal: remove old files and continue next milestone if things look safe
```

Why forbidden:

- missing exact forbidden changes
- vague cleanup authorization
- missing validation
- implicit next milestone start
- no fail-closed preconditions

## Validation Checklist

- Minimal structure is present.
- Scope is explicit.
- Forbidden changes are explicit.
- Validation is present.
- Expected final report is present.
- Final boundary rule is present.
- Canonical precedence is preserved.
- Hidden source-of-truth risk is blocked.
- High-risk tasks are expanded when needed.
