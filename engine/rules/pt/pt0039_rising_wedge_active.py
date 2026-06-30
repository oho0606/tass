"""PT0039 — Rising Wedge Active. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PT0039RisingWedgeActiveRule(SpecRule):
    rule_id = "PT0039"
    rule_name = "Rising Wedge Active"


def evaluate_pt0039(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PT0039."""
    return run_spec_rule(PT0039RisingWedgeActiveRule, df)
