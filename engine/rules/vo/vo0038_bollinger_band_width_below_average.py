"""VO0038 — Bollinger Band Width Below Average. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class VO0038BollingerBandWidthBelowAverageRule(SpecRule):
    rule_id = "VO0038"
    rule_name = "Bollinger Band Width Below Average"


def evaluate_vo0038(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for VO0038."""
    return run_spec_rule(VO0038BollingerBandWidthBelowAverageRule, df)
