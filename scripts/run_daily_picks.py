#!/usr/bin/env python3
"""TASS MVP: generate Today's Top 20 picks."""

from __future__ import annotations

import argparse
from pathlib import Path

from config.app_settings import get_settings
from engine.application import RecommendationService, format_daily_picks_summary
from engine.core.logging import setup_logging


def main() -> int:
    """Run daily picks via Application Service.

    Returns:
        Process exit code (0 = success).
    """
    parser = argparse.ArgumentParser(description="TASS Daily Top 20 Picks")
    parser.add_argument("--universe", type=Path, default=Path("config/universe_sample.csv"))
    parser.add_argument("--config", type=Path, default=Path("config/settings.yaml"))
    parser.add_argument("--output-dir", type=Path, default=None)
    parser.add_argument("--no-cache", action="store_true")
    args = parser.parse_args()

    settings = get_settings()
    setup_logging(log_level=settings.log_level, log_dir=settings.log_dir)

    service = RecommendationService(settings_path=args.config)
    result = service.run_daily_picks(
        args.universe,
        use_cache=not args.no_cache,
        output_dir=args.output_dir,
    )

    summary = format_daily_picks_summary(result)
    try:
        print(summary)
    except UnicodeEncodeError:
        print(summary.encode("ascii", errors="replace").decode("ascii"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
