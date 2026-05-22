import os
import sys

def create_task(title):
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
    queue_dir = os.path.join(base_dir, "tasks", "queue")
    
    if not os.path.exists(queue_dir):
        os.makedirs(queue_dir)
        
    i = 1
    while True:
        task_filename = f"task-{i:03d}.md"
        task_path = os.path.join(queue_dir, task_filename)
        if not os.path.exists(task_path):
            break
        i += 1
        
    content = f"""# Task: {title}

## Goal
{title}

## Risk
UNKNOWN

## Status
QUEUE
"""
    with open(task_path, 'w') as f:
        f.write(content)
    
    print(f"Created task: {task_path}")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] in ["--help", "-h"]:
        print("Usage: python3 new-task.py \"Task Title\"")
        print("Creates a new task file in tasks/queue/")
        sys.exit(0)
    if len(sys.argv) < 2:
        print("Usage: python3 new-task.py \"Task Title\"")
        sys.exit(1)
    create_task(sys.argv[1])
