# Known Limitations

## Purpose
This document records known non-blocking limitations of AgentOS during the M39 Release Candidate freeze phase. Known limitations are not resolved issues and are not approvals to bypass safety checks.

## Rules
- P0/P1 pilot blockers must not be hidden here.
- Known limitations must not weaken safety boundaries.
- Known limitations must not authorize unsupported workflows.
- Known limitations must not claim public release readiness.
- Each limitation must include impact and workaround if known.

## Limitation Entries

### LIM-001 — TUI Status Damaged
- **Source feedback ID:** M38-FB-002
- **Severity:** P2
- **Type:** Feature Gap / Metadata Sync
- **Impact:** TUI displays `STATUS_SOURCE_DAMAGED` and may show inconsistent repository state.
- **Workaround:** Use CLI validation commands (`scripts/agentos-validate.py all`) and manual report inspection in `reports/`.
- **Pilot blocking:** NO
- **Planned handling:** Repair metadata sync logic in Milestone 41+.
- **Related report:** [reports/m38-pilot-feedback-evidence-report.md](../reports/m38-pilot-feedback-evidence-report.md)

### LIM-002 — Manual YAML Formatting Required
- **Source feedback ID:** M38-FB-001
- **Severity:** P2 (Usability)
- **Type:** Validation Gap / Parser Limitation
- **Impact:** Empty lists in YAML blocks (e.g., `[]`) may cause parse failures in scope compliance scripts.
- **Workaround:** Leave the YAML field empty or remove the brackets entirely.
- **Pilot blocking:** NO
- **Planned handling:** Improve YAML parser resilience in Milestone 40+.
- **Related report:** [reports/m38-pilot-feedback-evidence-report.md](../reports/m38-pilot-feedback-evidence-report.md)
