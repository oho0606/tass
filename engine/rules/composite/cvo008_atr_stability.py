"""CVO008 — ATR Stability. TASS-027 composite rule."""

from __future__ import annotations

from engine.core.types import RuleResult
from engine.rules.composite._ratio import make_ratio_composite

_RULE = make_ratio_composite(
    rule_id="CVO008",
    rule_name="ATR Stability",
    atomic_prefix="VO",
    mode="quality",
)


def evaluate_cvo008(atomic: dict[str, RuleResult]) -> RuleResult:
    """Evaluate CVO008 from atomic rule results."""
    return _RULE.evaluate(atomic)
