"""CVL008 — Volume Quality. TASS-027 composite rule."""

from __future__ import annotations

from engine.core.types import RuleResult
from engine.rules.composite._ratio import make_ratio_composite

_RULE = make_ratio_composite(
    rule_id="CVL008",
    rule_name="Volume Quality",
    atomic_prefix="VL",
    mode="quality",
)


def evaluate_cvl008(atomic: dict[str, RuleResult]) -> RuleResult:
    """Evaluate CVL008 from atomic rule results."""
    return _RULE.evaluate(atomic)
