# Evidence Amendment Record Template

Evidence amendment record is integrity evidence, not approval.

```json
{
  "amendment_id": "amendment-smoke-001",
  "task_id": "task-smoke-001",
  "original_artifact": "artifacts/evidence-report.md",
  "artifact_type": "evidence_report",
  "previous_sha256": "sha256:e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855",
  "new_sha256": "sha256:4baf7e6f9f1c2d5c7a4a6f3d7c9f9b1b4a2c5d6e7f8091a2b3c4d5e6f708192a",
  "reason": "Corrected recorded command output after failed validation was preserved.",
  "correction_scope": "metadata-only",
  "failed_evidence_preserved": true,
  "rerun_cause": "Original command failed due to missing fixture path; fixture path corrected.",
  "created_by": "maintainer-or-runner",
  "reviewed_by": "human-owner",
  "created_at": "2026-05-14T00:00:00Z"
}
```
