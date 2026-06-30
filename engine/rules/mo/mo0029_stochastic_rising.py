"""MO0029 — Stochastic Rising. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MO0029StochasticRisingRule(SpecRule):
    rule_id = "MO0029"
    rule_name = "Stochastic Rising"


def evaluate_mo0029(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MO0029."""
    return run_spec_rule(MO0029StochasticRisingRule, df)
