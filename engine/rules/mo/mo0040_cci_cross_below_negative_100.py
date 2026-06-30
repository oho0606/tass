"""MO0040 — CCI Cross Below Negative 100. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MO0040CCICrossBelowNegative100Rule(SpecRule):
    rule_id = "MO0040"
    rule_name = "CCI Cross Below Negative 100"


def evaluate_mo0040(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MO0040."""
    return run_spec_rule(MO0040CCICrossBelowNegative100Rule, df)
