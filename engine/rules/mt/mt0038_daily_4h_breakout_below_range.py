"""MT0038 — Daily 4H Breakout Below Range. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MT0038Daily4HBreakoutBelowRangeRule(SpecRule):
    rule_id = "MT0038"
    rule_name = "Daily 4H Breakout Below Range"


def evaluate_mt0038(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MT0038."""
    return run_spec_rule(MT0038Daily4HBreakoutBelowRangeRule, df)
