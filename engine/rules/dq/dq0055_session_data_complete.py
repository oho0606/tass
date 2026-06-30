"""DQ0055 — Session Data Complete. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class DQ0055SessionDataCompleteRule(SpecRule):
    rule_id = "DQ0055"
    rule_name = "Session Data Complete"


def evaluate_dq0055(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for DQ0055."""
    return run_spec_rule(DQ0055SessionDataCompleteRule, df)
