"""One-off generator for MA0001–MA0020 rule files."""

from __future__ import annotations

from pathlib import Path

RULES = [
    ("MA0001", "Price Above SMA5", "sma", 5, "above"),
    ("MA0002", "Price Above SMA20", "sma", 20, "above"),
    ("MA0003", "Price Above SMA60", "sma", 60, "above"),
    ("MA0004", "Price Above SMA120", "sma", 120, "above"),
    ("MA0005", "Price Above SMA240", "sma", 240, "above"),
    ("MA0006", "Price Below SMA5", "sma", 5, "below"),
    ("MA0007", "Price Below SMA20", "sma", 20, "below"),
    ("MA0008", "Price Below SMA60", "sma", 60, "below"),
    ("MA0009", "Price Below SMA120", "sma", 120, "below"),
    ("MA0010", "Price Below SMA240", "sma", 240, "below"),
    ("MA0011", "Price Above EMA5", "ema", 5, "above"),
    ("MA0012", "Price Above EMA20", "ema", 20, "above"),
    ("MA0013", "Price Above EMA60", "ema", 60, "above"),
    ("MA0014", "Price Above EMA120", "ema", 120, "above"),
    ("MA0015", "Price Above EMA240", "ema", 240, "above"),
    ("MA0016", "Price Below EMA5", "ema", 5, "below"),
    ("MA0017", "Price Below EMA20", "ema", 20, "below"),
    ("MA0018", "Price Below EMA60", "ema", 60, "below"),
    ("MA0019", "Price Below EMA120", "ema", 120, "below"),
    ("MA0020", "Price Below EMA240", "ema", 240, "below"),
]

root = Path(__file__).resolve().parent.parent / "engine" / "rules" / "ma"
root.mkdir(parents=True, exist_ok=True)

for rule_id, rule_name, ma_type, period, direction in RULES:
    safe = rule_name.replace(" ", "")
    class_name = f"{rule_id}{safe}Rule"
    slug = rule_name.lower().replace(" ", "_")
    fname = f"{rule_id.lower()}_{slug}.py"
    fn = rule_id.lower()
    content = f'''"""{rule_id} — {rule_name}. TASS-015: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.ma._helpers import PricePositionRule, run_price_position_rule


class {class_name}(PricePositionRule):
    rule_id = "{rule_id}"
    rule_name = "{rule_name}"
    ma_type = "{ma_type}"
    period = {period}
    direction = "{direction}"


def evaluate_{fn}(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for {rule_id}."""
    return run_price_position_rule({class_name}, df)
'''
    (root / fname).write_text(content, encoding="utf-8")

print(f"wrote {len(RULES)} rule files to {root}")
