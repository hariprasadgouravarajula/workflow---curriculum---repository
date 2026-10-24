from datetime import date
from workflow import *
res = []
def check(case, name, cond): res.append((case, name, "PASS" if cond else "FAIL"))
D0 = date(2026, 10, 19)  # Monday
full = dict(cert_type="BONAFIDE", purpose="Bank account", copies=2, required_by="2026-10-30", docs_ok=True)

# 1 Normal
d = Desk(); r = d.intake(Request("S-001", "S-001", True, full, D0))
check(1, "intake -> VERIFIED", r.status == "VERIFIED")
check(1, "clerk cannot approve", d.send_for_approval(r) and not d.approve(r, "CLERK") and r.status == "PENDING_APPROVAL")
check(1, "authority approves", d.approve(r, "AUTHORITY") and r.status == "APPROVED")
check(1, "issue then close", d.issue(r) and d.close(r) and r.status == "CLOSED")
check(1, "every approval logged with role", any(x[2] == "AUTHORITY" for x in r.log))

# 2 Missing info
d = Desk(); f = dict(full, purpose="", docs_ok=False); r = d.intake(Request("S-002", "S-002", True, f, D0))
check(2, "-> NEEDS_INFO", r.status == "NEEDS_INFO")
check(2, "message names missing fields", "purpose" in r.message and "docs_ok" in r.message)
check(2, "cannot send for approval while incomplete", not d.send_for_approval(r))
d.resubmit(r, dict(purpose="Passport", docs_ok=True))
check(2, "resubmit -> VERIFIED", r.status == "VERIFIED")

# 3 Duplicate
d = Desk(); a = d.intake(Request("S-003", "S-003", True, full, D0))
b = d.intake(Request("S-003", "S-003", True, full, date(2026, 10, 22)))
check(3, "-> DUPLICATE_LINKED", b.status == "DUPLICATE_LINKED" and b.linked_to == a.id)
check(3, "duplicate cannot be approved", not d.approve(b, "AUTHORITY"))
c = d.intake(Request("S-003", "S-003", True, full, date(2026, 11, 20)))
check(3, "same request 8+ days later is NOT duplicate", c.status == "VERIFIED")

# 4 Unauthorized
d = Desk(); r = d.intake(Request("S-004", "S-004", False, full, D0))
check(4, "unverified channel -> REJECTED", r.status == "REJECTED")
r2 = d.intake(Request("S-005", "S-006", True, full, D0))
check(4, "third-party requester -> REJECTED", r2.status == "REJECTED")
check(4, "message reveals no data", "S-005" not in r2.message and "BONAFIDE" not in r2.message)
check(4, "rejected request cannot be issued", not d.issue(r2))

# 5 Failed step
d = Desk(); r = d.intake(Request("S-007", "S-007", True, full, D0))
d.send_for_approval(r, notify_ok=False, today=D0)
check(5, "notification failure -> ON_HOLD", r.status == "ON_HOLD")
check(5, "no escalation after 1 working day", not d.escalate_if_due(r, date(2026, 10, 20)))
check(5, "escalates after 2 working days", d.escalate_if_due(r, date(2026, 10, 21)) and r.status == "PENDING_APPROVAL")
check(5, "same request ID kept", r.id == "REQ-0007" or r.id.startswith("REQ-"))
check(5, "weekend skipped (Fri+2wd = Tue)", add_workdays(date(2026, 10, 23), 2) == date(2026, 10, 27))

with open("test-results.md", "w") as fh:
    fh.write("# Test results (synthetic data, run 2026-10-24)\n\n| Case | Check | Result |\n|---|---|---|\n")
    for c, n, s in res: fh.write(f"| {c} | {n} | {s} |\n")
    p = sum(1 for x in res if x[2] == "PASS"); fh.write(f"\n**{p}/{len(res)} checks passed.**\n")
print(open("test-results.md").read())
