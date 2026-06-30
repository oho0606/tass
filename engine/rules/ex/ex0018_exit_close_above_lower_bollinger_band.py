"""EX0018 — Exit Close Above Lower Bollinger Band. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class EX0018ExitCloseAboveLowerBollingerBandRule(SpecRule):
    rule_id = "EX0018"
    rule_name = "Exit Close Above Lower Bollinger Band"


def evaluate_ex0018(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for EX0018."""
    return run_spec_rule(EX0018ExitCloseAboveLowerBollingerBandRule, df)
