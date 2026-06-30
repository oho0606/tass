"""DQ0056 — Session Data Incomplete. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class DQ0056SessionDataIncompleteRule(SpecRule):
    rule_id = "DQ0056"
    rule_name = "Session Data Incomplete"


def evaluate_dq0056(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for DQ0056."""
    return run_spec_rule(DQ0056SessionDataIncompleteRule, df)
