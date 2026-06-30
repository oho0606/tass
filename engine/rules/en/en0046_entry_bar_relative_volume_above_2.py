"""EN0046 — Entry Bar Relative Volume Above 2. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class EN0046EntryBarRelativeVolumeAbove2Rule(SpecRule):
    rule_id = "EN0046"
    rule_name = "Entry Bar Relative Volume Above 2"


def evaluate_en0046(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for EN0046."""
    return run_spec_rule(EN0046EntryBarRelativeVolumeAbove2Rule, df)
