"""PT rule evaluator registry (auto-generated)."""

from __future__ import annotations

from collections.abc import Callable

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.pt.pt0001_bull_flag_formed import evaluate_pt0001
from engine.rules.pt.pt0002_bear_flag_formed import evaluate_pt0002
from engine.rules.pt.pt0003_bull_flag_active import evaluate_pt0003
from engine.rules.pt.pt0004_bear_flag_active import evaluate_pt0004
from engine.rules.pt.pt0005_bull_pennant_formed import evaluate_pt0005
from engine.rules.pt.pt0006_bear_pennant_formed import evaluate_pt0006
from engine.rules.pt.pt0007_bull_pennant_active import evaluate_pt0007
from engine.rules.pt.pt0008_bear_pennant_active import evaluate_pt0008
from engine.rules.pt.pt0009_rectangle_continuation_formed import evaluate_pt0009
from engine.rules.pt.pt0010_rectangle_continuation_active import evaluate_pt0010
from engine.rules.pt.pt0011_head_and_shoulders_formed import evaluate_pt0011
from engine.rules.pt.pt0012_inverse_head_and_shoulders_formed import evaluate_pt0012
from engine.rules.pt.pt0013_head_and_shoulders_active import evaluate_pt0013
from engine.rules.pt.pt0014_inverse_head_and_shoulders_active import evaluate_pt0014
from engine.rules.pt.pt0015_rounding_top_formed import evaluate_pt0015
from engine.rules.pt.pt0016_rounding_bottom_formed import evaluate_pt0016
from engine.rules.pt.pt0017_rounding_top_active import evaluate_pt0017
from engine.rules.pt.pt0018_rounding_bottom_active import evaluate_pt0018
from engine.rules.pt.pt0019_v_top_formed import evaluate_pt0019
from engine.rules.pt.pt0020_v_bottom_formed import evaluate_pt0020
from engine.rules.pt.pt0021_ascending_triangle_formed import evaluate_pt0021
from engine.rules.pt.pt0022_descending_triangle_formed import evaluate_pt0022
from engine.rules.pt.pt0023_symmetrical_triangle_formed import evaluate_pt0023
from engine.rules.pt.pt0024_ascending_triangle_active import evaluate_pt0024
from engine.rules.pt.pt0025_descending_triangle_active import evaluate_pt0025
from engine.rules.pt.pt0026_symmetrical_triangle_active import evaluate_pt0026
from engine.rules.pt.pt0027_triangle_upper_trendline_present import evaluate_pt0027
from engine.rules.pt.pt0028_triangle_lower_trendline_present import evaluate_pt0028
from engine.rules.pt.pt0029_triangle_apex_present import evaluate_pt0029
from engine.rules.pt.pt0030_triangle_boundaries_converging import evaluate_pt0030
from engine.rules.pt.pt0031_ascending_channel_formed import evaluate_pt0031
from engine.rules.pt.pt0032_descending_channel_formed import evaluate_pt0032
from engine.rules.pt.pt0033_horizontal_channel_formed import evaluate_pt0033
from engine.rules.pt.pt0034_rising_wedge_formed import evaluate_pt0034
from engine.rules.pt.pt0035_falling_wedge_formed import evaluate_pt0035
from engine.rules.pt.pt0036_ascending_channel_active import evaluate_pt0036
from engine.rules.pt.pt0037_descending_channel_active import evaluate_pt0037
from engine.rules.pt.pt0038_horizontal_channel_active import evaluate_pt0038
from engine.rules.pt.pt0039_rising_wedge_active import evaluate_pt0039
from engine.rules.pt.pt0040_falling_wedge_active import evaluate_pt0040
from engine.rules.pt.pt0041_double_top_formed import evaluate_pt0041
from engine.rules.pt.pt0042_double_bottom_formed import evaluate_pt0042
from engine.rules.pt.pt0043_double_top_active import evaluate_pt0043
from engine.rules.pt.pt0044_double_bottom_active import evaluate_pt0044
from engine.rules.pt.pt0045_double_top_peaks_equal import evaluate_pt0045
from engine.rules.pt.pt0046_double_bottom_troughs_equal import evaluate_pt0046
from engine.rules.pt.pt0047_double_top_neckline_present import evaluate_pt0047
from engine.rules.pt.pt0048_double_bottom_neckline_present import evaluate_pt0048
from engine.rules.pt.pt0049_double_top_first_peak_formed import evaluate_pt0049
from engine.rules.pt.pt0050_double_bottom_first_trough_formed import evaluate_pt0050
from engine.rules.pt.pt0051_pattern_upper_boundary_defined import evaluate_pt0051
from engine.rules.pt.pt0052_pattern_lower_boundary_defined import evaluate_pt0052
from engine.rules.pt.pt0053_pattern_boundaries_parallel import evaluate_pt0053
from engine.rules.pt.pt0054_pattern_boundaries_converging import evaluate_pt0054
from engine.rules.pt.pt0055_pattern_minimum_duration_met import evaluate_pt0055
from engine.rules.pt.pt0056_pattern_trendline_touches_met import evaluate_pt0056
from engine.rules.pt.pt0057_pattern_height_defined import evaluate_pt0057
from engine.rules.pt.pt0058_pattern_width_defined import evaluate_pt0058
from engine.rules.pt.pt0059_pattern_neckline_defined import evaluate_pt0059
from engine.rules.pt.pt0060_pattern_structure_complete import evaluate_pt0060

