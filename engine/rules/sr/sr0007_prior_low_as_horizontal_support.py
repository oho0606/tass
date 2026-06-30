"""SR0007 — Prior Low As Horizontal Support. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class SR0007PriorLowAsHorizontalSupportRule(SpecRule):
    rule_id = "SR0007"
    rule_name = "Prior Low As Horizontal Support"


def evaluate_sr0007(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for SR0007."""
    return run_spec_rule(SR0007PriorLowAsHorizontalSupportRule, df)
