"""VL0003 — Volume Equal N-Period Average. TASS-017: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.vl._absolute import AbsoluteVolumeRule, run_absolute_rule


class VL0003VolumeEqualNPeriodAverageRule(AbsoluteVolumeRule):
    rule_id = "VL0003"
    rule_name = "Volume Equal N-Period Average"
    mode = "equal_avg"


def evaluate_vl0003(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for VL0003."""
    return run_absolute_rule(VL0003VolumeEqualNPeriodAverageRule, df)
