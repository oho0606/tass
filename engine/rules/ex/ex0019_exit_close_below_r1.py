"""EX0019 — Exit Close Below R1. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class EX0019ExitCloseBelowR1Rule(SpecRule):
    rule_id = "EX0019"
    rule_name = "Exit Close Below R1"


def evaluate_ex0019(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for EX0019."""
    return run_spec_rule(EX0019ExitCloseBelowR1Rule, df)
