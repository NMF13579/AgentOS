## Flow Summary
M44 converts approved intent into queue-ready task contracts while preserving non-approval boundaries and lifecycle constraints.

## Required Inputs
- Approved Spec input
- Approved UX input
- UI Contract dependency
- Existing or planned task lifecycle constraints

## Approved Spec Input
- Approved Spec is mandatory.
- No approved Spec -> no decomposition.

## Approved UX Input
- Approved UX is mandatory.
- No approved UX -> no decomposition.

## UI Contract Input
- UI Contract dependency is mandatory for UI-related decomposition.
- No UI Contract for UI work -> no UI task decomposition.

## Existing or Planned Task State Constraints
- Existing lifecycle artifacts checked:
  - `docs/TASK-STATE-MACHINE.md` FOUND
  - `docs/TASK-TRANSITION-RULES.md` FOUND
- Treat as upstream constraints, not replaced by M44.

## Task Candidate Extraction
- Extract candidates from Spec requirements and UX steps.
- Attach rendering constraints from UI Contract dependency when present.
- No scope -> no task.

## Task Splitting Rules
- Split by implementation concern and boundary clarity.
- Ensure each candidate has explicit acceptance criteria and validation plan.
- No acceptance criteria -> no task.
- No validation plan -> no task.

## Task Merging Rules
- Merge only when boundaries, risk, and validation semantics remain clear.
- Queue convenience must not weaken traceability.

## Dependency Mapping
- Record upstream/downstream dependencies explicitly.
- Blocked dependency -> task cannot be marked ready.

## Queue Entry Preparation
- Prepare queue-ready contracts with scope, risk, dependencies, and validation plan.
- Queue orders work, but does not authorize work.

## Validation Before Queue
- Validate structure completeness and dependency state.
- Validation is a readiness check, not approval.

## Human Review Boundary
- Task decomposition does not approve execution.
- Task queue readiness does not approve execution.
- Task validation does not approve execution.
- UI readiness does not approve execution.
- Human approval remains separate from decomposition.
- Existing task state readiness does not replace HumanApprovalGate.
- Missing upstream artifact documentation does not authorize task execution.

## Final Output of M44
- Queue-ready task contracts for human-reviewed execution planning.
- No task execution and no autopilot execution in M44.

Approved Spec
↓
Approved UX
↓
UI Contract
↓
Task Candidates
↓
Task Contracts
↓
Task Queue
↓
M45 Controlled Autopilot

## Known Gaps
- KNOWN_GAP: `docs/UI-SEMANTIC-COMPONENT-CONTRACT.md` is missing.
- KNOWN_GAP: `docs/DESIGN-TOKENS-POLICY.md` is missing.
- KNOWN_GAP: `docs/UI-REPLACEABILITY-POLICY.md` is missing.
- UI task decomposition cannot be complete until the UI Contract artifact exists.
- Missing upstream artifact -> record KNOWN_GAP, do not invent evidence.
