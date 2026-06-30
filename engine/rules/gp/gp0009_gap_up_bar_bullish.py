"""GP0009 — Gap Up Bar Bullish. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class GP0009GapUpBarBullishRule(SpecRule):
    rule_id = "GP0009"
    rule_name = "Gap Up Bar Bullish"


def evaluate_gp0009(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for GP0009."""
    return run_spec_rule(GP0009GapUpBarBullishRule, df)
