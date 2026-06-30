"""CEN004 — Trend Entry. TASS-027 composite rule."""

from __future__ import annotations

from engine.core.types import RuleResult
from engine.rules.composite._ratio import make_ratio_composite

_RULE = make_ratio_composite(
    rule_id="CEN004",
    rule_name="Trend Entry",
    atomic_prefix="EN",
    mode="bullish",
)


def evaluate_cen004(atomic: dict[str, RuleResult]) -> RuleResult:
    """Evaluate CEN004 from atomic rule results."""
    return _RULE.evaluate(atomic)
