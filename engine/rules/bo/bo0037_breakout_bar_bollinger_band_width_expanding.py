"""BO0037 — Breakout Bar Bollinger Band Width Expanding. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class BO0037BreakoutBarBollingerBandWidthExpandingRule(SpecRule):
    rule_id = "BO0037"
    rule_name = "Breakout Bar Bollinger Band Width Expanding"


def evaluate_bo0037(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for BO0037."""
    return run_spec_rule(BO0037BreakoutBarBollingerBandWidthExpandingRule, df)
