# M28 Context Compliance Check

## Purpose

This check validates alignment with the selected Context Pack.
This check does not approve execution.
This check does not replace tests.
This check does not replace M27 runtime enforcement.
This check does not replace Human Gate approval.

No valid Context Pack -> No Context-Compliant Execution.

## Result Values and Exit Semantics

- CONTEXT_COMPLIANT => exit 0
- CONTEXT_COMPLIANT_WITH_WARNINGS => exit 1
- CONTEXT_VIOLATION => exit 1
- CONTEXT_NEEDS_REVIEW => exit 1
- CONTEXT_MISSING => exit 1

Missing required compliance input must return CONTEXT_MISSING.
Detailed result distinction must be read from stdout or --json output.

## What Compliance Means

Compliance means plan/verification artifacts explicitly align with selected rules, selected policies, lessons, out-of-scope constraints, and non-authorization boundaries from Context Pack.

Context compliance is not approval.
Context compliance does not authorize commit, push, merge, release, deployment, or protected changes.
Context compliance does not replace M27 runtime enforcement.
Context compliance does not replace Human Gate approval.

## What the Script Checks

- Context Pack presence and baseline validity.
- Plan acknowledgement/contradiction checks.
- Verification acknowledgement/contradiction checks.
- Lesson acknowledgement and repeat-risk checks.
- changed-files out-of-scope and path safety checks.
- Non-authorization contradiction checks.
- findings output with severity/category.

## What the Script Does Not Check

- It does not execute the plan.
- It does not run tests.
- It does not regenerate Context Pack.
- It does not call select-context.py automatically.
- It does not approve anything.

## Plan Compliance Behavior

- Missing selected-rule acknowledgement => CONTEXT_NEEDS_REVIEW.
- Explicit contradiction of selected policy/rule => CONTEXT_VIOLATION.
- Silence is not treated as compliance.
- silence on selected required context is needs_review.

## Verification Compliance Behavior

- Missing context-aware checks => CONTEXT_NEEDS_REVIEW.
- Explicit contradiction while claiming success => CONTEXT_VIOLATION.

## Heuristic Confidence Rules

The checker must prefer NEEDS_REVIEW over false COMPLIANT.
The checker must not infer compliance from silence.
Heuristic extraction must be based on section headers, exact phrases, and keyword matching only.
The script must not attempt semantic inference, embeddings, or model-based judgement.

## Lesson Compliance Behavior

Lesson checks are required when the Relevant Lessons section contains at least one non-empty lesson item.
repeats-known-lesson => CONTEXT_VIOLATION.

## Changed Files / Out-of-Scope Behavior

changed-files.txt must contain one repository-relative path per line.
POSIX absolute paths are invalid.
Windows absolute paths are invalid.
Out-of-scope touches produce CONTEXT_VIOLATION when explicit.

## Missing Input Behavior

- Missing context => CONTEXT_MISSING.
- If no plan/verification/changed-files is provided => CONTEXT_MISSING.
- Missing provided artifact path => CONTEXT_MISSING.

## Validation/Demo Artifact Behavior

Validation/demo artifacts may be created by the implementation agent before validation, not by check-context-compliance.py.
They must include header:
# VALIDATION/DEMO ARTIFACT — NOT A REAL TASK ARTIFACT

check-context-compliance.py must never create validation/demo artifacts.
Validation/demo artifacts must be prepared before running no-write validation.
No-write validation snapshot must be taken after any validation/demo artifacts are prepared.

repo_commit_hash: STALE_PLACEHOLDER is valid fixture strategy for stale-context-pack.
Fixtures must be static files only.

## No-Write Rule

- The script is read-only.
- It must not modify context/plan/verification/changed-files artifacts.
- It must not create plan/verification/changed-files artifacts.

## Non-Authorization Boundary

Context compliance is not approval.
Context compliance does not authorize commit, push, merge, release, deployment, or protected changes.
Context compliance does not replace M27 runtime enforcement.
Context compliance does not replace Human Gate approval.

## Additional Rules

- No valid Context Pack -> compliance cannot pass.
- Do not modify existing readiness, validation, or enforcement scripts.
- CONTEXT_VIOLATION is required for explicit contradiction, forbidden approval claim, or explicit out-of-scope touch.
- CONTEXT_NEEDS_REVIEW is required for ambiguity or uncertain extraction.
