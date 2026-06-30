"""VL0055 — OBV Slope Increasing. TASS-017: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.vl._quality import ObvSlopeTrendRule, run_quality_rule


class VL0055OBVSlopeIncreasingRule(ObvSlopeTrendRule):
    rule_id = "VL0055"
    rule_name = "OBV Slope Increasing"
    trend = "increasing"


def evaluate_vl0055(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for VL0055."""
    return run_quality_rule(VL0055OBVSlopeIncreasingRule, df)
