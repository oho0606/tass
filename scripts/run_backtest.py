#!/usr/bin/env python3

"""TASS Backtest CLI — validate Rules against historical OHLCV."""



from __future__ import annotations



import argparse

import json

from pathlib import Path



from config.app_settings import get_settings

from engine.application import BacktestService

from engine.core.logging import setup_logging

from tests.fixtures.ohlcv import make_downtrend_ohlcv, make_uptrend_ohlcv





def _build_synthetic_frames() -> dict[str, object]:

    """Build default synthetic OHLCV frames for offline backtest."""

    return {

        "SYN_UP": make_uptrend_ohlcv(n=200),

        "SYN_DOWN": make_downtrend_ohlcv(n=200),

    }





def main() -> int:

    """Run rule backtest from CLI via Application Service.



    Returns:

        Process exit code (0 = success).

    """

    parser = argparse.ArgumentParser(description="TASS Rule Backtest")

    parser.add_argument(

        "--config",

        type=Path,

        default=Path("config/backtest_v1.yaml"),

        help="Backtest config YAML path",

    )

    parser.add_argument(

        "--universe",

        type=Path,

        default=None,

        help="KOSPI/KOSDAQ universe CSV (uses cached OHLCV when available)",

    )

    parser.add_argument(

        "--rules",

        nargs="*",

        default=None,

        help="Rule IDs to test (default: config default_rules)",

    )

    parser.add_argument(

        "--output-dir",

        type=Path,

        default=None,

        help="Override report output directory",

    )

    parser.add_argument(

        "--lookback-days",

        type=int,

        default=None,

        help="History window for real-data backtest",

    )

    parser.add_argument(

        "--cache-dir",

        type=Path,

        default=None,

        help="OHLCV parquet cache directory",

    )

    parser.add_argument(

        "--no-cache",

        action="store_true",

        help="Do not read from local cache",

    )

    parser.add_argument(

        "--no-fetch",

        action="store_true",

        help="Do not fetch missing symbols from adapter (cache-only mode)",

    )

    parser.add_argument(

        "--synthetic",

        action="store_true",

        help="Force synthetic OHLCV backtest (offline demo)",

    )

    args = parser.parse_args()



    app_settings = get_settings()

    setup_logging(log_level=app_settings.log_level, log_dir=app_settings.log_dir)



    service = BacktestService(config_path=args.config)

    rule_ids = tuple(args.rules) if args.rules else None



    if args.synthetic or args.universe is None:

        service_result = service.run_rule_backtest(

            ohlcv_by_symbol=_build_synthetic_frames(),

            rule_ids=rule_ids,

            data_source="synthetic",

            output_dir=args.output_dir,

        )

    else:

        universe_path = args.universe

        if not universe_path.exists():

            default_universe = Path(service.config.data.default_universe)

            universe_path = default_universe if default_universe.exists() else universe_path



        service_result = service.run_universe_backtest(

            universe_path,

            rule_ids=rule_ids,

            use_cache=not args.no_cache,

            fetch_missing=not args.no_fetch,

            lookback_days=args.lookback_days,

            cache_dir=args.cache_dir,

            output_dir=args.output_dir,

        )



    summary = {

        "report": str(service_result.report_path),

        "markdown_reports": [str(path) for path in service_result.markdown_paths],

        "rules_tested": len({item.rule_id for item in service_result.run_result.rule_results}),

        "symbols_tested": len({item.symbol for item in service_result.run_result.rule_results}),

        "data_source": service_result.run_result.data_source,

        "verdicts": {item.rule_id: item.verdict for item in service_result.run_result.rule_results},

    }

    print(json.dumps(summary, ensure_ascii=False, indent=2))

    return 0





if __name__ == "__main__":

    raise SystemExit(main())

