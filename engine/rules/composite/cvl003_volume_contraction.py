"""CVL003 — Volume Contraction. TASS-027 composite rule."""

from __future__ import annotations

from engine.core.types import RuleResult
from engine.rules.composite._ratio import make_ratio_composite

_RULE = make_ratio_composite(
    rule_id="CVL003",
    rule_name="Volume Contraction",
    atomic_prefix="VL",
    mode="bearish",
)


def evaluate_cvl003(atomic: dict[str, RuleResult]) -> RuleResult:
    """Evaluate CVL003 from atomic rule results."""
    return _RULE.evaluate(atomic)
