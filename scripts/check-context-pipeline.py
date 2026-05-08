#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path
from typing import Any

READY='CONTEXT_PIPELINE_READY'
READY_WARN='CONTEXT_PIPELINE_READY_WITH_WARNINGS'
MISSING='CONTEXT_PIPELINE_MISSING'
INVALID='CONTEXT_PIPELINE_INVALID'
STALE='CONTEXT_PIPELINE_STALE'
VIOLATION='CONTEXT_PIPELINE_VIOLATION'
INCOMPLETE='CONTEXT_PIPELINE_INCOMPLETE'
NEEDS_REVIEW='CONTEXT_PIPELINE_NEEDS_REVIEW'
BLOCKED='CONTEXT_PIPELINE_BLOCKED'

ORDER={BLOCKED:0,VIOLATION:1,INVALID:2,STALE:3,INCOMPLETE:4,MISSING:5,NEEDS_REVIEW:6,READY_WARN:7,READY:8}

INDEX_MAP={
'CONTEXT_INDEX_FRESH':READY,
'CONTEXT_INDEX_FRESH_WITH_WARNINGS':READY_WARN,
'CONTEXT_INDEX_STALE':STALE,
'CONTEXT_INDEX_MISSING':MISSING,
'CONTEXT_INDEX_INVALID':INVALID,
'CONTEXT_INDEX_INCOMPLETE':INCOMPLETE,
'CONTEXT_INDEX_NEEDS_REVIEW':NEEDS_REVIEW,
'CONTEXT_INDEX_BLOCKED':BLOCKED,
}
PACK_MAP={
'CONTEXT_PACK_VALID':READY,
'CONTEXT_PACK_VALID_WITH_WARNINGS':READY_WARN,
'CONTEXT_PACK_MISSING':MISSING,
'CONTEXT_PACK_INVALID':INVALID,
'CONTEXT_PACK_STALE':STALE,
'CONTEXT_PACK_INCOMPLETE':INCOMPLETE,
'CONTEXT_PACK_NEEDS_REVIEW':NEEDS_REVIEW,
'CONTEXT_PACK_BLOCKED':BLOCKED,
}
COMP_MAP={
'CONTEXT_COMPLIANCE_PASS':READY,
'CONTEXT_COMPLIANCE_PASS_WITH_WARNINGS':READY_WARN,
'CONTEXT_COMPLIANCE_MISSING':MISSING,
'CONTEXT_COMPLIANCE_INVALID':INVALID,
'CONTEXT_COMPLIANCE_VIOLATION':VIOLATION,
'CONTEXT_COMPLIANCE_INCOMPLETE':INCOMPLETE,
'CONTEXT_COMPLIANCE_NEEDS_REVIEW':NEEDS_REVIEW,
'CONTEXT_COMPLIANCE_BLOCKED':BLOCKED,
}


def pick(a:str,b:str)->str:
    return b if ORDER[b] < ORDER[a] else a


def run_gate(cmd:list[str], timeout:int=30)->tuple[int,dict[str,Any]|None,str|None,str|None]:
    try:
        proc=subprocess.run(cmd,capture_output=True,text=True,shell=False,timeout=timeout)
    except subprocess.TimeoutExpired:
        return 124,None,None,'timeout'
    except Exception as exc:
        return 125,None,None,f'exec_failed:{exc}'
    try:
        data=json.loads(proc.stdout or '{}')
    except Exception:
        return proc.returncode,None,proc.stdout,'malformed_json'
    return proc.returncode,data,proc.stdout,None


