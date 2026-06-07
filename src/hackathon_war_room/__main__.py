from __future__ import annotations

import sys
from pathlib import Path


def run_demo() -> int:
    root = Path(__file__).resolve().parents[2]
    output_dir = root / "demo" / "output"
    output_dir.mkdir(parents=True, exist_ok=True)
    print("Hackathon War Room")
    print("Mission status: skeleton online")
    print(f"Output bay: {output_dir}")
    print("WAR_ROOM_DEMO_READY")
    return 0


def main(argv: list[str] | None = None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    command = args[0] if args else "demo"
    if command == "demo":
        return run_demo()
    if command in {"help", "--help", "-h"}:
        print("Usage: PYTHONPATH=\"$PWD/src\" python3 -m hackathon_war_room demo")
        return 0
    print(f"Unknown command: {command}")
    print("Usage: PYTHONPATH=\"$PWD/src\" python3 -m hackathon_war_room demo")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
