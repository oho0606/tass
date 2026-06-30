"""MA0036 — Short MA Cross Below Mid MA. TASS-015: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.ma._crossover import CrossoverRule, run_crossover_rule


class MA0036ShortMACrossBelowMidMARule(CrossoverRule):
    rule_id = "MA0036"
    rule_name = "Short MA Cross Below Mid MA"
    ma_type = "sma"
    fast_period = 5
    slow_period = 20
    direction = "death"


def evaluate_ma0036(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MA0036."""
    return run_crossover_rule(MA0036ShortMACrossBelowMidMARule, df)
