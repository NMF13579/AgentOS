# Evidence Immutability Record Template

Evidence immutability record is integrity evidence, not approval.
Evidence immutability metadata is not independent timestamp authority.

```json
{
  "task_id": "task-smoke-001",
  "evidence_set_id": "evidence-set-smoke-001",
  "status": "COMPLETED",
  "artifacts": [
    {
      "path": "artifacts/evidence-report.md",
      "artifact_type": "evidence_report",
      "protected": true,
      "finalized": true,
      "result_status": "PASS",
      "sha256_before": "sha256:e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
      "sha256_after": "sha256:e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
      "changed_after_finalization": false,
      "amendment_required": false,
      "amendment_record": null
    }
  ],
  "rerun": {
    "rerun_performed": false,
    "rerun_cause_recorded": false,
    "rerun_cause": null
  }
}
```
