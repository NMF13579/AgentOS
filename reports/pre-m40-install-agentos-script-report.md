# Pre-M40 Install AgentOS Script Report

## Purpose

This report records creation and validation of scripts/install-agentos.py.

## Scope

This task creates only the existing-project installer script.

It does not create user-facing install documentation.

## Dependency

This task depends on:

- Task 39.9.1 — Clean Full Template Assembly with Simple Mode Default
- Task 39.9.2 — GitHub Template Bootstrap / Use Template Readiness

## Files Created or Updated

- scripts/install-agentos.py
- reports/pre-m40-install-agentos-script-report.md

## Installer Safety

| Check | Result | Evidence |
|---|---|---|
| dry-run is default | PASS | Running without flags defaults to dry-run |
| --apply is explicit | PASS | Installation only happens with --apply |
| no overwrite behavior | PASS | shutil.copytree fails if dst exists; explicit checks added |
| no delete behavior | PASS | No destructive APIs used in script |
| no commit/push behavior | PASS | No git commands that modify history used |
| installs only into agentos/ and .agentos/ | PASS | Explicit mappings enforced |
| root tasks/reports not created | PASS | Subdirs created inside target/agentos/ |
| .github not created or modified | PASS | Explicitly skipped in root |
| Simple Mode remains default | PASS | Source template configuration preserved |
| Full Mode grants no extra permissions | PASS | Source template configuration preserved |

## Smoke Tests

| Test | Result | Notes |
|---|---|---|
| py_compile | PASS | python3 -m py_compile successful |
| help command | PASS | --help displays correct info |
| dry-run on clean temp git repo | PASS | Plan generated correctly |
| dry-run does not modify target | PASS | Verified target remains clean |
| apply on clean temp git repo | PASS | Files installed successfully |
| apply creates agentos and .agentos | PASS | Folders created in target root |
| apply preserves Simple Mode | PASS | .agentos/config.yml has mode: simple |
| README/docs/.github warnings are not blockers | PASS | Warnings issued but install proceeds |
| apply does not create .github | PASS | Verified .github not present in target |
| existing agentos blocks install | PASS | Blocking conflict detected |
| existing .agentos blocks install | PASS | Blocking conflict detected |
| non-git apply blocks | PASS | Git repository check enforced |

## Result Token

RESULT: PRE_M40_INSTALL_SCRIPT_READY

## Warnings

- None

## Blockers

- None

## Next Step

A later task may create user-facing documentation that references this script.

## Non-Claims

This report does not claim:
* production readiness;
* production-grade sandboxing;
* guaranteed safe AI output;
* bug-free AI output;
* automatic approval safety;
* destructive workflow support;
* SaaS readiness.
