"""DQ0045 — Abnormal Range Present. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class DQ0045AbnormalRangePresentRule(SpecRule):
    rule_id = "DQ0045"
    rule_name = "Abnormal Range Present"


def evaluate_dq0045(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for DQ0045."""
    return run_spec_rule(DQ0045AbnormalRangePresentRule, df)
