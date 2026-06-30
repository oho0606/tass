"""Generate VL0001–VL0060 rule files."""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent / "engine" / "rules" / "vl"

ABSOLUTE = [
    ("VL0001", "Volume Above N-Period Average", "above_avg"),
    ("VL0002", "Volume Below N-Period Average", "below_avg"),
    ("VL0003", "Volume Equal N-Period Average", "equal_avg"),
    ("VL0004", "Volume Above Prior Volume", "above_prior"),
    ("VL0005", "Volume Below Prior Volume", "below_prior"),
    ("VL0006", "Volume Equal Prior Volume", "equal_prior"),
    ("VL0007", "Volume Above N-Period High", "above_high"),
    ("VL0008", "Volume Below N-Period Low", "below_low"),
    ("VL0009", "Volume At N-Period High", "at_high"),
    ("VL0010", "Volume At N-Period Low", "at_low"),
]

RELATIVE = [
    ("VL0011", "Relative Volume Above 1", "RelativeVolumeRule", "above_1", None),
    ("VL0012", "Relative Volume Below 1", "RelativeVolumeRule", "below_1", None),
    ("VL0013", "Relative Volume Equal 1", "RelativeVolumeRule", "equal_1", None),
    ("VL0014", "Relative Volume Above 2", "RelativeVolumeRule", "above_2", None),
    ("VL0015", "Relative Volume Above Threshold", "RelativeVolumeRule", "above_threshold", None),
    ("VL0016", "Relative Volume Below Threshold", "RelativeVolumeRule", "below_threshold", None),
    ("VL0017", "Relative Volume Above Prior", "RelativeVolumeRule", "above_prior", None),
    ("VL0018", "Relative Volume Below Prior", "RelativeVolumeRule", "below_prior", None),
    ("VL0019", "Relative Volume At N-Period Average", "RelativeVolumeRule", "at_avg", None),
    ("VL0020", "Relative Volume At N-Period High", "RelativeVolumeRule", "at_high", None),
]

TREND = [
    ("VL0021", "Volume Rising", "VolumeDirectionRule", "rising"),
    ("VL0022", "Volume Falling", "VolumeDirectionRule", "falling"),
    ("VL0023", "Volume Slope Positive", "VolumeDirectionRule", "rising"),
    ("VL0024", "Volume Slope Negative", "VolumeDirectionRule", "falling"),
    ("VL0025", "Volume Slope Increasing", "VolumeSlopeTrendRule", "increasing"),
    ("VL0026", "Volume Slope Decreasing", "VolumeSlopeTrendRule", "decreasing"),
    ("VL0027", "Consecutive Higher Volume", "ConsecutiveVolumeRule", "higher"),
    ("VL0028", "Consecutive Lower Volume", "ConsecutiveVolumeRule", "lower"),
]

SPIKE = [
    ("VL0031", "Volume Spike", "VolumeSpikeRule", None),
    ("VL0032", "Volume Above Spike Threshold", "SpikeThresholdRule", None),
    ("VL0033", "Volume Sudden Increase", "SuddenVolumeChangeRule", "increase"),
    ("VL0034", "Volume Sudden Decrease", "SuddenVolumeChangeRule", "decrease"),
    ("VL0035", "Volume Expansion", "VolumeSpreadTrendRule", "expansion"),
    ("VL0036", "Volume Contraction", "VolumeSpreadTrendRule", "contraction"),
    ("VL0037", "Volume Climax", "VolumeClimaxRule", None),
    ("VL0038", "Volume Dry Up", "VolumeDryUpRule", None),
    ("VL0039", "Volume Spike Above Prior Spike", "SpikeCompareRule", "above_prior"),
    ("VL0040", "Volume Spike Below Prior Spike", "SpikeCompareRule", "below_prior"),
]

CONFIRMATION = [
    ("VL0041", "Up Bar Volume Above Average", "BarVolumeRule", "up_above_avg"),
    ("VL0042", "Down Bar Volume Above Average", "BarVolumeRule", "down_above_avg"),
    ("VL0043", "Up Bar Volume Below Average", "BarVolumeRule", "up_below_avg"),
    ("VL0044", "Down Bar Volume Below Average", "BarVolumeRule", "down_below_avg"),
    ("VL0045", "Up Bar Volume Above Prior Up Bar", "PriorSameBarVolumeRule", "up"),
    ("VL0046", "Down Bar Volume Above Prior Down Bar", "PriorSameBarVolumeRule", "down"),
    ("VL0047", "Price Up Volume Up", "PriceVolumeAgreementRule", "up_up"),
    ("VL0048", "Price Down Volume Up", "PriceVolumeAgreementRule", "down_up"),
    ("VL0049", "Price Up Volume Down", "PriceVolumeAgreementRule", "up_down"),
    ("VL0050", "Price Down Volume Down", "PriceVolumeAgreementRule", "down_down"),
]

