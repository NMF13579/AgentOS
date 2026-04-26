# Template Integrity Checker

Template Integrity Checker checks whether the AgentOS template still has the required file and directory structure for release readiness.

It is a read-only checker. Read-only means it only reads files and folders, prints a report, and exits with `PASS` or `FAIL`.

## How to run

Run from the repository root:

```bash
python3 scripts/check-template-integrity.py
```

Run against an explicit root:

```bash
python3 scripts/check-template-integrity.py --root tests/fixtures/template-integrity/valid-template
```

`--root` points the checker at another directory and treats that directory as the template root.

## Strict mode

`--strict` is accepted by the command line interface but does not change behavior in 7.0.1.

Strict mode is reserved for 7.0.2.

## What it checks

The checker verifies required AgentOS template areas:

- core files;
- input layer;
- task brief validation;
- review and trace files;
- contract generation files;
- queue lifecycle files and directories;
- runner dry-run protocol files;
- task health metrics files;
- `.gitignore` runtime artifact rule;
- forbidden auto-runner file paths.

## PASS

`PASS` means every required file and directory exists, `.gitignore` contains `tasks/drafts/`, and no forbidden file path exists.

The command exits with code `0`.

## FAIL

`FAIL` means at least one required file or directory is missing, `.gitignore` is missing or does not contain `tasks/drafts/`, the root path is invalid, or a forbidden file path exists.

The command exits with code `1`.

The checker collects all section errors before printing the final result.

## Forbidden auto-runner files

Forbidden auto-runner files are blocked because AgentOS must stay a Markdown-first guardrail framework. It must not become an autonomous runner that chooses, approves, or executes work by itself.

The checker only checks the exact forbidden relative paths. It does not search for similar file names.

## Runtime artifacts

`tasks/drafts/` must be listed in `.gitignore` because draft contracts are runtime artifacts.

Runtime artifacts are files created while using the system. They should not become a required tracked part of the template.

## Non-goals

Template Integrity Checker does not:

- execute tasks
- modify tasks/active-task.md
- generate task contracts
- move queue items
- approve execution
- run agent-next.py
- run agent-complete.py
- run agent-fail.py
- implement autonomous runner behavior
