"""VO0057 — Bollinger Band Width Within N-Period Range. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class VO0057BollingerBandWidthWithinNPeriodRangeRule(SpecRule):
    rule_id = "VO0057"
    rule_name = "Bollinger Band Width Within N-Period Range"


def evaluate_vo0057(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for VO0057."""
    return run_spec_rule(VO0057BollingerBandWidthWithinNPeriodRangeRule, df)
