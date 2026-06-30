"""BO0047 — Close Above Trendline Resistance. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class BO0047CloseAboveTrendlineResistanceRule(SpecRule):
    rule_id = "BO0047"
    rule_name = "Close Above Trendline Resistance"


def evaluate_bo0047(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for BO0047."""
    return run_spec_rule(BO0047CloseAboveTrendlineResistanceRule, df)
