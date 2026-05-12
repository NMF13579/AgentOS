#!/usr/bin/env python3
import os
import sys
import shutil
import argparse
from pathlib import Path

def check_git(target):
    return (target / '.git').exists()

def get_installer_plan(source_template, target_root):
    plan = {'add': [], 'skip': [], 'conflicts': []}
    
    # Folders to copy
    mappings = [
        (source_template / 'agentos', target_root / 'agentos'),
        (source_template / 'tasks', target_root / 'agentos' / 'tasks'),
        (source_template / 'reports', target_root / 'agentos' / 'reports'),
        (source_template / '.agentos', target_root / '.agentos'),
    ]

    for src, dst in mappings:
        if not src.exists():
            continue
        if dst.exists():
            plan['conflicts'].append(str(dst))
        else:
            plan['add'].append((str(src), str(dst)))
            
    return plan

def main():
    parser = argparse.ArgumentParser(description='AgentOS Installer')
    parser.add_argument('--target', default='.', help='Target directory')
    parser.add_argument('--dry-run', action='store_true', help='Show plan only')
    parser.add_argument('--apply', action='store_true', help='Apply changes')
    args = parser.parse_args()

    target_root = Path(args.target).resolve()
    installer_dir = Path(__file__).resolve().parent
    source_template = installer_dir.parent / 'templates' / 'agentos-clean'

    if not source_template.exists():
        print(f'ERROR: source template missing at {source_template}')
        sys.exit(1)

    if not check_git(target_root):
        print(f'ERROR: target {target_root} is not a git repository')
        sys.exit(1)

    plan = get_installer_plan(source_template, target_root)

    print(f'AgentOS Install Plan for {target_root}:')
    if plan['conflicts']:
        print('BLOCKING CONFLICTS:')
        for c in plan['conflicts']:
            print(f'  [FAIL] {c} already exists')
        if not args.dry_run and not args.apply:
            sys.exit(1)

    print('FILES/FOLDERS TO ADD:')
    for src, dst in plan['add']:
        print(f'  [ADD] {dst}')

    if args.dry_run:
        print('Dry-run complete. No files were modified.')
        return

    if args.apply:
        if plan['conflicts']:
            print('ERROR: Cannot apply due to blocking conflicts.')
            sys.exit(1)
        
        for src, dst in plan['add']:
            dst_path = Path(dst)
            dst_path.parent.mkdir(parents=True, exist_ok=True)
            if Path(src).is_dir():
                shutil.copytree(src, dst)
            else:
                shutil.copy2(src, dst)
        
        print('AgentOS successfully installed.')
        print('Next steps: Review files and commit manually.')
        return

    print('Use --dry-run to see the plan or --apply to install.')

if __name__ == "__main__":
    main()
