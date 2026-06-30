"""PB0033 — Pullback Volume Lower Than Advance Volume. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PB0033PullbackVolumeLowerThanAdvanceVolumeRule(SpecRule):
    rule_id = "PB0033"
    rule_name = "Pullback Volume Lower Than Advance Volume"


def evaluate_pb0033(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PB0033."""
    return run_spec_rule(PB0033PullbackVolumeLowerThanAdvanceVolumeRule, df)
