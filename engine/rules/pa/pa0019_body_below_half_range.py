"""PA0019 — Body Below Half Range. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PA0019BodyBelowHalfRangeRule(SpecRule):
    rule_id = "PA0019"
    rule_name = "Body Below Half Range"


def evaluate_pa0019(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PA0019."""
    return run_spec_rule(PA0019BodyBelowHalfRangeRule, df)
