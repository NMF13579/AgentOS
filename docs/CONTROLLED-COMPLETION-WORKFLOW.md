# Controlled Completion Workflow
## 1. Purpose
This document defines the user-facing controlled completion workflow after M15/M16.

Controlled completion is a lifecycle protocol, not a single command and not a validation result.

## 2. Workflow Boundary
- verification PASS does not complete a task
- readiness PASS does not complete a task
- prepared transition does not complete a task
- dry-run does not complete a task
- apply plan does not complete a task
- applied transition record does not complete a task
- mutation plan does not complete a task
- only controlled complete-active lifecycle mutation may complete active task state

## 3. Required Source-of-Truth Documents
- `docs/COMPLETION-READINESS.md`
- `docs/COMPLETION-TRANSITION.md`
- `docs/CONTROLLED-LIFECYCLE-MUTATION.md`
- `docs/APPLY-PRECONDITIONS.md`
- `docs/APPLY-PLAN.md`
- `docs/APPLIED-TRANSITION-RECORD.md`
- `docs/LIFECYCLE-INTEGRATION.md`
- `docs/APPLY-COMMAND-INTEGRATION.md`
- `docs/HUMAN-APPROVAL-BOUNDARY.md`

This workflow document summarizes usage and does not replace source-of-truth documents.

## 4. Canonical Controlled Completion Flow
```text
1. Produce verification evidence
2. Check completion readiness
3. Prepare completion transition
4. Check apply preconditions
5. Run apply dry-run
6. Prepare apply plan
7. Create applied transition record
8. Prepare complete-active mutation plan
9. Confirm approval boundary if approval is required
10. Run controlled complete-active lifecycle mutation
11. Run lifecycle validation
12. Run lifecycle audit
13. Preserve evidence for milestone report and review
```

Normative rules:
- steps MUST be followed in order
- no step may be skipped
- no step may be silently replaced by another step
- each step has its own preconditions
- passing one step does not authorize the next step unless the next step's own preconditions are satisfied

## 5. Step-by-Step Workflow
### Step 1: Produce verification evidence
- Purpose: establish test/check evidence for current task state.
- Expected input: active task context and verification scope.
- Expected output: durable verification evidence artifact.
- Does not authorize: completion or lifecycle mutation.
- Stop if fails: workflow MUST stop.

### Step 2: Check completion readiness
- Purpose: determine whether completion preparation is allowed.
- Expected input: verification evidence and required readiness inputs.
- Expected output: readiness result artifact.
- Does not authorize: lifecycle mutation.
- Stop if fails: workflow MUST stop.

### Step 3: Prepare completion transition
- Purpose: record prepared transition candidate.
- Expected input: readiness evidence.
- Expected output: prepared transition record.
- Does not authorize: lifecycle mutation.
- Stop if fails: workflow MUST stop.

### Step 4: Check apply preconditions
- Purpose: validate apply preconditions against prepared transition.
- Expected input: prepared transition and active task context.
- Expected output: PASS/BLOCKED preconditions result.
- Does not authorize: lifecycle mutation.
- Stop if fails: workflow MUST stop.

### Step 5: Run apply dry-run
- Purpose: simulate apply path in read-only mode.
- Expected input: prepared transition.
- Expected output: dry-run result.
- Does not authorize: lifecycle mutation.
- Stop if fails: workflow MUST stop.

### Step 6: Prepare apply plan
- Purpose: create explicit apply plan artifact.
- Expected input: prepared transition and valid plan output path.
- Expected output: apply plan file.
- Does not authorize: lifecycle mutation.
- Stop if fails: workflow MUST stop.

### Step 7: Create applied transition record
- Purpose: create controlled apply evidence artifact.
- Expected input: prepared transition + apply plan + explicit output path.
- Expected output: applied transition record file.
- Does not authorize: lifecycle mutation by itself.
- Stop if fails: workflow MUST stop.

### Step 8: Prepare complete-active mutation plan
- Purpose: produce mutation planning evidence.
- Expected input: prepared transition + apply plan + applied record.
- Expected output: mutation plan evidence.
- Does not authorize: lifecycle mutation.
- Stop if fails: workflow MUST stop.

### Step 9: Confirm approval boundary if approval is required
- Purpose: verify explicit approval evidence when required by lifecycle rules.
- Expected input: approval requirement and approval evidence.
- Expected output: explicit approval checkpoint decision.
- Does not authorize: bypassing preconditions/evidence.
- Stop if fails: workflow MUST stop.

### Step 10: Run controlled complete-active lifecycle mutation
- Purpose: execute supported lifecycle mutation path.
- Expected input: transition + plan + applied record + mutation plan.
- Expected output: controlled mutation result and modified task paths.
- Does not authorize: unsupported mutation paths.
- Stop if fails: workflow MUST stop.

### Step 11: Run lifecycle validation
- Purpose: check structural lifecycle apply coverage.
- Expected input: lifecycle artifacts.
- Expected output: validator result.
- Does not authorize: lifecycle mutation.
- Stop if fails: workflow MUST stop.

### Step 12: Run lifecycle audit
- Purpose: check lifecycle mutation audit visibility.
- Expected input: lifecycle docs/scripts/fixtures presence and hooks.
- Expected output: audit PASS/WARN/FAIL result.
- Does not authorize: lifecycle mutation.
- Stop if fails: workflow MUST stop.

