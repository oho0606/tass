"""PA0007 — Current High Above N-Period High. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PA0007CurrentHighAboveNPeriodHighRule(SpecRule):
    rule_id = "PA0007"
    rule_name = "Current High Above N-Period High"


def evaluate_pa0007(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PA0007."""
    return run_spec_rule(PA0007CurrentHighAboveNPeriodHighRule, df)
