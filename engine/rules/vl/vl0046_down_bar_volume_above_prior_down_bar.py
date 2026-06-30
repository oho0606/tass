"""VL0046 — Down Bar Volume Above Prior Down Bar. TASS-017: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.vl._confirmation import PriorSameBarVolumeRule, run_confirmation_rule


class VL0046DownBarVolumeAbovePriorDownBarRule(PriorSameBarVolumeRule):
    rule_id = "VL0046"
    rule_name = "Down Bar Volume Above Prior Down Bar"
    bar_direction = "down"


def evaluate_vl0046(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for VL0046."""
    return run_confirmation_rule(VL0046DownBarVolumeAbovePriorDownBarRule, df)
