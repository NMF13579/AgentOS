#!/bin/bash
find reports docs scripts tests templates schemas data -maxdepth 5 -type f \
  | grep -Ei "m61|m62|hardening|dogfooding|real-task-trial|diagnostic-trial" \
  | grep -Ev "^reports/(m[0-3][0-9]|m4[0-9]|milestone-10|agentos-validate-cli)|^docs/HONEST-PASS-|^tasks/queue/"
