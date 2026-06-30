#!/usr/bin/env python3
"""TASS application entry point (TASS-030)."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


def _run_daily_picks(argv: list[str]) -> int:
    """Delegate to the daily picks CLI script.

    Args:
        argv: Arguments forwarded to ``scripts/run_daily_picks.py``.

    Returns:
        Process exit code.
    """
    script = Path(__file__).resolve().parent / "scripts" / "run_daily_picks.py"
    result = subprocess.run([sys.executable, str(script), *argv], check=False)
    return int(result.returncode)


def _run_backtest(argv: list[str]) -> int:
    """Delegate to the backtest CLI script.

    Args:
        argv: Arguments forwarded to ``scripts/run_backtest.py``.

    Returns:
        Process exit code.
    """
    script = Path(__file__).resolve().parent / "scripts" / "run_backtest.py"
    result = subprocess.run([sys.executable, str(script), *argv], check=False)
    return int(result.returncode)


def _run_api(argv: list[str]) -> int:
    """Start the FastAPI server (requires ``pip install -e '.[api]'``).

    Args:
        argv: Unused; reserved for future API options.

    Returns:
        Process exit code.
    """
    try:
        import uvicorn
    except ImportError:
        print("API dependencies missing. Install with: pip install -e '.[api]'")
        return 1
    uvicorn.run("api.app:app", host="0.0.0.0", port=8000, reload=False)
    return 0


def cli() -> int:
    """Main CLI dispatcher for TASS commands.

    Returns:
        Exit code (0 = success).

    Example:
        ``tass picks --universe config/universe_sample.csv``
    """
    parser = argparse.ArgumentParser(
        prog="tass",
        description="TASS — Technical Analysis Scoring System",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    picks_parser = sub.add_parser("picks", help="Generate Today's Top 20 picks")
    picks_parser.add_argument("--universe", type=Path, default=Path("config/universe_sample.csv"))
    picks_parser.add_argument("--config", type=Path, default=Path("config/settings.yaml"))
    picks_parser.add_argument("--output-dir", type=Path, default=None)
    picks_parser.add_argument("--no-cache", action="store_true")

    backtest_parser = sub.add_parser("backtest", help="Run Rule backtest (TASS-009)")
    backtest_parser.add_argument("--config", type=Path, default=Path("config/backtest_v1.yaml"))
    backtest_parser.add_argument("--universe", type=Path, default=None)
    backtest_parser.add_argument("--rules", nargs="*", default=None)
    backtest_parser.add_argument("--output-dir", type=Path, default=None)
    backtest_parser.add_argument("--lookback-days", type=int, default=None)
    backtest_parser.add_argument("--cache-dir", type=Path, default=None)
    backtest_parser.add_argument("--no-cache", action="store_true")
    backtest_parser.add_argument("--no-fetch", action="store_true")
    backtest_parser.add_argument("--synthetic", action="store_true")

    sub.add_parser("api", help="Start REST API server (last — planned)")

    args, remainder = parser.parse_known_args()

    from config.app_settings import get_settings
    from engine.core.logging import setup_logging

    settings = get_settings()
    setup_logging(log_level=settings.log_level, log_dir=settings.log_dir)

    if args.command == "picks":
        picks_argv: list[str] = []
        if args.universe:
            picks_argv.extend(["--universe", str(args.universe)])
        if args.config:
            picks_argv.extend(["--config", str(args.config)])
        if args.output_dir:
            picks_argv.extend(["--output-dir", str(args.output_dir)])
        if args.no_cache:
            picks_argv.append("--no-cache")
        picks_argv.extend(remainder)
        return _run_daily_picks(picks_argv)

    if args.command == "backtest":
        bt_argv: list[str] = []
        if args.config:
            bt_argv.extend(["--config", str(args.config)])
        if args.universe:
            bt_argv.extend(["--universe", str(args.universe)])
        if args.rules:
            bt_argv.extend(["--rules", *args.rules])
        if args.output_dir:
            bt_argv.extend(["--output-dir", str(args.output_dir)])
        if args.lookback_days is not None:
            bt_argv.extend(["--lookback-days", str(args.lookback_days)])
        if args.cache_dir:
            bt_argv.extend(["--cache-dir", str(args.cache_dir)])
        if args.no_cache:
            bt_argv.append("--no-cache")
        if args.no_fetch:
            bt_argv.append("--no-fetch")
        if args.synthetic:
            bt_argv.append("--synthetic")
        bt_argv.extend(remainder)
        return _run_backtest(bt_argv)

    if args.command == "api":
        return _run_api(remainder)

    parser.print_help()
    return 1


if __name__ == "__main__":
    raise SystemExit(cli())
