"""DQ0044 — Abnormal Return Present. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class DQ0044AbnormalReturnPresentRule(SpecRule):
    rule_id = "DQ0044"
    rule_name = "Abnormal Return Present"


def evaluate_dq0044(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for DQ0044."""
    return run_spec_rule(DQ0044AbnormalReturnPresentRule, df)
