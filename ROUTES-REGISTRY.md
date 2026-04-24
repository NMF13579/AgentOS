# ROUTES-REGISTRY

This file is the primary routing and registry hub for the new architecture.
Use it to navigate modules after startup entry points (`llms.txt` for agents, `START.md` for humans).
`always` means required in baseline route.
`conditional` means read only when trigger matches the task context.
`on-request` means explicit owner/user request.
Read core modules first, then open optional modules only by trigger.
Deep docs are not part of mandatory route.
Legacy docs remain available as reference/history sources and deep detail during transition.
Statuses reflect migration maturity, not document quality. `legacy-backed` means the module entry is canonical but deep content still depends on legacy sources.

| Module | Path | Role | When to read | Status | Current source | Notes |
|---|---|---|---|---|---|---|
| core-rules | `core-rules/MAIN.md` | Core rules module entry | always | transitional | `core-rules/MAIN.md` | Core entry now surfaces the rule backbone and key policy rules; legacy sources remain direct-read for full detail |
| state | `state/MAIN.md` | Control-plane module entry | always | transitional | `state/MAIN.md`, `HANDOFF.md` | State entry and key continuity/control-plane rules are surfaced in `state/MAIN.md`; legacy sources remain direct-read for full detail |
| architecture | `architecture/MAIN.md` | Architecture module entry | always | transitional | `architecture/CANON.md`, `ARCHITECTURE.md` | `architecture/MAIN.md` is the entry layer; `architecture/CANON.md` is the truth source; `ARCHITECTURE.md` remains deep detail |
| workflow | `workflow/MAIN.md` | Operational workflow entry | always | transitional | `workflow/MAIN.md` | Workflow backbone and key execution/interview/change-control rules are surfaced in `workflow/MAIN.md`; legacy sources remain direct-read for full detail |
| adapters | `adapters/MAIN.md` | Adapter routing entry | conditional | legacy-backed | `adapters/MAIN.md`, `AGENTS.md`, `CLAUDE.md`, `GEMINI.md`, `DOMAIN-ADAPTER.md` | Adapter entry and key compatibility constraints are surfaced in `adapters/MAIN.md`; legacy adapter sources and validator policy remain direct-read for full detail |
| quality | `quality/MAIN.md` | Quality/QA routing entry | conditional | transitional | `quality/MAIN.md`, `CHECKLIST.md` | Quality entry and key verification/audit routing are surfaced in `quality/MAIN.md`; legacy sources remain direct-read for full detail |
| security | `security/MAIN.md` | Security routing entry | conditional | transitional | `security/MAIN.md` | Boundaries defined; consolidation still partial |
| medical | `medical/MAIN.md` | Medical safety routing entry | conditional | transitional | `medical/MAIN.md` | Optional domain layer; not universal core |
| incidents | `incidents/MAIN.md` | Incident response routing entry | conditional | transitional | `incidents/MAIN.md`, `LEARNING-LOOP.md`, `incidents/incident-template.md` | Situational evidence + recovery routing |
| doctor | `doctor/MAIN.md` | Diagnosis/stabilization routing entry | conditional | transitional | Recovery context from `error-handling`, `audit`, `STATE`, `HANDOFF` | Operational entry; deeper playbooks pending |
