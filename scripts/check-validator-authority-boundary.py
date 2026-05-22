#!/usr/bin/env python3
import argparse
import json
from pathlib import Path
import sys

OK="VALIDATOR_AUTHORITY_OK"
VIOL="VALIDATOR_AUTHORITY_VIOLATION"
REVIEW="VALIDATOR_AUTHORITY_NEEDS_REVIEW"
KNOWN_SOURCE_TYPES={"CI runner","AgentOS runner","approved validation entrypoint","trusted validation wrapper"}


def emit(result,failure_class,message,path,details,as_json):
    payload={"result":result,"failure_class":failure_class,"message":message,"checked_path":str(path),"details":details}
    if as_json: print(json.dumps(payload))
    else: print(f"{result}: {message}")
    return 0 if result==OK else 1


def load(path):
    if path.is_dir(): path=path/"validator-authority.json"
    return path, json.loads(path.read_text(encoding="utf-8"))


def main():
    ap=argparse.ArgumentParser(description="Check validator authority boundary.")
    ap.add_argument("path", nargs="?")
    ap.add_argument("--json", action="store_true", dest="as_json")
    args=ap.parse_args()
    if not args.path:
        ap.print_help(); return 0
    p=Path(args.path)
    try:
        file,data=load(p)
    except Exception as e:
        return emit(REVIEW,"VERIFICATION_AUTHORITY_AMBIGUOUS",f"Invalid input: {e}",p,[],args.as_json)
    details=[]
    exec_id=data.get("execution_agent_id")
    sources=data.get("trusted_validation_sources")
    if not sources:
        return emit(REVIEW,"TRUSTED_SOURCE_MISSING","Trusted source list missing.",p,details,args.as_json)
    for s in sources:
        if s.get("source_type") not in KNOWN_SOURCE_TYPES:
            return emit(REVIEW,"TRUSTED_SOURCE_UNKNOWN","Unknown source type.",p,details,args.as_json)
        if not s.get("created_by"):
            return emit(REVIEW,"VERIFICATION_AUTHORITY_AMBIGUOUS","Ambiguous source creator.",p,details,args.as_json)
        if s.get("created_during_execution") and str(s.get("created_by",""))==exec_id:
            return emit(VIOL,"AGENT_CREATED_TRUSTED_WRAPPER","Source created by execution agent during execution.",p,details,args.as_json)
        if s.get("modified_by_execution_agent") is True:
            return emit(VIOL,"AGENT_MODIFIED_VALIDATOR","Trusted source modified by execution agent.",p,details,args.as_json)
    tw=data.get("trusted_wrapper",{})
    if tw.get("created_during_execution") is True:
        return emit(VIOL,"AGENT_CREATED_TRUSTED_WRAPPER","Trusted wrapper created during execution.",p,details,args.as_json)
    if tw.get("modified_by_execution_agent") is True:
        return emit(VIOL,"AGENT_MODIFIED_TRUSTED_WRAPPER","Trusted wrapper modified by execution agent.",p,details,args.as_json)
    arts=data.get("validator_artifacts",[])
    if not arts:
        return emit(REVIEW,"VERIFICATION_AUTHORITY_AMBIGUOUS","Validator artifacts missing.",p,details,args.as_json)
    for a in arts:
        if not a.get("sha256_before") or not a.get("sha256_after"):
            return emit(REVIEW,"VERIFICATION_AUTHORITY_AMBIGUOUS","Artifact hash missing.",p,details,args.as_json)
        if a.get("strictness_reduced") is True:
            return emit(VIOL,"VALIDATOR_WEAKENED_AFTER_FAILURE","Strictness reduced.",p,details,args.as_json)
        if a.get("modified_during_execution") and str(a.get("modified_by",""))==exec_id:
            return emit(VIOL,"AGENT_MODIFIED_VALIDATOR","Validator artifact modified by execution agent.",p,details,args.as_json)
    if data.get("failure_context",{}).get("validator_changed_after_failure") is True:
        return emit(VIOL,"VALIDATOR_WEAKENED_AFTER_FAILURE","Validator changed after failure.",p,details,args.as_json)
    return emit(OK,None,"Validator authority boundary holds.",p,details,args.as_json)

if __name__=="__main__":
    sys.exit(main())
