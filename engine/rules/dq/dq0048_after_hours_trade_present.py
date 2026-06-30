"""DQ0048 — After Hours Trade Present. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class DQ0048AfterHoursTradePresentRule(SpecRule):
    rule_id = "DQ0048"
    rule_name = "After Hours Trade Present"


def evaluate_dq0048(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for DQ0048."""
    return run_spec_rule(DQ0048AfterHoursTradePresentRule, df)
