"""MA0040 — Multiple Death Cross. TASS-015: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.ma._crossover import MultipleCrossoverRule, run_crossover_rule


class MA0040MultipleDeathCrossRule(MultipleCrossoverRule):
    rule_id = "MA0040"
    rule_name = "Multiple Death Cross"
    ma_type = "sma"
    pairs = ((5, 20), (20, 60), (60, 120))
    direction = "death"
    min_crosses = 2


def evaluate_ma0040(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MA0040."""
    return run_crossover_rule(MA0040MultipleDeathCrossRule, df)
