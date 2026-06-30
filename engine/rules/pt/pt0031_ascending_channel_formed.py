"""PT0031 — Ascending Channel Formed. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PT0031AscendingChannelFormedRule(SpecRule):
    rule_id = "PT0031"
    rule_name = "Ascending Channel Formed"


def evaluate_pt0031(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PT0031."""
    return run_spec_rule(PT0031AscendingChannelFormedRule, df)
