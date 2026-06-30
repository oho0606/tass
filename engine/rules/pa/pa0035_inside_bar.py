"""PA0035 — Inside Bar. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PA0035InsideBarRule(SpecRule):
    rule_id = "PA0035"
    rule_name = "Inside Bar"


def evaluate_pa0035(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PA0035."""
    return run_spec_rule(PA0035InsideBarRule, df)
