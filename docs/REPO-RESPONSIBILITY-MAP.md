# Repo Responsibility Map
## M68.1 Boundary
This map is an M68.1 planning and review artifact.
This map does not authorize cleanup, deletion, compression, consolidation, or docs-to-code conversion.
This map does not create approval.
This map does not create lifecycle mutation.
This map does not complete M68.
Human review remains required before M68.2.

## Active Task Record
- active_task_id: task-68.1
- milestone: M68
- mode: EXECUTION / READ-ONLY ANALYSIS / MAP GENERATION

## Inputs Used
- tasks/active-task.md
- reports/m68-scan.rev.txt
- reports/m68-inventory.json
- reports/m68-duplicates.json
- reports/m68-owner-gaps.json
- reports/m68-protected-artifacts.json
- reports/m68-docs-to-code-drift.json
- reports/m68-prompt-metrics.json
- reports/m68-anomaly-grep.txt
- reports/m68-repo-raw-inventory.md

## Repository Revision
- branch: dev
- commit_sha: 49e29d3f13c2f232f44d409db4277131b352c743
- scan_generated_at: 2026-05-29T16:33:19.476400+00:00

## Top-Level Responsibility Summary
- `docs/`: policy, process and guidance texts (supporting doc candidates).
- `scripts/`: operational scripts and checks (execution/checker surface).
- `schemas/`: machine-readable contracts (schema artifact candidates).
- `templates/`: reusable document/task templates (template artifacts).
- `tests/` and `tests/fixtures/`: repeatable checks and fixtures (fixture surface).
- `reports/`: evidence outputs and historical run records (report artifacts).
- `tasks/`: active/queued task lifecycle records.
- `workflow/`, `policies/`, `security/`, `quality/`: governance and boundaries.
- `memory-bank/`, `data/`: reference memory and data registries/candidates.
- `.github/`: CI/workflow and ownership config.

## Bootstrap Surface
- Bootstrap/startup-adjacent files detected in M68.0 metrics: 197.
- Risk signal recorded: LARGE_STARTUP_FILE.

## Adapter Surface
- Adapter files count in M68.0 metrics: 0.
- Adapter drift candidates from M68.0 drift file: 14 (needs review).

## Canonical / Governance Modules
- `llms.txt` plus canonical modules in `core-rules/`, `state/`, `workflow/`, `quality/`, `security/` govern execution boundaries.
- Classification here is candidate-level only, not final canonical ownership.

## Validation Surface
- High concentration of approval/completion wording candidates: 1169.
- Repeated final status pattern candidates: 123.
- Candidate for M71 deterministic checks, not implemented here.

## Schema / Contract Surface
- `schemas/` appears as contract boundary surface.
- Protected schema artifacts (M61–M67 list): present 17/17.

## Fixture Surface
- `tests/fixtures/` exists and acts as test evidence input surface.
- No fixture creation or modification is performed in M68.1.

## Evidence / Reports Surface
- `reports/` holds scanner evidence and milestone reports.
- M68.0 anomaly grep lines: 4473 raw matches.

## Task Lifecycle Surface
- `tasks/active-task.md` binds runtime to `task-68.1` (read-only precondition in this task).
- Task ledger vs reports drift candidates: inventory freshness candidates = 6.

## GitHub / Workflow Surface
- `.github/` and `workflow/` expose CI permissions and automation behavior.
- Workflow permission candidates from drift scan: 19 (candidate for M71/M73 review).

## Data / Generated Navigation Surface
- `data/` and generated JSON/TXT reports form navigation evidence surfaces.
- They are derived artifacts and not authority by themselves.

## Protected Areas
- Protected artifact presence from M68.0: 17/17 found.
- Protected artifacts owner gap count: 0 explicit uncovered paths.

## Areas Requiring Later Review
- candidate for M69 review: source-of-truth drift and possible deprecated clusters.
- candidate for M70 review: script surface duplication and operational variants.
- candidate for M71 review: deterministic checks for repeated rule patterns.
- candidate for M72 review: ownership/registry normalization planning.
- candidate for M73 review: validation CLI and workflow permission normalization.
- active-tree ambiguity summary: same-stem signals = 371.

## Explicit Non-Authority Boundary
- This map is descriptive classification only.
- It does not define final canonical ownership.
- It does not authorize cleanup or execution of M69+ tasks.

## Final Status
FINAL_STATUS: M68_REPO_RESPONSIBILITY_MAP_COMPLETE_WITH_WARNINGS
