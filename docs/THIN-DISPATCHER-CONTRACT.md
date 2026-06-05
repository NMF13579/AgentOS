---
type: contract
module: m73-thin-dispatcher
status: draft
authority: supporting
created: 2026-05-30
source_of_truth: markdown
derived: false
---
This document is a Markdown contract artifact for M73 planning and implementation.
It is not approval.
It is not completion review.
It is not IO / exit-code contract.
It does not update M72 registries.
It does not automatically become a protected artifact.
It does not automatically become a canonical artifact.
If future governance requires protection/canonical registration, that must be handled by a separate explicit task with M72 protected-change rules.

# Thin Dispatcher Contract

## Purpose
This document establishes the Thin Dispatcher Contract for the AgentOS project. It defines the strict operational boundaries, permitted responsibilities, and forbidden capabilities of the validation dispatcher.

## Dispatcher Definition
The dispatcher is defined as the routing and orchestration layer only.
Dispatcher is not approval.
Dispatcher is not lifecycle mutation.
Dispatcher is not task completion.
Dispatcher is not cleanup authorization.
Dispatcher is not source of truth.
Dispatcher is not self-heal.
Dispatcher is not auto-fix.
Dispatcher routes validation.
Dispatcher does not own validator truth.

## Dispatcher Authority Boundary
The dispatcher may coordinate validation execution, but it must not create authority beyond the contracts and child validators it invokes.
The dispatcher must not become a competing source of truth against:
* Markdown/YAML contracts
* M72 protected/canonical governance
* child validator contracts
* human approval evidence

The dispatcher must not weaken source contracts.
The dispatcher must not replace human review.

## Allowed Dispatcher Responsibilities
The dispatcher may:
* accept a known CLI command
* parse dispatcher CLI arguments
* route to known child validators
* invoke known child validators
* capture stdout
* capture stderr
* capture exit code
* parse declared machine-readable child output when available
* preserve raw child evidence
* aggregate child results according to documented rules
* return a unified dispatcher-level result
* return a dispatcher-level exit code according to the M73.4 IO contract
* fail closed on unknown, missing, malformed, or inconsistent child output

The dispatcher may not use this allowed scope to expand task scope.

## Forbidden Dispatcher Responsibilities
The dispatcher must not:
* approve anything
* complete tasks
* mutate lifecycle
* modify task state
* mark milestones complete
* authorize protected/canonical writes
* perform cleanup
* delete files
* auto-fix files
* self-heal files
* rewrite child validators
* silently change child validator semantics
* hide child validator failure
* convert UNKNOWN to PASS
* convert NOT_RUN to PASS
* convert BLOCKED to PASS
* convert ERROR to PASS
* convert PASS_WITH_WARNINGS to clean PASS
* treat evidence as approval
* claim CI/platform enforcement
* start next milestone
* start M74
* create M74 fixtures
* trigger cascading automation

## Child Validator Boundary
Child validators own scoped deterministic checks.
The dispatcher invokes child validators but does not redefine their semantics.

Child validator failure must not be hidden.
Child validator BLOCKED must not become dispatcher PASS.
Child validator UNKNOWN must not become dispatcher PASS.
Child validator NOT_RUN must not become dispatcher PASS.
Malformed child output must fail closed.
Missing child validator must fail closed.
Child exit/result mismatch must fail closed.

The dispatcher may normalize output format, but it must not weaken child results.
If a child validator contract is missing, ambiguous, or unreadable, the dispatcher must fail closed or return a review-required blocked result.

## Aggregation Boundary
Aggregation is defined as mechanical result combination according to documented rules.
Aggregation must preserve:
* child result
* child exit code
* child stdout/stderr evidence
* child warning signals
* child blocker signals
* unknown signals
* not-run signals
* malformed output signals

Aggregation must not hide:
* failed checks
* unknowns
* warnings
* missing validators
* malformed outputs
* exit/result mismatch

Aggregation is not approval.
Aggregation is not completion.
Aggregation must not hide blockers.
Aggregation must not hide unknowns.
Aggregation must not convert warnings into clean PASS.

