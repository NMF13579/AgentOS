# Controlled Execution Session Architecture

## Purpose

This document defines the architecture of M58 — Controlled Execution Session.

M58 controls how AgentOS opens, bounds, observes, and closes a controlled execution session. M58 does not verify the final result. M58 does not approve task completion. M58 does not replace M59 verification.

M58 output is structured as input for M59 verification.

## Preconditions

Before any M58 task begins, the following must hold:

- `reports/m58-m57-completion-intake.md` exists and contains `FINAL_STATUS: M58_INTAKE_READY` or `FINAL_STATUS: M58_INTAKE_READY_WITH_WARNINGS`
- `reports/m58-m57-completion-intake.md` contains `MAY_PROCEED_TO_M58_PLANNING: true`
- `reports/m57-completion-review.md` exists with `final_status: M57_EXECUTION_AUTHORIZATION_COMPLETE` or `M57_EXECUTION_AUTHORIZATION_COMPLETE_WITH_WARNINGS`
- No M59 verification artifacts exist prematurely
- No approval records or lifecycle mutations have been performed

If preconditions fail, M58 planning must not begin and must report `PRECONDITION_FAILED_M58_INTAKE_NOT_READY`.

## M58 Position in the Execution Chain

```
M56 — Execution Readiness
  → M57 — Execution Authorization Boundary
    → M58 — Controlled Execution Session
      → M59 — Execution Result Verification
```

M58 must not start from M56 readiness alone. M58 must not start from M57 authorization alone. M58 must independently validate M57 completion via the M58 intake check before any M58 planning work.

M58 must not treat M57 authorization as task completion.

## Approved M58 Task Chain

- 58.0 — M57 Completion Intake
- 58.1 — Controlled Execution Session Architecture
- 58.2 — Execution Session Request Contract
- 58.3 — Execution Session Preconditions Contract
- 58.4 — Execution Session Boundary Contract
- 58.5 — Execution Session Record / Output Contract
- 58.6 — Controlled Execution Session Policy
- 58.7 — Controlled Execution Session CLI
- 58.8.1 — Positive Fixtures
- 58.8.2 — Negative Fixtures
- 58.9 — Fixture Runner
- 58.10 — Integration Summary
- 58.11 — Action Review
- 58.12 — Evidence Report
- 58.13 — Completion Review

The approved M58 task chain must not be expanded beyond 58.13 without an explicit architecture decision.

## Core Boundary

M58 controls execution session.
M58 does not verify final result.
M58 does not approve task completion.
M58 does not merge, push, release, or lifecycle-complete.
M58 output is input for M59 verification.

## Architecture Layers

### 1. Intake Layer

Task: 58.0

Reads the M57 completion review. Classifies M58 intake readiness. Does not start M58 execution. Does not authorize M58. Only determines whether M58 planning may begin.

### 2. Architecture Layer

Task: 58.1

Defines architecture, responsibilities, authority boundaries, artifact flow, and handoff from M58 to M59. This task only. Does not implement any M58 component.

### 3. Session Request Contract Layer

Task: 58.2

Defines the machine-readable input contract for an execution session request. Specifies required fields, allowed values, and validation rules. Does not implement the session.

### 4. Preconditions Contract Layer

Task: 58.3

Defines the machine-readable preconditions that must hold before an execution session may open. Includes readiness checks, authorization checks, and boundary assertions. Does not open the session.

### 5. Session Boundary Contract Layer

Task: 58.4

Defines the execution session boundary model. Covers scope, command, write, protected path, and session-state constraints. See Boundary Subcomponents section. Does not enforce the boundary itself — enforcement is the responsibility of downstream CLI and policy.

### 6. Session Record / Output Contract Layer

Task: 58.5

Defines the machine-readable output contract for a closed execution session. Specifies what data must be recorded, what format it must take, and what fields are required for M59 verification input. Does not run the session.

### 7. Policy Layer

Task: 58.6

