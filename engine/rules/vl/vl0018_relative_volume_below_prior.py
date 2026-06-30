"""VL0018 — Relative Volume Below Prior. TASS-017: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.vl._relative import RelativeVolumeRule, run_relative_rule


class VL0018RelativeVolumeBelowPriorRule(RelativeVolumeRule):
    rule_id = "VL0018"
    rule_name = "Relative Volume Below Prior"
    mode = "below_prior"


def evaluate_vl0018(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for VL0018."""
    return run_relative_rule(VL0018RelativeVolumeBelowPriorRule, df)
