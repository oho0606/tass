"""CSR004 — Resistance Break. TASS-027 composite rule."""

from __future__ import annotations

from engine.core.types import RuleResult
from engine.rules.composite._ratio import make_ratio_composite

_RULE = make_ratio_composite(
    rule_id="CSR004",
    rule_name="Resistance Break",
    atomic_prefix="SR",
    mode="bearish",
)


def evaluate_csr004(atomic: dict[str, RuleResult]) -> RuleResult:
    """Evaluate CSR004 from atomic rule results."""
    return _RULE.evaluate(atomic)
