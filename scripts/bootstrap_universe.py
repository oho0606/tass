#!/usr/bin/env python3
"""Bootstrap KRX universe CSVs — PyKRX live fetch with static MVP fallback."""

from __future__ import annotations

import argparse
import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

MVP_SOURCE = ROOT / "config" / "universe_krx_mvp.csv"
DEFAULT_OUTPUTS = {
    "krx": ROOT / "config" / "universe_krx_backtest.csv",
    "sample": ROOT / "config" / "universe_sample.csv",
    "kospi": ROOT / "config" / "universe_kospi_backtest.csv",
    "kosdaq": ROOT / "config" / "universe_kosdaq_backtest.csv",
}


def _split_markets(source: Path, kospi_out: Path, kosdaq_out: Path) -> tuple[int, int]:
    import pandas as pd

    df = pd.read_csv(source, dtype=str)
    df.columns = [c.strip().lower() for c in df.columns]
    symbol_col = "symbol" if "symbol" in df.columns else "code"
    market_col = "market"
    name_col = "name"
    df[symbol_col] = df[symbol_col].str.strip().str.zfill(6)
    df[market_col] = df[market_col].str.strip().str.upper()

    kospi = df[df[market_col].isin({"KS", "KOSPI"})].copy()
    kosdaq = df[df[market_col].isin({"KQ", "KOSDAQ"})].copy()

    for out_df, path in ((kospi, kospi_out), (kosdaq, kosdaq_out)):
        out_df.rename(columns={symbol_col: "symbol"})[
            ["symbol", name_col, market_col]
        ].to_csv(path, index=False)

    return len(kospi), len(kosdaq)


def _try_pykrx(output: Path) -> int:
    from engine.data.universe import generate_universe_csv, load_universe

    generate_universe_csv(output, markets=("KOSPI", "KOSDAQ"))
    return len(load_universe(output))


def _fallback_static(output: Path) -> int:
    if not MVP_SOURCE.exists():
        raise FileNotFoundError(f"Static fallback missing: {MVP_SOURCE}")
    shutil.copy2(MVP_SOURCE, output)
    from engine.data.universe import load_universe

    return len(load_universe(output))


def main() -> int:
    parser = argparse.ArgumentParser(description="Bootstrap universe CSV files")
    parser.add_argument("--force-static", action="store_true", help="Skip PyKRX, use universe_krx_mvp.csv")
    parser.add_argument("--sample-size", type=int, default=20, help="Rows for universe_sample.csv")
    parser.add_argument(
        "--require-live",
        action="store_true",
        help="Exit non-zero when live PyKRX universe bootstrap fails",
    )
    args = parser.parse_args()

    krx_out = DEFAULT_OUTPUTS["krx"]
    count = 0
    source = "static"

    pykrx_error: str | None = None
    if not args.force_static:
        try:
            count = _try_pykrx(krx_out)
            source = "pykrx"
        except Exception as exc:
            pykrx_error = str(exc)
            print(f"PyKRX failed ({exc}); using static MVP universe")

    if count == 0:
        count = _fallback_static(krx_out)
        source = "static"

    import pandas as pd

    df = pd.read_csv(krx_out, dtype=str)
    df.columns = [c.strip().lower() for c in df.columns]
    sym = "symbol" if "symbol" in df.columns else "code"
    sample = df.head(args.sample_size)
    sample.rename(columns={sym: "symbol"}).to_csv(DEFAULT_OUTPUTS["sample"], index=False)

    kospi_n, kosdaq_n = _split_markets(krx_out, DEFAULT_OUTPUTS["kospi"], DEFAULT_OUTPUTS["kosdaq"])

    summary = {
        "source": source,
        "live_bootstrap_ok": source == "pykrx",
        "pykrx_error": pykrx_error,
        "krx_count": count,
        "kospi_count": kospi_n,
        "kosdaq_count": kosdaq_n,
        "sample_count": len(sample),
        "outputs": {k: str(v) for k, v in DEFAULT_OUTPUTS.items()},
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    if args.require_live and source != "pykrx":
        print("Live universe bootstrap required but unavailable. Check network/KRX credentials.")
        return 2
    return 0 if count > 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
