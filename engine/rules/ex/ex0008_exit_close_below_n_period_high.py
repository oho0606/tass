"""EX0008 — Exit Close Below N-Period High. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class EX0008ExitCloseBelowNPeriodHighRule(SpecRule):
    rule_id = "EX0008"
    rule_name = "Exit Close Below N-Period High"


def evaluate_ex0008(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for EX0008."""
    return run_spec_rule(EX0008ExitCloseBelowNPeriodHighRule, df)
