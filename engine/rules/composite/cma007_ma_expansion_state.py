"""CMA007 — MA Expansion State. TASS-027 composite rule."""

from __future__ import annotations

from engine.core.types import RuleResult
from engine.rules.composite._ratio import make_ratio_composite

_RULE = make_ratio_composite(
    rule_id="CMA007",
    rule_name="MA Expansion State",
    atomic_prefix="MA",
    mode="neutral",
)


def evaluate_cma007(atomic: dict[str, RuleResult]) -> RuleResult:
    """Evaluate CMA007 from atomic rule results."""
    return _RULE.evaluate(atomic)
