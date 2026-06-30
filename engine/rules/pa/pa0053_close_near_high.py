"""PA0053 — Close Near High. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PA0053CloseNearHighRule(SpecRule):
    rule_id = "PA0053"
    rule_name = "Close Near High"


def evaluate_pa0053(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PA0053."""
    return run_spec_rule(PA0053CloseNearHighRule, df)
