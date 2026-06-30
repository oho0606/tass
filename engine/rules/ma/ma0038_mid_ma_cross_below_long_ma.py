"""MA0038 — Mid MA Cross Below Long MA. TASS-015: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.ma._crossover import CrossoverRule, run_crossover_rule


class MA0038MidMACrossBelowLongMARule(CrossoverRule):
    rule_id = "MA0038"
    rule_name = "Mid MA Cross Below Long MA"
    ma_type = "sma"
    fast_period = 20
    slow_period = 60
    direction = "death"


def evaluate_ma0038(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MA0038."""
    return run_crossover_rule(MA0038MidMACrossBelowLongMARule, df)
