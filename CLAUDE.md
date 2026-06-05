<!-- ROLE: CANONICAL ENTRYPOINT -->
<!-- AUTHORITY: NON-AUTHORITY -->
<!-- SOURCE_OF_TRUTH: no -->

Read `llms.txt` first. Follow it exactly.
Use `ROUTES-REGISTRY.md` to confirm module ownership.
Adapters are not runtime authority.
All rules from [core-rules/MAIN.md](file:///Users/muhammednazyrov/Documents/GitHub/AgentOS/core-rules/MAIN.md) and [quality/MAIN.md](file:///Users/muhammednazyrov/Documents/GitHub/AgentOS/quality/MAIN.md) apply.

When explaining issues: Russian first, no internal terminology, say only what is wrong / why / what to change.
When fixing: make the smallest possible change, show only the corrected content, no commentary.

## Safety Semantics Reference
- PASS is not approval.
- Evidence is not approval.
- CI PASS is not approval.
- UNKNOWN is not OK.
- NOT_RUN is not PASS.
- Human approval cannot be simulated.
- Human review remains required.
- No lifecycle mutation without explicit governed task.
- Final validation dispatcher cleanup belongs to M73.
- Validation authority caution must be preserved.
- Fail-closed semantics must be preserved.
