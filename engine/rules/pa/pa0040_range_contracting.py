"""PA0040 — Range Contracting. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PA0040RangeContractingRule(SpecRule):
    rule_id = "PA0040"
    rule_name = "Range Contracting"


def evaluate_pa0040(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PA0040."""
    return run_spec_rule(PA0040RangeContractingRule, df)
