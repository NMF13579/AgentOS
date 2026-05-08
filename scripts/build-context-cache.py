#!/usr/bin/env python3
"""Build/check optional SQLite cache derived from data/context-index.json."""

from __future__ import annotations

import argparse
import hashlib
import json
import sqlite3
import sys
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

CONTEXT_CACHE_BUILT = "CONTEXT_CACHE_BUILT"
CONTEXT_CACHE_OK = "CONTEXT_CACHE_OK"
CONTEXT_CACHE_INVALID = "CONTEXT_CACHE_INVALID"
CONTEXT_CACHE_STALE = "CONTEXT_CACHE_STALE"
CONTEXT_CACHE_SKIPPED = "CONTEXT_CACHE_SKIPPED"
CONTEXT_CACHE_NEEDS_REVIEW = "CONTEXT_CACHE_NEEDS_REVIEW"

EXIT_CODES = {
    CONTEXT_CACHE_BUILT: 0,
    CONTEXT_CACHE_OK: 0,
    CONTEXT_CACHE_INVALID: 1,
    CONTEXT_CACHE_STALE: 1,
    CONTEXT_CACHE_SKIPPED: 0,
    CONTEXT_CACHE_NEEDS_REVIEW: 1,
}

CACHE_SCHEMA_VERSION = "1.0.0"
GENERATOR = "scripts/build-context-cache.py"
DEFAULT_INDEX_PATH = "data/context-index.json"
DEFAULT_CACHE_PATH = ".agentos/cache/context.sqlite"

REQUIRED_TOP_LEVEL = [
    "schema_version",
    "repo_commit_hash",
    "generated_at",
    "generator_version",
    "entries",
]

REQUIRED_ENTRY_FIELDS = [
    "path",
    "type",
    "module",
    "status",
    "authority",
    "tags",
    "context_role",
    "summary",
    "source_hash",
]


@dataclass
class Outcome:
    result: str
    cache_path: str
    source_context_index_path: str
    source_context_index_hash: str | None
    entry_count: int
    warnings: list[str]
    errors: list[str]
    findings: list[dict[str, str]]


def now_utc_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return f"sha256:{h.hexdigest()}"


def is_hash_format(value: str) -> bool:
    if not isinstance(value, str) or not value.startswith("sha256:"):
        return False
    hex_part = value.split(":", 1)[1]
    return bool(hex_part) and all(c in "0123456789abcdef" for c in hex_part.lower())


def is_windows_abs(path_s: str) -> bool:
    if len(path_s) >= 3 and path_s[1] == ":" and path_s[2] in ("/", "\\") and path_s[0].isalpha():
        return True
    return False


def is_abs_or_escape(path_s: str) -> bool:
    p = Path(path_s)
    if p.is_absolute() or is_windows_abs(path_s):
        return True
    parts = p.parts
    return any(part == ".." for part in parts)


def normalize_rel(path_s: str) -> str:
    return Path(path_s).as_posix()


def validate_output_path(root: Path, output_arg: str) -> tuple[str, Path, str | None]:
    candidate = Path(output_arg)
    if not candidate.is_absolute():
        candidate = (root / candidate).resolve()
    else:
        candidate = candidate.resolve()

    cache_root = (root / ".agentos/cache").resolve()
    try:
        candidate.relative_to(cache_root)
    except ValueError:
        return CONTEXT_CACHE_NEEDS_REVIEW, candidate, "if --output resolves outside .agentos/cache/, do not write and return CONTEXT_CACHE_NEEDS_REVIEW"

    return CONTEXT_CACHE_OK, candidate, None


def parse_args(argv: list[str]) -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Build/check optional SQLite context cache")
    p.add_argument("--check", action="store_true", help="verify cache freshness/structure without rewriting")
    p.add_argument("--json", action="store_true", help="print machine-readable JSON")
    p.add_argument("--root", default=".", help="repository root")
    p.add_argument("--output", default=DEFAULT_CACHE_PATH, help="cache output path (must stay inside .agentos/cache/)")
    return p.parse_args(argv)


