#!/usr/bin/env python3
import argparse
import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

try:
    import yaml
except Exception:
    yaml = None

ALLOWED_SEVERITY = {"OK", "INFO", "WARNING", "NEEDS_REVIEW", "BLOCKED", "HUMAN_GATE", "UNKNOWN"}
ALLOWED_AUTHORITY = {"NONE", "HUMAN_REVIEW_OPTIONAL", "HUMAN_GATE_REQUIRED", "OWNER_REVIEW_REQUIRED", "SYSTEM_BLOCKED"}


def now_iso() -> str:
    return datetime.now().astimezone().isoformat(timespec="seconds")


def read_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def load_vocab(path: Path):
    if not path.exists():
        return None, "missing"
    try:
        if yaml is None:
            return None, "damaged"
        data = yaml.safe_load(read_text(path))
        if not isinstance(data, dict) or not isinstance(data.get("statuses"), list):
            return None, "damaged"
        by_code = {}
        for item in data["statuses"]:
            if not isinstance(item, dict) or "status_code" not in item:
                continue
            by_code[item["status_code"]] = item
        return by_code, "present"
    except Exception:
        return None, "damaged"


def source_state(path: Path):
    if not path.exists():
        return "missing"
    try:
        _ = path.read_bytes()
        return "present"
    except Exception:
        return "damaged"


def freshness(path: Path, stale_after: int = 300):
    if not path.exists():
        return "unknown"
    try:
        age = datetime.now(timezone.utc).timestamp() - path.stat().st_mtime
        return "stale" if age > stale_after else "fresh"
    except Exception:
        return "unknown"


def extract_status_from_md(path: Path):
    text = read_text(path)
    m = re.search(r"\b(CONTEXT_PIPELINE_[A-Z_]+|AGENTOS_STATUS_[A-Z_]+|CONTEXT_INDEX_[A-Z_]+|CONTEXT_PACK_[A-Z_]+|CONTEXT_COMPLIANCE_[A-Z_]+)\b", text)
    return m.group(1) if m else None


