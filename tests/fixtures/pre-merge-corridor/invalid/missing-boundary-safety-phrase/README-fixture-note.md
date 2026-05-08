# Fixture Note

This fixture was originally planned as review/missing-safety-phrase
with expected result NEEDS_REVIEW.

All 12 safety phrases defined in 26.10.1 are classified as boundary
phrases (is_boundary: True). A missing boundary phrase produces NOT_READY,
not NEEDS_REVIEW. Therefore this fixture is classified as invalid and
documents that boundary safety phrase removal produces NOT_READY.

NEEDS_REVIEW coverage for the safety phrase path is not possible with
the current 26.10.1 configuration. NEEDS_REVIEW coverage is provided
by review/missing-evidence-entry only.

To enable a NEEDS_REVIEW safety phrase fixture in a future task,
add at least one non-boundary safety phrase to 26.10.1
REQUIRED_SAFETY_PHRASES with is_boundary=False.
