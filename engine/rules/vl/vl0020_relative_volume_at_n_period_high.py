"""VL0020 — Relative Volume At N-Period High. TASS-017: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.vl._relative import RelativeVolumeRule, run_relative_rule


class VL0020RelativeVolumeAtNPeriodHighRule(RelativeVolumeRule):
    rule_id = "VL0020"
    rule_name = "Relative Volume At N-Period High"
    mode = "at_high"


def evaluate_vl0020(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for VL0020."""
    return run_relative_rule(VL0020RelativeVolumeAtNPeriodHighRule, df)
