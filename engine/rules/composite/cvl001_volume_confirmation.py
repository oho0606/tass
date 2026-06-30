"""CVL001 — Volume Confirmation. TASS-027 composite rule."""

from __future__ import annotations

from engine.core.types import RuleResult
from engine.rules.composite._ratio import make_ratio_composite

_RULE = make_ratio_composite(
    rule_id="CVL001",
    rule_name="Volume Confirmation",
    atomic_prefix="VL",
    mode="quality",
)


def evaluate_cvl001(atomic: dict[str, RuleResult]) -> RuleResult:
    """Evaluate CVL001 from atomic rule results."""
    return _RULE.evaluate(atomic)
