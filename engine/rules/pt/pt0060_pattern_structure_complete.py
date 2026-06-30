"""PT0060 — Pattern Structure Complete. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PT0060PatternStructureCompleteRule(SpecRule):
    rule_id = "PT0060"
    rule_name = "Pattern Structure Complete"


def evaluate_pt0060(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PT0060."""
    return run_spec_rule(PT0060PatternStructureCompleteRule, df)
