#!/usr/bin/env python3
"""
AgentOS MVP Readiness Audit Entrypoint.

Wrapper script that invokes the main audit runner in MVP readiness mode.
Identified as a P1 recommended fixup for M35.
"""

import sys
import subprocess
from pathlib import Path

def main():
    repo_root = Path(__file__).resolve().parent.parent
    audit_script = repo_root / "scripts" / "audit-agentos.py"
    
    if not audit_script.is_file():
        print(f"FAIL: audit script not found at {audit_script}")
        sys.exit(1)
        
    # Delegate to canonical audit runner with the M34 MVP readiness flag.
    # Note: audit-agentos.py may ignore this flag but it is required for 
    # compatibility with M34/M35 audit protocols.
    cmd = [sys.executable, str(audit_script), "--m34-mvp-readiness"]
    
    try:
        # Pass through any additional CLI args
        result = subprocess.run(cmd + sys.argv[1:], cwd=repo_root)
        sys.exit(result.returncode)
    except Exception as e:
        print(f"ERROR: failed to execute audit: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
