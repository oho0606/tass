"""TR-specific rule name parsing for catalog TR0005–TR0080."""

from __future__ import annotations

import re

from engine.rules._common.spec_runtime import RuleSpec


def parse_tr_rule_name(rule_id: str, rule_name: str) -> RuleSpec:
    """Parse TR catalog rule names into executable specs."""
    name = rule_name.strip()

    if name in {"Higher High", "Higher Low", "Lower High", "Lower Low"}:
        kind = "pivot_event"
        event = name
        return RuleSpec(rule_id, name, kind, {"event": event})

    trend_map = {
        "Uptrend": ("compare", {"series": "close", "op": "gt", "ref": "ma_20"}),
        "Downtrend": ("compare", {"series": "close", "op": "lt", "ref": "ma_20"}),
        "Sideways Trend": ("heuristic", {"label": "sideways trend"}),
        "Trend Reversal Up": ("slope", {"series": "close", "direction": "turning"}),
        "Trend Reversal Down": ("slope", {"series": "close", "direction": "turning"}),
        "Trend Continuation": ("heuristic", {"label": "trend continuation"}),
        "Strong Uptrend": ("heuristic", {"label": "strong uptrend"}),
        "Weak Uptrend": ("heuristic", {"label": "weak uptrend"}),
        "Strong Downtrend": ("heuristic", {"label": "strong downtrend"}),
        "Weak Downtrend": ("heuristic", {"label": "weak downtrend"}),
    }
    if name in trend_map:
        kind, params = trend_map[name]
        return RuleSpec(rule_id, name, kind, params)

    if name.startswith("ADX "):
        series = "adx_14"
        if "Rising" in name:
            return RuleSpec(rule_id, name, "slope", {"series": series, "direction": "rising"})
        if "Falling" in name:
            return RuleSpec(rule_id, name, "slope", {"series": series, "direction": "falling"})
        if "Above" in name:
            return RuleSpec(rule_id, name, "compare", {"series": series, "op": "gt", "ref": 25.0})
        return RuleSpec(rule_id, name, "compare", {"series": series, "op": "lt", "ref": 25.0})

    if "Momentum Increasing" in name or "Momentum Decreasing" in name:
        direction = "rising" if "Increasing" in name else "falling"
        return RuleSpec(rule_id, name, "slope", {"series": "roc_12", "direction": direction})

    if name.endswith(" Uptrend") or name.endswith(" Downtrend"):
        label = name.lower()
        return RuleSpec(rule_id, name, "heuristic", {"label": label})

    if "Choppy" in name or "Noisy" in name or "Unstable" in name:
        return RuleSpec(rule_id, name, "heuristic", {"label": name.lower()})
    if "Smooth" in name or "Stable" in name or "Clean" in name:
        return RuleSpec(rule_id, name, "heuristic", {"label": name.lower()})
    if "Consistency High" in name:
        return RuleSpec(rule_id, name, "stable", {"series": "close"})
    if "Consistency Low" in name:
        return RuleSpec(rule_id, name, "heuristic", {"label": "consistency low"})

    if "Slope" in name or "Accelerating" in name or "Decelerating" in name:
        direction = "rising"
        if "Negative" in name or "Decreasing" in name or "Decelerating" in name:
            direction = "falling"
        if "Flat" in name:
            direction = "flat"
        if "Reversal" in name:
            direction = "turning"
        return RuleSpec(rule_id, name, "slope", {"series": "close", "direction": direction})

    if name.startswith("Consecutive "):
        return RuleSpec(rule_id, name, "pivot_event", {"event": name})

    if "Persistence" in name or "Duration" in name or "Age" in name:
        return RuleSpec(rule_id, name, "heuristic", {"label": name.lower()})

    if "Exhaustion" in name or "Climax" in name or "Failure" in name:
        return RuleSpec(rule_id, name, "heuristic", {"label": name.lower()})

    if "Confirms Trend" in name or "Confirmation" in name:
        return RuleSpec(rule_id, name, "confirmation", {"label": name.lower()})

    if name.endswith(" Trend State") or name.startswith("Trend "):
        return RuleSpec(rule_id, name, "market_regime", {"label": name.lower()})

    if re.search(r"TR00(7[1-9]|80)", rule_id):
        return RuleSpec(rule_id, name, "market_regime", {"label": name.lower()})

    return RuleSpec(rule_id, name, "heuristic", {"label": name.lower()})
