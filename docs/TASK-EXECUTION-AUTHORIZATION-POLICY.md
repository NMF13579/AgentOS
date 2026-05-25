---
type: policy
milestone: M57
task: 57.5
title: Execution Authorization Policy
status: draft
source_intake: reports/m57-m56-completion-intake.md
source_architecture: docs/TASK-EXECUTION-AUTHORIZATION-ARCHITECTURE.md
source_input_contract: docs/TASK-EXECUTION-AUTHORIZATION-INPUT-CONTRACT.md
source_preconditions_contract: docs/TASK-EXECUTION-AUTHORIZATION-PRECONDITIONS-CONTRACT.md
source_output_contract: docs/TASK-EXECUTION-AUTHORIZATION-OUTPUT-CONTRACT.md
authority: policy-only
execution_authorized: false
execution_started: false
approval_created: false
lifecycle_mutation_authorized: false
m58_authorized: false
m58_started: false
---

# Execution Authorization Policy

## 1. Purpose

This document defines the M57 execution authorization policy.

## 2. Policy Summary

Execution authorization policy is not execution.
Execution authorization policy does not authorize execution by itself.
Execution authorization policy does not start execution.
Execution authorization policy does not start M58.
Execution authorization policy does not create approval records.
Execution authorization policy does not authorize lifecycle mutation.
Execution authorization policy does not modify tasks/active-task.md.
Execution authorization policy is not approval.
Execution authorization policy is not CLI implementation.
Execution authorization policy is not evidence approval.
Execution authorization policy is not completion review.
M56 COMPLETE does not automatically authorize M58.
M56 COMPLETE_WITH_LIMITATIONS does not automatically authorize M58.
M58 planning may be considered only after M57 completion review.
Exit code 0 is not execution.
Exit code 0 does not start M58.
Exit code 0 is not lifecycle mutation.
Exit code 0 is not approval.
Unknown policy decision must fail closed.
Malformed source data must fail closed.
Unsafe authority claims must fail closed.
Premature M58 artifacts must fail closed.
Already-started execution must fail closed.
Contradictory cross-source claims must fail closed.
Empty required traceability must fail closed.
Empty required boundaries must fail closed.
Empty non-authority markers must fail closed.

## 3. Decision Model

The decision model consumes status fields from M56 completion, M56 evidence, M57 input, M57 preconditions, and safety properties to determine the policy outcome.

## 4. Decision Priority

The decision priority order is defined as:
```text
EXECUTION_AUTHORIZATION_POLICY_BLOCKED > EXECUTION_AUTHORIZATION_POLICY_NOT_CONFIRMED > EXECUTION_AUTHORIZATION_POLICY_CONFIRMED_WITH_LIMITATIONS > EXECUTION_AUTHORIZATION_POLICY_CONFIRMED
```

## 5. Policy Decisions

The allowed policy decisions are:
* `EXECUTION_AUTHORIZATION_POLICY_CONFIRMED`
* `EXECUTION_AUTHORIZATION_POLICY_CONFIRMED_WITH_LIMITATIONS`
* `EXECUTION_AUTHORIZATION_POLICY_NOT_CONFIRMED`
* `EXECUTION_AUTHORIZATION_POLICY_BLOCKED`

## 6. Policy-to-Result Mapping

The mapping from policy decision to output result is defined as:
* `EXECUTION_AUTHORIZATION_POLICY_CONFIRMED -> EXECUTION_AUTHORIZATION_CONFIRMED`
* `EXECUTION_AUTHORIZATION_POLICY_CONFIRMED_WITH_LIMITATIONS -> EXECUTION_AUTHORIZATION_CONFIRMED_WITH_LIMITATIONS`
* `EXECUTION_AUTHORIZATION_POLICY_NOT_CONFIRMED -> EXECUTION_AUTHORIZATION_NOT_CONFIRMED`
* `EXECUTION_AUTHORIZATION_POLICY_BLOCKED -> EXECUTION_AUTHORIZATION_BLOCKED`

## 7. Result-to-Exit-Code Mapping

The mapping from output result to exit code is defined as:
* `EXECUTION_AUTHORIZATION_CONFIRMED -> 0`
* `EXECUTION_AUTHORIZATION_CONFIRMED_WITH_LIMITATIONS -> 0`
* `EXECUTION_AUTHORIZATION_NOT_CONFIRMED -> 1`
* `EXECUTION_AUTHORIZATION_BLOCKED -> 2`

## 8. M56 Final Status Policy

