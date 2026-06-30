#!/usr/bin/env python3
"""Generate TASS universe CSV from PyKRX listings."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from config.app_settings import get_settings
from engine.core.logging import setup_logging
from engine.data.universe import generate_universe_csv, load_universe


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate KRX universe CSV via PyKRX")
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("config/universe_krx_generated.csv"),
        help="Output CSV path",
    )
    parser.add_argument(
        "--date",
        default="",
        help="As-of date (YYYY-MM-DD). Empty = latest trading day.",
    )
    parser.add_argument(
        "--markets",
        nargs="+",
        default=["KOSPI", "KOSDAQ"],
        help="Markets to include",
    )
    args = parser.parse_args()

    app_settings = get_settings()
    setup_logging(log_level=app_settings.log_level, log_dir=app_settings.log_dir)

    output = generate_universe_csv(
        args.output,
        markets=tuple(args.markets),
        target_date=args.date,
    )
    entries = load_universe(output)
    summary = {
        "output": str(output),
        "markets": args.markets,
        "date": args.date or "latest",
        "count": len(entries),
        "sample": [
            {"symbol": e.symbol, "name": e.name, "market": e.market}
            for e in entries[:5]
        ],
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0 if entries else 1


if __name__ == "__main__":
    raise SystemExit(main())
