"""Synthetic prototype of the certificate-request workflow. No real data. Not production."""
from datetime import date, timedelta
REQUIRED = ["cert_type", "purpose", "copies", "required_by", "docs_ok"]
CERT_TYPES = {"BONAFIDE", "NO_DUES", "CHARACTER", "TRANSCRIPT_REQUEST"}
DUP_WINDOW_DAYS = 7

def add_workdays(d, n):
    while n > 0:
        d += timedelta(days=1)
        if d.weekday() < 5: n -= 1
    return d

class Request:
    _seq = 0
    def __init__(self, student_ref, requester_ref, channel_verified, fields, submitted):
        Request._seq += 1
        self.id = f"REQ-{Request._seq:04d}"
        self.student_ref, self.requester_ref = student_ref, requester_ref
        self.channel_verified, self.fields, self.submitted = channel_verified, dict(fields), submitted
        self.status, self.message, self.linked_to, self.log = "SUBMITTED", "", None, []
        self.hold_since = None
    def to(self, status, who, note=""):
        self.log.append((self.status, status, who, note)); self.status = status

class Desk:
    """Owner role: Academic Office desk in-charge."""
    def __init__(self): self.requests = []
    def intake(self, r):
        self.requests.append(r)
        if not r.channel_verified or r.requester_ref != r.student_ref:
            r.message = "Request cannot be accepted. Apply from your verified college account."
            r.to("REJECTED", "SYSTEM", "unverified channel or third-party requester"); return r
        missing = [f for f in REQUIRED if not r.fields.get(f)]
        if r.fields.get("cert_type") and r.fields["cert_type"] not in CERT_TYPES: missing.append("cert_type(valid)")
        if missing:
            r.message = "Missing: " + ", ".join(missing); r.to("NEEDS_INFO", "SYSTEM", r.message); return r
        for o in self.requests:
            if o is not r and o.student_ref == r.student_ref and o.status not in ("REJECTED", "NEEDS_INFO") \
               and o.fields.get("cert_type") == r.fields["cert_type"] and o.fields.get("purpose") == r.fields["purpose"] \
               and abs((r.submitted - o.submitted).days) <= DUP_WINDOW_DAYS:
                r.linked_to = o.id; r.message = f"Linked to {o.id}"; r.to("DUPLICATE_LINKED", "SYSTEM", r.message); return r
        r.to("VERIFIED", "SYSTEM", "complete, unique"); return r
    def resubmit(self, r, fields):
        assert r.status == "NEEDS_INFO"; r.fields.update(fields); r.status = "SUBMITTED"
        self.requests.remove(r); return self.intake(r)
    def send_for_approval(self, r, notify_ok=True, today=None):
        if r.status != "VERIFIED": return False
        r.to("PENDING_APPROVAL", "CLERK")
        if not notify_ok: r.hold_since = today; r.to("ON_HOLD", "SYSTEM", "approver notification failed")
        return True
    def approve(self, r, role):
        if role != "AUTHORITY" or r.status != "PENDING_APPROVAL":
            return False  # clerks/automation can never approve
        r.to("APPROVED", role); return True
    def escalate_if_due(self, r, today):
        if r.status == "ON_HOLD" and r.hold_since and today >= add_workdays(r.hold_since, 2):
            r.to("PENDING_APPROVAL", "OWNER", "escalated to alternate signatory; manual fallback, same ID"); return True
        return False
    def issue(self, r):
        if r.status != "APPROVED": return False
        r.to("ISSUED", "CLERK"); return True
    def close(self, r):
        if r.status != "ISSUED": return False
        r.to("CLOSED", "CLERK"); return True
