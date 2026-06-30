"""VL0052 — OBV Falling. TASS-017: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.vl._quality import ObvDirectionRule, run_quality_rule


class VL0052OBVFallingRule(ObvDirectionRule):
    rule_id = "VL0052"
    rule_name = "OBV Falling"
    direction = "falling"


def evaluate_vl0052(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for VL0052."""
    return run_quality_rule(VL0052OBVFallingRule, df)
