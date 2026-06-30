"""DQ0059 — Instrument Data Present. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class DQ0059InstrumentDataPresentRule(SpecRule):
    rule_id = "DQ0059"
    rule_name = "Instrument Data Present"


def evaluate_dq0059(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for DQ0059."""
    return run_spec_rule(DQ0059InstrumentDataPresentRule, df)
