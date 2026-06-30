"""MT0009 — 4H 1H Uptrend Match. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class MT00094H1HUptrendMatchRule(SpecRule):
    rule_id = "MT0009"
    rule_name = "4H 1H Uptrend Match"


def evaluate_mt0009(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MT0009."""
    return run_spec_rule(MT00094H1HUptrendMatchRule, df)
