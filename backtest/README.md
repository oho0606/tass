# backtest

Backtest specifications, experiment definitions, and test outputs.

## Engine

Implementation: `engine/backtest/` (Backtest Engine v1.0 — Frozen)

Spec: `docs/TASS-031_Backtest_Engine_v1.0.md`

Config: `config/backtest_v1.yaml`

## Reports

Output directory: `backtest/reports/`

- `backtest_YYYY-MM-DD.json` — full run summary
- `{RULE_ID}_YYYY-MM-DD.md` — per-rule Markdown report

## CLI

```bash
# Synthetic (offline)
python main.py backtest --synthetic

# Real KRX data (cache first, then backtest)
python scripts/cache_market_data.py --universe config/universe_krx_backtest.csv
python scripts/run_backtest.py --universe config/universe_krx_backtest.csv

# Or via main entry
python main.py backtest --universe config/universe_krx_backtest.csv --no-fetch
python scripts/run_backtest.py --rules TR0001
```

## Regression

Rule 변경 시 `tests/regression/` 가 baseline과 비교한다.

Every Rule and scoring change must be validated with backtest results before adoption.
