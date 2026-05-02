# Troubleshooting

symptom: validation command fails
likely cause: missing required file or wrong working directory
correct interpretation: current state is not ready for PASS
safe next step: fix missing artifacts and rerun validation

symptom: result is NOT_RUN
likely cause: check was available but not executed
correct interpretation: no evidence was produced
safe next step: run the check and record evidence

symptom: result is ERROR
likely cause: command or checker failed unexpectedly
correct interpretation: execution state is unknown, not PASS
safe next step: inspect error output, fix root cause, rerun