def map_context_pipeline(code: str):
    if code == "CONTEXT_PIPELINE_READY":
        return "AGENTOS_STATUS_OK", "OK", "NONE", True, False, False
    if code == "CONTEXT_PIPELINE_BLOCKED":
        return "AGENTOS_STATUS_BLOCKED", "BLOCKED", "SYSTEM_BLOCKED", False, True, False
    if code == "CONTEXT_PIPELINE_NEEDS_REVIEW":
        return "AGENTOS_STATUS_NEEDS_REVIEW", "NEEDS_REVIEW", "HUMAN_REVIEW_OPTIONAL", False, False, False
    if code in {"CONTEXT_PIPELINE_STALE", "CONTEXT_INDEX_STALE", "CONTEXT_PACK_MISSING", "CONTEXT_PACK_INVALID", "CONTEXT_COMPLIANCE_MISSING"}:
        return "AGENTOS_STATUS_NEEDS_REVIEW", "NEEDS_REVIEW", "HUMAN_REVIEW_OPTIONAL", False, False, False
    return "AGENTOS_STATUS_UNKNOWN", "UNKNOWN", "SYSTEM_BLOCKED", False, True, True


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--strict", action="store_true")
    ap.add_argument("--no-color", action="store_true")
    ap.add_argument("--ascii", action="store_true")
    ap.add_argument("--root", default=".")
    ap.add_argument("--snapshot", nargs="?", const="reports/status-snapshot.md")
    ap.add_argument("--source-summary", action="store_true")
    args = ap.parse_args()

    root = Path(args.root).resolve()
    vocab_path = root / "data/explanations/status-vocabulary.yml"
    cp_json = root / "reports/context-pipeline.json"
    cp_md = root / "reports/context-pipeline.md"
    cv_md = root / "reports/context-verification.md"

    warnings = []
    errors = []
    sources = []
    missing_sources = []
    damaged_sources = []
    stale_sources = []

    vocab, vocab_state = load_vocab(vocab_path)
    sources.append({"name": "status-vocabulary", "path": "data/explanations/status-vocabulary.yml", "state": vocab_state, "freshness": freshness(vocab_path)})
    if vocab_state == "missing":
        missing_sources.append("data/explanations/status-vocabulary.yml")
    if vocab_state == "damaged":
        damaged_sources.append("data/explanations/status-vocabulary.yml")

    cp_source = None
    cp_code = None

    for name, p, fmt in [
        ("context-pipeline", cp_json, "json"),
        ("context-pipeline-fallback", cp_md, "md"),
        ("context-verification-fallback", cv_md, "md"),
    ]:
        st = source_state(p)
        fr = freshness(p)
        item = {"name": name, "path": str(p.relative_to(root)) if p.exists() else str(p.relative_to(root)), "state": st, "freshness": fr, "status_code": None}
        if fr == "stale":
            stale_sources.append(item["path"])
        if st == "missing":
            missing_sources.append(item["path"])
        if st == "damaged":
            damaged_sources.append(item["path"])
        if cp_source is None and st == "present":
            try:
                if fmt == "json":
                    obj = read_json(p)
                    cp_code = obj.get("result") or obj.get("top_status_code")
                    if not cp_code:
                        raise ValueError("missing status code")
                else:
                    cp_code = extract_status_from_md(p)
                    if not cp_code:
                        raise ValueError("cannot extract status")
                cp_source = item["path"]
                item["status_code"] = cp_code
            except Exception:
                item["state"] = "damaged"
                damaged_sources.append(item["path"])
                errors.append("damaged status source: {}".format(item["path"]))
        sources.append(item)

    if cp_source is None:
        cp_code = "STATUS_SOURCE_MISSING"

    overall, sev, auth, is_ready, is_blocked, is_unknown = map_context_pipeline(cp_code)
    top = cp_code

    if vocab_state in {"missing", "damaged"}:
        overall = "AGENTOS_STATUS_UNKNOWN"
        top = "STATUS_SOURCE_MISSING" if vocab_state == "missing" else "STATUS_SOURCE_DAMAGED"
        sev = "UNKNOWN"
        auth = "SYSTEM_BLOCKED"
        is_ready = False
        is_blocked = True
        is_unknown = True

    if vocab and top not in vocab:
        overall = "AGENTOS_STATUS_UNKNOWN"
        top = "STATUS_SOURCE_DAMAGED"
        sev = "UNKNOWN"
        auth = "SYSTEM_BLOCKED"
        is_ready = False
        is_blocked = True
        is_unknown = True
        errors.append("missing vocabulary entry for observed status code")

    if cp_source is None:
        overall = "AGENTOS_STATUS_UNKNOWN"
        sev = "UNKNOWN"
        auth = "SYSTEM_BLOCKED"
        is_ready = False
        is_blocked = True
        is_unknown = True

    if stale_sources and overall == "AGENTOS_STATUS_OK":
        overall = "AGENTOS_STATUS_NEEDS_REVIEW"
        top = "STATUS_STALE"
        sev = "NEEDS_REVIEW"
        auth = "HUMAN_REVIEW_OPTIONAL"
        is_ready = False
        warnings.append("critical source is stale")

    result = {
        "schema_version": "1.0",
        "generated_at": now_iso(),
        "repo_root": str(root),
        "overall_status": overall,
        "top_status_code": top,
        "severity": sev,
        "authority": auth,
        "is_ready": is_ready,
        "is_blocked": is_blocked,
        "is_unknown": is_unknown,
        "sources": sources,
        "missing_sources": sorted(set(missing_sources)),
        "damaged_sources": sorted(set(damaged_sources)),
        "stale_sources": sorted(set(stale_sources)),
        "warnings": warnings,
        "errors": errors,
        "summary": {
            "AGENTOS_STATUS_OK": "AgentOS в норме.",
            "AGENTOS_STATUS_NEEDS_REVIEW": "AgentOS: нужно проверить.",
            "AGENTOS_STATUS_BLOCKED": "AgentOS: действие заблокировано.",
            "AGENTOS_STATUS_UNKNOWN": "AgentOS: статус неизвестен.",
            "AGENTOS_STATUS_WARN": "AgentOS: есть предупреждение.",
        }.get(overall, "AgentOS: неизвестный статус."),
    }

    if args.snapshot:
        snap = Path(args.snapshot)
        snap_abs = (root / snap).resolve() if not snap.is_absolute() else snap.resolve()
        if not str(snap_abs).startswith(str(root)):
            print("unsafe snapshot path", file=sys.stderr)
            return 3
        protected = {root / "reports/context-pipeline.md", root / "reports/M30-EVIDENCE-REPORT.md"}
        if snap_abs in protected:
            print("unsafe snapshot path", file=sys.stderr)
            return 3
        snap_abs.parent.mkdir(parents=True, exist_ok=True)
        snap_abs.write_text(
            "# AgentOS Status Snapshot\n\n"
            f"generated_at: {result['generated_at']}\n"
            f"overall_status: {overall}\n"
            f"top_status_code: {top}\n"
            f"severity: {sev}\n"
            f"authority: {auth}\n\n"
            f"sources: {', '.join([s['path'] for s in sources])}\n\n"
            "This snapshot is not approval.\n",
            encoding="utf-8",
        )

    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        label = {"AGENTOS_STATUS_OK": "✅", "AGENTOS_STATUS_NEEDS_REVIEW": "🔎", "AGENTOS_STATUS_BLOCKED": "⛔", "AGENTOS_STATUS_UNKNOWN": "❓", "AGENTOS_STATUS_WARN": "⚠️"}.get(overall, "❓")
        if args.ascii:
            label = {"AGENTOS_STATUS_OK": "[OK]", "AGENTOS_STATUS_NEEDS_REVIEW": "[REVIEW]", "AGENTOS_STATUS_BLOCKED": "[BLOCKED]", "AGENTOS_STATUS_UNKNOWN": "[UNKNOWN]", "AGENTOS_STATUS_WARN": "[WARNING]"}.get(overall, "[UNKNOWN]")
        print(f"{label} AgentOS: {result['summary']}")
        print(f"Status: {overall}")
        print(f"Reason: {top}")
        if cp_source:
            print(f"Source: {cp_source}")

    if args.strict:
        return 0 if overall == "AGENTOS_STATUS_OK" else 1
    return 0 if overall in {"AGENTOS_STATUS_OK", "AGENTOS_STATUS_WARN"} else 1


if __name__ == "__main__":
    sys.exit(main())
