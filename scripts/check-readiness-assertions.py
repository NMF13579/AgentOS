#!/usr/bin/env python3
"""
Governance Claim Guard (Readiness Assertions)

Validates that files do not declare readiness without a valid completion review token.
"""
import os
import re
import sys
from pathlib import Path

# Result tokens
PASS = "PASS"
FAIL = "FAIL"
WARN = "WARN"

# Readiness tokens (Source of Truth for readiness)
VALID_TOKENS = {
    "M37_PILOT_READY",
    "M38_PILOT_FEEDBACK_HARDENED",
    "M38_PILOT_FEEDBACK_HARDENED_WITH_GAPS",
    "M39_PUBLIC_MVP_READY",
    "M39_PUBLIC_MVP_READY_WITH_GAPS",
}

# Detection patterns (Positive assertions only)
READINESS_CLAIMS = [
    r"(?<!not\s)(?<!not\s\s)(?<!не\s)готов к использованию",
    r"(?<!not\s)(?<!not\s\s)(?<!не\s)готов к пилоту",
    r"(?<!not\s)(?<!not\s\s)(?<!не\s)готов к",
    r"(?<!not\s)(?<!not\s\s)(?<!не\s)ready for use",
    r"(?<!not\s)(?<!not\s\s)(?<!не\s)ready for deployment",
    r"(?<!not\s)(?<!not\s\s)(?<!не\s)ready for pilot",
    r"(?<!not\s)(?<!not\s\s)(?<!не\s)ready for",
    r"(?<!not\s)(?<!not\s\s)(?<!не\s)production-ready",
    r"(?<!not\s)(?<!not\s\s)(?<!не\s)public MVP ready",
]

# Exceptions (allowed without tokens)
EXCEPTIONS = [
    r"готов к рассмотрению",
    r"ready for review",
    r"can be evaluated",
    r"candidate for readiness decision",
    r"NOT_READY", # Status token, not a claim
    r"not production-ready",
    r"not ready for",
]

# Evidence markers that contradict readiness (Source of Truth for FAIL/BLOCKED)
# We only check for these in reports where results are actual
CONTRADICTIONS = ["FAIL", "BLOCKED"]

def check_file(file_path: Path):
    content = file_path.read_text(encoding="utf-8")
    lines = content.splitlines()
    
    findings = []
    has_valid_token = any(token in content for token in VALID_TOKENS)
    
    # We only look for contradictions in files that are supposed to be "ready"
    found_contradictions = []
    if "reports/" in str(file_path):
        found_contradictions = [c for c in CONTRADICTIONS if c in content]

    for i, line in enumerate(lines):
        line_num = i + 1
        
        # Check if line contains a readiness claim
        claim_match = None
        for pattern in READINESS_CLAIMS:
            if re.search(pattern, line, re.IGNORECASE):
                # Check if it's an exception
                is_exception = False
                for exc_pattern in EXCEPTIONS:
                    if re.search(exc_pattern, line, re.IGNORECASE):
                        is_exception = True
                        break
                
                if not is_exception:
                    claim_match = pattern
                    break
        
        if claim_match:
            if not has_valid_token or found_contradictions:
                issue = "Readiness claim without completion review token"
                if found_contradictions and not has_valid_token:
                    issue = f"Readiness claim contradicts evidence markers: {', '.join(found_contradictions)}"
                elif found_contradictions and has_valid_token:
                    issue = f"Readiness claim (even with token) contradicts evidence markers in same file: {', '.join(found_contradictions)}"
                
                # Determine severity
                # ERROR if in reports or contradicts evidence
                severity = ERROR if ("reports/" in str(file_path) or found_contradictions) else WARNING
                if str(file_path).endswith("README.md") and not found_contradictions:
                    severity = WARNING # docs rule
                
                findings.append({
                    "line": line_num,
                    "text": line.strip(),
                    "issue": issue,
                    "severity": severity,
                    "suggested_fix": 'Replace with "ready for review" or add explicit status token'
                })

    return findings

ERROR = "ERROR"
WARNING = "WARNING"

def main():
    repo_root = Path(__file__).resolve().parent.parent
    
    # Files to check
    targets = []
    targets.append(repo_root / "README.md")
    targets.extend(repo_root.glob("docs/*.md"))
    targets.extend(repo_root.glob("reports/*.md"))
    
    all_findings = {}
    has_error = False
    
    for target in targets:
        if not target.is_file():
            continue
        findings = check_file(target)
        if findings:
            all_findings[target.relative_to(repo_root)] = findings
            if any(f["severity"] == ERROR for f in findings):
                has_error = True

    if not all_findings:
        print("PASS: No premature readiness claims detected.")
        return 0

    print("GOVERNANCE_VIOLATION_PREMATURE_READINESS_CLAIM detected:")
    has_warning = False
    for path, findings in all_findings.items():
        print(f"\nFile: {path}")
        for f in findings:
            print(f"  Line {f['line']} [{f['severity']}]: {f['issue']}")
            print(f"    Text: \"{f['text']}\"")
            print(f"    Suggested fix: {f['suggested_fix']}")
            if f["severity"] == WARNING:
                has_warning = True

    if has_error:
        return 1
    if has_warning:
        return 2
    return 0

if __name__ == "__main__":
    sys.exit(main())
