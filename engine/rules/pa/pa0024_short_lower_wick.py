"""PA0024 — Short Lower Wick. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PA0024ShortLowerWickRule(SpecRule):
    rule_id = "PA0024"
    rule_name = "Short Lower Wick"


def evaluate_pa0024(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PA0024."""
    return run_spec_rule(PA0024ShortLowerWickRule, df)
