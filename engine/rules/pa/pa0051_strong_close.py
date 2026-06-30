"""PA0051 — Strong Close. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PA0051StrongCloseRule(SpecRule):
    rule_id = "PA0051"
    rule_name = "Strong Close"


def evaluate_pa0051(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PA0051."""
    return run_spec_rule(PA0051StrongCloseRule, df)
