## Task
M43.HK1 Spec Conflict Fix (safe to delete validation rule conflict)

## Goal
Resolve contradictory validation wording where one rule required a phrase with `safe to delete` while another rule prohibited any `safe to delete` string.

## Scope
Reports-only conflict-rule correction.
No changes to scripts, fixtures, docs, or validation logic.

## Detection Method
Commands used:
```bash
rg -n "Archive candidate does not mean safe to delete|safe to delete" .
rg -n "grep -R \"safe to delete\"|Archive candidate does not mean safe to delete" reports docs tasks scripts .
```

## Conflicting Rule Locations Found
- `reports/m43-2-historical-report-archive-map.md`
- `reports/m43-6-post-honest-pass-consolidation-closure.md`

## Applied Fix
Replaced phrase:
- from: `Archive candidate does not mean safe to delete.`
- to: `Archive candidate does not authorize deletion.`

Updated target grep-check form:
```bash
grep -R "Archive candidate does not authorize deletion." <target>
```

## Verification
```bash
rg -n "Archive candidate does not authorize deletion" reports/m43-2-historical-report-archive-map.md reports/m43-6-post-honest-pass-consolidation-closure.md
rg -n "Archive candidate does not mean safe to delete|safe to delete" reports/m43-2-historical-report-archive-map.md reports/m43-6-post-honest-pass-consolidation-closure.md
```

Expected:
- New phrase present in both target files.
- Old conflicting phrase absent from both target files.

## Outcome
Conflict wording replaced in discovered rule locations without altering validation behavior.
