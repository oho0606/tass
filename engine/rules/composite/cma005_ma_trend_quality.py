"""CMA005 — MA Trend Quality. TASS-027 composite rule."""

from __future__ import annotations

from engine.core.types import RuleResult
from engine.rules.composite._ratio import make_ratio_composite

_RULE = make_ratio_composite(
    rule_id="CMA005",
    rule_name="MA Trend Quality",
    atomic_prefix="MA",
    mode="quality",
)


def evaluate_cma005(atomic: dict[str, RuleResult]) -> RuleResult:
    """Evaluate CMA005 from atomic rule results."""
    return _RULE.evaluate(atomic)
