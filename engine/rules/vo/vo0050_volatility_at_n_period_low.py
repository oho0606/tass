"""VO0050 — Volatility At N-Period Low. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class VO0050VolatilityAtNPeriodLowRule(SpecRule):
    rule_id = "VO0050"
    rule_name = "Volatility At N-Period Low"


def evaluate_vo0050(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for VO0050."""
    return run_spec_rule(VO0050VolatilityAtNPeriodLowRule, df)
