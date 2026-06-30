"""PA0020 — Marubozu Body. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PA0020MarubozuBodyRule(SpecRule):
    rule_id = "PA0020"
    rule_name = "Marubozu Body"


def evaluate_pa0020(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PA0020."""
    return run_spec_rule(PA0020MarubozuBodyRule, df)
