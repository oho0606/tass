"""GP0056 — Gap Filled Intraday. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class GP0056GapFilledIntradayRule(SpecRule):
    rule_id = "GP0056"
    rule_name = "Gap Filled Intraday"


def evaluate_gp0056(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for GP0056."""
    return run_spec_rule(GP0056GapFilledIntradayRule, df)
