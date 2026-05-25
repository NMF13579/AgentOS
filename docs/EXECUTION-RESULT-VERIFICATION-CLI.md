# Execution Result Verification CLI

## Purpose

This document details the Execution Result Verification CLI foundation for milestone M59. The CLI is designed to programmatically evaluate verification inputs, preconditions, scope limits, and validation evidence to classify the result verification status.

## Preconditions

The preconditions for the CLI foundation are:
1. `reports/m59-m58-completion-intake.md` exists and contains `MAY_PROCEED_TO_M59_VERIFICATION_PLANNING: true`
2. `docs/EXECUTION-RESULT-VERIFICATION-POLICY.md` exists and contains:
   - `FINAL_STATUS: M59_EXECUTION_RESULT_VERIFICATION_POLICY_DEFINED`
   - `Upstream verification layers are authoritative for safety classification.`
   - `The result/output consistency table is authoritative for resolving mixed upstream/output states.`
3. `reports/m58-completion-review.md` exists

## Position in M59

The CLI represents task 59.8.1 in the M59 milestone chain. It implements the command-line surface and foundation logic described in the result verification policy (59.7), preparing the codebase for full policy matrix validation in 59.8.2.

## CLI Role

The CLI acts as a read-only compliance checker. It is not an active task executor.
- M59 CLI foundation does not verify execution result.
- M59 CLI foundation does not approve task completion.
- M59 CLI foundation does not create approval.
- M59 CLI foundation does not authorize merge, push, or release.
- M59 CLI foundation does not mutate lifecycle state.
- M59 CLI foundation does not replace human review.
- M59 CLI foundation does not start M60 cleanup.

## CLI Arguments

The CLI implements the following arguments:
- `--root`: Directory to resolve all paths relative to (defaults to current directory).
- `--input`: Path to the input JSON file.
- `--preconditions`: Path to the preconditions JSON file.
- `--diff-scope`: Path to the diff/scope verification JSON file.
- `--validation-evidence`: Path to the validation evidence JSON file.
- `--result-output`: Path to the result output JSON file.
- `--json`: Force JSON output to stdout.
- `--explain`: Prints a human-readable explanation and safety warnings.
- `--strict`: Upgrades verification warnings to blockers.

## Input Artifacts

The CLI reads five JSON files corresponding to M59 verification layers:
1. Input contract (`--input`)
2. Preconditions (`--preconditions`)
3. Git diff and scope (`--diff-scope`)
4. Validation evidence (`--validation-evidence`)
5. Verification result/output (`--result-output`)

## Path Safety

Path containment is strictly checked using resolved path checks:
```python
resolved_path == resolved_root or resolved_root in resolved_path.parents
```
Any path resolving or traversing outside the repo root directory triggers `EXECUTION_RESULT_BLOCKED` and exit 2. Absolute path printouts are suppressed to prevent leakage of sensitive workspace information.

## JSON Loading

The CLI attempts to load each JSON file:
- Missing files trigger fail-closed behavior, returning `EXECUTION_RESULT_BLOCKED` and exit 2.
- Malformed JSON structures trigger fail-closed behavior, returning `EXECUTION_RESULT_BLOCKED` and exit 2.
- Path safety issues trigger exit 2.
- In JSON mode, loading errors still result in a valid JSON output structure.

## Status Fields Read

The CLI extracts the following fields when available:
- `input_status`
- `preconditions_status`
- `diff_scope_status`
- `validation_evidence_status`
- `verification_result_status`

In 59.8.1, missing status fields are classified as blockers.

## Policy Decision Values

The CLI defines exactly these policy decision constants:
- `M59_VERIFICATION_POLICY_VERIFIED`
- `M59_VERIFICATION_POLICY_VERIFIED_WITH_WARNINGS`
- `M59_VERIFICATION_POLICY_NOT_VERIFIED`
- `M59_VERIFICATION_POLICY_BLOCKED`

## Result Values

The CLI defines exactly these result value constants:
- `EXECUTION_RESULT_VERIFIED`
- `EXECUTION_RESULT_VERIFIED_WITH_WARNINGS`
- `EXECUTION_RESULT_NOT_VERIFIED`
- `EXECUTION_RESULT_BLOCKED`

