"""VL0025 — Volume Slope Increasing. TASS-017: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.vl._trend import VolumeSlopeTrendRule, run_trend_rule


class VL0025VolumeSlopeIncreasingRule(VolumeSlopeTrendRule):
    rule_id = "VL0025"
    rule_name = "Volume Slope Increasing"
    trend = "increasing"


def evaluate_vl0025(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for VL0025."""
    return run_trend_rule(VL0025VolumeSlopeIncreasingRule, df)
