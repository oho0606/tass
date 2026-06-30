"""PA0026 — Lower Wick Larger Than Body. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PA0026LowerWickLargerThanBodyRule(SpecRule):
    rule_id = "PA0026"
    rule_name = "Lower Wick Larger Than Body"


def evaluate_pa0026(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PA0026."""
    return run_spec_rule(PA0026LowerWickLargerThanBodyRule, df)
