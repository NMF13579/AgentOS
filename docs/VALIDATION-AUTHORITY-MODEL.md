---
type: contract
module: m73-validation-authority
status: draft
authority: supporting
created: 2026-05-30
source_of_truth: markdown
derived: false
---

# Validation Authority Model

## Purpose
The purpose of this document is to define the validation authority hierarchy and boundaries for the AgentOS project. It establishes a formal contract specifying how validation results, execution triggers, and human approvals are structured and separated.

## Authority Hierarchy
The validation authority in AgentOS is structured in the following strict hierarchy:
1. Markdown/YAML validation contracts = source of truth
2. Validator scripts = deterministic implementation of scoped checks
3. Thin dispatcher = routing/orchestration only
4. Compatibility wrappers = non-authoritative convenience layer
5. CI workflows = execution surface only
6. Reports = evidence only
7. Human review = approval layer

No script can create human approval.
No CI result can create human approval.
No evidence report can create human approval.
No dispatcher result can create task completion.

## Source of Truth Rules
Markdown/YAML contracts are source of truth.
JSON/index/cache artifacts are derived/navigation only.
Generated reports are evidence only.
Runtime outputs are execution evidence only.
VALIDATORS.md is supporting documentation unless explicitly classified otherwise by governance.

The model must not create a new JSON authority.
The model must not make CI the source of truth.
The model must not make agentos-validate.py the source of truth.

## Validator Script Role
Validator scripts are deterministic implementations of scoped validation checks.
Validator scripts may:
* check stable deterministic conditions
* return documented result tokens
* return documented exit codes
* emit evidence

Validator scripts must not:
* approve work
* mark tasks complete
* mutate lifecycle state unless explicitly scoped by a future task
* silently change validation semantics
* hide failed checks
* convert UNKNOWN to PASS
* convert NOT_RUN to PASS

## Thin Dispatcher Role
The thin dispatcher serves as the routing and orchestration layer only.
Dispatcher is not approval.
Dispatcher is not lifecycle mutation.
Dispatcher is not task completion.

Dispatcher may:
* accept a known validation command
* route to known child validator
* run known child validators
* capture stdout
* capture stderr
* capture exit code
* aggregate result according to documented rules
* fail closed on malformed, missing, or inconsistent child validator output

Dispatcher must not:
* approve anything
* complete tasks
* mutate lifecycle
* modify files unless explicitly scoped by a future implementation task
* auto-fix
* self-heal
* hide child validator failures
* reinterpret child validator result into false PASS
* treat evidence as approval
* start next milestone
* trigger cascading automation

Dispatcher must not reinterpret child validator result into false PASS.
UNKNOWN must not become PASS.
NOT_RUN must not become PASS.
Child validator failure must not be hidden.
Malformed child output must fail closed.
Missing child validator must fail closed.

## Wrapper Role
Wrappers are compatibility or convenience entrypoints that may delegate to dispatcher but must not create independent validation authority.
Wrappers must not:
* invent PASS
* hide dispatcher failure
* modify files unexpectedly
* create reports unexpectedly
* claim approval
* claim lifecycle completion
* override dispatcher result semantics

## CI Role
CI workflows serve as the execution surface only.
CI may:
* run dispatcher
* store logs
* expose artifacts
* fail or pass a platform job based on dispatcher exit code

CI must not:
* create approval
* claim human review
* claim task completion
* claim branch protection unless verified by external platform evidence
* claim platform enforcement unless verified by external platform evidence

CI PASS ≠ approval.
CI PASS ≠ task completion.
CI job success only means the configured command completed according to its configured semantics.

## Evidence Report Role
Reports serve as evidence artifacts only.
Reports may:
* record validation results
* record warnings
* record blockers
* record unknowns
* carry forward risk

Reports must not:
* approve work
* complete work
* mutate lifecycle
* authorize protected/canonical writes
* suppress unknowns
* convert warnings into clean PASS

Evidence ≠ approval.
Evidence report is not completion review unless explicitly scoped as completion review.
Evidence report does not authorize lifecycle mutation.

## Human Approval Layer
Human approval is above all validation signals.
Human approval cannot be simulated by scripts, reports, CI, dispatcher, wrappers, or agent-written claims.
Protected/canonical writes require explicit human checkpoint evidence when M72 governance requires it.
Agent-written claims do not satisfy human checkpoint evidence.

## Result Semantics Boundary
The result semantics boundaries are defined as follows:
- PASS is not approval.
- PASS_WITH_WARNINGS is not clean PASS.
- BLOCKED is not failure to be hidden.
- UNKNOWN is not OK.
- NOT_RUN is not PASS.
- ERROR is not PASS.

A higher-level entrypoint must not weaken a lower-level child validator result.
Examples:
- Child BLOCKED -> Dispatcher must not report PASS.
- Child UNKNOWN -> Dispatcher must not report PASS.
- Child NOT_RUN -> Dispatcher must not report PASS.
- Malformed child output -> Dispatcher must fail closed.
- Missing child validator -> Dispatcher must fail closed.

## Authority Drift Risks
The following validation authority drift risks are identified:
* multiple validation entrypoints claiming authority
* wrapper returning different result than dispatcher
* CI treating job success as approval
* docs referencing outdated validation commands
* reports treated as approval
* JSON/index artifacts treated as source of truth
* child validator failure hidden by aggregator
* --help or discovery command causing side effects
* shell wrapper masking exit code
* protected/canonical governance bypassed by docs update

## Protected / Canonical Governance Boundary
M72 protected/canonical governance remains binding.
This document does not authorize protected/canonical writes.
This document does not update protected/canonical registries.
If a future task modifies protected/canonical artifacts, explicit human checkpoint evidence is required before the write when M72 policy requires it.
UNKNOWN protected/canonical status blocks writes.
Readiness does not authorize writes.
Evidence does not authorize writes.
PASS does not authorize writes.

## Forbidden Authority Claims
The validation authority model explicitly forbids these claims:
- Dispatcher PASS means approval.
- CI PASS means approval.
- Evidence means approval.
- Report existence means task completion.
- Wrapper success means validation authority.
- JSON output is source of truth.
- UNKNOWN can be treated as OK.
- NOT_RUN can be treated as PASS.
- Readiness starts next milestone.

## M73 Relationship
M73.2 creates the authority model only.
M73.2 does not implement dispatcher behavior.
M73.2 does not select the final dispatcher.
M73.2 does not modify scripts, wrappers, docs references, or CI workflows.
M73.2 does not start M73.3 automatically.
M73.2 does not start M74.

## Final Boundary Statement
The Validation Authority Model defines authority boundaries only.
It does not approve work.
It does not complete tasks.
It does not mutate lifecycle.
It does not authorize protected/canonical writes.
It does not start M73.3.
It does not start M74.
