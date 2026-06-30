"""VO0055 — ATR Within N-Period Range. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class VO0055ATRWithinNPeriodRangeRule(SpecRule):
    rule_id = "VO0055"
    rule_name = "ATR Within N-Period Range"


def evaluate_vo0055(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for VO0055."""
    return run_spec_rule(VO0055ATRWithinNPeriodRangeRule, df)
