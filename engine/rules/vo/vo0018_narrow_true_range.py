"""VO0018 — Narrow True Range. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class VO0018NarrowTrueRangeRule(SpecRule):
    rule_id = "VO0018"
    rule_name = "Narrow True Range"


def evaluate_vo0018(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for VO0018."""
    return run_spec_rule(VO0018NarrowTrueRangeRule, df)
