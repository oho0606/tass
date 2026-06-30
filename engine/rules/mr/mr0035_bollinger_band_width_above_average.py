"""MR0035 — Bollinger Band Width Above Average. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MR0035BollingerBandWidthAboveAverageRule(SpecRule):
    rule_id = "MR0035"
    rule_name = "Bollinger Band Width Above Average"


def evaluate_mr0035(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MR0035."""
    return run_spec_rule(MR0035BollingerBandWidthAboveAverageRule, df)
