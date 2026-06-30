"""PA0004 — Current Low Above Prior Low. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PA0004CurrentLowAbovePriorLowRule(SpecRule):
    rule_id = "PA0004"
    rule_name = "Current Low Above Prior Low"


def evaluate_pa0004(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PA0004."""
    return run_spec_rule(PA0004CurrentLowAbovePriorLowRule, df)
