# Hackathon War Room Demo Video Script

Target length: 60 to 90 seconds

## Opening Hook

Hackathons are not just about building. They are about shipping.

Most teams lose time because the final project is scattered: the README is unfinished, the demo is unclear, requirements are easy to miss, risks are unknown, and nobody knows when to stop adding features.

## Scene 1 - Mission Board

Show the Hackathon War Room dashboard.

Narration: Hackathon War Room is an AI assisted creative command center for builders. It turns hackathon chaos into a judge ready launch packet.

## Scene 2 - Launch Gate

Show the readiness score and verdict.

Narration: The Launch Gate gives the team a clear verdict: ready to submit, needs polish, at risk, or blocked. This demo currently shows Needs Polish because the system is honest about missing assets.

## Scene 3 - Judge Lens

Show scorecard, strengths, and risk console.

Narration: Judge Lens reframes the project through what judges need to see: rules fit, Microsoft IQ alignment, technical completeness, demo clarity, safety, and polish.

## Scene 4 - Export Packet

Run the export command.

Command: PYTHONPATH="$PWD/src" python3 -m hackathon_war_room export

Narration: One command generates the judge packet and dashboard from grounded project and rule context.

## Scene 5 - Smoke Proof

Run the smoke test.

Command: PYTHONPATH="$PWD/src" python3 tests/test_demo_workflow.py

Narration: The workflow is deterministic and locally testable, which makes it reliable for judging.

## Closing Line

The funny part is that this tool could help teams submit to the same hackathon it was built for.
