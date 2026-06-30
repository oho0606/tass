"""VO0003 — ATR Above Prior ATR. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class VO0003ATRAbovePriorATRRule(SpecRule):
    rule_id = "VO0003"
    rule_name = "ATR Above Prior ATR"


def evaluate_vo0003(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for VO0003."""
    return run_spec_rule(VO0003ATRAbovePriorATRRule, df)