QUALITY = [
    ("VL0051", "OBV Rising", "ObvDirectionRule", "rising"),
    ("VL0052", "OBV Falling", "ObvDirectionRule", "falling"),
    ("VL0053", "OBV Above Prior OBV", "ObvCompareRule", "above_prior"),
    ("VL0054", "OBV Below Prior OBV", "ObvCompareRule", "below_prior"),
    ("VL0055", "OBV Slope Increasing", "ObvSlopeTrendRule", "increasing"),
    ("VL0056", "OBV Slope Decreasing", "ObvSlopeTrendRule", "decreasing"),
    ("VL0057", "Money Flow Positive", "MoneyFlowRule", "positive"),
    ("VL0058", "Money Flow Negative", "MoneyFlowRule", "negative"),
]


def _write_absolute(rule_id: str, rule_name: str, mode: str) -> None:
    safe = rule_name.replace(" ", "").replace("-", "")
    class_name = f"{rule_id}{safe}Rule"
    slug = rule_name.lower().replace(" ", "_").replace("-", "_")
    content = f'''"""{rule_id} — {rule_name}. TASS-017: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.vl._absolute import AbsoluteVolumeRule, run_absolute_rule


class {class_name}(AbsoluteVolumeRule):
    rule_id = "{rule_id}"
    rule_name = "{rule_name}"
    mode = "{mode}"


def evaluate_{rule_id.lower()}(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for {rule_id}."""
    return run_absolute_rule({class_name}, df)
'''
    (ROOT / f"{rule_id.lower()}_{slug}.py").write_text(content, encoding="utf-8")


def _write_module_rule(
    rule_id: str,
    rule_name: str,
    module: str,
    base_cls: str,
    runner: str,
    body: str,
) -> None:
    safe = rule_name.replace(" ", "").replace("-", "")
    class_name = f"{rule_id}{safe}Rule"
    slug = rule_name.lower().replace(" ", "_").replace("-", "_")
    content = f'''"""{rule_id} — {rule_name}. TASS-017: One Rule · One Class · One File."""

from __future__ import annotations

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.vl.{module} import {base_cls}, {runner}


class {class_name}({base_cls}):
    rule_id = "{rule_id}"
    rule_name = "{rule_name}"
{body}

def evaluate_{rule_id.lower()}(df: pd.DataFrame) -> RuleResult:
    """Functional entry point for {rule_id}."""
    return {runner}({class_name}, df)
'''
    (ROOT / f"{rule_id.lower()}_{slug}.py").write_text(content, encoding="utf-8")


def main() -> None:
    ROOT.mkdir(parents=True, exist_ok=True)
    for rule_id, name, mode in ABSOLUTE:
        _write_absolute(rule_id, name, mode)
    for rule_id, name, base, mode, _ in RELATIVE:
        _write_module_rule(rule_id, name, "_relative", base, "run_relative_rule", f'    mode = "{mode}"')
    for rule_id, name, base, direction in TREND:
        field = "direction" if "Direction" in base else "mode" if "Consecutive" in base else "trend"
        _write_module_rule(rule_id, name, "_trend", base, "run_trend_rule", f'    {field} = "{direction}"')
    _write_module_rule("VL0029", "Volume Flat", "_trend", "VolumeFlatRule", "run_trend_rule", "")
    _write_module_rule("VL0030", "Volume Turning", "_trend", "VolumeTurningRule", "run_trend_rule", "")
    for rule_id, name, base, param in SPIKE:
        body = ""
        if param and base == "SuddenVolumeChangeRule":
            body = f'    direction = "{param}"'
        elif param and base == "VolumeSpreadTrendRule":
            body = f'    trend = "{param}"'
        elif param and base == "SpikeCompareRule":
            body = f'    comparison = "{param}"'
        _write_module_rule(rule_id, name, "_spike", base, "run_spike_rule", body)
    for rule_id, name, base, mode in CONFIRMATION:
        if base == "PriorSameBarVolumeRule":
            body = f'    bar_direction = "{mode}"'
        elif base == "PriceVolumeAgreementRule":
            body = f'    mode = "{mode}"'
        else:
            body = f'    mode = "{mode}"'
        _write_module_rule(rule_id, name, "_confirmation", base, "run_confirmation_rule", body)
    for rule_id, name, base, param in QUALITY:
        if base == "ObvDirectionRule":
            body = f'    direction = "{param}"'
        elif base == "ObvCompareRule":
            body = f'    comparison = "{param}"'
        elif base == "ObvSlopeTrendRule":
            body = f'    trend = "{param}"'
        else:
            body = f'    direction = "{param}"'
        _write_module_rule(rule_id, name, "_quality", base, "run_quality_rule", body)
    _write_module_rule(
        "VL0059",
        "Volume Structure Stable",
        "_quality",
        "VolumeStructureStableRule",
        "run_quality_rule",
        "",
    )
    _write_module_rule(
        "VL0060",
        "Volume Pattern Consistent",
        "_quality",
        "VolumePatternConsistentRule",
        "run_quality_rule",
        "",
    )
    print("generated VL0001-VL0060")


if __name__ == "__main__":
    main()
