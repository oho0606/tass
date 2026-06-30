"""Generate MA0041–MA0060 rule files."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "engine" / "rules" / "ma"

SLOPE_RULES = [
    ("MA0041", "SMA Rising", "MaSlopeRule", "sma", "rising"),
    ("MA0042", "SMA Falling", "MaSlopeRule", "sma", "falling"),
    ("MA0043", "EMA Rising", "MaSlopeRule", "ema", "rising"),
    ("MA0044", "EMA Falling", "MaSlopeRule", "ema", "falling"),
    ("MA0045", "SMA Slope Increasing", "MaSlopeTrendRule", "sma", "increasing"),
    ("MA0046", "SMA Slope Decreasing", "MaSlopeTrendRule", "sma", "decreasing"),
    ("MA0047", "EMA Slope Increasing", "MaSlopeTrendRule", "ema", "increasing"),
    ("MA0048", "EMA Slope Decreasing", "MaSlopeTrendRule", "ema", "decreasing"),
]

STRUCTURE_RULES = [
    ("MA0051", "Price Extended Above MA", "PriceDistanceRule", "extended_above"),
    ("MA0052", "Price Extended Below MA", "PriceDistanceRule", "extended_below"),
    ("MA0053", "Price Near Moving Average", "PriceDistanceRule", "near"),
    ("MA0054", "Moving Average Compression", "MaSpreadTrendRule", "compression"),
    ("MA0055", "Moving Average Expansion", "MaSpreadTrendRule", "expansion"),
    ("MA0056", "Moving Average Convergence", "MaSpreadLevelRule", "convergence"),
    ("MA0057", "Moving Average Divergence", "MaSpreadLevelRule", "divergence"),
    ("MA0058", "Dynamic Support Holding", "DynamicLevelRule", "support"),
    ("MA0059", "Dynamic Resistance Holding", "DynamicLevelRule", "resistance"),
]


def _write_slope(rule_id: str, rule_name: str, base_cls: str, ma_type: str, direction: str) -> None:
    safe = rule_name.replace(" ", "")
    class_name = f"{rule_id}{safe}Rule"
    slug = rule_name.lower().replace(" ", "_")
    fname = f"{rule_id.lower()}_{slug}.py"
    if base_cls == "MaSlopeRule":
        body = f"""    ma_type = \"{ma_type}\"
    direction = \"{direction}\"
"""
        import_line = "from engine.rules.ma._slope import MaSlopeRule, run_slope_rule"
    else:
        body = f"""    ma_type = \"{ma_type}\"
    trend = \"{direction}\"
"""
        import_line = "from engine.rules.ma._slope import MaSlopeTrendRule, run_slope_rule"

    content = f'''"""{rule_id} — {rule_name}. TASS-015: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
{import_line}


class {class_name}({base_cls}):
    rule_id = "{rule_id}"
    rule_name = "{rule_name}"
{body}

def evaluate_{rule_id.lower()}(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for {rule_id}."""
    return run_slope_rule({class_name}, df)
'''
    (ROOT / fname).write_text(content, encoding="utf-8")


def _write_flat_or_turning(rule_id: str, rule_name: str, base_cls: str) -> None:
    safe = rule_name.replace(" ", "")
    class_name = f"{rule_id}{safe}Rule"
    slug = rule_name.lower().replace(" ", "_")
    fname = f"{rule_id.lower()}_{slug}.py"
    content = f'''"""{rule_id} — {rule_name}. TASS-015: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.ma._slope import {base_cls}, run_slope_rule


class {class_name}({base_cls}):
    rule_id = "{rule_id}"
    rule_name = "{rule_name}"


def evaluate_{rule_id.lower()}(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for {rule_id}."""
    return run_slope_rule({class_name}, df)
'''
    (ROOT / fname).write_text(content, encoding="utf-8")


def _write_structure(rule_id: str, rule_name: str, base_cls: str, mode: str) -> None:
    safe = rule_name.replace(" ", "")
    class_name = f"{rule_id}{safe}Rule"
    slug = rule_name.lower().replace(" ", "_")
    fname = f"{rule_id.lower()}_{slug}.py"

    if base_cls == "PriceDistanceRule":
        body = f'    mode = "{mode}"\n'
    elif base_cls == "MaSpreadTrendRule":
        body = f'    trend = "{mode}"\n'
    elif base_cls == "MaSpreadLevelRule":
        body = f'    level = "{mode}"\n'
    else:
        body = f'    level = "{mode}"\n'

    content = f'''"""{rule_id} — {rule_name}. TASS-015: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.ma._structure import {base_cls}, run_structure_rule


class {class_name}({base_cls}):
    rule_id = "{rule_id}"
    rule_name = "{rule_name}"
{body}

def evaluate_{rule_id.lower()}(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for {rule_id}."""
    return run_structure_rule({class_name}, df)
'''
    (ROOT / fname).write_text(content, encoding="utf-8")


def _write_structure_stable() -> None:
    content = '''"""MA0060 — Moving Average Structure Stable. TASS-015: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.ma._structure import MaStructureStableRule, run_structure_rule


class MA0060MovingAverageStructureStableRule(MaStructureStableRule):
    rule_id = "MA0060"
    rule_name = "Moving Average Structure Stable"


def evaluate_ma0060(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for MA0060."""
    return run_structure_rule(MA0060MovingAverageStructureStableRule, df)
'''
    (ROOT / "ma0060_moving_average_structure_stable.py").write_text(content, encoding="utf-8")


def main() -> None:
    for item in SLOPE_RULES:
        _write_slope(*item)
    _write_flat_or_turning("MA0049", "Moving Average Flat", "MaFlatRule")
    _write_flat_or_turning("MA0050", "Moving Average Turning", "MaTurningRule")
    for item in STRUCTURE_RULES:
        _write_structure(*item)
    _write_structure_stable()
    print("generated MA0041-MA0060")


if __name__ == "__main__":
    main()
