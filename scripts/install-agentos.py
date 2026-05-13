#!/usr/bin/env python3
import argparse
import json
import os
import shutil
import sys
from pathlib import Path

def get_installer_plan(source_template, target_root):
    plan = {'planned_operations': [], 'warnings': [], 'blockers': []}
    
    # 1. Target checks
    if not target_root.exists():
        plan['blockers'].append(f'target {target_root} does not exist')
        return plan
    if not target_root.is_dir():
        plan['blockers'].append(f'target {target_root} is not a directory')
        return plan
    if not (target_root / '.git').exists():
        plan['blockers'].append(f'target {target_root} is not a git repository')

    # 2. Source checks
    if not source_template.exists():
        plan['blockers'].append(f'source template missing at {source_template}')
        return plan
    
    config_path = source_template / '.agentos' / 'config.yml'
    if not config_path.exists():
        plan['blockers'].append('source template has no .agentos/config.yml')
    else:
        config_text = config_path.read_text()
        if 'mode: simple' not in config_text:
            plan['blockers'].append('source template has no Simple Mode default')
        if 'full_mode_grants_extra_permissions: false' not in config_text:
            plan['blockers'].append('Full Mode permission boundary missing in source template')

    # 3. Conflict checks
    if (target_root / 'agentos').exists():
        plan['blockers'].append('target/agentos/ already exists')
    if (target_root / '.agentos').exists():
        plan['blockers'].append('target/.agentos/ already exists')

    # 4. Warnings
    for w in ['README.md', '.github', 'docs', 'scripts', 'tasks', 'reports']:
        if (target_root / w).exists():
            plan['warnings'].append(f'target/{w} already exists (will be skipped during integration)')

    # 5. Compute operations
    if not plan['blockers'] or True: # Always compute if possible, blockers will be checked later
        # agentos/
        src_agentos = source_template / 'agentos'
        if src_agentos.exists():
            plan['planned_operations'].append({'src': str(src_agentos), 'dst': str(target_root / 'agentos'), 'action': 'copy_tree'})
        
        # .agentos/
        src_dot_agentos = source_template / '.agentos'
        if src_dot_agentos.exists():
            plan['planned_operations'].append({'src': str(src_dot_agentos), 'dst': str(target_root / '.agentos'), 'action': 'copy_tree'})
        
        # Managed subdirs inside target/agentos/
        for sub in ['tasks/queue', 'tasks/done', 'tasks/failed', 'reports']:
            dst_sub = target_root / 'agentos' / sub
            plan['planned_operations'].append({'src': None, 'dst': str(dst_sub), 'action': 'mkdir_p'})
            plan['planned_operations'].append({'src': 'empty', 'dst': str(dst_sub / '.gitkeep'), 'action': 'touch'})

    return plan

def main():
    parser = argparse.ArgumentParser(description='AgentOS Safe Installer')
    parser.add_argument('--target', required=True, help='Target repository root')
    parser.add_argument('--template', default='templates/agentos-clean', help='Source template path')
    parser.add_argument('--dry-run', action='store_true', help='Show plan only (default)')
    parser.add_argument('--apply', action='store_true', help='Execute installation')
    parser.add_argument('--json', action='store_true', help='Output in JSON format')
    args = parser.parse_args()

    if args.dry_run and args.apply:
        print('ERROR: provide either --dry-run or --apply, not both')
        sys.exit(1)

    target_root = Path(args.target).resolve()
    source_template = Path(args.template).resolve()
    op_mode = 'apply' if args.apply else 'dry-run'
    
    plan = get_installer_plan(source_template, target_root)
    
    # Determine result token
    if plan['blockers']:
        result_token = 'INSTALL_PLAN_BLOCKED' if op_mode == 'dry-run' else 'AGENTOS_INSTALL_BLOCKED'
    elif plan['warnings']:
        result_token = 'INSTALL_PLAN_SAFE_WITH_WARNINGS' if op_mode == 'dry-run' else 'AGENTOS_INSTALL_APPLIED_WITH_WARNINGS'
    else:
        result_token = 'INSTALL_PLAN_SAFE' if op_mode == 'dry-run' else 'AGENTOS_INSTALL_APPLIED'

    if args.json:
        output = {
            'target': str(target_root),
            'template': str(source_template),
            'operation_mode': op_mode,
            'agentos_mode': 'simple',
            'warnings': plan['warnings'],
            'blockers': plan['blockers'],
            'planned_operations': plan['planned_operations'] if not plan['blockers'] else [],
            'result_token': result_token
        }
        print(json.dumps(output, indent=2))
        sys.exit(0 if not plan['blockers'] else 1)

    print('AgentOS Existing Project Install Plan')
    print(f'\nTarget:')
    print(f'  - path: {target_root}')
    print(f'  - is git repo: {"yes" if (target_root / ".git").exists() else "no"}')
    
    detected = "no"
    if (target_root / "agentos").exists() or (target_root / ".agentos").exists():
        detected = "yes"
    print(f'  - existing AgentOS detected: {detected}')

    print(f'\nSource template:')
    print(f'  - path: {source_template}')
    print(f'  - Simple Mode default: yes')
    print(f'  - Full Mode grants extra permissions: no')

    if not plan['blockers']:
        print(f'\nPlanned operations:')
        for op in plan['planned_operations']:
            print(f'  - {op["action"]}: {op["src"] if op["src"] else "[internal]"} -> {op["dst"]}')

    if plan['warnings']:
        print(f'\nWarnings:')
        for w in plan['warnings']:
            print(f'  - {w}')

    if plan['blockers']:
        print(f'\nBlocking conflicts:')
        for b in plan['blockers']:
            print(f'  - [FAIL] {b}')

    print(f'\nResult:\n  {result_token}')

    if op_mode == 'dry-run':
        sys.exit(0 if not plan['blockers'] else 1)

    if plan['blockers']:
        print('\nERROR: Cannot apply due to blocking conflicts.')
        sys.exit(1)

    print('\nApplying installation...')
    try:
        for op in plan['planned_operations']:
            dst_path = Path(op['dst'])
            if op['action'] == 'copy_tree':
                shutil.copytree(op['src'], op['dst'])
            elif op['action'] == 'mkdir_p':
                dst_path.mkdir(parents=True, exist_ok=True)
            elif op['action'] == 'touch':
                dst_path.parent.mkdir(parents=True, exist_ok=True)
                with open(dst_path, 'w') as f:
                    f.write('')
        
        print('\nAGENTOS_INSTALL_APPLIED')
        sys.exit(0)
    except Exception as e:
        print(f'\nERROR: Installation failed: {e}')
        sys.exit(1)

if __name__ == "__main__":
    main()
