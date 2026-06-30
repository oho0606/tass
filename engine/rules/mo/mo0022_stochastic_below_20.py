"""MO0022 — Stochastic Below 20. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MO0022StochasticBelow20Rule(SpecRule):
    rule_id = "MO0022"
    rule_name = "Stochastic Below 20"


def evaluate_mo0022(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MO0022."""
    return run_spec_rule(MO0022StochasticBelow20Rule, df)
