"""VL0019 — Relative Volume At N-Period Average. TASS-017: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.vl._relative import RelativeVolumeRule, run_relative_rule


class VL0019RelativeVolumeAtNPeriodAverageRule(RelativeVolumeRule):
    rule_id = "VL0019"
    rule_name = "Relative Volume At N-Period Average"
    mode = "at_avg"


def evaluate_vl0019(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for VL0019."""
    return run_relative_rule(VL0019RelativeVolumeAtNPeriodAverageRule, df)
