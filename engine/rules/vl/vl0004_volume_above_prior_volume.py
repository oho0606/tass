"""VL0004 — Volume Above Prior Volume. TASS-017: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.vl._absolute import AbsoluteVolumeRule, run_absolute_rule


class VL0004VolumeAbovePriorVolumeRule(AbsoluteVolumeRule):
    rule_id = "VL0004"
    rule_name = "Volume Above Prior Volume"
    mode = "above_prior"


def evaluate_vl0004(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for VL0004."""
    return run_absolute_rule(VL0004VolumeAbovePriorVolumeRule, df)
