"""Generate MA0022–MA0040 rule files."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "engine" / "rules" / "ma"

ALIGNMENT_RULES = [
    ("MA0022", "SMA Bearish Alignment", "AlignmentRule", "bearish", "sma", "DEFAULT_PERIODS"),
    ("MA0023", "EMA Bullish Alignment", "AlignmentRule", "bullish", "ema", "DEFAULT_PERIODS"),
    ("MA0024", "EMA Bearish Alignment", "AlignmentRule", "bearish", "ema", "DEFAULT_PERIODS"),
    ("MA0025", "SMA Alignment Improving", "AlignmentTrendRule", "improving", "sma", "DEFAULT_PERIODS"),
    ("MA0026", "SMA Alignment Weakening", "AlignmentTrendRule", "weakening", "sma", "DEFAULT_PERIODS"),
    ("MA0027", "EMA Alignment Improving", "AlignmentTrendRule", "improving", "ema", "DEFAULT_PERIODS"),
    ("MA0028", "EMA Alignment Weakening", "AlignmentTrendRule", "weakening", "ema", "DEFAULT_PERIODS"),
    ("MA0029", "Full Bullish Alignment", "FullAlignmentRule", "bullish", None, "DEFAULT_PERIODS"),
    ("MA0030", "Full Bearish Alignment", "FullAlignmentRule", "bearish", None, "DEFAULT_PERIODS"),
]

CROSSOVER_RULES = [
    ("MA0031", "SMA Golden Cross", "CrossoverRule", "sma", 20, 60, "golden"),
    ("MA0032", "SMA Death Cross", "CrossoverRule", "sma", 20, 60, "death"),
    ("MA0033", "EMA Golden Cross", "CrossoverRule", "ema", 20, 60, "golden"),
    ("MA0034", "EMA Death Cross", "CrossoverRule", "ema", 20, 60, "death"),
    ("MA0035", "Short MA Cross Above Mid MA", "CrossoverRule", "sma", 5, 20, "golden"),
    ("MA0036", "Short MA Cross Below Mid MA", "CrossoverRule", "sma", 5, 20, "death"),
    ("MA0037", "Mid MA Cross Above Long MA", "CrossoverRule", "sma", 20, 60, "golden"),
    ("MA0038", "Mid MA Cross Below Long MA", "CrossoverRule", "sma", 20, 60, "death"),
]


def _write_alignment(rule_id, rule_name, base_cls, direction, ma_type, periods) -> None:
    safe = rule_name.replace(" ", "")
    class_name = f"{rule_id}{safe}Rule"
    slug = rule_name.lower().replace(" ", "_")
    fname = f"{rule_id.lower()}_{slug}.py"
    if base_cls == "AlignmentRule":
        body = f"""    ma_type = \"{ma_type}\"
    direction = \"{direction}\"
    periods = {periods}
"""
    elif base_cls == "AlignmentTrendRule":
        body = f"""    ma_type = \"{ma_type}\"
    trend = \"{direction}\"
    periods = {periods}
"""
    else:
        body = f"""    direction = \"{direction}\"
    periods = {periods}
"""
    import_line = "from engine.rules.ma._alignment import AlignmentRule, run_alignment_rule"
    if base_cls == "AlignmentTrendRule":
        import_line = (
            "from engine.rules.ma._alignment import AlignmentTrendRule, run_alignment_rule, DEFAULT_PERIODS"
        )
    elif base_cls == "FullAlignmentRule":
        import_line = (
            "from engine.rules.ma._alignment import FullAlignmentRule, run_alignment_rule, DEFAULT_PERIODS"
        )
    else:
        import_line = (
            "from engine.rules.ma._alignment import AlignmentRule, run_alignment_rule, DEFAULT_PERIODS"
        )

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
    return run_alignment_rule({class_name}, df)
'''
    (ROOT / fname).write_text(content, encoding="utf-8")


def _write_crossover(rule_id, rule_name, base_cls, ma_type, fast, slow, direction) -> None:
    safe = rule_name.replace(" ", "")
    class_name = f"{rule_id}{safe}Rule"
    slug = rule_name.lower().replace(" ", "_")
    fname = f"{rule_id.lower()}_{slug}.py"
    if base_cls == "MultipleCrossoverRule":
        content = f'''"""{rule_id} — {rule_name}. TASS-015: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.ma._crossover import MultipleCrossoverRule, run_crossover_rule


class {class_name}(MultipleCrossoverRule):
    rule_id = "{rule_id}"
    rule_name = "{rule_name}"
    ma_type = "{ma_type}"
    pairs = ((5, 20), (20, 60), (60, 120))
    direction = "{direction}"
    min_crosses = 2


def evaluate_{rule_id.lower()}(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for {rule_id}."""
    return run_crossover_rule({class_name}, df)
'''
    else:
        content = f'''"""{rule_id} — {rule_name}. TASS-015: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.ma._crossover import CrossoverRule, run_crossover_rule


class {class_name}(CrossoverRule):
    rule_id = "{rule_id}"
    rule_name = "{rule_name}"
    ma_type = "{ma_type}"
    fast_period = {fast}
    slow_period = {slow}
    direction = "{direction}"


def evaluate_{rule_id.lower()}(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for {rule_id}."""
    return run_crossover_rule({class_name}, df)
'''
    (ROOT / fname).write_text(content, encoding="utf-8")


def main() -> None:
    for item in ALIGNMENT_RULES:
        _write_alignment(*item)
    for item in CROSSOVER_RULES:
        _write_crossover(*item)
    _write_crossover("MA0039", "Multiple Golden Cross", "MultipleCrossoverRule", "sma", 0, 0, "golden")
    _write_crossover("MA0040", "Multiple Death Cross", "MultipleCrossoverRule", "sma", 0, 0, "death")
    print("generated MA0022-MA0040")


if __name__ == "__main__":
    main()
