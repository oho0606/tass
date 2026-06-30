"""PA0039 — Range Expanding. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PA0039RangeExpandingRule(SpecRule):
    rule_id = "PA0039"
    rule_name = "Range Expanding"


def evaluate_pa0039(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PA0039."""
    return run_spec_rule(PA0039RangeExpandingRule, df)
