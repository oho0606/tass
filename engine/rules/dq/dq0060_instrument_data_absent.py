"""DQ0060 — Instrument Data Absent. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class DQ0060InstrumentDataAbsentRule(SpecRule):
    rule_id = "DQ0060"
    rule_name = "Instrument Data Absent"


def evaluate_dq0060(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for DQ0060."""
    return run_spec_rule(DQ0060InstrumentDataAbsentRule, df)
