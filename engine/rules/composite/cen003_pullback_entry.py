"""CEN003 — Pullback Entry. TASS-027 composite rule."""

from __future__ import annotations

from engine.core.types import RuleResult
from engine.rules.composite._ratio import make_ratio_composite

_RULE = make_ratio_composite(
    rule_id="CEN003",
    rule_name="Pullback Entry",
    atomic_prefix="EN",
    mode="bullish",
)


def evaluate_cen003(atomic: dict[str, RuleResult]) -> RuleResult:
    """Evaluate CEN003 from atomic rule results."""
    return _RULE.evaluate(atomic)
