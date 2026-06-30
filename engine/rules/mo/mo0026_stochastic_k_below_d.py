"""MO0026 — Stochastic %K Below %D. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MO0026StochasticKBelowDRule(SpecRule):
    rule_id = "MO0026"
    rule_name = "Stochastic %K Below %D"


def evaluate_mo0026(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MO0026."""
    return run_spec_rule(MO0026StochasticKBelowDRule, df)
