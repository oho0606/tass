"""VO0005 — ATR Above N-Period Average. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class VO0005ATRAboveNPeriodAverageRule(SpecRule):
    rule_id = "VO0005"
    rule_name = "ATR Above N-Period Average"


def evaluate_vo0005(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for VO0005."""
    return run_spec_rule(VO0005ATRAboveNPeriodAverageRule, df)
