# AgentOS Validators Registry

## Canonical Validators
These validate the current primary (modular) architecture.
PASS from these = system is healthy.

| Script | Purpose |
|---|---|
| validate-architecture.sh | Checks modular control plane structure |
| validate-route.py | Validates ROUTES-REGISTRY.md routing logic |
| validate-docs.py | Checks doc integrity against modular spec |
| tools/doc-tests/* | Doc-level contract tests |
| run-all.sh | Orchestration entrypoint — canonical checks only |

## Legacy / Compatibility Validators
PASS from these does NOT mean the current architecture is healthy.

| Script | Status | Notes |
|---|---|---|
| legacy-health-check.sh | legacy-compatibility | Checks old identity and LAYER-1 topology |
| validate-adapters.sh | legacy-compatibility | Requires bash>=4, checks legacy adapter paths |
| check-identity-drift.sh | legacy-compatibility | May reference old identity (Vibe-coding-docs) |

## Deprecated
(none yet)
