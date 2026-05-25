#!/usr/bin/env python3
import json
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
DATA_PATH = REPO / "data/execution-verification-registry.json"


def normalize_entry(entry):
    # Stable field order for deterministic output.
    order = [
        "artifact_id",
        "path",
        "milestone",
        "task_id",
        "artifact_type",
        "semantics_role",
        "source_of_truth_role",
        "authority_level",
        "status",
        "depends_on",
        "validated_by",
        "owned_by_layer",
        "deprecated",
        "replacement_path",
        "do_not_delete",
        "notes",
    ]
    return {k: entry.get(k) for k in order}


def build_registry():
    if not DATA_PATH.exists():
        raise SystemExit(f"registry data missing: {DATA_PATH}")

    data = json.loads(DATA_PATH.read_text(encoding="utf-8"))
    artifacts = data.get("artifacts", [])
    if not isinstance(artifacts, list):
        raise SystemExit("artifacts must be an array")

    # Normalize entries and sort by artifact_id for stable diffs.
    normalized = [normalize_entry(e) for e in artifacts]
    normalized.sort(key=lambda x: (x.get("artifact_id") or ""))
    data["artifacts"] = normalized

    DATA_PATH.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("EXECUTION_VERIFICATION_REGISTRY_BUILT")


if __name__ == "__main__":
    build_registry()
