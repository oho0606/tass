"""VO0037 — Bollinger Band Width Above Average. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class VO0037BollingerBandWidthAboveAverageRule(SpecRule):
    rule_id = "VO0037"
    rule_name = "Bollinger Band Width Above Average"


def evaluate_vo0037(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for VO0037."""
    return run_spec_rule(VO0037BollingerBandWidthAboveAverageRule, df)
