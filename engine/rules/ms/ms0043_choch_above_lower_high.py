"""MS0043 — CHoCH Above Lower High. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MS0043CHoCHAboveLowerHighRule(SpecRule):
    rule_id = "MS0043"
    rule_name = "CHoCH Above Lower High"


def evaluate_ms0043(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MS0043."""
    return run_spec_rule(MS0043CHoCHAboveLowerHighRule, df)
