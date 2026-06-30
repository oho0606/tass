"""VL0002 — Volume Below N-Period Average. TASS-017: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.vl._absolute import AbsoluteVolumeRule, run_absolute_rule


class VL0002VolumeBelowNPeriodAverageRule(AbsoluteVolumeRule):
    rule_id = "VL0002"
    rule_name = "Volume Below N-Period Average"
    mode = "below_avg"


def evaluate_vl0002(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for VL0002."""
    return run_absolute_rule(VL0002VolumeBelowNPeriodAverageRule, df)
