"""VO0001 — ATR Rising. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class VO0001ATRRisingRule(SpecRule):
    rule_id = "VO0001"
    rule_name = "ATR Rising"


def evaluate_vo0001(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for VO0001."""
    return run_spec_rule(VO0001ATRRisingRule, df)
