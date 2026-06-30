"""VL0010 — Volume At N-Period Low. TASS-017: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.vl._absolute import AbsoluteVolumeRule, run_absolute_rule


class VL0010VolumeAtNPeriodLowRule(AbsoluteVolumeRule):
    rule_id = "VL0010"
    rule_name = "Volume At N-Period Low"
    mode = "at_low"


def evaluate_vl0010(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for VL0010."""
    return run_absolute_rule(VL0010VolumeAtNPeriodLowRule, df)
