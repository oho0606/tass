"""MO0024 — Stochastic Below 50. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MO0024StochasticBelow50Rule(SpecRule):
    rule_id = "MO0024"
    rule_name = "Stochastic Below 50"


def evaluate_mo0024(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MO0024."""
    return run_spec_rule(MO0024StochasticBelow50Rule, df)
