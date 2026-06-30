"""PA0002 — Current High Below Prior High. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PA0002CurrentHighBelowPriorHighRule(SpecRule):
    rule_id = "PA0002"
    rule_name = "Current High Below Prior High"


def evaluate_pa0002(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PA0002."""
    return run_spec_rule(PA0002CurrentHighBelowPriorHighRule, df)
