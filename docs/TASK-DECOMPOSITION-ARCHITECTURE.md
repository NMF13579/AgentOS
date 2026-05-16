## Purpose
Define M44 task decomposition architecture from approved Spec/UX/UI inputs into scoped task contracts.

M44 decomposes approved intent into executable task contracts.
M44 does not execute implementation work.

## Position in Roadmap
- M41: Spec Builder
- M42: Research Intake
- M43: Spec-to-UX Pipeline
- M43.5: Neutral UI Foundation / UI Contract
- M44: Spec/UX-to-Task Decomposition
- M45: Controlled Autopilot (future, not started here)

## Input Authority
- Approved Spec defines WHAT.
- Approved UX defines HOW USER EXPERIENCES IT.
- UI Contract dependency defines HOW IT MAY BE RENDERED.
- M44 defines WHAT AGENT MAY IMPLEMENT.

## Existing Task Lifecycle Context
- Existing lifecycle constraints were checked:
  - `docs/TASK-STATE-MACHINE.md` FOUND
  - `docs/TASK-TRANSITION-RULES.md` FOUND
- These are upstream constraints and are not replaced by M44.

## Decomposition Flow
1. Validate presence of approved inputs.
2. Detect implementation areas.
3. Split into scoped task candidates.
4. Attach acceptance criteria and validation plan.
5. Record dependencies and risk metadata.
6. Prepare queue-ready task contracts (without execution approval).

## Implementation Area Detection
- Functional area from approved Spec requirements.
- User interaction area from approved UX flow.
- Rendering constraints from UI Contract dependency.
- Cross-cutting constraints: validation, safety, and scope boundaries.

## Task Boundary Rules
- No scope -> no task.
- No acceptance criteria -> no task.
- No validation plan -> no task.
- Boundaries must isolate one implementation concern per task where practical.
- Scope must be explicit in in-scope/out-of-scope form.

## Dependency Rules
- Blocked dependency -> task cannot be marked ready.
- Dependencies must include upstream artifact references.
- Dependencies must distinguish hard blockers vs sequencing dependencies.

## Priority Rules
- Priority based on user impact, safety impact, and dependency criticality.
- Priority must not bypass lifecycle constraints.
- Priority ordering in queue is planning metadata only.

## Risk Level Rules
- LOW/MEDIUM/HIGH/CRITICAL must be assigned per task contract.
- HIGH or CRITICAL risk -> human approval metadata required.

## Validation Plan Rules
- Every task must include explicit validation plan.
- Validation plan must reference expected checks and evidence outputs.
- Task validation does not approve execution.

## Queue Readiness Rules
- Queue orders work, but does not authorize work.
- Task Contract readiness is a prerequisite for execution, not execution approval.
- Task queue readiness does not approve execution.

## Non-Approval Boundary
- Task decomposition does not approve execution.
- Task queue readiness does not approve execution.
- Task validation does not approve execution.
- UI readiness does not approve execution.
- Human approval remains separate from decomposition.
- Existing task state readiness does not replace HumanApprovalGate.
- Missing upstream artifact documentation does not authorize task execution.

## Relationship to Existing or Planned State Machine
- M44 consumes existing or planned task lifecycle constraints.
- M44 does not alter state machine rules.
- Lifecycle alignment is bounded by upstream task-state and transition documents.

## Relationship to M45 Autopilot
- M44 prepares decomposition-ready contracts only.
- M44 must not start M45 autopilot.
- Any M45 execution path remains blocked until separate approval and controls.

## Known Gaps
- KNOWN_GAP: `docs/UI-SEMANTIC-COMPONENT-CONTRACT.md` is missing.
- KNOWN_GAP: `docs/DESIGN-TOKENS-POLICY.md` is missing.
- KNOWN_GAP: `docs/UI-REPLACEABILITY-POLICY.md` is missing.
- UI task decomposition cannot be complete until the UI Contract artifact exists.
- Missing upstream artifact -> record KNOWN_GAP, do not invent evidence.
