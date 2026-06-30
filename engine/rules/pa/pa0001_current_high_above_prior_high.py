"""PA0001 — Current High Above Prior High. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PA0001CurrentHighAbovePriorHighRule(SpecRule):
    rule_id = "PA0001"
    rule_name = "Current High Above Prior High"


def evaluate_pa0001(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PA0001."""
    return run_spec_rule(PA0001CurrentHighAbovePriorHighRule, df)
