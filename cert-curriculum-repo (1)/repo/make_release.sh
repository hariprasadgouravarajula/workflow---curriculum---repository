#!/bin/sh
# Run after replacing data. Needs a GitHub repo already created and `git remote add origin ...`
git init -b main 2>/dev/null; git add -A && git commit -m "Submission: certificate workflow and curriculum redesign"
git tag -a v1.0-submission -m "Submission release"
git push -u origin main --tags
git rev-parse HEAD   # full 40-character SHA for the commit URL
echo "Then create the release from tag v1.0-submission on GitHub."
