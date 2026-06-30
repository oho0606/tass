"""CEN002 — Breakout Entry. TASS-027 composite rule."""

from __future__ import annotations

from engine.core.types import RuleResult
from engine.rules.composite._ratio import make_ratio_composite

_RULE = make_ratio_composite(
    rule_id="CEN002",
    rule_name="Breakout Entry",
    atomic_prefix="EN",
    mode="bullish",
)


def evaluate_cen002(atomic: dict[str, RuleResult]) -> RuleResult:
    """Evaluate CEN002 from atomic rule results."""
    return _RULE.evaluate(atomic)
