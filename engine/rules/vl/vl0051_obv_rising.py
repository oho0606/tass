"""VL0051 — OBV Rising. TASS-017: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.vl._quality import ObvDirectionRule, run_quality_rule


class VL0051OBVRisingRule(ObvDirectionRule):
    rule_id = "VL0051"
    rule_name = "OBV Rising"
    direction = "rising"


def evaluate_vl0051(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for VL0051."""
    return run_quality_rule(VL0051OBVRisingRule, df)
