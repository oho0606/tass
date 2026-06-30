"""PT0006 — Bear Pennant Formed. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PT0006BearPennantFormedRule(SpecRule):
    rule_id = "PT0006"
    rule_name = "Bear Pennant Formed"


def evaluate_pt0006(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PT0006."""
    return run_spec_rule(PT0006BearPennantFormedRule, df)
