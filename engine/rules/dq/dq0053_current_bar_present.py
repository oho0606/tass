"""DQ0053 — Current Bar Present. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class DQ0053CurrentBarPresentRule(SpecRule):
    rule_id = "DQ0053"
    rule_name = "Current Bar Present"


def evaluate_dq0053(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for DQ0053."""
    return run_spec_rule(DQ0053CurrentBarPresentRule, df)
