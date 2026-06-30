"""PA0003 — Current High Equal Prior High. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PA0003CurrentHighEqualPriorHighRule(SpecRule):
    rule_id = "PA0003"
    rule_name = "Current High Equal Prior High"


def evaluate_pa0003(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PA0003."""
    return run_spec_rule(PA0003CurrentHighEqualPriorHighRule, df)
