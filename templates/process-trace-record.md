# Process Trace Record Template

Purpose: record execution trace evidence for PASS claims.

Agent-written trace is claim, not proof.
runner_generated: true must be set by runner, trusted validation wrapper, or approved validation entrypoint.
Process Trace is validation evidence, not approval.

Required fields:
- result_claim
- execution_trace[].command
- execution_trace[].exit_code
- execution_trace[].output_artifact
- execution_trace[].output_hash
- execution_trace[].generated_at
- execution_trace[].runner_generated
- execution_trace[].validation_source_id
- execution_trace[].trace_writable_by_execution_agent

Trusted boundary: runner/approved wrapper generated trace only.
Writable trace limitation must be recorded.

```json
{
  "result_claim": "PASS",
  "execution_trace": [
    {
      "command": "python3 scripts/agentos-validate.py all --json",
      "exit_code": 0,
      "output_artifact": "reports/ci/agentos-validate.json",
      "output_hash": "sha256:...",
      "generated_at": "2026-05-14T08:05:00Z",
      "runner_generated": true,
      "validation_source_id": "agentos-runner",
      "trace_writable_by_execution_agent": false
    }
  ]
}
```
