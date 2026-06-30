"""MO0030 — Stochastic Falling. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MO0030StochasticFallingRule(SpecRule):
    rule_id = "MO0030"
    rule_name = "Stochastic Falling"


def evaluate_mo0030(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MO0030."""
    return run_spec_rule(MO0030StochasticFallingRule, df)
