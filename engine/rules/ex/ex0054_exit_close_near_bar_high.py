"""EX0054 — Exit Close Near Bar High. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class EX0054ExitCloseNearBarHighRule(SpecRule):
    rule_id = "EX0054"
    rule_name = "Exit Close Near Bar High"


def evaluate_ex0054(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for EX0054."""
    return run_spec_rule(EX0054ExitCloseNearBarHighRule, df)
