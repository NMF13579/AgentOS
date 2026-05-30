# Validators

Canonical validation orchestration in AgentOS is routed by the thin dispatcher `scripts/agentos-validate.py`.

| Entrypoint | Type | Role |
|---|---|---|
| `agentos-validate.py` | Thin Dispatcher | Official validation orchestrator and routing entrypoint |
| `run-all.sh` | Compatibility Wrapper | Delegates to the thin dispatcher `agentos-validate.py all` |
| `health-check.sh` | Compatibility Wrapper | Runs module layout checks and delegates validation to the thin dispatcher |
| `validate-architecture.sh` | Legacy Wrapper | Delegates architecture validation flows to the thin dispatcher |

## Validation and Authority Boundaries
- **PASS is not approval.** Human approval cannot be simulated.
- **CI PASS is not approval.**
- **Dispatcher PASS is not task completion** or lifecycle mutation. The dispatcher serves as the routing and orchestration layer only.
- **Wrappers are compatibility surfaces only** and do not create independent validation authority.
- **Generated reports are evidence only** and do not authorize changes or mark tasks complete.
