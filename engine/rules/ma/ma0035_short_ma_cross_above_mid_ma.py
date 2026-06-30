"""MA0035 — Short MA Cross Above Mid MA. TASS-015: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.ma._crossover import CrossoverRule, run_crossover_rule


class MA0035ShortMACrossAboveMidMARule(CrossoverRule):
    rule_id = "MA0035"
    rule_name = "Short MA Cross Above Mid MA"
    ma_type = "sma"
    fast_period = 5
    slow_period = 20
    direction = "golden"


def evaluate_ma0035(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MA0035."""
    return run_crossover_rule(MA0035ShortMACrossAboveMidMARule, df)
