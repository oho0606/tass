#!/usr/bin/env python3
"""Daily pipeline: cache update → picks generation → optional webhook notify (Phase 6)."""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path

from config.app_settings import get_settings
from engine.application import RecommendationService, format_daily_picks_summary
from engine.application.market_data_loader import build_market_cache
from engine.application.settings import load_pipeline_settings
from engine.core.logging import setup_logging


def _post_webhook(url: str, payload: dict) -> None:
    body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
    request = urllib.request.Request(
        url,
        data=body,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        if response.status >= 400:
            raise RuntimeError(f"Webhook returned HTTP {response.status}")


def _build_notification(result, *, success: bool, error: str | None = None) -> dict:
    if not success:
        return {
            "text": f"TASS Daily Pipeline FAILED\nError: {error or 'unknown'}",
        }
    top5 = result.picks[:5]
    lines = [f"TASS Daily Picks — {result.date} ({len(result.picks)} picks)"]
    for pick in top5:
        lines.append(
            f"#{pick.rank} {pick.symbol} {pick.name} — {pick.recommendation} "
            f"(score {pick.total_score:.0f})"
        )
    return {"text": "\n".join(lines)}


def main() -> int:
    parser = argparse.ArgumentParser(description="TASS daily automation pipeline")
    parser.add_argument("--universe", type=Path, default=Path("config/universe_sample.csv"))
    parser.add_argument("--config", type=Path, default=Path("config/settings.yaml"))
    parser.add_argument("--output-dir", type=Path, default=None)
    parser.add_argument("--skip-cache-update", action="store_true")
    parser.add_argument("--webhook-url", default=os.environ.get("WEBHOOK_URL", ""))
    args = parser.parse_args()

    app_settings = get_settings()
    setup_logging(log_level=app_settings.log_level, log_dir=app_settings.log_dir)
    pipeline = load_pipeline_settings(args.config)

    webhook = args.webhook_url.strip()
    result = None
    try:
        if not args.skip_cache_update:
            cache_result = build_market_cache(
                args.universe,
                start_date="2020-01-01",
                cache_dir=pipeline.cache_dir,
                adapter=pipeline.adapter,
                min_bars=pipeline.min_bars,
                incremental=True,
            )
            if not cache_result.ohlcv_by_symbol:
                raise RuntimeError("Cache update produced no symbols")

        service = RecommendationService(settings_path=args.config)
        result = service.run_daily_picks(
            args.universe,
            use_cache=True,
            output_dir=args.output_dir,
        )
        summary = format_daily_picks_summary(result)
        try:
            print(summary)
        except UnicodeEncodeError:
            print(summary.encode("ascii", errors="replace").decode("ascii"))

        if webhook:
            _post_webhook(webhook, _build_notification(result, success=True))

        return 0 if result.picks else 1
    except Exception as exc:
        if webhook:
            try:
                _post_webhook(webhook, _build_notification(result, success=False, error=str(exc)))
            except (urllib.error.URLError, RuntimeError) as notify_err:
                print(f"Webhook notify failed: {notify_err}", file=sys.stderr)
        print(f"Pipeline failed: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
