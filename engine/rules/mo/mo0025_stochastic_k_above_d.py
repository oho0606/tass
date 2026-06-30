"""MO0025 — Stochastic %K Above %D. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MO0025StochasticKAboveDRule(SpecRule):
    rule_id = "MO0025"
    rule_name = "Stochastic %K Above %D"


def evaluate_mo0025(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MO0025."""
    return run_spec_rule(MO0025StochasticKAboveDRule, df)
