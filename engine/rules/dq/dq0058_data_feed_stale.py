"""DQ0058 — Data Feed Stale. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class DQ0058DataFeedStaleRule(SpecRule):
    rule_id = "DQ0058"
    rule_name = "Data Feed Stale"


def evaluate_dq0058(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for DQ0058."""
    return run_spec_rule(DQ0058DataFeedStaleRule, df)
