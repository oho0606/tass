"""MO0028 — Stochastic %K Cross Below %D. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MO0028StochasticKCrossBelowDRule(SpecRule):
    rule_id = "MO0028"
    rule_name = "Stochastic %K Cross Below %D"


def evaluate_mo0028(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MO0028."""
    return run_spec_rule(MO0028StochasticKCrossBelowDRule, df)
