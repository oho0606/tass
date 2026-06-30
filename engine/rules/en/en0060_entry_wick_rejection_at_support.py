"""EN0060 — Entry Wick Rejection At Support. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class EN0060EntryWickRejectionAtSupportRule(SpecRule):
    rule_id = "EN0060"
    rule_name = "Entry Wick Rejection At Support"


def evaluate_en0060(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for EN0060."""
    return run_spec_rule(EN0060EntryWickRejectionAtSupportRule, df)
