"""VL0056 — OBV Slope Decreasing. TASS-017: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.vl._quality import ObvSlopeTrendRule, run_quality_rule


class VL0056OBVSlopeDecreasingRule(ObvSlopeTrendRule):
    rule_id = "VL0056"
    rule_name = "OBV Slope Decreasing"
    trend = "decreasing"


def evaluate_vl0056(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for VL0056."""
    return run_quality_rule(VL0056OBVSlopeDecreasingRule, df)
