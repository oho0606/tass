"""MR0052 — ADX Rising. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MR0052ADXRisingRule(SpecRule):
    rule_id = "MR0052"
    rule_name = "ADX Rising"


def evaluate_mr0052(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MR0052."""
    return run_spec_rule(MR0052ADXRisingRule, df)
