"""EN0056 — Entry Bar Body Below Half Range. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class EN0056EntryBarBodyBelowHalfRangeRule(SpecRule):
    rule_id = "EN0056"
    rule_name = "Entry Bar Body Below Half Range"


def evaluate_en0056(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for EN0056."""
    return run_spec_rule(EN0056EntryBarBodyBelowHalfRangeRule, df)
