"""MO0023 — Stochastic Above 50. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MO0023StochasticAbove50Rule(SpecRule):
    rule_id = "MO0023"
    rule_name = "Stochastic Above 50"


def evaluate_mo0023(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MO0023."""
    return run_spec_rule(MO0023StochasticAbove50Rule, df)