def main()->int:
    ap=argparse.ArgumentParser(description='M30.5 Unified Context Pipeline Check')
    ap.add_argument('--json',action='store_true')
    ap.add_argument('--root',default='.')
    ap.add_argument('--task',default='tasks/active-task.md')
    ap.add_argument('--index',default='data/context-index.json')
    ap.add_argument('--context',default='reports/context-pack.md')
    ap.add_argument('--plan',default='reports/plan.md')
    ap.add_argument('--verification',default='reports/context-verification.md')
    ap.add_argument('--changed-files',default='reports/changed-files.txt')
    ap.add_argument('--strict',action='store_true',default=True)
    ap.add_argument('--mode',choices=['plan','verification','both'],default='both')
    a=ap.parse_args()

    root=Path(a.root).resolve()
    gates=[]
    findings=[]
    warnings=[]
    errors=[]
    result=READY

    def record(gate,cmd,mapd,ready_value):
        nonlocal result
        path=root/cmd[1]
        if not path.exists():
            findings.append({'severity':'error','category':'gate_missing','artifact':cmd[1],'message':'required gate script missing'})
            gates.append({'gate':gate,'command':' '.join(cmd),'result':None,'exit_code':127,'parsed_json':None,'warnings':[],'errors':['missing script'],'findings':[]})
            result=pick(result,MISSING)
            return
        rc,data,stdout,err=run_gate(cmd)
        gfind=[]; gw=[]; ge=[]
        if err=='timeout':
            gfind.append({'severity':'needs_review','category':'gate_timeout','message':'gate timeout'})
            gres=NEEDS_REVIEW
        elif err=='malformed_json' or data is None:
            gfind.append({'severity':'error','category':'gate_json_malformed','message':'malformed gate JSON'})
            gres=INCOMPLETE
        elif err:
            gfind.append({'severity':'error','category':'gate_execution_failed','message':err})
            gres=INCOMPLETE
        else:
            gr=data.get('result')
            if not gr:
                gfind.append({'severity':'error','category':'gate_result_missing','message':'gate result missing'})
                gres=INCOMPLETE
            else:
                gres=mapd.get(gr,INCOMPLETE)
                strict_ready = (gr==ready_value)
                if rc==0 and not strict_ready:
                    gfind.append({'severity':'error','category':'gate_exit_result_mismatch','message':'exit 0 without strict ready'})
                    gres=INCOMPLETE
                if strict_ready and rc!=0:
                    gfind.append({'severity':'error','category':'gate_exit_result_mismatch','message':'strict ready with non-zero exit'})
                    gres=INCOMPLETE
        gates.append({'gate':gate,'command':' '.join(cmd),'result':gres,'exit_code':rc,'parsed_json':data,'warnings':gw,'errors':ge,'findings':gfind})
        result=pick(result,gres)
        findings.extend(gfind)

    # Preferred behavior: invoke all three gates independently
    record('context-index-freshness',[sys.executable,'scripts/check-context-index-freshness.py','--json','--root',str(root),'--index',a.index],INDEX_MAP,'CONTEXT_INDEX_FRESH')
    record('required-context-pack',[sys.executable,'scripts/check-required-context-pack.py','--json','--root',str(root),'--task',a.task,'--context',a.context,'--index',a.index],PACK_MAP,'CONTEXT_PACK_VALID')
    record('context-compliance',[sys.executable,'scripts/check-required-context-compliance.py','--json','--root',str(root),'--task',a.task,'--context',a.context,'--plan',a.plan,'--verification',a.verification,'--changed-files',a.changed_files,'--mode',a.mode],COMP_MAP,'CONTEXT_COMPLIANCE_PASS')

    # ready-with-warnings strict behavior
    if result==READY_WARN and a.strict:
        findings.append({'severity':'warning','category':'warning_result_in_strict_mode','message':'READY_WITH_WARNINGS is non-ready in strict mode'})

    if any(f.get('severity')=='blocking' for f in findings) and result in (READY,READY_WARN): result=BLOCKED
    if any(f.get('severity')=='needs_review' for f in findings) and result==READY: result=NEEDS_REVIEW
    if any(f.get('severity')=='error' for f in findings) and result in (READY,READY_WARN): result=INCOMPLETE

    for f in findings:
        line=f"{f.get('category')}: {f.get('message')}"
        if f.get('severity') in ('warning','needs_review'): warnings.append(line)
        if f.get('severity') in ('error','blocking'): errors.append(line)

    out={
        'result':result,
        'mode':a.mode,
        'strict':True,
        'task_path':a.task,
        'index_path':a.index,
        'context_path':a.context,
        'plan_path':a.plan,
        'verification_path':a.verification,
        'changed_files_path':a.changed_files,
        'gate_results':gates,
        'warnings':warnings,
        'errors':errors,
        'findings':findings,
    }

    if a.json:
        print(json.dumps(out,ensure_ascii=False,indent=2))
    else:
        print(f"RESULT: {result}")
        print(f"strict: true")
        print(f"task_path: {a.task}")
        print(f"index_path: {a.index}")
        print(f"context_path: {a.context}")
        print(f"plan_path: {a.plan}")
        print(f"verification_path: {a.verification}")
        for g in gates:
            print(f"- gate={g['gate']} result={g['result']} exit={g['exit_code']}")
        print(f"warnings: {len(warnings)}")
        print(f"errors: {len(errors)}")
        print(result)

    return 0 if result==READY else 1


if __name__=='__main__':
    raise SystemExit(main())
