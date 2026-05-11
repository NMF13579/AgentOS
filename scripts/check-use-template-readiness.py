import os
import sys
import argparse
import subprocess

def main():
    parser = argparse.ArgumentParser(description="Check AgentOS use-template readiness")
    parser.add_argument("--template", default="templates/agentos-clean", help="Template directory")
    args = parser.parse_args()

    template_dir = args.template
    
    checks = []
    
    # Basic existence checks
    checks.append((os.path.exists(template_dir), f"Template dir {template_dir} exists"))
    checks.append((os.path.exists(os.path.join(template_dir, "template-manifest.yml")), "Manifest exists"))
    checks.append((os.path.exists(os.path.join(template_dir, ".github", "workflows", "agentos-bootstrap.yml")), "Bootstrap workflow exists"))
    checks.append((os.path.exists(os.path.join(template_dir, ".github", "ISSUE_TEMPLATE", "agentos_task.yml")), "Issue template exists"))
    
    # Mode check
    config_path = os.path.join(template_dir, ".agentos", "config.yml")
    if os.path.exists(config_path):
        with open(config_path, 'r') as f:
            content = f.read()
            checks.append(("mode: simple" in content, "Simple Mode is default"))
            checks.append(("full_mode_grants_extra_permissions: false" in content, "Full Mode boundary enforced"))

    # Workflow safety check
    workflow_path = os.path.join(template_dir, ".github", "workflows", "agentos-bootstrap.yml")
    if os.path.exists(workflow_path):
        with open(workflow_path, 'r') as f:
            content = f.read()
            checks.append(("contents: read" in content, "Workflow has read-only permission"))
            checks.append(("contents: write" not in content, "Workflow has no write permission"))
            checks.append(("git commit" not in content and "git push" not in content, "Workflow has no mutating commands"))

    # Run template-local checks
    print("Running template-local checks...")
    
    bootstrap_script = os.path.join(template_dir, "agentos", "scripts", "check-bootstrap-readiness.py")
    if os.path.exists(bootstrap_script):
        res = subprocess.run([sys.executable, bootstrap_script], capture_output=True, text=True)
        checks.append((res.returncode == 0, f"Template bootstrap readiness: {res.stdout.strip()}"))
        
    history_script = os.path.join(template_dir, "agentos", "scripts", "check-clean-history.py")
    if os.path.exists(history_script):
        res = subprocess.run([sys.executable, history_script], capture_output=True, text=True)
        checks.append((res.returncode == 0, f"Template clean history: {res.stdout.strip()}"))

    validate_script = os.path.join(template_dir, "agentos", "scripts", "agentos-validate.py")
    if os.path.exists(validate_script):
        # Try 'all' first
        res = subprocess.run([sys.executable, validate_script, "all"], capture_output=True, text=True)
        if res.returncode != 0:
            print("WARNING: 'all' failed or unsupported, trying fallback...")
            res = subprocess.run([sys.executable, validate_script], capture_output=True, text=True)
            checks.append((res.returncode == 0, f"Template validation (fallback): {res.stdout.strip()}"))
        else:
            checks.append((True, f"Template validation (all): {res.stdout.strip()}"))

    all_pass = True
    for passed, msg in checks:
        if not passed:
            print(f"[FAIL] {msg}")
            all_pass = False
        else:
            print(f"[PASS] {msg}")
            
    if all_pass:
        print("USE_TEMPLATE_READY")
        sys.exit(0)
    else:
        print("USE_TEMPLATE_NOT_READY")
        sys.exit(1)

if __name__ == "__main__":
    main()
