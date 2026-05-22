## Task
M43.HK1 Housekeeping — Spec Conflict Fix

## Scope Result
- Conflict rule phrase updated in discovered locations only.
- No scripts/fixtures/docs changed.
- No validation logic changed.

## Changed Files
- `reports/m43-2-historical-report-archive-map.md`
- `reports/m43-6-post-honest-pass-consolidation-closure.md`
- `reports/m43-hk1-spec-conflict-fix-evidence.md`
- `reports/m43-hk1-completion-review.md`

## Validation Check Update
Use:
```bash
grep -R "Archive candidate does not authorize deletion." <target>
```

## Final Status
M43_HK1_SPEC_CONFLICT_FIXED
