# AI-assisted exercises (one per subject, five subjects)

Model for all five: Claude Sonnet 5.5 (Anthropic), run in the claude.ai chat interface on 2026-10-24. Outputs are in `code/`. Verification was executed by `run_verification.py` (result: `verification-log.md`, 5/5 PASS).
**Provenance note:** these were produced while drafting this repo, not in a real class. Before submission, re-run each prompt yourself and record your own date, output and checks.

| # | Subject | Prompt (as sent) | Output file | How verified | Result |
|---|---|---|---|---|---|
| 1 | Data Structures (CS102) | "Write a Python binary search returning the index or -1. Handle an empty list." | `code/ex1_binary_search.py` | 2,000 random sorted lists (incl. empty) compared with `list.index` | 0 mismatches |
| 2 | Database Management Systems (CS206) | "Table results(dept, score). Give SQL for the 2 departments with highest average score, ignoring departments with fewer than 3 rows." | `code/ex2_query.sql` | Ran in in-memory SQLite on 12 synthetic rows; compared with a separate Python calculation; checked that the 2-row dept is excluded | matches |
| 3 | Computer Networks (CS306) | "For 192.168.10.0/26 give mask, usable hosts, first/last host, broadcast." | `code/ex3_subnet.txt` | Compared with Python `ipaddress` module | all 6 facts match |
| 4 | Machine Learning (DS304) | "TP=40, FP=10, FN=20, TN=130. Compute accuracy, precision, recall, F1 and comment." | `code/ex4_metrics.txt` | Recomputed by hand and in Python | matches |
| 5 | Software Engineering (CS304) | "Write is_leap(year) and unit tests that would catch a missing century rule." | `code/ex5_leap.py` | Own tests pass; compared with `calendar.isleap` for 1800-2499; mutant without century rule fails tests (1900, 2100) | caught |

## What this shows for the curriculum
All five were correct, but only because each had an independent check. This supports ADD "Responsible AI and Output Verification" (R7) and the Tools Lab and clean-code emphasis (R3, R5). Five correct outputs prove little about error rates; a fair claim is "these simple tasks worked", not "AI is reliable".
