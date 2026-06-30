"""Backtest report writer (TASS-009 §15)."""

from __future__ import annotations

import json
from dataclasses import asdict
from datetime import datetime
from pathlib import Path

from engine.backtest.types import BacktestRunResult, RuleBacktestResult


def save_json_report(result: BacktestRunResult, output_dir: Path) -> Path:
    """Persist backtest run result as JSON.

    Args:
        result: Aggregated backtest output.
        output_dir: Directory for report files.

    Returns:
        Path to the written JSON file.
    """
    output_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d")
    path = output_dir / f"backtest_{timestamp}.json"
    payload = _serialize_run_result(result)
    with path.open("w", encoding="utf-8") as handle:
        json.dump(payload, handle, ensure_ascii=False, indent=2)
    return path


def save_rule_markdown_report(
    rule_result: RuleBacktestResult,
    output_dir: Path,
) -> Path:
    """Persist single-rule backtest report as Markdown.

    Args:
        rule_result: Rule backtest output.
        output_dir: Directory for report files.

    Returns:
        Path to the written Markdown file.
    """
    output_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d")
    path = output_dir / f"{rule_result.rule_id}_{timestamp}.md"
    content = _render_rule_markdown(rule_result)
    path.write_text(content, encoding="utf-8")
    return path


def _serialize_run_result(result: BacktestRunResult) -> dict[str, object]:
    """Convert run result to JSON-serializable dict."""
    return {
        "config_version": result.config_version,
        "run_date": result.run_date,
        "data_source": result.data_source,
        "reasons": result.reasons,
        "rule_results": [_serialize_rule_result(item) for item in result.rule_results],
    }


def _serialize_rule_result(result: RuleBacktestResult) -> dict[str, object]:
    """Convert rule result to JSON-serializable dict."""
    payload = {
        "rule_id": result.rule_id,
        "symbol": result.symbol,
        "verdict": result.verdict,
        "reasons": result.reasons,
        "version": result.version,
        "metrics": asdict(result.metrics),
        "trade_count": len(result.trades),
    }
    if result.split_metrics is not None:
        payload["split_metrics"] = {
            "in_sample": asdict(result.split_metrics.in_sample),
            "out_of_sample": asdict(result.split_metrics.out_of_sample),
        }
    return payload


def _render_rule_markdown(result: RuleBacktestResult) -> str:
    """Render Markdown report for one rule backtest."""
    metrics = result.metrics
    lines = [
        f"# Backtest Report: {result.rule_id}",
        "",
        f"**Symbol:** {result.symbol}",
        f"**Verdict:** {result.verdict}",
        f"**Version:** {result.version}",
        "",
        "## Summary",
        "",
        "| Metric | Value |",
        "|--------|-------|",
        f"| Total Return | {metrics.total_return_pct:.2f}% |",
        f"| CAGR | {metrics.cagr_pct:.2f}% |",
        f"| Win Rate | {metrics.win_rate:.2%} |",
        f"| Avg Win | {metrics.avg_win_pct:.2f}% |",
        f"| Avg Loss | {metrics.avg_loss_pct:.2f}% |",
        f"| R:R | {metrics.reward_risk_ratio:.2f} |",
        f"| Profit Factor | {metrics.profit_factor:.2f} |",
        f"| MDD | {metrics.max_drawdown_pct:.2f}% |",
        f"| Sharpe | {metrics.sharpe_ratio:.2f} |",
        f"| Sortino | {metrics.sortino_ratio:.2f} |",
        f"| Trades | {metrics.trade_count} |",
        "",
        "## Reasons",
        "",
    ]
    lines.extend(f"- {reason}" for reason in result.reasons)
    lines.append("")
    return "\n".join(lines)
