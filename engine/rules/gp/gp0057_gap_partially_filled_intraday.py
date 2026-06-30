"""GP0057 — Gap Partially Filled Intraday. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class GP0057GapPartiallyFilledIntradayRule(SpecRule):
    rule_id = "GP0057"
    rule_name = "Gap Partially Filled Intraday"


def evaluate_gp0057(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for GP0057."""
    return run_spec_rule(GP0057GapPartiallyFilledIntradayRule, df)
