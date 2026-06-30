"""VO0006 — ATR Below N-Period Average. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class VO0006ATRBelowNPeriodAverageRule(SpecRule):
    rule_id = "VO0006"
    rule_name = "ATR Below N-Period Average"


def evaluate_vo0006(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for VO0006."""
    return run_spec_rule(VO0006ATRBelowNPeriodAverageRule, df)