Defines the controlled execution session policy: what is allowed, what is forbidden, how boundary violations are handled, and what the session close criteria are. Does not implement the CLI.

### 8. CLI Layer

Task: 58.7

Implements the read-only or session-control CLI that enforces the policy and boundary contracts. Must be able to classify session requests as CONFIRMED, NOT_CONFIRMED, or BLOCKED. Does not start execution directly.

### 9. Fixtures Layer

Tasks: 58.8.1 (positive), 58.8.2 (negative)

Provides test fixture data for the CLI. Positive fixtures prove correct handling of valid, well-formed session requests. Negative fixtures prove fail-closed behavior for invalid, blocked, or unsafe inputs.

### 10. Fixture Runner Layer

Task: 58.9

Implements the test harness that runs the CLI against fixture manifests and verifies expected results and exit codes. Does not authorize execution.

### 11. Integration Summary Layer

Task: 58.10

Summarizes the structural connection and validation results of the M58 execution session chain. Does not authorize execution.

### 12. Action Review Layer

Task: 58.11

Machine-readable review that checks whether only allowed artifacts were created and no forbidden actions were performed during M58. Does not authorize execution.

### 13. Evidence Report Layer

Task: 58.12

Summarizes the evidence produced by M58. Records whether the M58 execution session chain is supported by integration and action-review evidence. Does not authorize execution.

### 14. Completion Review Layer

Task: 58.13

Closes M58 as a milestone review artifact. Records final M58 status. Sets `may_proceed_to_m59_verification` flag. Does not start M59. Does not approve execution. Does not mutate lifecycle state.

### 15. Handoff to M59 Layer

Defined within 58.13. The M58 completion review produces a structured handoff record that M59 uses as its intake source. M59 must independently validate M58 completion before M59 planning.

## Artifact Flow

```
M57 completion review
→ M58 intake (58.0)
→ M58 architecture (58.1)
→ M58 session request contract (58.2)
→ M58 preconditions contract (58.3)
→ M58 session boundary contract (58.4)
→ M58 session record / output contract (58.5)
→ M58 policy (58.6)
→ M58 CLI (58.7)
→ M58 positive fixtures (58.8.1)
→ M58 negative fixtures (58.8.2)
→ M58 fixture runner (58.9)
→ M58 integration summary (58.10)
→ M58 action review (58.11)
→ M58 evidence report (58.12)
→ M58 completion review (58.13)
→ M59 verification planning
```

## Responsibility Matrix

| Layer                        | Task  | Creates              | Must Not Do                         |
|------------------------------|-------|----------------------|-------------------------------------|
| Intake                       | 58.0  | Intake report        | Start M58, authorize execution      |
| Architecture                 | 58.1  | Architecture doc     | Implement any component             |
| Session Request Contract     | 58.2  | Input schema/doc     | Run session                         |
| Preconditions Contract       | 58.3  | Preconditions schema | Open session                        |
| Session Boundary Contract    | 58.4  | Boundary doc/schema  | Enforce boundary                    |
| Session Record/Output        | 58.5  | Output schema/doc    | Run session                         |
| Policy                       | 58.6  | Policy doc           | Implement CLI                       |
| CLI                          | 58.7  | CLI script           | Start execution directly            |
| Fixtures (positive)          | 58.8.1| Fixture files        | Run fixtures                        |
| Fixtures (negative)          | 58.8.2| Fixture files        | Run fixtures                        |
| Fixture Runner               | 58.9  | Runner script        | Authorize execution                 |
| Integration Summary          | 58.10 | Summary report       | Authorize execution                 |
| Action Review                | 58.11 | JSON review          | Authorize execution                 |
| Evidence Report              | 58.12 | Evidence report      | Authorize execution                 |
| Completion Review            | 58.13 | Completion report    | Start M59, approve execution        |

## Session Boundary Model

The M58 session boundary model constrains all aspects of a controlled execution session. It is defined in `58.4 — Execution Session Boundary Contract` as a unified contract.

