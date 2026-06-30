"""CSR002 — Resistance Quality. TASS-027 composite rule."""

from __future__ import annotations

from engine.core.types import RuleResult
from engine.rules.composite._ratio import make_ratio_composite

_RULE = make_ratio_composite(
    rule_id="CSR002",
    rule_name="Resistance Quality",
    atomic_prefix="SR",
    mode="bearish",
)


def evaluate_csr002(atomic: dict[str, RuleResult]) -> RuleResult:
    """Evaluate CSR002 from atomic rule results."""
    return _RULE.evaluate(atomic)
