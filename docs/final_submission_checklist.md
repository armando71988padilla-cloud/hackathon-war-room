# Final Submission Checklist

## Current Launch State

- [x] Public GitHub repository exists
- [x] README explains the project clearly
- [x] Dashboard screenshot is captured and linked in README
- [x] Cinematic dashboard is generated
- [x] Interactive sidebar, top-card hotspots, Asset Bay links, and Settings drawer are implemented
- [x] Judge packet is generated
- [x] Launch packet is generated
- [x] Release manifest is generated and judge-facing
- [x] Copilot Build Log documents AI assisted development
- [x] Architecture notes document Microsoft IQ alignment honestly
- [x] Demo video script is updated for the final dashboard
- [x] GitHub Actions Smoke Test is green
- [x] Local smoke test passes with `WAR_ROOM_SMOKE_OK`
- [x] Final check passes with `WAR_ROOM_FINAL_CHECK_OK`
- [x] Secret scan completed with no credential hits
- [x] Demo uses synthetic data only

## Remaining Manual Submission Steps

- [ ] Record final demo video
- [ ] Upload or attach final demo video in the submission portal
- [ ] Paste final portal description from `docs/submission_notes.md`
- [ ] Attach public GitHub repository link
- [ ] Submit the project

## Final Proof Commands

```bash
PYTHONPATH="$PWD/src" python3 -m hackathon_war_room export
PYTHONPATH="$PWD/src" python3 -m hackathon_war_room final-check
PYTHONPATH="$PWD/src" python3 tests/test_demo_workflow.py
```

Expected proof:

```text
WAR_ROOM_EXPORT_OK
WAR_ROOM_FINAL_CHECK_OK
WAR_ROOM_SMOKE_OK
```

## Final Safety Scan

```bash
grep -RInE "ghp_|github_pat_|hf_[A-Za-z0-9]{20,}|sk-[A-Za-z0-9_-]{20,}|AKIA[0-9A-Z]{16}|BEGIN RSA PRIVATE KEY|BEGIN OPENSSH PRIVATE KEY|password[[:space:]]*=|token[[:space:]]*=|api_key[[:space:]]*=" . --exclude-dir=.git --exclude="*.bak_*" --exclude="*.pyc" --exclude="project_readiness_dashboard.html" --exclude="project_readiness_dashboard_preview.html" | sed -n "1,160p" || true
echo "WAR_ROOM_SECRET_SCAN_DONE"
```

Expected proof:

```text
WAR_ROOM_SECRET_SCAN_DONE
```

## Freeze Rule

Feature work is frozen. Do not add new runtime features before submission unless a final proof check exposes a real blocker.

Remaining work should focus only on final demo recording, portal copy, submission upload, and final verification.

