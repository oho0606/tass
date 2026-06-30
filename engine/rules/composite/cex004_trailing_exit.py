"""CEX004 — Trailing Exit. TASS-027 composite rule."""

from __future__ import annotations

from engine.core.types import RuleResult
from engine.rules.composite._ratio import make_ratio_composite

_RULE = make_ratio_composite(
    rule_id="CEX004",
    rule_name="Trailing Exit",
    atomic_prefix="EX",
    mode="bullish",
)


def evaluate_cex004(atomic: dict[str, RuleResult]) -> RuleResult:
    """Evaluate CEX004 from atomic rule results."""
    return _RULE.evaluate(atomic)
