"""CEX002 — Stop Loss Exit. TASS-027 composite rule."""

from __future__ import annotations

from engine.core.types import RuleResult
from engine.rules.composite._ratio import make_ratio_composite

_RULE = make_ratio_composite(
    rule_id="CEX002",
    rule_name="Stop Loss Exit",
    atomic_prefix="EX",
    mode="bearish",
)


def evaluate_cex002(atomic: dict[str, RuleResult]) -> RuleResult:
    """Evaluate CEX002 from atomic rule results."""
    return _RULE.evaluate(atomic)
