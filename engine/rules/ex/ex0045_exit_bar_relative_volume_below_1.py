"""EX0045 — Exit Bar Relative Volume Below 1. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class EX0045ExitBarRelativeVolumeBelow1Rule(SpecRule):
    rule_id = "EX0045"
    rule_name = "Exit Bar Relative Volume Below 1"


def evaluate_ex0045(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for EX0045."""
    return run_spec_rule(EX0045ExitBarRelativeVolumeBelow1Rule, df)
