#!/usr/bin/env python3
import os
import sys
import glob
from pathlib import Path

def check():
    print('Checking AgentOS clean history...')
    repo_root = Path(__file__).resolve().parent.parent.parent
    
    forbidden_patterns = [
        'reports/m37*',
        'reports/m38*',
        'reports/m39*',
        'reports/m40*',
        'reports/*completion-review.md',
        'reports/*evidence-report.md',
        'reports/context-pack.md',
        'reports/context-selection-record.md',
        'data/context-index.json',
        '.agentos/runtime/STATUS.md',
        '.agentos/cache/**',
        '.agentos/runtime/cache/**',
    ]

    dirty = []
    for pattern in forbidden_patterns:
        matches = glob.glob(str(repo_root / pattern), recursive=True)
        if matches:
            dirty.extend(matches)

    if dirty:
        print(f'[FAIL] Forbidden artifacts found: {dirty}')
        print('CLEAN_HISTORY_DIRTY')
        sys.exit(1)

    print('[PASS] Template clean history: CLEAN_HISTORY_OK')
    print('CLEAN_HISTORY_OK')
    sys.exit(0)

if __name__ == '__main__':
    check()
