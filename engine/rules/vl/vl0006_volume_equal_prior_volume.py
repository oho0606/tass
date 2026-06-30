"""VL0006 — Volume Equal Prior Volume. TASS-017: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.vl._absolute import AbsoluteVolumeRule, run_absolute_rule


class VL0006VolumeEqualPriorVolumeRule(AbsoluteVolumeRule):
    rule_id = "VL0006"
    rule_name = "Volume Equal Prior Volume"
    mode = "equal_prior"


def evaluate_vl0006(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for VL0006."""
    return run_absolute_rule(VL0006VolumeEqualPriorVolumeRule, df)
