"""PA0048 — Equal Swing Lows. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PA0048EqualSwingLowsRule(SpecRule):
    rule_id = "PA0048"
    rule_name = "Equal Swing Lows"


def evaluate_pa0048(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PA0048."""
    return run_spec_rule(PA0048EqualSwingLowsRule, df)
