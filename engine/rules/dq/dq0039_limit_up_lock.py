"""DQ0039 — Limit Up Lock. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class DQ0039LimitUpLockRule(SpecRule):
    rule_id = "DQ0039"
    rule_name = "Limit Up Lock"


def evaluate_dq0039(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for DQ0039."""
    return run_spec_rule(DQ0039LimitUpLockRule, df)
