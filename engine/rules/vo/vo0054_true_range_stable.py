"""VO0054 — True Range Stable. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class VO0054TrueRangeStableRule(SpecRule):
    rule_id = "VO0054"
    rule_name = "True Range Stable"


def evaluate_vo0054(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for VO0054."""
    return run_spec_rule(VO0054TrueRangeStableRule, df)
