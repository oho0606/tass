"""CMA006 — MA Compression State. TASS-027 composite rule."""

from __future__ import annotations

from engine.core.types import RuleResult
from engine.rules.composite._ratio import make_ratio_composite

_RULE = make_ratio_composite(
    rule_id="CMA006",
    rule_name="MA Compression State",
    atomic_prefix="MA",
    mode="neutral",
)


def evaluate_cma006(atomic: dict[str, RuleResult]) -> RuleResult:
    """Evaluate CMA006 from atomic rule results."""
    return _RULE.evaluate(atomic)
