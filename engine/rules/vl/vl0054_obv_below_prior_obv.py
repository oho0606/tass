"""VL0054 — OBV Below Prior OBV. TASS-017: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.vl._quality import ObvCompareRule, run_quality_rule


class VL0054OBVBelowPriorOBVRule(ObvCompareRule):
    rule_id = "VL0054"
    rule_name = "OBV Below Prior OBV"
    comparison = "below_prior"


def evaluate_vl0054(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for VL0054."""
    return run_quality_rule(VL0054OBVBelowPriorOBVRule, df)
