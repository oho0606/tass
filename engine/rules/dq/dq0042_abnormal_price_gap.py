"""DQ0042 — Abnormal Price Gap. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class DQ0042AbnormalPriceGapRule(SpecRule):
    rule_id = "DQ0042"
    rule_name = "Abnormal Price Gap"


def evaluate_dq0042(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for DQ0042."""
    return run_spec_rule(DQ0042AbnormalPriceGapRule, df)
