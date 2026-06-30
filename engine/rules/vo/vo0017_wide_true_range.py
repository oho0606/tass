"""VO0017 — Wide True Range. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class VO0017WideTrueRangeRule(SpecRule):
    rule_id = "VO0017"
    rule_name = "Wide True Range"


def evaluate_vo0017(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for VO0017."""
    return run_spec_rule(VO0017WideTrueRangeRule, df)
