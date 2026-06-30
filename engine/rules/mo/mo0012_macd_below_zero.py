"""MO0012 — MACD Below Zero. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MO0012MACDBelowZeroRule(SpecRule):
    rule_id = "MO0012"
    rule_name = "MACD Below Zero"


def evaluate_mo0012(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MO0012."""
    return run_spec_rule(MO0012MACDBelowZeroRule, df)
