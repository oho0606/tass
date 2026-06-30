"""VL0029 — Volume Flat. TASS-017: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.vl._trend import VolumeFlatRule, run_trend_rule


class VL0029VolumeFlatRule(VolumeFlatRule):
    rule_id = "VL0029"
    rule_name = "Volume Flat"


def evaluate_vl0029(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for VL0029."""
    return run_trend_rule(VL0029VolumeFlatRule, df)
