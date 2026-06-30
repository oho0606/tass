"""VO0011 — True Range Above Prior True Range. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class VO0011TrueRangeAbovePriorTrueRangeRule(SpecRule):
    rule_id = "VO0011"
    rule_name = "True Range Above Prior True Range"


def evaluate_vo0011(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for VO0011."""
    return run_spec_rule(VO0011TrueRangeAbovePriorTrueRangeRule, df)
