#!/usr/bin/env python3
import argparse, json
from pathlib import Path
import sys

OK='EVIDENCE_AMENDMENT_OK'
VIOL='EVIDENCE_AMENDMENT_VIOLATION'
REVIEW='EVIDENCE_AMENDMENT_NEEDS_REVIEW'
SCOPES={'metadata-only','command-output-correction','hash-correction','rerun-record','report-correction','other'}


def emit(r,f,m,p,d,j):
    out={"result":r,"failure_class":f,"message":m,"checked_path":str(p),"details":d}
    print(json.dumps(out) if j else f"{r}: {m}")
    return 0 if r==OK else 1

def load(p):
    if p.is_dir(): p=p/'evidence-amendment.json'
    return p, json.loads(p.read_text(encoding='utf-8'))

def main():
    ap=argparse.ArgumentParser(description='Check evidence amendments.')
    ap.add_argument('path', nargs='?')
    ap.add_argument('--json', action='store_true', dest='as_json')
    a=ap.parse_args()
    if not a.path: ap.print_help(); return 0
    p=Path(a.path)
    try: _,d=load(p)
    except Exception as e: return emit(REVIEW,'AMENDMENT_AUTHORITY_AMBIGUOUS',f'Invalid input: {e}',p,[],a.as_json)

    prev=d.get('previous_sha256'); new=d.get('new_sha256')
    if not prev or not new: return emit(VIOL,'AMENDMENT_HASH_LINK_BROKEN','Missing hash link.',p,[],a.as_json)
    if prev==new: return emit(VIOL,'AMENDMENT_HASH_LINK_BROKEN','Previous and new hash identical for correction.',p,[],a.as_json)
    if not str(d.get('reason','')).strip(): return emit(VIOL,'AMENDMENT_REASON_MISSING','Reason missing.',p,[],a.as_json)
    scope=d.get('correction_scope')
    if not scope or scope not in SCOPES: return emit(VIOL,'AMENDMENT_SCOPE_AMBIGUOUS','Scope missing or unknown.',p,[],a.as_json)
    if scope=='other': return emit(REVIEW,'AMENDMENT_SCOPE_AMBIGUOUS','Scope other requires review.',p,[],a.as_json)
    if d.get('failed_evidence_preserved') is not True: return emit(VIOL,'FAILED_EVIDENCE_NOT_PRESERVED','Failed evidence not preserved.',p,[],a.as_json)
    if not str(d.get('rerun_cause','')).strip(): return emit(VIOL,'RERUN_CAUSE_MISSING','Rerun cause missing.',p,[],a.as_json)
    if str(d.get('created_by','')).lower()=='execution-agent': return emit(VIOL,'AMENDMENT_AUTHORITY_AMBIGUOUS','Execution agent cannot author amendment authority.',p,[],a.as_json)
    if d.get('claims_approval_authority') is True: return emit(VIOL,'AMENDMENT_AUTHORITY_AMBIGUOUS','Amendment claims approval authority.',p,[],a.as_json)
    if not d.get('reviewed_by'): return emit(REVIEW,'AMENDMENT_AUTHORITY_AMBIGUOUS','Reviewer missing.',p,[],a.as_json)
    if str(d.get('created_by','')).strip() in {'','unknown','ambiguous'}: return emit(REVIEW,'AMENDMENT_AUTHORITY_AMBIGUOUS','Amendment author ambiguous.',p,[],a.as_json)
    if not d.get('created_at'): return emit(REVIEW,'AMENDMENT_AUTHORITY_AMBIGUOUS','created_at missing.',p,[],a.as_json)
    return emit(OK,None,'Amendment record is valid.',p,[],a.as_json)

if __name__=='__main__': sys.exit(main())
