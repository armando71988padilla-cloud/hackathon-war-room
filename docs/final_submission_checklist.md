# Final Submission Checklist

## Required Proof

- Public GitHub repository exists
- README explains the project clearly
- Smoke test passes with WAR_ROOM_SMOKE_OK
- Export command generates judge packet
- Export command generates dashboard
- Copilot Build Log documents AI assisted development
- Microsoft IQ alignment is stated honestly
- Demo uses synthetic data only
- No credentials, tokens, or private data are included

## Demo Assets

- Dashboard screenshot captured
- Judge packet reviewed
- Demo video recorded
- Portal description drafted
- Project tagline finalized
- Submission safety notes reviewed

## Final Commands

```bash
PYTHONPATH="$PWD/src" python3 -m hackathon_war_room export
PYTHONPATH="$PWD/src" python3 tests/test_demo_workflow.py
```

## Freeze Rule

After the export command, smoke test, README, demo video, and submission assets are ready, stop adding features. Only polish wording, verify safety, and submit.

