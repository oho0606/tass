"""DQ0033 — Delisted Instrument. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class DQ0033DelistedInstrumentRule(SpecRule):
    rule_id = "DQ0033"
    rule_name = "Delisted Instrument"


def evaluate_dq0033(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for DQ0033."""
    return run_spec_rule(DQ0033DelistedInstrumentRule, df)
