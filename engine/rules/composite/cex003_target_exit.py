"""CEX003 — Target Exit. TASS-027 composite rule."""

from __future__ import annotations

from engine.core.types import RuleResult
from engine.rules.composite._ratio import make_ratio_composite

_RULE = make_ratio_composite(
    rule_id="CEX003",
    rule_name="Target Exit",
    atomic_prefix="EX",
    mode="bullish",
)


def evaluate_cex003(atomic: dict[str, RuleResult]) -> RuleResult:
    """Evaluate CEX003 from atomic rule results."""
    return _RULE.evaluate(atomic)
