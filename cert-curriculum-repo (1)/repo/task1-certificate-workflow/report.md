# Task 1: Student certificate request workflow

> Synthetic data: figures, steps and cases are sample or assumed, as labelled in `evidence-log.csv`.

## 1. Process studied
Issuing student certificates (bonafide, no-dues, character, transcript request) through an academic office. Map: `process-map-current.md`.

## 2. Problem
Paper submission, no tracking, no completeness check at intake, and a single signatory create rework and waiting.

## 3. Scale (synthetic baseline, 20 invented cases, `synthetic-baseline-cases.csv`)
| Measure | Value | Label |
|---|---|---|
| Rework rate | 5/20 = 25% | computed from synthetic file |
| Median / mean turnaround | 4 / 4.4 days | computed from synthetic file |
| Annual staff burden | 800 req x 14 min / 60 = about 187 h | ESTIMATE (invented inputs) |
| Rework share | 25% x 800 = 200 requests, about 33 h at +10 min each | ESTIMATE |

With 20 cases the rates are indicative only (a 95% interval on 25% is roughly 11%-47%).

## 4. Proposal
See `process-map-proposed.md`: structured inputs, 10 statuses, one accountable role, hard approval boundary, 1-day manual fallback.

## 5. Testing
Five synthetic cases, 21/21 checks passed (`test-cases.md`, `test-results.md`). Re-run: `python3 run_tests.py`.

## 6. Net time saved
Gross 3,200 min minus 820 min review, audit, support and setup = **2,380 min (about 39.7 h) per semester** under assumed inputs. Range 2.3 h to 87.7 h across 200-800 requests and 4-8 min saving (`net-time-calc.md`). Gains vanish below about 155 requests per semester at a 4 min saving.

## 7. Risks and limits
Invented inputs; a real office may differ in volume, signatories and rules; no integration, no real users; privacy handled by using pseudonymous IDs only.