## Failure and Unknown Handling
Dispatcher must fail closed.
UNKNOWN is not OK.
NOT_RUN is not PASS.
ERROR is not PASS.

Required mappings at the contract level:
- UNKNOWN -> BLOCKED or review-required blocked result
- NOT_RUN -> not PASS
- missing child validator -> BLOCKED
- malformed child output -> BLOCKED
- child exit/result mismatch -> BLOCKED
- unsupported runtime validator state -> BLOCKED
- CLI misuse -> dispatcher error
- internal dispatcher error -> dispatcher error

## Side-Effect Boundary
Dispatcher discovery and help behavior must be side-effect free.
The dispatcher must not modify files during:
* --help
* command listing
* dry discovery
* validation planning
* unsupported command handling
* error handling

If any mode writes files, it must be explicitly scoped by a future task and must respect M72 protected/canonical governance.

## Cascading Automation Boundary
One signal = one action.
Dispatcher must not trigger cascading automation.

Forbidden cascade examples:
- validation -> auto-fix -> revalidate -> commit
- validation -> cleanup -> report -> lifecycle mutation
- CI job -> dispatcher -> self-heal -> commit
- dispatcher PASS -> task completion -> next milestone start

Any multi-step automation requires explicit human checkpoint between levels.

## Source of Truth Boundary
Markdown/YAML contracts remain source of truth.
JSON/index/cache artifacts are derived/navigation only.
Dispatcher output is runtime evidence only.
Dispatcher output is not source of truth.
The dispatcher must not create a new JSON authority.
The dispatcher must not treat generated machine output as higher authority than Markdown/YAML contracts.

## Evidence Boundary
Dispatcher output is evidence.
Evidence ≠ approval.
Dispatcher evidence may support review, but it does not approve work and does not complete tasks.
The dispatcher must preserve child evidence when aggregating.
If evidence is incomplete, malformed, or missing, the dispatcher must not claim clean PASS.

## Human Approval Boundary
Human approval cannot be simulated by dispatcher, scripts, reports, wrappers, CI, or agent-written claims.
The dispatcher must never claim:
* human approval
* human checkpoint completion
* protected write authorization
* task acceptance
* milestone completion

## Protected / Canonical Governance Boundary
M72 protected/canonical governance remains binding.
This contract does not authorize protected/canonical writes.
Dispatcher implementation does not authorize protected/canonical writes.
UNKNOWN protected/canonical status blocks writes.
Readiness does not authorize writes.
Evidence does not authorize writes.
PASS does not authorize writes.
Any future dispatcher implementation that modifies protected/canonical artifacts requires explicit human checkpoint evidence before the write when M72 policy requires it.

## Relationship to M73.4
M73.3 defines dispatcher behavioral boundaries.
M73.4 defines dispatcher IO and exit-code semantics.
M73.3 must not replace M73.4.
M73.3 may refer to failure classes, but exact result/exit-code matrix belongs to M73.4.

## Relationship to M74
M73.3 does not create regression fixtures.
M73.3 does not start M74.
M74 owns dispatcher regression fixtures.
M73.3 may identify required future regression coverage, but it must not create M74 fixtures.

## Forbidden Claims
The document explicitly forbids these claims:
- Dispatcher PASS means approval.
- Dispatcher PASS means task completion.
- Dispatcher PASS means protected write authorization.
- Dispatcher PASS starts next milestone.
- Dispatcher output is source of truth.
- Dispatcher can override child validator result.
- Dispatcher can ignore UNKNOWN.
- Dispatcher can ignore NOT_RUN.
- Dispatcher can hide child validator failure.
- Dispatcher can self-heal.
- Dispatcher can auto-fix.
- Dispatcher can start M74.

## Final Boundary Statement
The Thin Dispatcher Contract defines dispatcher boundaries only.
It does not approve work.
It does not complete tasks.
It does not mutate lifecycle.
It does not authorize protected/canonical writes.
It does not define the final IO / exit-code matrix.
It does not implement dispatcher behavior.
It does not select the final dispatcher.
It does not start M73.4.
It does not start M74.
