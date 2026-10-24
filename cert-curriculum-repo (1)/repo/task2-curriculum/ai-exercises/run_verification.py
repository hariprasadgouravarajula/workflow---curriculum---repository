import sqlite3, random, ipaddress, calendar, sys, datetime
sys.path.insert(0, "code")
from ex1_binary_search import binary_search
from ex5_leap import is_leap, run_tests
out = ["# Verification log (run %s by script, Python %s)\n" % (datetime.date.today(), sys.version.split()[0])]
# 1
random.seed(1); bad = 0
for _ in range(2000):
    a = sorted(random.sample(range(100), random.randint(0, 30))); x = random.randint(-5, 105)
    want = a.index(x) if x in a else -1
    bad += binary_search(a, x) != want
out.append(f"1. binary_search vs list.index on 2000 random cases (incl. empty list): {bad} mismatches -> {'PASS' if bad==0 else 'FAIL'}")
# 2
db = sqlite3.connect(":memory:"); db.execute("create table results(dept text, score real)")
rows = [("CSE",80),("CSE",90),("CSE",70),("ECE",60),("ECE",65),("ECE",70),("ME",95),("ME",99),("CIV",88),("CIV",90),("CIV",92),("CIV",70)]
db.executemany("insert into results values(?,?)", rows)
got = db.execute(open("code/ex2_query.sql").read().strip().rstrip(";")).fetchall()
from collections import defaultdict
g = defaultdict(list); [g[d].append(s) for d, s in rows]
want = sorted([(d, round(sum(v)/len(v), 2)) for d, v in g.items() if len(v) >= 3], key=lambda t: -t[1])[:2]
out.append(f"2. SQL result {got} vs independent Python {want}; ME (2 rows) correctly excluded by HAVING -> {'PASS' if got==want else 'FAIL'}")
# 3
n = ipaddress.ip_network("192.168.10.0/26"); h = list(n.hosts())
ok = (n.netmask == ipaddress.ip_address("255.255.255.192") and n.num_addresses == 64 and len(h) == 62 and str(h[0]) == "192.168.10.1" and str(h[-1]) == "192.168.10.62" and str(n.broadcast_address) == "192.168.10.63")
out.append(f"3. subnet facts checked with ipaddress module -> {'PASS' if ok else 'FAIL'}")
# 4
TP, FP, FN, TN = 40, 10, 20, 130
acc, pr, rc = (TP+TN)/200, TP/(TP+FP), TP/(TP+FN); f1 = 2*pr*rc/(pr+rc)
ok = (round(acc,2), round(pr,2), round(rc,3), round(f1,3)) == (0.85, 0.80, 0.667, 0.727)
out.append(f"4. metrics recomputed: acc={acc:.2f} prec={pr:.2f} rec={rc:.3f} F1={f1:.3f} -> {'PASS' if ok else 'FAIL'}")
# 5
fails = run_tests(is_leap); stdlib = [y for y in range(1800, 2500) if is_leap(y) != calendar.isleap(y)]
mut = run_tests(lambda y: y % 4 == 0)
out.append(f"5. is_leap: failing own tests={fails}; mismatches vs calendar.isleap over 1800-2499={len(stdlib)}; mutant (drops century rule) caught by tests: {mut} -> {'PASS' if not fails and not stdlib and mut else 'FAIL'}")
open("verification-log.md", "w").write("\n\n".join(out) + "\n"); print("\n\n".join(out))
