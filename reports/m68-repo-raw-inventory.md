# M68.0 — Repository Scan / Authoritative Raw Inventory
## Task Boundary
This report is scanner-backed inventory evidence only.
This report records repository facts and raw review signals only.
This report does not identify canonical documents.
This report does not identify deprecated documents.
This report does not approve cleanup, deletion, compression, consolidation, or docs-to-code conversion.
This report does not create registries.
This report does not create validators.
This report does not create fixtures.
This report does not modify protected artifacts.
This report does not complete M68.
Human review remains required before M68.1.
## Active Task Record
- active_task_id: task-68.0
## Scan Revision
- generated_at: 2026-05-29T16:33:19.476400+00:00
- branch: dev
- commit_sha: 49e29d3f13c2f232f44d409db4277131b352c743
## Scanner Boundary
Read-only scanner. No cleanup, no approval, no lifecycle mutation.
## Generated Artifacts
- reports/m68-anomaly-grep.txt
- reports/m68-docs-to-code-drift.json
- reports/m68-duplicates.json
- reports/m68-inventory.json
- reports/m68-owner-gaps.json
- reports/m68-prompt-metrics.json
- reports/m68-protected-artifacts.json
- reports/m68-tree.json
- reports/m68-tree.txt
## Repository Tree Summary
- total_paths: 6717
## Directory Inventory Summary
- top_level_directories: .agentos, .githooks, .github, approvals, architecture, core-rules, data, docs, examples, generated, handoff, incidents, lessons, memory-bank, policies, project, prompt-packs, prompts, quality, reports, schemas, scratch, scripts, security, shared, stages, state, tasks, templates, tests, tools, workflow
## Root-Level Inventory
- top_level_count: 57
## Bootstrap Surface Inventory
- bootstrap_files: 197
## scripts/ Inventory
- files: 298
## schemas/ Inventory
- files: 68
## tests/fixtures/ Inventory
- files: 3692
## reports/ Inventory
- files: 370
## tasks/ Inventory
- files: 33
## .github/ Inventory
- files: 15
## .agentos/ Inventory
- present: True
## Protected Artifacts Presence
- total_listed: 17
- present_count: 17
## Owner Gap Signals
- codeowners_present: True
- uncovered_count: 0
## Duplicate / Backup Filename Signals
- signal_count: 794
## Active-Tree Ambiguity Signals
- same_stem_signals: 371
## Idle-State Format Signals
- candidates: 8
## Adapter Drift Signals
- candidates: 14
## Validation Authority Drift Signals
- candidates: 1169
## Task Ledger vs Reports Signals
- inventory_freshness_candidates: 6
## Workflow Permission Risk Signals
- candidates: 19
## Large Generated Artifact Signals
- large_generated_reports: 2
## Prompt / Bootstrap Metrics
- bootstrap_startup_adjacent_files: 197
- adapter_files: 0
## Raw Review Signals For M68.1
- Review JSON/TXT artifacts only; no cleanup action in M68.0.
## Explicit Non-Conclusions
- No deletion decision.
- No compression decision.
- No docs-to-code decision.
- No M69 start authorization.
## Final Status
FINAL_STATUS: M68_RAW_INVENTORY_COMPLETE_WITH_WARNINGS
- warnings: duplicate_or_copy_signals
