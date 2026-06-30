"""EN0043 — Entry Bar Volume Above Prior Bar. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class EN0043EntryBarVolumeAbovePriorBarRule(SpecRule):
    rule_id = "EN0043"
    rule_name = "Entry Bar Volume Above Prior Bar"


def evaluate_en0043(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for EN0043."""
    return run_spec_rule(EN0043EntryBarVolumeAbovePriorBarRule, df)
