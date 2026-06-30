"""BO0040 — Breakout Bar Bollinger Band Width At N-Period High. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class BO0040BreakoutBarBollingerBandWidthAtNPeriodHighRule(SpecRule):
    rule_id = "BO0040"
    rule_name = "Breakout Bar Bollinger Band Width At N-Period High"


def evaluate_bo0040(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for BO0040."""
    return run_spec_rule(BO0040BreakoutBarBollingerBandWidthAtNPeriodHighRule, df)
