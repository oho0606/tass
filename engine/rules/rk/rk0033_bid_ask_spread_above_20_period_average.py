"""RK0033 — Bid-Ask Spread Above 20-Period Average. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class RK0033BidAskSpreadAbove20PeriodAverageRule(SpecRule):
    rule_id = "RK0033"
    rule_name = "Bid-Ask Spread Above 20-Period Average"


def evaluate_rk0033(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for RK0033."""
    return run_spec_rule(RK0033BidAskSpreadAbove20PeriodAverageRule, df)
