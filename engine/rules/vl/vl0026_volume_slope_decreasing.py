"""VL0026 — Volume Slope Decreasing. TASS-017: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.vl._trend import VolumeSlopeTrendRule, run_trend_rule


class VL0026VolumeSlopeDecreasingRule(VolumeSlopeTrendRule):
    rule_id = "VL0026"
    rule_name = "Volume Slope Decreasing"
    trend = "decreasing"


def evaluate_vl0026(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for VL0026."""
    return run_trend_rule(VL0026VolumeSlopeDecreasingRule, df)
