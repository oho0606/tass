"""EN0044 — Entry Bar Volume Below Prior Bar. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class EN0044EntryBarVolumeBelowPriorBarRule(SpecRule):
    rule_id = "EN0044"
    rule_name = "Entry Bar Volume Below Prior Bar"


def evaluate_en0044(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for EN0044."""
    return run_spec_rule(EN0044EntryBarVolumeBelowPriorBarRule, df)
