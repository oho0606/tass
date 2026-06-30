"""VO0049 — Volatility At N-Period High. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class VO0049VolatilityAtNPeriodHighRule(SpecRule):
    rule_id = "VO0049"
    rule_name = "Volatility At N-Period High"


def evaluate_vo0049(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for VO0049."""
    return run_spec_rule(VO0049VolatilityAtNPeriodHighRule, df)
