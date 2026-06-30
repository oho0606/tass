"""PT0002 — Bear Flag Formed. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PT0002BearFlagFormedRule(SpecRule):
    rule_id = "PT0002"
    rule_name = "Bear Flag Formed"


def evaluate_pt0002(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PT0002."""
    return run_spec_rule(PT0002BearFlagFormedRule, df)
