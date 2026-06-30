"""CF0026 — Stochastic Confirms Bearish Trend. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class CF0026StochasticConfirmsBearishTrendRule(SpecRule):
    rule_id = "CF0026"
    rule_name = "Stochastic Confirms Bearish Trend"


def evaluate_cf0026(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for CF0026."""
    return run_spec_rule(CF0026StochasticConfirmsBearishTrendRule, df)
