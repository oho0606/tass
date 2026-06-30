"""MA0034 — EMA Death Cross. TASS-015: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.ma._crossover import CrossoverRule, run_crossover_rule


class MA0034EMADeathCrossRule(CrossoverRule):
    rule_id = "MA0034"
    rule_name = "EMA Death Cross"
    ma_type = "ema"
    fast_period = 20
    slow_period = 60
    direction = "death"


def evaluate_ma0034(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MA0034."""
    return run_crossover_rule(MA0034EMADeathCrossRule, df)
