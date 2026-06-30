"""PA0052 — Weak Close. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PA0052WeakCloseRule(SpecRule):
    rule_id = "PA0052"
    rule_name = "Weak Close"


def evaluate_pa0052(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PA0052."""
    return run_spec_rule(PA0052WeakCloseRule, df)
