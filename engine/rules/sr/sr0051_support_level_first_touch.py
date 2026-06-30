"""SR0051 — Support Level First Touch. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class SR0051SupportLevelFirstTouchRule(SpecRule):
    rule_id = "SR0051"
    rule_name = "Support Level First Touch"


def evaluate_sr0051(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for SR0051."""
    return run_spec_rule(SR0051SupportLevelFirstTouchRule, df)
