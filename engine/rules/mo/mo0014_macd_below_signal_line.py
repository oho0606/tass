"""MO0014 — MACD Below Signal Line. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MO0014MACDBelowSignalLineRule(SpecRule):
    rule_id = "MO0014"
    rule_name = "MACD Below Signal Line"


def evaluate_mo0014(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MO0014."""
    return run_spec_rule(MO0014MACDBelowSignalLineRule, df)
