"""VL0030 — Volume Turning. TASS-017: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.vl._trend import VolumeTurningRule, run_trend_rule


class VL0030VolumeTurningRule(VolumeTurningRule):
    rule_id = "VL0030"
    rule_name = "Volume Turning"


def evaluate_vl0030(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for VL0030."""
    return run_trend_rule(VL0030VolumeTurningRule, df)
