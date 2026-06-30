"""PA0005 — Current Low Below Prior Low. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PA0005CurrentLowBelowPriorLowRule(SpecRule):
    rule_id = "PA0005"
    rule_name = "Current Low Below Prior Low"


def evaluate_pa0005(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PA0005."""
    return run_spec_rule(PA0005CurrentLowBelowPriorLowRule, df)
