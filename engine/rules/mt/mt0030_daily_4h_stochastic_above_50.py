"""MT0030 — Daily 4H Stochastic Above 50. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MT0030Daily4HStochasticAbove50Rule(SpecRule):
    rule_id = "MT0030"
    rule_name = "Daily 4H Stochastic Above 50"


def evaluate_mt0030(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MT0030."""
    return run_spec_rule(MT0030Daily4HStochasticAbove50Rule, df)
