"""CPA009 — Price Stability. TASS-027 composite rule."""

from __future__ import annotations

from engine.core.types import RuleResult
from engine.rules.composite._ratio import make_ratio_composite

_RULE = make_ratio_composite(
    rule_id="CPA009",
    rule_name="Price Stability",
    atomic_prefix="PA",
    mode="quality",
)


def evaluate_cpa009(atomic: dict[str, RuleResult]) -> RuleResult:
    """Evaluate CPA009 from atomic rule results."""
    return _RULE.evaluate(atomic)
