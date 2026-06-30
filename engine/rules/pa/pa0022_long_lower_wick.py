"""PA0022 — Long Lower Wick. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PA0022LongLowerWickRule(SpecRule):
    rule_id = "PA0022"
    rule_name = "Long Lower Wick"


def evaluate_pa0022(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PA0022."""
    return run_spec_rule(PA0022LongLowerWickRule, df)
