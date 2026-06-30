"""MA0039 — Multiple Golden Cross. TASS-015: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.ma._crossover import MultipleCrossoverRule, run_crossover_rule


class MA0039MultipleGoldenCrossRule(MultipleCrossoverRule):
    rule_id = "MA0039"
    rule_name = "Multiple Golden Cross"
    ma_type = "sma"
    pairs = ((5, 20), (20, 60), (60, 120))
    direction = "golden"
    min_crosses = 2


def evaluate_ma0039(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MA0039."""
    return run_crossover_rule(MA0039MultipleGoldenCrossRule, df)