Core M56 policy mapping:
* `M56_EXECUTION_READINESS_COMPLETE -> may allow EXECUTION_AUTHORIZATION_POLICY_CONFIRMED if all other checks pass`
* `M56_EXECUTION_READINESS_COMPLETE_WITH_LIMITATIONS -> may allow EXECUTION_AUTHORIZATION_POLICY_CONFIRMED_WITH_LIMITATIONS if all other checks pass`
* `M56_EXECUTION_READINESS_INCOMPLETE -> EXECUTION_AUTHORIZATION_POLICY_NOT_CONFIRMED`
* `M56_EXECUTION_READINESS_BLOCKED -> EXECUTION_AUTHORIZATION_POLICY_BLOCKED`

Policy distinctions:
* M56_EXECUTION_READINESS_INCOMPLETE must be classified as EXECUTION_AUTHORIZATION_NOT_CONFIRMED by policy, not as a successful authorization.
* M56_EXECUTION_READINESS_BLOCKED must be classified as EXECUTION_AUTHORIZATION_BLOCKED by policy.

## 9. M56 Evidence Status Policy

The M56 evidence status policy is defined as:
* `M56_EXECUTION_READINESS_EVIDENCE_READY -> may allow authorization evaluation if all other checks pass`
* `M56_EXECUTION_READINESS_EVIDENCE_NOT_PASSING -> EXECUTION_AUTHORIZATION_POLICY_NOT_CONFIRMED`
* `M56_EXECUTION_READINESS_EVIDENCE_BLOCKED -> EXECUTION_AUTHORIZATION_POLICY_BLOCKED`

## 10. Authorization Input Status Policy

The authorization input status policy is defined as:
* `EXECUTION_AUTHORIZATION_INPUT_READY -> may allow confirmed policy decision if all other checks pass`
* `EXECUTION_AUTHORIZATION_INPUT_READY_WITH_LIMITATIONS -> may allow confirmed-with-limitations policy decision if all other checks pass`
* `EXECUTION_AUTHORIZATION_INPUT_NOT_READY -> EXECUTION_AUTHORIZATION_POLICY_NOT_CONFIRMED`
* `EXECUTION_AUTHORIZATION_INPUT_BLOCKED -> EXECUTION_AUTHORIZATION_POLICY_BLOCKED`

## 11. Preconditions Status Policy

The preconditions status policy is defined as:
* `EXECUTION_AUTHORIZATION_PRECONDITIONS_PASS -> may allow confirmed policy decision if all other checks pass`
* `EXECUTION_AUTHORIZATION_PRECONDITIONS_PASS_WITH_WARNINGS -> may allow confirmed-with-limitations policy decision if all other checks pass`
* `EXECUTION_AUTHORIZATION_PRECONDITIONS_NOT_READY -> EXECUTION_AUTHORIZATION_POLICY_NOT_CONFIRMED`
* `EXECUTION_AUTHORIZATION_PRECONDITIONS_BLOCKED -> EXECUTION_AUTHORIZATION_POLICY_BLOCKED`

## 12. Traceability Policy

Clean confirmed authorization requires M56 complete, M56 evidence ready, input ready, preconditions pass, traceability present, boundaries present, no blockers, no unsafe claims, no performed action violations, and no carry-forward limitations.

## 13. Boundary Policy

Confirmed with limitations requires no blockers and may result from M56 complete with limitations, input ready with limitations, preconditions pass with warnings, warnings, or carry-forward limitations.

## 14. Performed Actions Policy

The performed action violations policy is defined as:
* `active_task_modified: true -> EXECUTION_AUTHORIZATION_POLICY_BLOCKED`
* `approval_record_created: true -> EXECUTION_AUTHORIZATION_POLICY_BLOCKED`
* `lifecycle_mutation_performed: true -> EXECUTION_AUTHORIZATION_POLICY_BLOCKED`
* `execution_started: true -> EXECUTION_AUTHORIZATION_POLICY_BLOCKED`
* `m58_artifact_created: true -> EXECUTION_AUTHORIZATION_POLICY_BLOCKED`
* `m58_started: true -> EXECUTION_AUTHORIZATION_POLICY_BLOCKED`

## 15. Carry-Forward Limitations Policy

No carry-forward limitations are carried forward from the output contract. The M56 readiness limitation was closed in 57.4 Known Accepted Risks.

## 16. Warnings Policy

Warnings do not force a blocked status but prevent clean confirmation, requiring the confirmed-with-limitations decision.

## 17. Blockers Policy

Blockers will force the blocked decision.

## 18. Unsafe Authority Claims

Unsafe authority claims must fail closed.
The policy blocks unsafe authority claims equivalent to:
* `execution is approved`
* `execution is authorized`
* `M58 is authorized`
* `M58 may start`
* `M58 started`
* `approval has been created`
* `lifecycle mutation has been authorized`
* `tasks/active-task.md was modified by M57`

## 19. Malformed Source Policy

Malformed source data must fail closed.

## 20. Unknown Status Policy

Unknown status values in upstream contracts must fail closed.

