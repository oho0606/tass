"""VL0028 — Consecutive Lower Volume. TASS-017: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.vl._trend import ConsecutiveVolumeRule, run_trend_rule


class VL0028ConsecutiveLowerVolumeRule(ConsecutiveVolumeRule):
    rule_id = "VL0028"
    rule_name = "Consecutive Lower Volume"
    mode = "lower"


def evaluate_vl0028(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for VL0028."""
    return run_trend_rule(VL0028ConsecutiveLowerVolumeRule, df)
