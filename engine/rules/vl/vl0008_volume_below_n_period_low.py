"""VL0008 — Volume Below N-Period Low. TASS-017: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.vl._absolute import AbsoluteVolumeRule, run_absolute_rule


class VL0008VolumeBelowNPeriodLowRule(AbsoluteVolumeRule):
    rule_id = "VL0008"
    rule_name = "Volume Below N-Period Low"
    mode = "below_low"


def evaluate_vl0008(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for VL0008."""
    return run_absolute_rule(VL0008VolumeBelowNPeriodLowRule, df)
