"""EN0045 — Entry Bar Relative Volume Above 1. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class EN0045EntryBarRelativeVolumeAbove1Rule(SpecRule):
    rule_id = "EN0045"
    rule_name = "Entry Bar Relative Volume Above 1"


def evaluate_en0045(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for EN0045."""
    return run_spec_rule(EN0045EntryBarRelativeVolumeAbove1Rule, df)
