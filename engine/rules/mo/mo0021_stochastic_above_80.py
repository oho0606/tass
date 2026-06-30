"""MO0021 — Stochastic Above 80. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MO0021StochasticAbove80Rule(SpecRule):
    rule_id = "MO0021"
    rule_name = "Stochastic Above 80"


def evaluate_mo0021(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MO0021."""
    return run_spec_rule(MO0021StochasticAbove80Rule, df)
