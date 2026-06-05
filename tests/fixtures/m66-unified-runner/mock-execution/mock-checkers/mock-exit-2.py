#!/usr/bin/env python3
import sys
import json
print(json.dumps({"result": "BLOCKED"}), file=sys.stderr)
sys.exit(2)