## 21. Contradictory Source Policy

Contradictory cross-source claims must fail closed.

## 22. Empty Required Structures Policy

Empty required structures must fail closed:
* `Empty required traceability must fail closed.`
* `Empty required boundaries must fail closed.`
* `Empty non-authority markers must fail closed.`

## 23. No-M58-Start Policy

Execution authorization policy confirmed does not start M58.

## 24. No-Execution Policy

Execution authorization policy is not execution.

## 25. No-Approval Policy

Execution authorization policy is not approval.

## 26. No-Lifecycle-Mutation Policy

Execution authorization policy does not authorize lifecycle mutation.

## 27. No Active-Task Mutation Policy

Execution authorization policy does not modify tasks/active-task.md.

## 28. Relationship to M56

The policy consumes M56 final status and evidence reports to confirm that readiness checks are complete.

## 29. Relationship to M57 CLI

The policy establishes the logical rules that the CLI checks.

## 30. Relationship to M57 Output Contract

The policy maps its internal decisions directly to the statuses defined in the output contract.

## 31. Relationship to M58

The policy acts as a gate to prevent premature M58 session planning.

## 32. Downstream Implementation Requirements

Downstream implementation constraints:
* `The later M57 CLI must implement this policy without weakening any non-authority boundary.`
* `The later M57 CLI must return result and exit code according to the output contract.`
* `The later M57 CLI must not start M58, create M58 artifacts, execute active tasks, create approval records, or mutate lifecycle state.`

## 33. Non-Authority Boundary

Non-authority markers:
* `M57 execution authorization policy is not execution.`
* `M57 execution authorization policy does not authorize execution by itself.`
* `M57 execution authorization policy does not start execution.`
* `M57 execution authorization policy does not create approval records.`
* `M57 execution authorization policy does not authorize lifecycle mutation.`
* `M57 execution authorization policy does not authorize M58.`
* `M57 execution authorization policy does not start M58.`
* `M57 execution authorization policy does not modify tasks/active-task.md.`
* `M58 must independently validate M57 completion before any M58 planning work.`

## 34. Summary

This section summarizes the policy rules defined above.

The policy rules are:
* `EXECUTION_AUTHORIZATION_POLICY_BLOCKED outranks every other decision.`
* `EXECUTION_AUTHORIZATION_POLICY_NOT_CONFIRMED outranks confirmed-with-limitations and confirmed.`
* `EXECUTION_AUTHORIZATION_POLICY_CONFIRMED_WITH_LIMITATIONS outranks confirmed.`
* `Unknown policy decision must be treated as blocked.`
* `Unknown input status must be treated as blocked.`
* `Unknown preconditions status must be treated as blocked.`
* `Unknown M56 final status must be treated as blocked.`
* `Unknown M56 evidence status must be treated as blocked.`
* `Missing source data must be treated as blocked.`
* `Malformed source data must be treated as blocked.`
* `Contradictory source data must be treated as blocked.`
* `Empty required_traceability must be treated as blocked.`
* `Empty required_boundaries must be treated as blocked.`
* `Empty non_authority_markers must be treated as blocked.`
* `Unsafe authority claim must be treated as blocked.`
* `Any performed action violation must be treated as blocked.`
* `M56_EXECUTION_READINESS_INCOMPLETE must become not-confirmed, not confirmed-with-limitations.`
* `M56_EXECUTION_READINESS_BLOCKED must become blocked.`
* `M56_EXECUTION_READINESS_EVIDENCE_NOT_PASSING must become not-confirmed.`
* `M56_EXECUTION_READINESS_EVIDENCE_BLOCKED must become blocked.`
* `Input not ready must become not-confirmed.`
* `Input blocked must become blocked.`
* `Preconditions not ready must become not-confirmed.`
* `Preconditions blocked must become blocked.`
* `Carry-forward limitations must prevent clean confirmed.`
* `Warnings must prevent clean confirmed.`
* `Blockers must force blocked.`
* `M56 complete does not automatically authorize M58.`
* `Policy confirmed does not start M58.`
* `Policy confirmed does not authorize execution by itself.`
* `Policy confirmed does not approve the task.`
* `Policy confirmed does not mutate lifecycle.`
* `Policy confirmed does not modify tasks/active-task.md.`
* `Policy confirmed does not create approval records.`

Not confirmed means authorization cannot be confirmed, but no unsafe boundary violation was proven.
Blocked means authorization must fail closed due to unsafe, malformed, contradictory, unverifiable, or boundary-violating state.

## Final Status

FINAL_STATUS: M57_POLICY_DEFINED
may_proceed_to_57_6: true

This means only that the policy document exists and is valid.
It does not approve or authorize execution.
It does not mean M57 is complete.
It does not start M58 or allow M58 to start.
