"""RK0034 — Bid-Ask Spread Below 20-Period Average. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class RK0034BidAskSpreadBelow20PeriodAverageRule(SpecRule):
    rule_id = "RK0034"
    rule_name = "Bid-Ask Spread Below 20-Period Average"


def evaluate_rk0034(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for RK0034."""
    return run_spec_rule(RK0034BidAskSpreadBelow20PeriodAverageRule, df)
