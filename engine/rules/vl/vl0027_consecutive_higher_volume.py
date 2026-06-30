"""VL0027 — Consecutive Higher Volume. TASS-017: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.vl._trend import ConsecutiveVolumeRule, run_trend_rule


class VL0027ConsecutiveHigherVolumeRule(ConsecutiveVolumeRule):
    rule_id = "VL0027"
    rule_name = "Consecutive Higher Volume"
    mode = "higher"


def evaluate_vl0027(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for VL0027."""
    return run_trend_rule(VL0027ConsecutiveHigherVolumeRule, df)
