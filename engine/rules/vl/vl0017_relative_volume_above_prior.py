"""VL0017 — Relative Volume Above Prior. TASS-017: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.vl._relative import RelativeVolumeRule, run_relative_rule


class VL0017RelativeVolumeAbovePriorRule(RelativeVolumeRule):
    rule_id = "VL0017"
    rule_name = "Relative Volume Above Prior"
    mode = "above_prior"


def evaluate_vl0017(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for VL0017."""
    return run_relative_rule(VL0017RelativeVolumeAbovePriorRule, df)
