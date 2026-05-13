import os
import sys
import argparse
import shutil

def main():
    parser = argparse.ArgumentParser(description="Prepare AgentOS clean template")
    parser.add_argument("--template", default="templates/agentos-clean", help="Template directory")
    parser.add_argument("--force", action="store_true", help="Overwrite existing files")
    parser.add_argument("--check", action="store_true", help="Read-only check")
    args = parser.parse_args()

    template_dir = args.template
    manifest_path = os.path.join(template_dir, "template-manifest.yml")

    if not os.path.exists(manifest_path):
        print(f"ERROR: Manifest missing at {manifest_path}")
        sys.exit(1)

    # In a real scenario, we might read the manifest and copy files from a source.
    # Here, the task instructed us to create the files.
    # This script will act as a validator/refresher.

    required_dirs = [
        ".agentos/runtime",
        ".github/ISSUE_TEMPLATE",
        "agentos/docs",
        "agentos/templates",
        "agentos/scripts",
        "tasks/queue",
        "tasks/done",
        "tasks/failed",
        "reports"
    ]

    missing_files = []
    
    # Check if directories exist
    if args.check:
        all_present = True
        for d in required_dirs:
            if not os.path.exists(os.path.join(template_dir, d)):
                print(f"MISSING DIR: {d}")
                all_present = False
        
        # Check for forbidden files
        forbidden_found = False
        for root, dirs, files in os.walk(template_dir):
            for file in files:
                if any(m in file for m in ["m37", "m38", "m39", "m40"]):
                    print(f"FORBIDDEN FILE: {os.path.join(root, file)}")
                    forbidden_found = True
        
        if all_present and not forbidden_found:
            print("CLEAN_TEMPLATE_ALREADY_CLEAN")
            sys.exit(0)
        else:
            print("CLEAN_TEMPLATE_NOT_CLEAN")
            sys.exit(1)

    # Implementation of refresh/build (simplified for this task)
    print(f"Refreshing template at {template_dir}")
    # ... logic to ensure dirs exist ...
    for d in required_dirs:
        os.makedirs(os.path.join(template_dir, d), exist_ok=True)
        gitkeep = os.path.join(template_dir, d, ".gitkeep")
        if d in ["tasks/queue", "tasks/done", "tasks/failed", "reports", ".agentos/runtime"]:
             if not os.path.exists(gitkeep):
                 with open(gitkeep, 'w') as f: pass

    print("CLEAN_TEMPLATE_PREPARED")

if __name__ == "__main__":
    main()