def load_index(index_path: Path) -> tuple[dict[str, Any] | None, list[str]]:
    errors: list[str] = []
    try:
        raw = index_path.read_text(encoding="utf-8")
        data = json.loads(raw)
    except FileNotFoundError:
        return None, []
    except Exception as exc:
        return {}, [f"context index is invalid JSON: {exc}"]

    for key in REQUIRED_TOP_LEVEL:
        if key not in data:
            errors.append(f"missing required index field: {key}")

    entries = data.get("entries")
    if not isinstance(entries, list):
        errors.append("entries must be a list")
        return data, errors

    for i, entry in enumerate(entries):
        if not isinstance(entry, dict):
            errors.append(f"entry[{i}] must be object")
            continue
        for k in REQUIRED_ENTRY_FIELDS:
            if k not in entry:
                errors.append(f"entry[{i}] missing field: {k}")
        if "path" in entry and isinstance(entry["path"], str):
            if is_abs_or_escape(entry["path"]):
                errors.append(f"if data/context-index.json contains an entry with an absolute path or .. escape, cache is invalid: {entry['path']}")
        if "source_hash" in entry and isinstance(entry["source_hash"], str):
            if not is_hash_format(entry["source_hash"]):
                errors.append(f"entry[{i}] source_hash is not sha256:hexdigest")

    return data, errors


def create_schema(conn: sqlite3.Connection) -> None:
    conn.executescript(
        """
        CREATE TABLE IF NOT EXISTS metadata(
          key TEXT PRIMARY KEY,
          value TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS context_entries(
          path TEXT PRIMARY KEY,
          type TEXT,
          module TEXT,
          status TEXT,
          authority TEXT,
          context_role TEXT,
          tags_json TEXT,
          summary TEXT,
          source_hash TEXT,
          indexed_at TEXT
        );

        CREATE INDEX IF NOT EXISTS idx_context_entries_type ON context_entries(type);
        CREATE INDEX IF NOT EXISTS idx_context_entries_module ON context_entries(module);
        CREATE INDEX IF NOT EXISTS idx_context_entries_status ON context_entries(status);
        CREATE INDEX IF NOT EXISTS idx_context_entries_authority ON context_entries(authority);
        CREATE INDEX IF NOT EXISTS idx_context_entries_context_role ON context_entries(context_role);
        """
    )


