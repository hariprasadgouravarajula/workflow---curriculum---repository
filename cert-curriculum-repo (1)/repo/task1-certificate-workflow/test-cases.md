# Five synthetic test cases (code: `workflow.py`, runner: `run_tests.py`, results: `test-results.md`)

| # | Case | Given | When | Then (expected) | Recovery | Actual |
|---|---|---|---|---|---|---|
| 1 | Normal | complete bonafide request, verified login | submitted, sent, authority approves | VERIFIED -> PENDING_APPROVAL -> APPROVED -> ISSUED -> CLOSED; a clerk's approval attempt is refused | none | 5/5 PASS |
| 2 | Missing information | purpose empty, checklist not ticked | submitted | NEEDS_INFO naming `purpose` and `docs_ok`; cannot go to approval | student resubmits, becomes VERIFIED | 4/4 PASS |
| 3 | Duplicate | same student, type, purpose 3 days later | submitted | DUPLICATE_LINKED to the first ID; cannot be approved. The same request 8+ days later is treated as new | clerk confirms and tells student | 3/3 PASS |
| 4 | Unauthorized | unverified channel; another person requesting for a student | submitted | REJECTED; message reveals no student data or certificate type; cannot be issued | student reapplies from own verified account; owner sees it in weekly review | 4/4 PASS |
| 5 | Failed step | approver notification fails | sent for approval | ON_HOLD; not escalated after 1 working day; escalated after 2 (weekends skipped) with the same ID | alternate signatory / manual path | 5/5 PASS |

Limit: these test my own prototype's rules on invented data. They show the design is internally consistent, not that it works in a real college.
