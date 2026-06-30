"""EX0013 — Exit Close Below Horizontal Resistance. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class EX0013ExitCloseBelowHorizontalResistanceRule(SpecRule):
    rule_id = "EX0013"
    rule_name = "Exit Close Below Horizontal Resistance"


def evaluate_ex0013(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for EX0013."""
    return run_spec_rule(EX0013ExitCloseBelowHorizontalResistanceRule, df)
