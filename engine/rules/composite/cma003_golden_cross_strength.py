"""CMA003 — Golden Cross Strength. TASS-027 composite rule."""

from __future__ import annotations

from engine.core.types import RuleResult
from engine.rules.composite._ratio import make_ratio_composite

_RULE = make_ratio_composite(
    rule_id="CMA003",
    rule_name="Golden Cross Strength",
    atomic_prefix="MA",
    mode="bullish",
)


def evaluate_cma003(atomic: dict[str, RuleResult]) -> RuleResult:
    """Evaluate CMA003 from atomic rule results."""
    return _RULE.evaluate(atomic)
