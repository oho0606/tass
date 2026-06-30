"""PA0006 — Current Low Equal Prior Low. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PA0006CurrentLowEqualPriorLowRule(SpecRule):
    rule_id = "PA0006"
    rule_name = "Current Low Equal Prior Low"


def evaluate_pa0006(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PA0006."""
    return run_spec_rule(PA0006CurrentLowEqualPriorLowRule, df)
