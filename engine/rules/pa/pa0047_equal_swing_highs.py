"""PA0047 — Equal Swing Highs. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class PA0047EqualSwingHighsRule(SpecRule):
    rule_id = "PA0047"
    rule_name = "Equal Swing Highs"


def evaluate_pa0047(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for PA0047."""
    return run_spec_rule(PA0047EqualSwingHighsRule, df)
