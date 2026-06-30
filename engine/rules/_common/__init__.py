"""Shared rule framework for catalog-driven atomic rules."""

from engine.rules._common.spec_runtime import RuleSpec, SpecRule, evaluate_spec, run_spec_rule

__all__ = ["RuleSpec", "SpecRule", "evaluate_spec", "run_spec_rule"]
