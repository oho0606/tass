"""EX0014 — Exit Close Above Horizontal Support. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class EX0014ExitCloseAboveHorizontalSupportRule(SpecRule):
    rule_id = "EX0014"
    rule_name = "Exit Close Above Horizontal Support"


def evaluate_ex0014(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for EX0014."""
    return run_spec_rule(EX0014ExitCloseAboveHorizontalSupportRule, df)
