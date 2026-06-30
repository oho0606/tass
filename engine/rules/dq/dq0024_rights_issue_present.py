"""DQ0024 — Rights Issue Present. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class DQ0024RightsIssuePresentRule(SpecRule):
    rule_id = "DQ0024"
    rule_name = "Rights Issue Present"


def evaluate_dq0024(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for DQ0024."""
    return run_spec_rule(DQ0024RightsIssuePresentRule, df)
