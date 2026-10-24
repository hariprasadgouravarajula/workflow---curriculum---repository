def net(req=400, old=14.0, new=6.0, review_min=20, weeks=16, audit_pct=.10, audit_min=3, support_pct=.05, support_min=10, setup=180):
    gross = req*(old-new); over = review_min*weeks + req*audit_pct*audit_min + req*support_pct*support_min + setup
    return gross, over, gross-over
g,o,n = net()
L = ["# Net time saved (SYNTHETIC ASSUMPTIONS, per semester)\n",
"| Input | Value | Label |\n|---|---|---|",
"| Requests per semester | 400 | ASSUMPTION |","| Staff min/request, current | 14 | ASSUMPTION |","| Staff min/request, proposed | 6 | ASSUMPTION |",
"| Weekly exception review | 20 min x 16 wk | ASSUMPTION |","| Spot-check audit | 10% of requests x 3 min | ASSUMPTION |",
"| Support queries | 5% of requests x 10 min | ASSUMPTION |","| Setup + training (one-time, charged to semester 1) | 180 min | ASSUMPTION |\n",
f"Gross saving = 400 x (14-6) = **{g:.0f} min**\n\nOverhead = 320 + 120 + 200 + 180 = **{o:.0f} min**\n\n**Net saved = {n:.0f} min = {n/60:.1f} h per semester**\n",
"Steady-state (setup already paid): %.0f min = %.1f h per semester.\n" % (n+180, (n+180)/60),
"## Sensitivity (net hours per semester)\n","| Requests/sem | saving 4 min | saving 6 min | saving 8 min |\n|---|---|---|---|"]
for rq in (200,400,800):
    L.append(f"| {rq} | " + " | ".join(f"{net(req=rq, old=6+s)[2]/60:.1f}" for s in (4,6,8)) + " |")
L.append("\nAll cells stay positive here, but the gain shrinks fast: at 200 requests and 4 min saving it is only about 2 h per semester, barely above the review effort. Below roughly 155 requests per semester at that saving, the change would cost more than it saves.")
open("net-time-calc.md","w").write("\n".join(L)); print("\n".join(L))
