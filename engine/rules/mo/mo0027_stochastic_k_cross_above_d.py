"""MO0027 — Stochastic %K Cross Above %D. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MO0027StochasticKCrossAboveDRule(SpecRule):
    rule_id = "MO0027"
    rule_name = "Stochastic %K Cross Above %D"


def evaluate_mo0027(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MO0027."""
    return run_spec_rule(MO0027StochasticKCrossAboveDRule, df)
