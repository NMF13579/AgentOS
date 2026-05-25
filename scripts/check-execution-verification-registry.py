#!/usr/bin/env python3
import argparse
import json
import os
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SCHEMA_PATH = REPO / "schemas/execution-verification-registry.schema.json"
DATA_PATH = REPO / "data/execution-verification-registry.json"


def _err(msg, errors):
    errors.append(msg)


def _warn(msg, warnings):
    warnings.append(msg)


def _load_json(path, errors, label):
    if not path.exists():
        _err(f"{label} missing: {path}", errors)
        return None
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        _err(f"{label} invalid JSON: {exc}", errors)
        return None


def validate_structure(schema, data, errors):
    top_required = schema.get("required", [])
    top_props = schema.get("properties", {})
    for k in top_required:
        if k not in data:
            _err(f"missing top-level required field: {k}", errors)
    if schema.get("additionalProperties") is False:
        for k in data.keys():
            if k not in top_props:
                _err(f"unknown top-level field: {k}", errors)

    if not isinstance(data.get("artifacts"), list):
        _err("artifacts must be array", errors)
        return None

    item_schema = top_props.get("artifacts", {}).get("items", {})
    item_required = set(item_schema.get("required", []))
    item_props = item_schema.get("properties", {})
    return item_required, item_props, item_schema.get("additionalProperties")


def validate_entries(data, item_required, item_props, addl_false, errors, warnings):
    enum_fields = {
        "artifact_type",
        "semantics_role",
        "source_of_truth_role",
        "authority_level",
        "status",
        "owned_by_layer",
    }

    ids = set()
    paths = set()

    for i, e in enumerate(data.get("artifacts", [])):
        tag = f"artifacts[{i}]"
        if not isinstance(e, dict):
            _err(f"{tag} must be object", errors)
            continue
        for k in item_required:
            if k not in e:
                _err(f"{tag} missing required field: {k}", errors)

        if addl_false is False:
            for k in e.keys():
                if k not in item_props:
                    _err(f"{tag} unknown field: {k}", errors)

        aid = e.get("artifact_id")
        if isinstance(aid, str):
            if aid in ids:
                _err(f"duplicate artifact_id: {aid}", errors)
            ids.add(aid)

        p = e.get("path")
        if isinstance(p, str):
            if p in paths:
                _warn(f"duplicate path referenced: {p}", warnings)
            paths.add(p)
            if not (REPO / p).exists():
                _warn(f"path missing on disk: {p}", warnings)

        for f in enum_fields:
            val = e.get(f)
            allowed = item_props.get(f, {}).get("enum", [])
            if val is not None and allowed and val not in allowed:
                _err(f"{tag} invalid enum for {f}: {val}", errors)

        if not isinstance(e.get("deprecated"), bool):
            _err(f"{tag} deprecated must be boolean", errors)
        if not isinstance(e.get("do_not_delete"), bool):
            _err(f"{tag} do_not_delete must be boolean", errors)
        if not isinstance(e.get("depends_on"), list):
            _err(f"{tag} depends_on must be array", errors)
        if not isinstance(e.get("validated_by"), list):
            _err(f"{tag} validated_by must be array", errors)
        if not isinstance(e.get("notes"), str):
            _err(f"{tag} notes must be string", errors)

        rp = e.get("replacement_path")
        if rp is not None and not isinstance(rp, str):
            _err(f"{tag} replacement_path must be string or null", errors)

        # Contract conflict rules
        if e.get("source_of_truth_role") == "canonical" and e.get("authority_level") != "canonical":
            _err(f"{tag} canonical source_of_truth_role requires canonical authority_level", errors)

        if e.get("deprecated") and e.get("do_not_delete"):
            _err(f"{tag} deprecated=true conflicts with do_not_delete=true", errors)

        if e.get("deprecated") and rp is None and not e.get("notes"):
            _err(f"{tag} deprecated=true requires replacement_path or explanatory notes", errors)

    # dependency checks after ids/paths available
    for i, e in enumerate(data.get("artifacts", [])):
        tag = f"artifacts[{i}]"
        aid = e.get("artifact_id")
        for dep in e.get("depends_on", []):
            if not isinstance(dep, str):
                _err(f"{tag} dependency must be string", errors)
                continue
            if dep == aid:
                _err(f"{tag} circular self dependency: {dep}", errors)
                continue
            # dep may be artifact_id or path
            if dep not in ids and dep not in paths:
                _err(f"{tag} dependency not found: {dep}", errors)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    errors, warnings = [], []
    schema = _load_json(SCHEMA_PATH, errors, "schema")
    data = _load_json(DATA_PATH, errors, "registry")

    if schema and data:
        result = validate_structure(schema, data, errors)
        if result:
            item_required, item_props, addl_false = result
            validate_entries(data, item_required, item_props, addl_false, errors, warnings)

    if errors:
        status = "EXECUTION_VERIFICATION_REGISTRY_INVALID"
        code = 1
    elif warnings:
        status = "EXECUTION_VERIFICATION_REGISTRY_VALID_WITH_WARNINGS"
        code = 0
    else:
        status = "EXECUTION_VERIFICATION_REGISTRY_VALID"
        code = 0

    payload = {
        "status": status,
        "errors": errors,
        "warnings": warnings,
    }

    if args.json:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        print(status)
        if errors:
            for e in errors:
                print(f"ERROR: {e}")
        if warnings:
            for w in warnings:
                print(f"WARN: {w}")

    return code


if __name__ == "__main__":
    raise SystemExit(main())
