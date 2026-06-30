"""PB0038 — Pullback Volume Higher Than Advance Volume. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PB0038PullbackVolumeHigherThanAdvanceVolumeRule(SpecRule):
    rule_id = "PB0038"
    rule_name = "Pullback Volume Higher Than Advance Volume"


def evaluate_pb0038(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PB0038."""
    return run_spec_rule(PB0038PullbackVolumeHigherThanAdvanceVolumeRule, df)
