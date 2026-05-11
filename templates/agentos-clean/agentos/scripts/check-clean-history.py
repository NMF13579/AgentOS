import os
import sys

def check():
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    
    forbidden_patterns = ["m37", "m38", "m39", "m40"]
    forbidden_files = [
        "completion-review.md", 
        "evidence-report.md",
        "context-pack.md",
        "context-selection-record.md",
        "context-index.json",
        "STATUS.md"
    ]
    forbidden_dirs = [".agentos/cache", ".agentos/runtime/cache"]
    
    found_forbidden = []
    
    for root, dirs, files in os.walk(base_dir):
        # Skip template directory for specific template-owned files
        if "agentos/templates" in root:
            continue
            
        for file in files:
            if any(p in file for p in forbidden_patterns):
                found_forbidden.append(os.path.join(root, file))
            if any(f == file for f in forbidden_files):
                # Extra check for STATUS.md - only forbidden under .agentos/runtime/
                if file == "STATUS.md" and ".agentos/runtime" not in root:
                    continue
                found_forbidden.append(os.path.join(root, file))
                
        for d in dirs:
            full_dir = os.path.relpath(os.path.join(root, d), base_dir)
            if any(f == full_dir for f in forbidden_dirs):
                found_forbidden.append(full_dir)

    # Check tasks/done and tasks/failed for actual tasks
    for d in ["tasks/done", "tasks/failed"]:
        full_path = os.path.join(base_dir, d)
        if os.path.exists(full_path):
            files = [f for f in os.listdir(full_path) if f != ".gitkeep"]
            if files:
                found_forbidden.append(f"{d} contains tasks: {files}")

    if found_forbidden:
        print("CLEAN_HISTORY_DIRTY")
        for f in found_forbidden:
            print(f"  - Found forbidden: {f}")
        sys.exit(1)
    else:
        print("CLEAN_HISTORY_OK")
        sys.exit(0)

if __name__ == "__main__":
    check()