### Step 13: Preserve evidence for milestone report and review
- Purpose: ensure durable traceability for review.
- Expected input: all previous evidence artifacts.
- Expected output: preserved evidence set for reporting/review.
- Does not authorize: retroactive mutation.
- Stop if fails: workflow MUST stop.

## 6. Command Reference
```bash
python3 scripts/check-apply-preconditions.py \
  --transition <prepared-transition-file>
```

```bash
python3 scripts/apply-transition.py \
  --transition <prepared-transition-file> \
  --dry-run
```

```bash
python3 scripts/apply-transition.py \
  --transition <prepared-transition-file> \
  --prepare \
  --plan-out <apply-plan-file>
```

```bash
python3 scripts/apply-transition.py \
  --transition <prepared-transition-file> \
  --plan <apply-plan-file> \
  --apply \
  --applied-record-out <applied-transition-record-file>
```

```bash
python3 scripts/apply-transition.py \
  --transition <prepared-transition-file> \
  --plan <apply-plan-file> \
  --applied-record <applied-transition-record-file> \
  --complete-active-plan
```

```bash
python3 scripts/apply-transition.py \
  --transition <prepared-transition-file> \
  --plan <apply-plan-file> \
  --applied-record <applied-transition-record-file> \
  --mutation-plan <complete-active-mutation-plan-file> \
  --complete-active
```

```bash
python3 scripts/validate-lifecycle-apply.py
```

```bash
python3 scripts/audit-lifecycle-mutation.py
```

Command examples are documentation only. They do not create approval or lifecycle authority by themselves.

## 7. Stop Conditions
Workflow MUST stop when:
- verification fails
- completion readiness fails
- prepared transition is missing or invalid
- apply preconditions are BLOCKED
- dry-run fails
- apply plan cannot be prepared safely
- applied transition record cannot be created safely
- mutation plan is missing, invalid, or says mutation must not occur
- approval is required but explicit approval evidence is missing
- complete-active command fails
- validator reports FAIL
- audit reports FAIL

Failure does not authorize retry, skipping, or mutation.

## 8. Human Approval Checkpoint
- approval is checked only when required by lifecycle rules
- approval must be explicit
- approval must be scope-bound
- approval must be durable and inspectable
- approval cannot be inferred from vague user text
- approval cannot be inferred from successful commands
- approval cannot bypass preconditions, evidence chain, mutation plan, or unsupported mutation boundaries

## 9. Evidence Preservation
Preserve:
- verification evidence
- completion readiness evidence
- prepared transition record
- apply preconditions result
- dry-run result or captured output if relevant
- apply plan
- applied transition record
- complete-active mutation plan
- controlled mutation evidence
- validation result
- audit result
- approval evidence if required
- known limitations if any

Transient command output is not enough unless captured in a durable artifact when durable evidence is required.

## 10. Validation and Audit Usage
- `validate-lifecycle-apply.py` checks structural lifecycle apply coverage
- `audit-lifecycle-mutation.py` checks lifecycle mutation audit visibility
- validation PASS does not imply lifecycle mutation
- audit PASS does not imply lifecycle mutation
- validation or audit WARN must be reviewed
- validation or audit FAIL blocks completion review until resolved or explicitly documented

## 11. Unsupported Workflow Paths
This workflow does not support:
- needs_review lifecycle mutation
- failed lifecycle mutation
- blocked lifecycle mutation
- manual_abort lifecycle mutation
- general apply engine
- automatic approval creation
- autonomous retry
- autonomous abort
- background execution
- autonomous task completion

Unsupported paths remain unsupported even if a user or agent says they are approved.

## 12. Agent Behavior Rules
Agents MUST:
- read relevant source-of-truth documents before acting
- follow canonical order
- stop on failure
- report missing evidence
- report missing approval when approval is required
- preserve distinction between evidence and lifecycle mutation
- preserve distinction between approval and command success
- avoid claiming task completion until controlled mutation actually occurred

Agents MUST NOT:
- skip steps
- reorder steps
- infer approval
- fabricate evidence
- treat PASS as task completion
- treat applied record as lifecycle mutation
- mutate real lifecycle state outside controlled complete-active command
- proceed automatically after failure

## 13. Machine Validation Hooks
This workflow document is designed to be machine-checkable.

Detectable requirements:
- canonical controlled completion flow is defined
- controlled apply command sequence is documented
- stop conditions are documented
- human approval checkpoint is documented
- evidence preservation is documented
- validation and audit usage are documented
- unsupported workflow paths are documented
- autonomous lifecycle authority is disallowed

```yaml
controlled_completion_workflow:
  canonical_flow_defined: true
  strict_order_required: true
  command_sequence_documented: true
  stop_conditions_defined: true
  human_approval_checkpoint_defined: true
  evidence_preservation_required: true
  validation_usage_defined: true
  audit_usage_defined: true
  unsupported_paths_documented: true
  autonomous_lifecycle_authority: false
  automatic_approval_creation_allowed: false
  supported_mutation_paths:
    - complete-active
  unsupported_mutation_paths:
    - needs_review
    - failed
    - blocked
    - manual_abort
```

## 14. Known Limitations
This workflow document does not implement:
- new commands
- new validators
- new audit behavior
- approval enforcement
- approval record writing
- new lifecycle mutation paths
- autonomous workflow execution
- background runner mode

## 15. Final Rule
A task may be considered lifecycle-completed only when the controlled completion workflow has been followed in order, required durable evidence exists, approval is explicit when required, and the controlled complete-active mutation path has actually mutated the active task lifecycle state.
