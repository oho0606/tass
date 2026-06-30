"""MT0037 — Daily 4H Breakout Above Range. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MT0037Daily4HBreakoutAboveRangeRule(SpecRule):
    rule_id = "MT0037"
    rule_name = "Daily 4H Breakout Above Range"


def evaluate_mt0037(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MT0037."""
    return run_spec_rule(MT0037Daily4HBreakoutAboveRangeRule, df)
