"""MR0045 — Bollinger Band Width Below Average. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MR0045BollingerBandWidthBelowAverageRule(SpecRule):
    rule_id = "MR0045"
    rule_name = "Bollinger Band Width Below Average"


def evaluate_mr0045(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MR0045."""
    return run_spec_rule(MR0045BollingerBandWidthBelowAverageRule, df)