RuleEvaluator = Callable[[pd.DataFrame], RuleResult]

PT_EVALUATORS: dict[str, RuleEvaluator] = {
    "PT0001": evaluate_pt0001,
    "PT0002": evaluate_pt0002,
    "PT0003": evaluate_pt0003,
    "PT0004": evaluate_pt0004,
    "PT0005": evaluate_pt0005,
    "PT0006": evaluate_pt0006,
    "PT0007": evaluate_pt0007,
    "PT0008": evaluate_pt0008,
    "PT0009": evaluate_pt0009,
    "PT0010": evaluate_pt0010,
    "PT0011": evaluate_pt0011,
    "PT0012": evaluate_pt0012,
    "PT0013": evaluate_pt0013,
    "PT0014": evaluate_pt0014,
    "PT0015": evaluate_pt0015,
    "PT0016": evaluate_pt0016,
    "PT0017": evaluate_pt0017,
    "PT0018": evaluate_pt0018,
    "PT0019": evaluate_pt0019,
    "PT0020": evaluate_pt0020,
    "PT0021": evaluate_pt0021,
    "PT0022": evaluate_pt0022,
    "PT0023": evaluate_pt0023,
    "PT0024": evaluate_pt0024,
    "PT0025": evaluate_pt0025,
    "PT0026": evaluate_pt0026,
    "PT0027": evaluate_pt0027,
    "PT0028": evaluate_pt0028,
    "PT0029": evaluate_pt0029,
    "PT0030": evaluate_pt0030,
    "PT0031": evaluate_pt0031,
    "PT0032": evaluate_pt0032,
    "PT0033": evaluate_pt0033,
    "PT0034": evaluate_pt0034,
    "PT0035": evaluate_pt0035,
    "PT0036": evaluate_pt0036,
    "PT0037": evaluate_pt0037,
    "PT0038": evaluate_pt0038,
    "PT0039": evaluate_pt0039,
    "PT0040": evaluate_pt0040,
    "PT0041": evaluate_pt0041,
    "PT0042": evaluate_pt0042,
    "PT0043": evaluate_pt0043,
    "PT0044": evaluate_pt0044,
    "PT0045": evaluate_pt0045,
    "PT0046": evaluate_pt0046,
    "PT0047": evaluate_pt0047,
    "PT0048": evaluate_pt0048,
    "PT0049": evaluate_pt0049,
    "PT0050": evaluate_pt0050,
    "PT0051": evaluate_pt0051,
    "PT0052": evaluate_pt0052,
    "PT0053": evaluate_pt0053,
    "PT0054": evaluate_pt0054,
    "PT0055": evaluate_pt0055,
    "PT0056": evaluate_pt0056,
    "PT0057": evaluate_pt0057,
    "PT0058": evaluate_pt0058,
    "PT0059": evaluate_pt0059,
    "PT0060": evaluate_pt0060,
}


def get_pt_evaluator(rule_id: str) -> RuleEvaluator:
    """Return evaluator for PT rule ID."""
    return PT_EVALUATORS[rule_id]
