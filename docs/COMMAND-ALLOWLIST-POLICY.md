---
type: policy
module: m26-pre-merge-corridor
status: active
authority: canonical
version: 1.0.0
created: 2026-05-03
task_id: 26.3.1
milestone: M26
---

# Command Allowlist Policy

## Allowlist

Commands allowed without approval:

- `git status`
- `git diff`
- `git log`
- `git show`
- `ls`
- `cat`
- `grep`
- `find`
- `python3 --version`

## Blocklist

Commands that are never allowed:

- `rm -rf`
- `git push --force`
- `curl <external>`
- `sudo`
- `chmod 777`

## Requires Approval

Commands that require explicit human approval:

- `git commit`
- `git push`
- `pip install`
- any write operations outside allowlist

## Policy Rule

If a command is unclear, treat it as `BLOCKED`.
Do not guess.

## Command Types

- `SAFE_READ`
- `SAFE_VALIDATE`
- `SAFE_TEST`
- `WRITE_LOCAL`
- `GIT_LOCAL`
- `GIT_REMOTE`
- `DANGEROUS`
- `FORBIDDEN`
