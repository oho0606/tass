"""PT0033 — Horizontal Channel Formed. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PT0033HorizontalChannelFormedRule(SpecRule):
    rule_id = "PT0033"
    rule_name = "Horizontal Channel Formed"


def evaluate_pt0033(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PT0033."""
    return run_spec_rule(PT0033HorizontalChannelFormedRule, df)
