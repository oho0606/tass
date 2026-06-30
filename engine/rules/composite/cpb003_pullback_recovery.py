"""CPB003 — Pullback Recovery. TASS-027 composite rule."""

from __future__ import annotations

from engine.core.types import RuleResult
from engine.rules.composite._ratio import make_ratio_composite

_RULE = make_ratio_composite(
    rule_id="CPB003",
    rule_name="Pullback Recovery",
    atomic_prefix="PB",
    mode="bullish",
)


def evaluate_cpb003(atomic: dict[str, RuleResult]) -> RuleResult:
    """Evaluate CPB003 from atomic rule results."""
    return _RULE.evaluate(atomic)
