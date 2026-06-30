"""VL0011 — Relative Volume Above 1. TASS-017: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.vl._relative import RelativeVolumeRule, run_relative_rule


class VL0011RelativeVolumeAbove1Rule(RelativeVolumeRule):
    rule_id = "VL0011"
    rule_name = "Relative Volume Above 1"
    mode = "above_1"


def evaluate_vl0011(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for VL0011."""
    return run_relative_rule(VL0011RelativeVolumeAbove1Rule, df)
