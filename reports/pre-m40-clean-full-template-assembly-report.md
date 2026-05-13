# Pre-M40 Clean Full Template Assembly Report

## Purpose

This report records preparation of the AgentOS clean full template before M40 dogfooding.

## Source Boundary

- AgentOS source repo is not copied directly to users.
- Clean template is generated under templates/agentos-clean/.
- User projects start from the clean template only.
- The clean template defaults to Simple Mode.

## Files Created or Updated

- docs/CLEAN-TEMPLATE-BOUNDARY.md
- templates/agentos-clean/template-manifest.yml
- scripts/prepare-clean-template.py
- scripts/check-template-cleanliness.py
- templates/agentos-clean/README.md
- templates/agentos-clean/.gitignore
- templates/agentos-clean/.agentos/config.yml
- templates/agentos-clean/.github/ISSUE_TEMPLATE/agentos_task.yml
- templates/agentos-clean/agentos/docs/*
- templates/agentos-clean/agentos/templates/*
- templates/agentos-clean/agentos/scripts/*
- templates/agentos-clean/tasks/*
- templates/agentos-clean/reports/.gitkeep
- templates/agentos-clean/.agentos/runtime/.gitkeep

## Script Boundary

- Root scripts are source-repo maintainer tools.
- Template agentos/scripts are user-project tools.

## Mode Boundary

- Default mode: simple
- Available modes: simple / advanced / full
- Full Mode grants extra permissions: no
- Advanced/Full require explicit user intent: yes

## Simple Mode Entry

- GitHub Issue Template exists: yes
- Issue Template title: AgentOS Task Request
- README points to New issue → AgentOS Task Request: yes

## Cleanliness Checks

| Check | Result | Evidence |
|---|---|---|
| must_include files exist | PASS | All files in manifest confirmed |
| must_not_include files absent | PASS | glob check passed |
| reports are empty except .gitkeep | PASS | ls confirmed |
| tasks history absent | PASS | tasks/queue empty except .gitkeep |
| runtime/cache absent | PASS | rm -rf performed and checked |
| .agentos/runtime gitignored | PASS | .gitignore check passed |
| milestone reports absent | PASS | find check passed |
| completion/evidence history absent | PASS | find check passed (excluding templates) |
| default mode is simple | PASS | config.yml check passed |
| full mode grants no extra permissions | PASS | config.yml check passed |
| GitHub Issue Template exists | PASS | exists check passed |

## Commands Run

| Command | Result |
|---|---|
| python3 scripts/prepare-clean-template.py --check | CLEAN_TEMPLATE_ALREADY_CLEAN |
| python3 scripts/check-template-cleanliness.py --template templates/agentos-clean | TEMPLATE_CLEAN |
| python3 templates/agentos-clean/agentos/scripts/agentos-validate.py all | OVERALL: PASS |

## Result Token

RESULT: PRE_M40_CLEAN_FULL_TEMPLATE_READY

## Warnings

- Broad `find` glob for `*completion-review.md` matches the template file `agentos/templates/completion-review.md`. Validated by excluding `agentos/templates/` from the check.

## Blockers

- None

## M40 Input

M40 may start. The clean full template is ready.

## Non-Claims

This report does not claim:

- public MVP readiness
- production readiness
- production-grade sandboxing
- guaranteed safe AI output
- automatic approval safety
- SaaS readiness
