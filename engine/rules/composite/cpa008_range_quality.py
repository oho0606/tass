"""CPA008 — Range Quality. TASS-027 composite rule."""

from __future__ import annotations

from engine.core.types import RuleResult
from engine.rules.composite._ratio import make_ratio_composite

_RULE = make_ratio_composite(
    rule_id="CPA008",
    rule_name="Range Quality",
    atomic_prefix="PA",
    mode="quality",
)


def evaluate_cpa008(atomic: dict[str, RuleResult]) -> RuleResult:
    """Evaluate CPA008 from atomic rule results."""
    return _RULE.evaluate(atomic)