The boundary model governs:

- What scope (files, directories, targets) the session may touch
- What commands the session may execute
- What writes the session may perform
- Which paths are protected from modification
- What constitutes a valid open, active, and closed session state
- When and how a session may be closed

A session operating outside these boundaries must be classified as a boundary violation and recorded as such in the session record.

## Boundary Subcomponents

The following are architectural subcomponents of `58.4 — Execution Session Boundary Contract`. They are defined and enforced within that single task. They are not separate downstream task IDs.

- **Scope boundary**: defines which files, directories, modules, or targets the session may access or modify.
- **Command boundary**: defines which commands or operations are allowed and which are forbidden during a session.
- **Write boundary**: defines which paths and file types the session may write to.
- **Protected path boundary**: defines paths that must never be modified, read in forbidden ways, or inspected outside the allowed scope.
- **Session state boundary**: defines valid session states (OPEN, ACTIVE, CLOSED, VIOLATED) and allowed transitions.
- **Session close boundary**: defines conditions under which a session may be closed, and which close states require M59 verification before proceeding.

Scope, command, write, protected path, and session-state boundaries are subcomponents of 58.4 — Execution Session Boundary Contract, not separate downstream task IDs.

## Session Record and Output Model

The session record is defined in `58.5 — Execution Session Record / Output Contract`. It must capture:

- Session request reference
- Precondition check results
- Session boundary classification
- Commands or operations observed during the session
- Output artifacts produced
- Any boundary violations detected
- Session close state
- Structured fields sufficient for M59 verification input

The session record must be designed as input for M59 verification. It must not claim execution result approval or task completion.

## Result Handoff to M59

M58 closes with the completion review (58.13). The completion review produces:

- Final M58 status
- `may_proceed_to_m59_verification` flag
- Reference to the session record as M59 input

M59 must independently validate M58 completion before M59 planning. M58 does not verify the result. M58 does not approve the task. M58 does not replace M59.

The handoff is a structured boundary, not an authorization.

## Non-Authority Rules

M58 architecture does not start execution.
M58 architecture does not authorize task completion.
M58 architecture does not verify execution result.
M58 architecture does not create an execution session.
M58 architecture does not create approval.
M58 architecture does not mutate lifecycle state.
M58 architecture only defines the structure for future controlled execution session tasks.

M58 must not approve, merge, push, release, or lifecycle-complete.
M58 output must be designed as input for M59 verification.

## Forbidden Architecture Claims

M58 must not claim:

- execution result is verified
- task is complete
- task is approved
- task may be merged
- task may be pushed
- lifecycle state may be mutated
- human review is replaced
- M59 verification is optional
- M58 downstream task map extends beyond 58.13

## Downstream Task Map

The following M58 tasks are approved. No task ID beyond 58.13 may be added without an explicit architecture decision.

- 58.2 — Execution Session Request Contract
- 58.3 — Execution Session Preconditions Contract
- 58.4 — Execution Session Boundary Contract
- 58.5 — Execution Session Record / Output Contract
- 58.6 — Controlled Execution Session Policy
- 58.7 — Controlled Execution Session CLI
- 58.8.1 — Positive Fixtures
- 58.8.2 — Negative Fixtures
- 58.9 — Fixture Runner
- 58.10 — Integration Summary
- 58.11 — Action Review
- 58.12 — Evidence Report
- 58.13 — Completion Review

M58 architecture preserves the approved downstream task map through 58.13.

## Known Gaps

- Actual session execution logic (runner or agent) is deferred. M58 CLI (58.7) defines the interface and classification only; it does not implement an execution engine.
- Session observability and logging format details are deferred to 58.5.
- Protected path enumeration is deferred to 58.4.
- Boundary violation handling details (automatic close vs. warning) are deferred to 58.6.

## Final Architecture Status

FINAL_STATUS: M58_ARCHITECTURE_DEFINED

This status means only that the architecture document exists and can guide later M58 tasks.
It does not mean execution has started.
