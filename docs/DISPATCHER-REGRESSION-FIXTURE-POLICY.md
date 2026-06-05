# Dispatcher Regression Fixture Policy

## Purpose
This document defines the policy, rules, and architecture for validation regression fixtures within the AgentOS repository.

## Authority Boundary
The validation regression layer has strict authority limits. Regression layer execution does not govern or override production validation decisions.

## Regression vs Smoke
Smoke checks verify that basic scripts run and do not crash. Regression testing verifies correctness against a matrix of expected/unexpected inputs, failure scenarios, and boundary conditions.

## Regression vs Approval
Regression fixtures are evidence.

Regression fixtures are not approval.

Regression PASS is not approval.

## Regression vs Repair
Regression detects failures.

Regression does not repair failures.

Fixture failure creates action review input.

Fixture failure does not authorize automatic repair.

Fixture NOT_RUN is not PASS.

UNKNOWN is not PASS.

NOT_RUN is not PASS.

## Fixture Category Classification
Regression fixtures are classified into three category classes:
- ESSENTIAL
- CONDITIONAL
- SUPPORTING

## Essential Fixture Categories
The ESSENTIAL category class contains:
- exit-code semantics
- child validator failure behavior
- UNKNOWN / NOT_RUN false PASS resistance
- warning visibility

Essential categories cannot be skipped. Essential fixture NOT_RUN blocks M74 completion unless explicitly escalated as BLOCKED.

## Conditional Fixture Categories
The CONDITIONAL category class contains:
- wrapper regression fixtures

Conditional categories may be NOT_APPLICABLE only with direct evidence.

## Supporting Fixture Categories
The SUPPORTING category class contains:
- CI interpretation boundary
- branch/platform enforcement claim boundary
- M74 carry-forward marker review

Supporting categories cannot replace essential regression fixtures.

## Fixture Isolation Rule
M74 fixtures must live only under fixtures/m74-dispatcher-regression/.

## Mock Child Validator Boundary
Mock child validators must live only under fixtures/m74-dispatcher-regression/mock-child-validators/.
Mock child validators must not be placed under scripts/.
Mock child validators must not be referenced by production dispatcher configuration.
Mock child validators must not replace real validators.
Mock child validators are test fixtures only.

## Controlled Execution Mode
M74 regression runner must execute dispatcher only in controlled test mode.
Controlled test mode must not mutate repository state.
Controlled test mode must use isolated mock child validator paths.
Controlled test mode must not write outside reports/m74-*.
Controlled test mode must not modify dispatcher configuration.
Controlled test mode must not modify production validators.
Controlled test mode must not modify wrappers.
Controlled test mode must not modify docs or workflows.
If controlled test mode is unavailable, M74.8 must block.

The runner must fail closed if:
- fixture malformed
- required fixture field missing
- mock child validator path escapes fixture directory
- dispatcher cannot be invoked
- stdout cannot be captured
- stderr cannot be captured
- exit code cannot be captured
- expected result cannot be evaluated
- actual result is UNKNOWN
- actual result is NOT_RUN

## Gap Lifecycle States
The gap statuses are defined exactly as:
- OPEN
- CLOSED_BY_FIXTURE
- NOT_APPLICABLE_WITH_EVIDENCE
- BLOCKED
- REQUIRES_FIX_TASK

## Failure Handling
The gap statuses carry the following meanings:
- OPEN = gap remains unresolved and must be carried forward.
- CLOSED_BY_FIXTURE = fixture executed and proved expected behavior.
- NOT_APPLICABLE_WITH_EVIDENCE = direct evidence proves the gap does not apply.
- BLOCKED = gap could not be tested because prerequisite or environment was missing.
- REQUIRES_FIX_TASK = fixture exposed a real defect requiring separate fix task.

Every M73 carry-forward marker must receive a gap_status in M74. Warnings cannot be carried forever without classification.

## Action Review Boundary
A gap with REQUIRES_FIX_TASK blocks clean M74 completion. A gap with BLOCKED blocks M74 completion unless explicitly accepted as warning by human review in completion review.

## Source of Truth Boundary
Fixture files are not source of truth for validator semantics. Real validator contracts and M73 dispatcher contracts remain source of truth.

## M74 Completion Boundary
M74 validation checks must be cleanly executed, and all essential fixtures must pass or be classified under acceptable gap statuses before milestone completion can be claimed.
