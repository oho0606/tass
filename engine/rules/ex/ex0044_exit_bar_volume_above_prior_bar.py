"""EX0044 — Exit Bar Volume Above Prior Bar. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class EX0044ExitBarVolumeAbovePriorBarRule(SpecRule):
    rule_id = "EX0044"
    rule_name = "Exit Bar Volume Above Prior Bar"


def evaluate_ex0044(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for EX0044."""
    return run_spec_rule(EX0044ExitBarVolumeAbovePriorBarRule, df)
