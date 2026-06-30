"""MS0003 — Higher High Exceeds Prior. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MS0003HigherHighExceedsPriorRule(SpecRule):
    rule_id = "MS0003"
    rule_name = "Higher High Exceeds Prior"


def evaluate_ms0003(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MS0003."""
    return run_spec_rule(MS0003HigherHighExceedsPriorRule, df)
