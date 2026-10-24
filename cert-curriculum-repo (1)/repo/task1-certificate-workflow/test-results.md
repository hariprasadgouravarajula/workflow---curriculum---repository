# Test results (synthetic data, run 2026-10-24)

| Case | Check | Result |
|---|---|---|
| 1 | intake -> VERIFIED | PASS |
| 1 | clerk cannot approve | PASS |
| 1 | authority approves | PASS |
| 1 | issue then close | PASS |
| 1 | every approval logged with role | PASS |
| 2 | -> NEEDS_INFO | PASS |
| 2 | message names missing fields | PASS |
| 2 | cannot send for approval while incomplete | PASS |
| 2 | resubmit -> VERIFIED | PASS |
| 3 | -> DUPLICATE_LINKED | PASS |
| 3 | duplicate cannot be approved | PASS |
| 3 | same request 8+ days later is NOT duplicate | PASS |
| 4 | unverified channel -> REJECTED | PASS |
| 4 | third-party requester -> REJECTED | PASS |
| 4 | message reveals no data | PASS |
| 4 | rejected request cannot be issued | PASS |
| 5 | notification failure -> ON_HOLD | PASS |
| 5 | no escalation after 1 working day | PASS |
| 5 | escalates after 2 working days | PASS |
| 5 | same request ID kept | PASS |
| 5 | weekend skipped (Fri+2wd = Tue) | PASS |

**21/21 checks passed.**
