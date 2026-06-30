"""DQ0015 — Zero Price Present. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class DQ0015ZeroPricePresentRule(SpecRule):
    rule_id = "DQ0015"
    rule_name = "Zero Price Present"


def evaluate_dq0015(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for DQ0015."""
    return run_spec_rule(DQ0015ZeroPricePresentRule, df)
