"""VO0008 — ATR At N-Period Low. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class VO0008ATRAtNPeriodLowRule(SpecRule):
    rule_id = "VO0008"
    rule_name = "ATR At N-Period Low"


def evaluate_vo0008(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for VO0008."""
    return run_spec_rule(VO0008ATRAtNPeriodLowRule, df)
