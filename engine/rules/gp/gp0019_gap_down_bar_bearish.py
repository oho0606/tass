"""GP0019 — Gap Down Bar Bearish. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class GP0019GapDownBarBearishRule(SpecRule):
    rule_id = "GP0019"
    rule_name = "Gap Down Bar Bearish"


def evaluate_gp0019(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for GP0019."""
    return run_spec_rule(GP0019GapDownBarBearishRule, df)
