"""EX0017 — Exit Close Below Upper Bollinger Band. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class EX0017ExitCloseBelowUpperBollingerBandRule(SpecRule):
    rule_id = "EX0017"
    rule_name = "Exit Close Below Upper Bollinger Band"


def evaluate_ex0017(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for EX0017."""
    return run_spec_rule(EX0017ExitCloseBelowUpperBollingerBandRule, df)
