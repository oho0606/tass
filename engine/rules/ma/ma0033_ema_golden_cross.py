"""MA0033 — EMA Golden Cross. TASS-015: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.ma._crossover import CrossoverRule, run_crossover_rule


class MA0033EMAGoldenCrossRule(CrossoverRule):
    rule_id = "MA0033"
    rule_name = "EMA Golden Cross"
    ma_type = "ema"
    fast_period = 20
    slow_period = 60
    direction = "golden"


def evaluate_ma0033(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MA0033."""
    return run_crossover_rule(MA0033EMAGoldenCrossRule, df)
