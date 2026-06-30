"""MA0031 — SMA Golden Cross. TASS-015: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.ma._crossover import CrossoverRule, run_crossover_rule


class MA0031SMAGoldenCrossRule(CrossoverRule):
    rule_id = "MA0031"
    rule_name = "SMA Golden Cross"
    ma_type = "sma"
    fast_period = 20
    slow_period = 60
    direction = "golden"


def evaluate_ma0031(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MA0031."""
    return run_crossover_rule(MA0031SMAGoldenCrossRule, df)
