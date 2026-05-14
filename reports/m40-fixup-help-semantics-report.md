# M40 Fixup — Safe Help Semantics

## Source Gap

M40 dogfooding found a P1 safety gap where template scripts did not handle `--help` or `-h` flags safely. Instead of displaying help and exiting, they executed their main logic, leading to side effects like creating task files or running validation in environments that weren't ready.

## Files Changed

- `templates/agentos-clean/agentos/scripts/agentos-validate.py`
- `templates/agentos-clean/agentos/scripts/check-bootstrap-readiness.py`
- `templates/agentos-clean/agentos/scripts/new-task.py`

## Behavior Before

- `agentos-validate.py --help`: Ran validation immediately.
- `check-bootstrap-readiness.py --help`: Ran readiness checks immediately.
- `new-task.py --help`: Created a task file named `task-001.md` with the title `--help`.

## Behavior After

### agentos-validate.py
- command: `python3 templates/agentos-clean/agentos/scripts/agentos-validate.py --help`
- exit result: 0
- help shown: yes
- side effects observed: no
- notes: Correctly prints usage and exits without running validation.

### check-bootstrap-readiness.py
- command: `python3 templates/agentos-clean/agentos/scripts/check-bootstrap-readiness.py --help`
- exit result: 0
- help shown: yes
- side effects observed: no
- notes: Correctly prints usage and exits without running readiness checks.

### new-task.py
- command: `python3 templates/agentos-clean/agentos/scripts/new-task.py --help`
- exit result: 0
- help shown: yes
- side effects observed: no
- notes: Correctly prints usage and exits without creating a task file.

## Validation Output Summary

### Help Commands
- `agentos-validate.py --help`: PASS (Exit 0, Usage shown)
- `check-bootstrap-readiness.py --help`: PASS (Exit 0, Usage shown)
- `new-task.py --help`: PASS (Exit 0, Usage shown)

### Side Effect Check
- `git status --short`:
  M templates/agentos-clean/agentos/scripts/agentos-validate.py
  M templates/agentos-clean/agentos/scripts/check-bootstrap-readiness.py
  M templates/agentos-clean/agentos/scripts/new-task.py
- `find templates/agentos-clean -path "*tasks/queue/*" -type f`:
  templates/agentos-clean/tasks/queue/.gitkeep
  (No new task files created)

## Remaining Gaps

None identified.

## Final Result

HELP_SEMANTICS_FIX_PASS

## Safety Confirmation

- no dogfood sandbox modified: CONFIRMED
- no new task created by --help: CONFIRMED
- no dependency install: CONFIRMED
- no full validation run: CONFIRMED
- no commit: CONFIRMED
- no push: CONFIRMED
