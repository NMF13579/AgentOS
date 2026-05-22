---
type: ux-planning-readiness-validation
milestone: M48
status: canonical
authority: validation-framework
version: 1.0.0
created: 2026-05-21
owner: human
---

# UX Planning Readiness Validation

## Purpose
This document defines the deterministic validation framework for UX Planning Readiness Reports in M48.

M48 validator checks structure, required fields, decision consistency, downstream limits, and authority boundaries.
M48 validator does not judge visual design quality.
M48 validator does not approve implementation.
M48 validator does not authorize task generation.
M48 validator does not authorize execution.

## Role in M48
The validator checks whether a report follows M48 reporting rules.
The validator is a structural quality gate for readiness report format only.

## Relationship to Readiness Architecture
The validator enforces architecture boundaries from M48 by checking that readiness remains non-authority.

## Relationship to Readiness Criteria
The validator enforces required criteria fields and core consistency rules from the readiness criteria.

## Relationship to Gap Classification Policy
The validator enforces allowed gap classes and core blocking/limitation logic.

## Relationship to Readiness Report Template
The validator validates reports that follow the canonical template format.

## Validator Scope
The validator checks:
- file existence and readability;
- size threshold (max 1 MB);
- frontmatter structure and required fields;
- required section headers;
- required report record fields;
- decision allowlists and consistency;
- accepted limitation structure;
- NOT_APPLICABLE structure;
- optional evidence sentinel rules;
- required downstream limits;
- required non-authority block;
- forbidden authority claims.

## Validator Non-Goals
The validator does not:
- generate tasks;
- create task contracts;
- authorize implementation;
- authorize execution;
- judge visual design quality;
- parse full Markdown semantics.

## CLI Interface
Supported commands:
- `python3 scripts/validate-ux-planning-readiness.py --report <path>`
- `python3 scripts/validate-ux-planning-readiness.py --report <path> --json`
- `python3 scripts/validate-ux-planning-readiness.py --fixtures`
- `python3 scripts/validate-ux-planning-readiness.py --fixtures --json`
- `python3 scripts/validate-ux-planning-readiness.py --explain`
- `python3 scripts/validate-ux-planning-readiness.py --explain --json`

Mode rules:
- `--report` validates one readiness report.
- `--fixtures` validates all positive and negative fixtures.
- `--explain` prints rules and performs no report validation.
- invalid CLI usage returns `UX_PLANNING_READINESS_VALIDATION_BLOCKED`.

## Result Tokens
The validator uses exactly these result tokens:
- `UX_PLANNING_READINESS_VALIDATION_OK`
- `UX_PLANNING_READINESS_VALIDATION_FAILED`
- `UX_PLANNING_READINESS_VALIDATION_BLOCKED`

## Exit Semantics
- `UX_PLANNING_READINESS_VALIDATION_OK` => exit 0
- `UX_PLANNING_READINESS_VALIDATION_FAILED` => exit 1
- `UX_PLANNING_READINESS_VALIDATION_BLOCKED` => exit 2

## Input Reading Requirements
- Input is read as UTF-8 with UTF-8 BOM support.
- File size above 1 MB returns BLOCKED.
- Read failures return BLOCKED.
- Missing files return BLOCKED.

## Validation Checks
The validator performs deterministic checks for:
1. file exists;
2. file readable;
3. file size <= 1 MB;
4. frontmatter exists;
5. frontmatter required keys exist;
6. required sections exist;
7. required record fields exist;
8. readiness_decision allowlist;
9. validation_result allowlist;
10. validation token consistency for readiness decisions;
11. UX_PLANNING_READY cannot include blocking gaps;
12. UX_PLANNING_READY cannot include major gaps;
13. limitations carry-forward consistency;
14. accepted limitation required fields;
15. not applicable required fields;
16. preview sentinel consistency;
17. snapshot sentinel consistency;
18. downstream limits required lines;
19. required non-authority lines;
20. forbidden authority claims absent.

## Decision Consistency Rules
- `UX_PLANNING_READY` and `UX_PLANNING_READY_WITH_LIMITATIONS` require `UX_CONTRACT_VALIDATION_OK`.
- `UX_PLANNING_READY` must not include blocking gaps.
- `UX_PLANNING_READY` must not include major gaps.
- `UX_PLANNING_READY_WITH_LIMITATIONS` must carry limitations forward if limitations exist.

## Optional Evidence Sentinel Rules
- If `preview_required: false`, then `preview_path: NOT_APPLICABLE` is required.
- If `snapshot_required: false`, then `snapshot_path: NOT_APPLICABLE` is required.

## Accepted Limitation Rules
Each accepted limitation must include:
- `limitation`
- `gap_class: UX_GAP_ACCEPTED_LIMITATION`
- `rationale`
- `downstream_risk`
- `owner`
- `carry_forward_required: true`

## Not Applicable Rules
Each NOT_APPLICABLE item must include:
- `criterion`
- `rationale`
- `owner`

## Downstream Limit Rules
Reports must include these exact downstream limits:
- `No task generation authorized.`
- `No implementation authorized.`
- `No execution planning authorized.`
- `No commit, push, merge, deploy, or release authorized.`
- `Future UX-to-task decomposition requires a separate authorized task contract.`
- `Future frontend implementation requires separate authorized task contracts.`

## Forbidden Authority Claims
Validation fails if report contains case-insensitive authority claims such as:
- readiness report authorizes task generation;
- readiness report authorizes implementation;
- readiness report authorizes execution;
- `UX_PLANNING_READY` authorizes task generation/implementation/execution;
- readiness report approves implementation/task generation;
- claims that interpret a validator pass outcome as permission for task generation, implementation, or execution.

## Fixture Strategy
Fixture directories:
- `tests/fixtures/ux-planning-readiness/valid/`
- `tests/fixtures/ux-planning-readiness/negative/`

Required fixture contract:
- one positive fixture that must validate OK;
- thirteen negative fixtures that must validate FAILED.

## Fixture Runner Semantics
`--fixtures` behavior:
- validates all positive fixtures;
- validates all negative fixtures;
- returns OK only when all positives pass and all negatives fail as expected;
- returns FAILED if any positive fails or any negative unexpectedly passes;
- returns BLOCKED if fixture directories are missing;
- reports fixture counts.

## JSON Output
Report mode `--json` output shape includes:
- `result`
- `mode`
- `report`
- `errors`
- `warnings`

Fixtures mode `--json` output shape includes:
- `result`
- `mode`
- `fixture_summary` with:
  - `positive_passed`
  - `positive_failed`
  - `negative_failed_as_expected`
  - `negative_unexpectedly_passed`

## Explain Mode
- `--explain` prints human-readable rules and returns OK.
- `--explain` does not validate reports.
- `--explain --json` returns mode `explain` with non-empty `rules` array.

## MVP Limitations
- The script uses deterministic text and regex checks.
- The script does not fully parse Markdown semantics.
- The script validates M48 report structure and rule consistency only.

## Non-Authority Boundary
UX Planning Readiness Validator is not task generation.
UX Planning Readiness Validator is not implementation approval.
UX Planning Readiness Validator does not authorize task generation.
UX Planning Readiness Validator does not authorize implementation.
UX Planning Readiness Validator does not authorize execution planning.
UX Planning Readiness Validator does not authorize commit, push, merge, deploy, or release.
UX Planning Readiness Validator may validate readiness report structure only.
Future task generation requires a separate authorized task contract.
Future implementation requires separate authorized task contracts.

## Summary
This framework provides deterministic M48 validation with fixed result tokens, strict exit semantics, required boundary enforcement, and predictable fixture-based verification.
