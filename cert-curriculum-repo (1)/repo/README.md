# Certificate request workflow and curriculum redesign

> Synthetic data: Task 1 process figures and cases only. Task 2 uses the student's portal course list (semesters I-VII) and three real job postings. Student work, not an official syllabus revision.

## Contents
| Path | What |
|---|---|
| `task1-certificate-workflow/` | report, evidence log, current and proposed process maps, working prototype (`workflow.py`), five-case tests (21/21 pass), net-time calculation |
| `task2-curriculum/` | report, credit map, 11 reasons, three real JDs, five AI exercises with verification, capstone lab, feedback note, interactive calculator, portal screenshots |
| `sources.md`, `ai-use-record.md`, `personal-contribution.md`, `limitations.md` | required records |

## Headline results (synthetic inputs)
- Task 1: net saving about 39.7 h per semester (2,380 min) after review, audit, support and setup; range 2.3 to 87.7 h.
- Task 2: 36 of 152 credits affected (23.7%, semesters I-VII); total stays 152; semester loads 20-23 (was 16-24).

## Run it
```
python3 task1-certificate-workflow/run_tests.py     # run from inside that folder
python3 task1-certificate-workflow/net_time.py
python3 task2-curriculum/build_credit_map.py        # run from inside that folder
python3 task2-curriculum/ai-exercises/run_verification.py
open task2-curriculum/calculator/index.html
```

## Release (fill in after publishing)
- Release: `v1.0-submission` -> `https://github.com/<user>/<repo>/releases/tag/v1.0-submission`
- Full commit URL: `https://github.com/<user>/<repo>/commit/<40-character-sha>`

Do not move or delete the tag after submitting.
