# M73.1 — Validation Entry Point Inventory

## Purpose
This report serves as a read-only inventory of validation entrypoints and authority claims within the AgentOS repository for Task 73.1. It discovers and documents existing validation surfaces, registry statuses, and potential risks without altering files or changing validation configurations.

## Input Preconditions
m73_0_intake_exists: true
m73_0_final_status: M73_M72_COMPLETION_INTAKE_READY_WITH_WARNINGS
may_prepare_m73_1: true_with_warnings
m73_1_allowed_to_run: true_with_warnings

## Inventory Method
The inventory was conducted via read-only repository scanning and checking validation surfaces. 
Commands used for discovery:
- `find scripts -maxdepth 2 -type f 2>/dev/null`
- `find .github/workflows -maxdepth 2 -type f 2>/dev/null`
- `find docs -maxdepth 3 -type f 2>/dev/null`
- `grep` to scan for validation scripts, workflows, and documentation references.

## Scanned Surfaces
- scripts/: present
- run-all.sh: not_present
- run-all*.sh: not_present
- VALIDATORS.md: not_present
- README.md: present
- docs/: present
- .github/workflows/: present
- Makefile: not_present
- package.json: not_present
- pyproject.toml: not_present
- tox.ini: not_present
- noxfile.py: not_present

## Validation Entrypoint Inventory
| path | entrypoint_name | entrypoint_kind | command_or_reference | runs_child_validators | creates_reports | mutates_files | help_mode_side_effect_risk | shell_execution_risk | overlaps_with | authority_claim | protected_status | canonical_status | classification | review_required_reason | notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| scripts/agentos-validate.py | agentos-validate.py | python_validator | python3 scripts/agentos-validate.py | true | true | false | false | false | scripts/run-all.sh, scripts/health-check.sh | true | NOT_PROTECTED | NOT_CANONICAL | ENTRYPOINT_CANONICAL_CANDIDATE | Needs M73.5 alignment review to formalize thin dispatcher status | Unified validator CLI wrapper |
| scripts/run-all.sh | run-all.sh | shell_wrapper | bash scripts/run-all.sh | true | false | false | false | true | scripts/agentos-validate.py | false | NOT_PROTECTED | NOT_CANONICAL | ENTRYPOINT_LEGACY_CANDIDATE | Legacy script incompatibilities | Calls legacy validator scripts |
| scripts/health-check.sh | health-check.sh | shell_wrapper | bash scripts/health-check.sh | true | false | false | false | true | scripts/agentos-validate.py | true | NOT_PROTECTED | NOT_CANONICAL | ENTRYPOINT_COMPATIBILITY_WRAPPER_CANDIDATE | Integrates legacy validation flows under architecture check | Modular check runner |
| scripts/validate-architecture.sh | validate-architecture.sh | shell_wrapper | bash scripts/validate-architecture.sh | true | false | false | false | true | scripts/health-check.sh | false | NOT_PROTECTED | NOT_CANONICAL | ENTRYPOINT_LEGACY_CANDIDATE | Shell wrapper overlaps with python-driven checks | Runs documentation and link checks |
| .github/workflows/agentos-validate.yml | agentos-validate.yml | ci_workflow | GitHub CI Job | true | true | false | false | true | none | true | NOT_PROTECTED | NOT_CANONICAL | ENTRYPOINT_CI_REFERENCE | Hardcoded python checking logic inside YAML | PR/branch merge block validation |
| scripts/validate-lifecycle-apply.py | validate-lifecycle-apply.py | python_validator | python3 scripts/validate-lifecycle-apply.py | false | false | false | false | false | none | true | PROTECTED | NOT_CANONICAL | ENTRYPOINT_LEGACY_CANDIDATE | High-risk lifecycle transition script | Governed validator in protected registry |
| scripts/check-execution-readiness.py | check-execution-readiness.py | python_validator | python3 scripts/check-execution-readiness.py | false | false | false | false | false | scripts/check-active-task-readiness.py | true | PROTECTED | NOT_CANONICAL | ENTRYPOINT_LEGACY_CANDIDATE | Enforces runtime execution readiness | In protected registry |

## Authority Claim Inventory
- path: docs/VALIDATOR-AUTHORITY-BOUNDARY.md
  line_or_section: "Execution agent must not create trusted validation authority."
  claim_summary: "Restricts execution agent from creating validation authority during runtime."
  claim_type: canonical_validation_claim
  conflict_risk: none
  needs_alignment: false
- path: docs/CANONICAL-ARTIFACTS-REGISTRY.md
  line_or_section: "Canonical domains and roles for core artifacts."
  claim_summary: "Defines primary source of truth for repository review governance."
  claim_type: canonical_validation_claim
  conflict_risk: low
  needs_alignment: false
- path: .github/workflows/agentos-validate.yml
  line_or_section: "Enforce AgentOS validation result"
  claim_summary: "Enforces that the validation result is strictly 'PASS' before merging."
  claim_type: ci_validation_claim
  conflict_risk: medium
  needs_alignment: true
- path: README.md
  line_or_section: "Unified Validation table and CLI descriptions"
  claim_summary: "Lists validation subcommands such as template, negative, guard, audit, queue, runner."
  claim_type: documentation_reference
  conflict_risk: medium
  needs_alignment: true

## Wrapper / Legacy Candidate Inventory
canonical_dispatcher_candidates_count: 1
compatibility_wrapper_candidates_count: 1
legacy_entrypoint_candidates_count: 5
unknown_entrypoint_classification_count: 0

Provisional statements:
- `scripts/agentos-validate.py` may be a canonical thin dispatcher candidate pending M73.5 alignment review.
- `run-all.sh` may be a compatibility wrapper candidate pending M73.5 alignment review.

## CI / Workflow Reference Inventory
- workflow_path: .github/workflows/agentos-validate.yml
  validation_command: python scripts/agentos-validate.py all
  called_entrypoint: scripts/agentos-validate.py
  claims_required_check: true
  claims_approval: false
  claims_platform_enforcement: false
  risk: medium
  notes: Hardcoded validation checks inside GitHub actions step script.

## Protected / Canonical Status Reflection
protected_registry_read: true
canonical_registry_read: true
protected_or_canonical_entrypoint_count: 2
unknown_protected_or_canonical_status_count: 0

## Risk Summary
entrypoint_count: 7
authority_claim_count: 5
mutation_risk_count: 0
help_side_effect_risk_count: 0
shell_execution_risk_count: 4
ci_authority_claim_count: 1
ci_approval_claim_count: 0
protected_or_canonical_entrypoint_count: 2
unknown_review_required_count: 5

## Warnings and Unknowns
- Overlapping validation entrypoints: `scripts/agentos-validate.py`, `scripts/health-check.sh`, `scripts/run-all.sh`, and `scripts/validate-architecture.sh` overlap in scopes.
- Shell execution risks: Shell scripts/workflows (`run-all.sh`, `health-check.sh`, `validate-architecture.sh`, `agentos-validate.yml`) run raw shell commands.
- Documentation references drift in README.md (mentions unsupported subcommands).
- CI workflow `agentos-validate.yml` embeds raw validation evaluation Python code.

## Intake Decision for 73.2
may_prepare_m73_2: true_with_warnings

## Boundary Statement
This inventory report is for roadmapping and discovery purposes only. It does not approve M72/M73, does not select final dispatcher, does not authorize cleanup, and does not modify scripts, wrappers, docs, workflows, protected artifacts, or canonical artifacts.

## Final Status
FINAL_STATUS: M73_VALIDATION_ENTRYPOINT_INVENTORY_COMPLETE_WITH_WARNINGS
