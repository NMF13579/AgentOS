# M40 Fixup — Clean Template Dotfiles Portability

## Source Gap

M40 dogfooding found a P1 portability gap where copying the clean template to an external project resulted in missing dotfiles (`.agentos/` and `.github/`). This caused readiness checks to fail because the `.agentos/config.yml` and GitHub templates were not present. The gap occurred because standard copy commands (like `cp -r *`) skip hidden files by default, and the template documentation lacked explicit guidance on preserving dotfiles.

## Template Dotfile Inspection

- templates/agentos-clean/.agentos/: PRESENT
- templates/agentos-clean/.agentos/config.yml: PRESENT
- templates/agentos-clean/.github/: PRESENT
- templates/agentos-clean/.github/ISSUE_TEMPLATE/: PRESENT

## Files Changed

- `templates/agentos-clean/README.md`
- `templates/agentos-clean/agentos/docs/quickstart.md`
- `templates/agentos-clean/agentos/docs/use-template.md`

## Copy Guidance Fix

Explicit dotfile-preserving local copy instructions were added.

Command added to documentation:
```bash
cp -a templates/agentos-clean/. <target>/
```
Warnings against using `cp -r * <target>/` were also explicitly included.

## Template Consistency Result

DOTFILES_PRESENT_AND_DOCUMENTED

## Validation Output Summary

- `find templates/agentos-clean -maxdepth 4 -type f | sort`: Output confirmed the presence of 26 files including `.agentos/config.yml` and `.github/ISSUE_TEMPLATE/agentos_task.yml`.
- `find templates/agentos-clean -maxdepth 4 -type d | sort`: Output confirmed the presence of 15 directories including `.agentos`, `.agentos/runtime`, `.github`, and `.github/ISSUE_TEMPLATE`.
- help command checks:
  - `python3 templates/agentos-clean/agentos/scripts/check-bootstrap-readiness.py --help`: Exited safely, showing usage.
  - `python3 templates/agentos-clean/agentos/scripts/agentos-validate.py --help`: Exited safely, showing usage.
- `git status --short`:
```
 M templates/agentos-clean/README.md
 M templates/agentos-clean/agentos/docs/quickstart.md
 M templates/agentos-clean/agentos/docs/use-template.md
```

## Remaining Gaps

None identified.

## Final Result

DOTFILES_PORTABILITY_FIX_PASS

## Safety Confirmation

- no dogfood sandbox modified: CONFIRMED
- no dependency install: CONFIRMED
- no full validation run: CONFIRMED
- no commit: CONFIRMED
- no push: CONFIRMED
- no unrelated files modified: CONFIRMED
