"""VO0012 — True Range Below Prior True Range. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class VO0012TrueRangeBelowPriorTrueRangeRule(SpecRule):
    rule_id = "VO0012"
    rule_name = "True Range Below Prior True Range"


def evaluate_vo0012(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for VO0012."""
    return run_spec_rule(VO0012TrueRangeBelowPriorTrueRangeRule, df)
