"""EX0050 — Exit Bar RSI Above 50. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class EX0050ExitBarRSIAbove50Rule(SpecRule):
    rule_id = "EX0050"
    rule_name = "Exit Bar RSI Above 50"


def evaluate_ex0050(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for EX0050."""
    return run_spec_rule(EX0050ExitBarRSIAbove50Rule, df)
