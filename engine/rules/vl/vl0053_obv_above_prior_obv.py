"""VL0053 — OBV Above Prior OBV. TASS-017: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.vl._quality import ObvCompareRule, run_quality_rule


class VL0053OBVAbovePriorOBVRule(ObvCompareRule):
    rule_id = "VL0053"
    rule_name = "OBV Above Prior OBV"
    comparison = "above_prior"


def evaluate_vl0053(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for VL0053."""
    return run_quality_rule(VL0053OBVAbovePriorOBVRule, df)
