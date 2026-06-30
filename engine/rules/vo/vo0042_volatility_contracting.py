"""VO0042 — Volatility Contracting. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class VO0042VolatilityContractingRule(SpecRule):
    rule_id = "VO0042"
    rule_name = "Volatility Contracting"


def evaluate_vo0042(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for VO0042."""
    return run_spec_rule(VO0042VolatilityContractingRule, df)
