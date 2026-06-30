"""CGP001 — Bullish Gap. TASS-027 composite rule."""

from __future__ import annotations

from engine.core.types import RuleResult
from engine.rules.composite._ratio import make_ratio_composite

_RULE = make_ratio_composite(
    rule_id="CGP001",
    rule_name="Bullish Gap",
    atomic_prefix="GP",
    mode="bullish",
)


def evaluate_cgp001(atomic: dict[str, RuleResult]) -> RuleResult:
    """Evaluate CGP001 from atomic rule results."""
    return _RULE.evaluate(atomic)
