"""DQ0050 — Statistical Outlier Present. TASS catalog: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules._common.spec_runtime import SpecRule, run_spec_rule


class DQ0050StatisticalOutlierPresentRule(SpecRule):
    rule_id = "DQ0050"
    rule_name = "Statistical Outlier Present"


def evaluate_dq0050(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for DQ0050."""
    return run_spec_rule(DQ0050StatisticalOutlierPresentRule, df)