def write_cache(cache_path: Path, index_data: dict[str, Any], index_hash: str, warnings: list[str]) -> tuple[str, list[str]]:
    errors: list[str] = []

    repo_commit_hash = index_data.get("repo_commit_hash", "")
    if not isinstance(repo_commit_hash, str) or not repo_commit_hash.strip():
        return CONTEXT_CACHE_INVALID, ["repo_commit_hash missing/empty in context index"]

    cache_path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(cache_path))
    try:
        create_schema(conn)
        conn.execute("DELETE FROM metadata")
        conn.execute("DELETE FROM context_entries")

        metadata = {
            "cache_schema_version": CACHE_SCHEMA_VERSION,
            "source_context_index_path": DEFAULT_INDEX_PATH,
            "source_context_index_hash": index_hash,
            "repo_commit_hash": repo_commit_hash,
            "built_at": now_utc_iso(),
            "generator": GENERATOR,
            "sqlite_is_not_source_of_truth": "true",
        }

        conn.executemany(
            "INSERT INTO metadata(key, value) VALUES(?, ?)",
            [(k, str(v)) for k, v in metadata.items()],
        )

        rows = []
        for entry in sorted(index_data.get("entries", []), key=lambda e: str(e.get("path", ""))):
            path = normalize_rel(str(entry.get("path", "")))
            if is_abs_or_escape(path):
                return CONTEXT_CACHE_INVALID, [f"invalid entry path for cache: {path}"]
            rows.append(
                (
                    path,
                    str(entry.get("type", "")),
                    str(entry.get("module", "")),
                    str(entry.get("status", "")),
                    str(entry.get("authority", "")),
                    str(entry.get("context_role", "")),
                    json.dumps(entry.get("tags", []), ensure_ascii=False, sort_keys=True),
                    str(entry.get("summary", "")),
                    str(entry.get("source_hash", "")),
                    str(entry.get("indexed_at", "")),
                )
            )

        conn.executemany(
            """
            INSERT INTO context_entries(
              path, type, module, status, authority, context_role,
              tags_json, summary, source_hash, indexed_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            rows,
        )
        conn.commit()
    except sqlite3.Error as exc:
        errors.append(f"sqlite write failed: {exc}")
    finally:
        conn.close()

    if errors:
        return CONTEXT_CACHE_INVALID, errors

    if len(index_data.get("entries", [])) == 0:
        warnings.append("entries: [] is schema-valid but operationally suspicious")

    return CONTEXT_CACHE_BUILT, []


def load_metadata(conn: sqlite3.Connection) -> dict[str, str]:
    cur = conn.execute("SELECT key, value FROM metadata")
    return {str(k): str(v) for k, v in cur.fetchall()}


def check_cache(root: Path, cache_path: Path, index_path: Path, index_data: dict[str, Any], index_hash: str) -> tuple[str, list[str], list[str]]:
    warnings: list[str] = []
    errors: list[str] = []

    if not cache_path.exists():
        return CONTEXT_CACHE_INVALID, warnings, ["cache file is missing"]

    try:
        conn = sqlite3.connect(f"file:{cache_path}?mode=ro", uri=True)
    except sqlite3.Error as exc:
        return CONTEXT_CACHE_INVALID, warnings, [f"cache cannot be opened: {exc}"]

    try:
        tables = {r[0] for r in conn.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()}
        if "metadata" not in tables or "context_entries" not in tables:
            return CONTEXT_CACHE_INVALID, warnings, ["required tables are missing"]

        meta = load_metadata(conn)
        required_meta = [
            "cache_schema_version",
            "source_context_index_path",
            "source_context_index_hash",
            "repo_commit_hash",
            "built_at",
            "generator",
            "sqlite_is_not_source_of_truth",
        ]
        for k in required_meta:
            if k not in meta:
                errors.append(f"metadata missing: {k}")

        if errors:
            return CONTEXT_CACHE_INVALID, warnings, errors

        if meta.get("sqlite_is_not_source_of_truth") != "true":
            errors.append("sqlite_is_not_source_of_truth must be true")

        stored_idx_path = meta.get("source_context_index_path", "")
        if stored_idx_path != DEFAULT_INDEX_PATH:
            warnings.append("source_context_index_path differs from default data/context-index.json")

        stored_hash = meta.get("source_context_index_hash", "")
        if stored_hash != index_hash:
            return CONTEXT_CACHE_STALE, warnings, ["source_context_index_hash mismatch"]

        repo_commit_hash = str(index_data.get("repo_commit_hash", ""))
        if meta.get("repo_commit_hash", "") != repo_commit_hash:
            return CONTEXT_CACHE_STALE, warnings, ["repo_commit_hash mismatch between cache and index"]

        cache_count = conn.execute("SELECT COUNT(*) FROM context_entries").fetchone()[0]
        index_count = len(index_data.get("entries", []))
        if cache_count != index_count:
            return CONTEXT_CACHE_STALE, warnings, ["context_entries count mismatch"]

        bad_paths = []
        for (p,) in conn.execute("SELECT path FROM context_entries"):
            ps = str(p)
            if is_abs_or_escape(ps):
                bad_paths.append(ps)

        if bad_paths:
            return CONTEXT_CACHE_INVALID, warnings, [f"cache contains invalid stored paths: {', '.join(sorted(bad_paths)[:5])}"]

        if index_count == 0:
            warnings.append("entries: [] is schema-valid but operationally suspicious")

        if errors:
            return CONTEXT_CACHE_INVALID, warnings, errors

        return CONTEXT_CACHE_OK, warnings, []
    finally:
        conn.close()


def main(argv: list[str]) -> int:
    args = parse_args(argv)

    root = Path(args.root).resolve()
    output_state, cache_path_abs, output_error = validate_output_path(root, args.output)

    findings: list[dict[str, str]] = []
    warnings: list[str] = []
    errors: list[str] = []

    if output_state == CONTEXT_CACHE_NEEDS_REVIEW:
        errors.append(output_error or "unsafe output path")
        payload = Outcome(
            result=CONTEXT_CACHE_NEEDS_REVIEW,
            cache_path=str(Path(args.output).as_posix()),
            source_context_index_path=DEFAULT_INDEX_PATH,
            source_context_index_hash=None,
            entry_count=0,
            warnings=warnings,
            errors=errors,
            findings=[{"severity": "needs_review", "category": "output_path", "message": output_error or "unsafe output path"}],
        )
        print_output(args.json, payload)
        return EXIT_CODES[payload.result]

    index_path = root / DEFAULT_INDEX_PATH
    if not index_path.exists():
        payload = Outcome(
            result=CONTEXT_CACHE_SKIPPED,
            cache_path=str(cache_path_abs.relative_to(root).as_posix()) if cache_path_abs.is_relative_to(root) else str(cache_path_abs),
            source_context_index_path=DEFAULT_INDEX_PATH,
            source_context_index_hash=None,
            entry_count=0,
            warnings=["data/context-index.json is missing; SQLite cache is optional and skipped"],
            errors=[],
            findings=[{"severity": "info", "category": "missing_index", "message": "missing data/context-index.json -> CONTEXT_CACHE_SKIPPED"}],
        )
        print_output(args.json, payload)
        return EXIT_CODES[payload.result]

    index_data, index_errors = load_index(index_path)
    if index_data is None:
        # guarded above, keep defensive
        payload = Outcome(CONTEXT_CACHE_SKIPPED, str(args.output), DEFAULT_INDEX_PATH, None, 0, ["missing index"], [], [])
        print_output(args.json, payload)
        return EXIT_CODES[payload.result]

    if index_errors:
        payload = Outcome(
            result=CONTEXT_CACHE_INVALID,
            cache_path=str(cache_path_abs.relative_to(root).as_posix()) if cache_path_abs.is_relative_to(root) else str(cache_path_abs),
            source_context_index_path=DEFAULT_INDEX_PATH,
            source_context_index_hash=None,
            entry_count=0,
            warnings=[],
            errors=index_errors,
            findings=[{"severity": "error", "category": "index_invalid", "message": e} for e in index_errors],
        )
        print_output(args.json, payload)
        return EXIT_CODES[payload.result]

    assert isinstance(index_data, dict)
    index_hash = sha256_file(index_path)
    entry_count = len(index_data.get("entries", []))

    if args.check:
        result, chk_warnings, chk_errors = check_cache(root, cache_path_abs, index_path, index_data, index_hash)
        warnings.extend(chk_warnings)
        errors.extend(chk_errors)
        payload = Outcome(
            result=result,
            cache_path=str(cache_path_abs.relative_to(root).as_posix()) if cache_path_abs.is_relative_to(root) else str(cache_path_abs),
            source_context_index_path=DEFAULT_INDEX_PATH,
            source_context_index_hash=index_hash,
            entry_count=entry_count,
            warnings=warnings,
            errors=errors,
            findings=[],
        )
        print_output(args.json, payload)
        return EXIT_CODES[result]

    result, build_errors = write_cache(cache_path_abs, index_data, index_hash, warnings)
    errors.extend(build_errors)
    if build_errors and result != CONTEXT_CACHE_BUILT:
        pass

    payload = Outcome(
        result=result,
        cache_path=str(cache_path_abs.relative_to(root).as_posix()) if cache_path_abs.is_relative_to(root) else str(cache_path_abs),
        source_context_index_path=DEFAULT_INDEX_PATH,
        source_context_index_hash=index_hash,
        entry_count=entry_count,
        warnings=warnings,
        errors=errors,
        findings=findings,
    )
    print_output(args.json, payload)
    return EXIT_CODES[result]


def print_output(as_json: bool, payload: Outcome) -> None:
    if as_json:
        print(
            json.dumps(
                {
                    "result": payload.result,
                    "cache_path": payload.cache_path,
                    "source_context_index_path": payload.source_context_index_path,
                    "source_context_index_hash": payload.source_context_index_hash,
                    "entry_count": payload.entry_count,
                    "warnings": payload.warnings,
                    "errors": payload.errors,
                    "findings": payload.findings,
                },
                ensure_ascii=False,
                sort_keys=True,
                indent=2,
            )
        )
        return

    print(f"result={payload.result}")
    print(f"cache_path={payload.cache_path}")
    print(f"source_context_index_path={payload.source_context_index_path}")
    print(f"source_context_index_hash={payload.source_context_index_hash}")
    print(f"entry_count={payload.entry_count}")
    if payload.warnings:
        print("warnings:")
        for w in payload.warnings:
            print(f"- {w}")
    if payload.errors:
        print("errors:")
        for e in payload.errors:
            print(f"- {e}")


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
