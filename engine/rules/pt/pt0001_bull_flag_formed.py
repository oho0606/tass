"""PT0001 — Bull Flag Formed. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PT0001BullFlagFormedRule(SpecRule):
    rule_id = "PT0001"
    rule_name = "Bull Flag Formed"


def evaluate_pt0001(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PT0001."""
    return run_spec_rule(PT0001BullFlagFormedRule, df)