## Exit Code Mapping

The CLI maps result states to standard shell exit codes:
- `EXECUTION_RESULT_VERIFIED` -> exit 0
- `EXECUTION_RESULT_VERIFIED_WITH_WARNINGS` -> exit 0
- `EXECUTION_RESULT_NOT_VERIFIED` -> exit 1
- `EXECUTION_RESULT_BLOCKED` -> exit 2

## Priority Order

The CLI follows the priority logic:
```text
BLOCKED > NOT_VERIFIED > VERIFIED_WITH_WARNINGS > VERIFIED
```
A blocker overrides all other signals. A not-ready condition overrides warnings or clean states.

## Upstream Authority Rule

Upstream validation layers (preconditions, scope, evidence) are authoritative for safety classification. The result/output status (59.6) serves as a consistency check and cannot self-authorize success.

## Result / Output Consistency Rule

Verification outputs are only accepted when they match the status levels of preconditions, scope verification, and validation evidence. Any mismatch or contradiction forces `NOT_VERIFIED` or `BLOCKED` depending on rule severity.

## Authority Claim Detection

Any artifact claiming that:
- Task is complete
- Task is approved
- Human review is replaced
- Push/merge/release is allowed
- Lifecycle state may be mutated
- M60 cleanup has started
is detected as a blocker, triggering fail-closed blocking.

## Human Review Handoff

Automated checks do not bypass the human gate. All clean or warning results are formatted as verification handoffs for manual review.

## Strict Mode

When `--strict` is active:
- Any verification warning causes the result to be upgraded to `EXECUTION_RESULT_BLOCKED` with exit code 2.
- The `strict_upgrades_applied` count is incremented.

## JSON Output

In JSON output mode, the CLI emits valid JSON on stdout including:
- `result`
- `policy_decision`
- `exit_code`
- `strict`
- `strict_upgrades_applied`
- `upstream_state`
- `output_state`
- `input_status`
- `preconditions_status`
- `diff_scope_status`
- `validation_evidence_status`
- `verification_result_status`
- `warnings`
- `blockers`
- `not_verified_reasons`
- `non_authority`

## Human Output

Human-readable output includes:
- `RESULT:`
- `POLICY_DECISION:`
- `EXIT_CODE:`
- `UPSTREAM_STATE:`
- `OUTPUT_STATE:`
- `STRICT:`
- `WARNINGS:`
- `BLOCKERS:`
- `NOT_VERIFIED_REASONS:`

## Explain Output

Explain mode provides a detailed breakdown covering:
- `upstream` layers
- `consistency` validation
- `not approval` safety warnings
- `human review` requirements
- `merge` gates
- `lifecycle` mutation rules

## Fail-Closed Behavior

Any file access issue, invalid path, parsing failure, or missing required field prevents classification and forces exit 2 (`EXECUTION_RESULT_BLOCKED`).

## Non-Authority Rules

The CLI enforces the following non-authority rules:
- M59 CLI does not approve task completion.
- M59 CLI does not create approval.
- M59 CLI does not authorize merge, push, or release.
- M59 CLI does not mutate lifecycle state.
- M59 CLI does not replace human review.
- M59 CLI only classifies execution result verification state for human review handoff.

## Relationship to 59.7 Policy

The CLI foundation implements the structure and exit codes established in the policy contract document (59.7).

## Relationship to 59.8.2 Behavioral Validation

The full matrix of consistency states, authority claims, and compliance rules is implemented and verified in task 59.8.2.

## Relationship to 59.9 Fixtures

Positive and negative fixtures check that the CLI handles correct inputs and rejects violations.

## Relationship to 59.10 Fixture Runner

The runner automates verifying CLI classification outcomes against fixtures.

## Forbidden Claims

The documentation must not claim that the task is complete, approved, or that human review is bypassed.

## Final CLI Status

```text
FINAL_STATUS: M59_EXECUTION_RESULT_VERIFICATION_CLI_DEFINED
```

This status means only that the Execution Result Verification CLI is defined.
It does not mean execution result was verified.
It does not mean task completion was approved.

