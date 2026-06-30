"""CMT005 — Lower Timeframe Agreement. TASS-027 composite rule."""

from __future__ import annotations

from engine.core.types import RuleResult
from engine.rules.composite._ratio import make_ratio_composite

_RULE = make_ratio_composite(
    rule_id="CMT005",
    rule_name="Lower Timeframe Agreement",
    atomic_prefix="MT",
    mode="quality",
)


def evaluate_cmt005(atomic: dict[str, RuleResult]) -> RuleResult:
    """Evaluate CMT005 from atomic rule results."""
    return _RULE.evaluate(atomic)
