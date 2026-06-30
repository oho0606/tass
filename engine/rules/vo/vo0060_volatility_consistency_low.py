"""VO0060 — Volatility Consistency Low. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class VO0060VolatilityConsistencyLowRule(SpecRule):
    rule_id = "VO0060"
    rule_name = "Volatility Consistency Low"


def evaluate_vo0060(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for VO0060."""
    return run_spec_rule(VO0060VolatilityConsistencyLowRule, df)
