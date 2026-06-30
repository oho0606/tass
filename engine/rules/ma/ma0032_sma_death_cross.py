"""MA0032 — SMA Death Cross. TASS-015: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.ma._crossover import CrossoverRule, run_crossover_rule


class MA0032SMADeathCrossRule(CrossoverRule):
    rule_id = "MA0032"
    rule_name = "SMA Death Cross"
    ma_type = "sma"
    fast_period = 20
    slow_period = 60
    direction = "death"


def evaluate_ma0032(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MA0032."""
    return run_crossover_rule(MA0032SMADeathCrossRule, df)
