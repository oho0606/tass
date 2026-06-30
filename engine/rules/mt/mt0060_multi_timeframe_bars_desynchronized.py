"""MT0060 — Multi Timeframe Bars Desynchronized. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MT0060MultiTimeframeBarsDesynchronizedRule(SpecRule):
    rule_id = "MT0060"
    rule_name = "Multi Timeframe Bars Desynchronized"


def evaluate_mt0060(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MT0060."""
    return run_spec_rule(MT0060MultiTimeframeBarsDesynchronizedRule, df)
