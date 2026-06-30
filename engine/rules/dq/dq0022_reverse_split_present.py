"""DQ0022 — Reverse Split Present. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class DQ0022ReverseSplitPresentRule(SpecRule):
    rule_id = "DQ0022"
    rule_name = "Reverse Split Present"


def evaluate_dq0022(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for DQ0022."""
    return run_spec_rule(DQ0022ReverseSplitPresentRule, df)
