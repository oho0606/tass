"""MA0037 — Mid MA Cross Above Long MA. TASS-015: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.ma._crossover import CrossoverRule, run_crossover_rule


class MA0037MidMACrossAboveLongMARule(CrossoverRule):
    rule_id = "MA0037"
    rule_name = "Mid MA Cross Above Long MA"
    ma_type = "sma"
    fast_period = 20
    slow_period = 60
    direction = "golden"


def evaluate_ma0037(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MA0037."""
    return run_crossover_rule(MA0037MidMACrossAboveLongMARule, df)
