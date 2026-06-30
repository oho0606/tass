"""Backtest summary loader for API."""

from __future__ import annotations

import json
from pathlib import Path

from api.schemas.backtest import BacktestRuleSummary, BacktestSummaryResponse


def load_backtest_summary(reports_dir: Path | None = None) -> BacktestSummaryResponse:
    """Load latest backtest JSON report and shape for frontend table."""
    target = reports_dir or Path("backtest/reports")
    if not target.exists():
        return BacktestSummaryResponse(
            available=False,
            message="No backtest reports found. Run: tass backtest",
        )

    files = sorted(target.glob("backtest_*.json"), reverse=True)
    if not files:
        return BacktestSummaryResponse(
            available=False,
            message="No backtest reports found. Run: tass backtest",
        )

    try:
        payload = json.loads(files[0].read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError) as exc:
        return BacktestSummaryResponse(available=False, message=str(exc))

    rule_results = payload.get("rule_results") or []
    summaries: list[BacktestRuleSummary] = []
    adopt = reject = 0
    for item in rule_results:
        verdict = str(item.get("verdict", ""))
        if verdict == "ADOPT":
            adopt += 1
        elif verdict == "REJECT":
            reject += 1
        metrics = item.get("metrics") or {}
        summaries.append(
            BacktestRuleSummary(
                rule_id=str(item.get("rule_id", "")),
                symbol=str(item.get("symbol", "")),
                verdict=verdict,
                total_return_pct=float(metrics.get("total_return_pct", 0)),
                win_rate=float(metrics.get("win_rate", 0)),
                max_drawdown_pct=float(metrics.get("max_drawdown_pct", 0)),
                sharpe_ratio=float(metrics.get("sharpe_ratio", 0)),
                trade_count=int(item.get("trade_count", metrics.get("trade_count", 0))),
                sample_days=int(metrics.get("sample_days", 0)),
            )
        )

    return BacktestSummaryResponse(
        run_date=str(payload.get("run_date", "")),
        config_version=str(payload.get("config_version", "")),
        data_source=str(payload.get("data_source", "")),
        rule_count=len(summaries),
        adopt_count=adopt,
        reject_count=reject,
        rules=summaries,
        available=True,
    )
