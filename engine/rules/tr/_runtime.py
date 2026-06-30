"""TR spec rule runtime."""

from __future__ import annotations

from engine.rules._common.spec_runtime import SpecRule, evaluate_spec
from engine.rules.tr._name_parser import parse_tr_rule_name


class TrendSpecRule(SpecRule):
    """Trend catalog rule using TR-specific spec parsing."""


def run_trend_spec_rule(rule_cls: type[TrendSpecRule], df):
    rule = rule_cls()
    rule.initialize()
    spec = parse_tr_rule_name(rule.rule_id, rule.rule_name)
    payload = evaluate_spec(df, spec)
    rule._calculation = payload  # noqa: SLF001
    verdict = "PASS" if payload.get("passed") else "FAIL"
    return rule._build_result(verdict)  # noqa: SLF001
