"""VL0012 — Relative Volume Below 1. TASS-017: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.vl._relative import RelativeVolumeRule, run_relative_rule


class VL0012RelativeVolumeBelow1Rule(RelativeVolumeRule):
    rule_id = "VL0012"
    rule_name = "Relative Volume Below 1"
    mode = "below_1"


def evaluate_vl0012(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for VL0012."""
    return run_relative_rule(VL0012RelativeVolumeBelow1Rule, df)
