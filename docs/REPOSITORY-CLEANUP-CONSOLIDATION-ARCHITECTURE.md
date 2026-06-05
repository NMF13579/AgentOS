# Repository Cleanup / Documentation & Script Consolidation Architecture

## Purpose

Define the M60 cleanup architecture boundaries for consolidating M56–M59 artifacts while preserving safety semantics.

## Scope

This document defines architecture and boundaries only for M60. It does not execute cleanup.

## Position After M59

M59 completion and M60 intake allow planning continuation into M60 architecture definition only.

## M60 Task Chain

60.0  — M59 Completion Intake
60.1  — Cleanup Architecture and Safety Preservation Boundary
60.2  — M56–M59 Artifact Inventory
60.3  — Source-of-Truth Classification
60.4  — Duplication and Drift Audit
60.5  — Registry Contract
60.6  — Registry Builder and Validator
60.7  — Validator Consolidation Plan
60.8  — Reusable Checks Consolidation
60.9  — Documentation Pruning Plan
60.10 — Safe Documentation Consolidation
60.11 — M56–M59 Regression Validation Runner
60.12 — Cleanup Integration Summary
60.13 — Cleanup Action Review
60.14 — Cleanup Evidence Report
60.15 — Cleanup Completion Review

M60 task chain ends at 60.15.
M60 must not introduce 60.16 or later tasks without explicit planning approval.

## Cleanup Philosophy

M60 cleanup is structural consolidation with semantic preservation.

## Safety Semantics Preservation Rule

M60 may change structure, not safety meaning.
M60 must not change M56–M59 safety semantics.
M60 must not introduce new execution flows.
M60 must not introduce new policy states.
M60 must not introduce new approval paths.
M60 must not introduce new result-verification semantics.
M60 must not weaken non-authority boundaries.
M60 must not convert PASS into approval.
M60 must not replace human review.

## Forbidden Semantic Changes

Forbidden:
- changing M56 execution readiness semantics
- changing M57 execution authorization semantics
- changing M58 controlled execution session semantics
- changing M59 execution result verification semantics
- changing policy decision mappings
- changing result mappings
- changing exit code mappings
- changing approval boundaries
- changing human review boundaries
- changing merge/push/release boundaries
- changing lifecycle mutation boundaries
- changing fixture oracle meanings
- changing runner result meanings
- changing completion review meanings

## Allowed Structural Changes

Allowed structural changes only:
- artifact inventory
- source-of-truth classification
- duplication audit
- drift audit
- registry creation
- registry validation
- validator consolidation planning
- safe reusable check extraction
- safe documentation pruning plan
- safe documentation consolidation
- regression validation runner creation
- cleanup reports

Allowed structural changes must not alter safety semantics.

## Semantic Source Preservation

Semantic source classes:
- policy documents
- contract documents
- schema files
- CLI behavior documents
- completion reviews
- action reviews
- evidence reports
- fixture oracle files
- runner result contracts

Semantic source artifacts must not be downgraded, deleted, replaced, or overridden by summary documents, registries, indexes, dashboards, or overview docs.

## Source-of-Truth Hierarchy

1. Prior milestone completion reviews and explicit policy/contract documents
2. Contract documents and schemas
3. CLI behavior documents and implementation scripts
4. Fixture oracle files and runner result contracts
5. Evidence reports and action reviews
6. Registry and generated indexes
7. Overview docs, summaries, dashboards, and navigation documents

If a registry, generated index, overview document, summary, or dashboard conflicts with canonical contracts, policies, schemas, CLI behavior, fixture oracles, or completion reviews, the registry/index/overview/summary/dashboard is stale or invalid.

## Registry Role

Registry is a navigation and validation aid.
Registry does not override canonical Markdown contracts, policy documents, schemas, CLI contracts, fixture oracles, or completion reviews.
If registry conflicts with canonical source-of-truth artifacts, the registry is considered stale or invalid.
Registry must not introduce new authority.
Registry must not create approval.
Registry must not change execution verification semantics.

## Validator Consolidation Role

Reusable validators may orchestrate or check existing M56–M59 semantics.
Reusable validators must not create new policy decisions.
Reusable validators must not create new result meanings.
Reusable validators must not downgrade BLOCKED to WARNING.
Reusable validators must not convert UNKNOWN, NOT_RUN, malformed, missing, or contradictory input into PASS.

## Documentation Pruning Boundary

No safety-boundary text may be removed unless a canonical replacement reference exists.
No non-authority boundary may be removed unless the replacement source is canonical, current, and validated.
Documentation pruning must not change policy decisions, exit code mappings, final statuses, approval semantics, execution boundaries, or result verification semantics.
Human-facing explanatory duplication may remain when it preserves local readability and does not create policy drift.
Safety-critical boundary repetition may remain intentionally.
Not all repetition is bad.

## Reusable Checks Boundary

Reusable checks may consolidate repeated verification mechanics only when they preserve existing semantics and boundaries.

## Regression Validation Boundary

Regression runner validates preservation of M56–M59 mechanics.
Regression runner does not approve task completion.
Regression runner does not verify a real execution result.
Regression runner does not replace human review.
Regression runner does not authorize merge, push, release, or lifecycle mutation.
Regression runner does not start M61 or M62.

## M61 and M62 Non-Start Boundary

M60 does not start M61.
M60 does not start M62.
M60 completion may recommend next planning direction only.
may_proceed_to_m61_hardening: true is not M61 start.
may_proceed_to_m61_hardening: true is not approval.
may_proceed_to_m61_hardening: true does not create hardening tasks automatically.
may_proceed_to_m62_light_diagnostic: true is not M62 start.
may_proceed_to_m62_light_diagnostic: true is not approval.
may_proceed_to_m62_light_diagnostic: true does not start real-task trial automatically.

## Non-Authority Boundary

M60 architecture is not approval.
M60 architecture does not start cleanup execution.
M60 architecture does not mutate lifecycle state.
M60 architecture does not authorize merge, push, or release.
M60 architecture does not change M56–M59 safety semantics.
M60 architecture does not create registry, validators, inventory, evidence, or completion review.
M60 architecture does not authorize starting 60.2 automatically.

## Risks

- Structural cleanup may accidentally drift semantics without strict boundary checks.
- Registry/summary artifacts may become stale if not continuously validated against canonical sources.

## Required Downstream Artifacts

Required downstream artifacts are limited to the approved M60 task chain from 60.2 through 60.15.

## Final Architecture Status

FINAL_STATUS: M60_CLEANUP_ARCHITECTURE_DEFINED

This final status means only that M60 architecture and safety boundary are defined.
It does not mean cleanup has started.
It does not mean artifacts were inventoried.
It does not mean registry exists.
It does not mean validators were consolidated.
It does not mean documentation was pruned.
It does not mean M60 is complete.
