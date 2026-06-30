"""PT0047 — Double Top Neckline Present. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PT0047DoubleTopNecklinePresentRule(SpecRule):
    rule_id = "PT0047"
    rule_name = "Double Top Neckline Present"


def evaluate_pt0047(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PT0047."""
    return run_spec_rule(PT0047DoubleTopNecklinePresentRule, df)
