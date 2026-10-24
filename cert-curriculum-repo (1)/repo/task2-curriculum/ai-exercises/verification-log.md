# Verification log (run 2026-10-24 by script, Python 3.12.3)


1. binary_search vs list.index on 2000 random cases (incl. empty list): 0 mismatches -> PASS

2. SQL result [('CIV', 85.0), ('CSE', 80.0)] vs independent Python [('CIV', 85.0), ('CSE', 80.0)]; ME (2 rows) correctly excluded by HAVING -> PASS

3. subnet facts checked with ipaddress module -> PASS

4. metrics recomputed: acc=0.85 prec=0.80 rec=0.667 F1=0.727 -> PASS

5. is_leap: failing own tests=[]; mismatches vs calendar.isleap over 1800-2499=0; mutant (drops century rule) caught by tests: [1900, 2100] -> PASS
