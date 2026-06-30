"""DQ0040 — Limit Down Lock. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class DQ0040LimitDownLockRule(SpecRule):
    rule_id = "DQ0040"
    rule_name = "Limit Down Lock"


def evaluate_dq0040(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for DQ0040."""
    return run_spec_rule(DQ0040LimitDownLockRule, df)
