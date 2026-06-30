"""VL0001 — Volume Above N-Period Average. TASS-017: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.vl._absolute import AbsoluteVolumeRule, run_absolute_rule


class VL0001VolumeAboveNPeriodAverageRule(AbsoluteVolumeRule):
    rule_id = "VL0001"
    rule_name = "Volume Above N-Period Average"
    mode = "above_avg"


def evaluate_vl0001(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for VL0001."""
    return run_absolute_rule(VL0001VolumeAboveNPeriodAverageRule, df)
