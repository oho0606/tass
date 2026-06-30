"""VL rule evaluator registry."""

from __future__ import annotations

from collections.abc import Callable

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.vl.vl0001_volume_above_n_period_average import evaluate_vl0001
from engine.rules.vl.vl0002_volume_below_n_period_average import evaluate_vl0002
from engine.rules.vl.vl0003_volume_equal_n_period_average import evaluate_vl0003
from engine.rules.vl.vl0004_volume_above_prior_volume import evaluate_vl0004
from engine.rules.vl.vl0005_volume_below_prior_volume import evaluate_vl0005
from engine.rules.vl.vl0006_volume_equal_prior_volume import evaluate_vl0006
from engine.rules.vl.vl0007_volume_above_n_period_high import evaluate_vl0007
from engine.rules.vl.vl0008_volume_below_n_period_low import evaluate_vl0008
from engine.rules.vl.vl0009_volume_at_n_period_high import evaluate_vl0009
from engine.rules.vl.vl0010_volume_at_n_period_low import evaluate_vl0010
from engine.rules.vl.vl0011_relative_volume_above_1 import evaluate_vl0011
from engine.rules.vl.vl0012_relative_volume_below_1 import evaluate_vl0012
from engine.rules.vl.vl0013_relative_volume_equal_1 import evaluate_vl0013
from engine.rules.vl.vl0014_relative_volume_above_2 import evaluate_vl0014
from engine.rules.vl.vl0015_relative_volume_above_threshold import evaluate_vl0015
from engine.rules.vl.vl0016_relative_volume_below_threshold import evaluate_vl0016
from engine.rules.vl.vl0017_relative_volume_above_prior import evaluate_vl0017
from engine.rules.vl.vl0018_relative_volume_below_prior import evaluate_vl0018
from engine.rules.vl.vl0019_relative_volume_at_n_period_average import evaluate_vl0019
from engine.rules.vl.vl0020_relative_volume_at_n_period_high import evaluate_vl0020
from engine.rules.vl.vl0021_volume_rising import evaluate_vl0021
from engine.rules.vl.vl0022_volume_falling import evaluate_vl0022
from engine.rules.vl.vl0023_volume_slope_positive import evaluate_vl0023
from engine.rules.vl.vl0024_volume_slope_negative import evaluate_vl0024
from engine.rules.vl.vl0025_volume_slope_increasing import evaluate_vl0025
from engine.rules.vl.vl0026_volume_slope_decreasing import evaluate_vl0026
from engine.rules.vl.vl0027_consecutive_higher_volume import evaluate_vl0027
from engine.rules.vl.vl0028_consecutive_lower_volume import evaluate_vl0028
from engine.rules.vl.vl0029_volume_flat import evaluate_vl0029
from engine.rules.vl.vl0030_volume_turning import evaluate_vl0030
from engine.rules.vl.vl0031_volume_spike import evaluate_vl0031
from engine.rules.vl.vl0032_volume_above_spike_threshold import evaluate_vl0032
from engine.rules.vl.vl0033_volume_sudden_increase import evaluate_vl0033
from engine.rules.vl.vl0034_volume_sudden_decrease import evaluate_vl0034
from engine.rules.vl.vl0035_volume_expansion import evaluate_vl0035
from engine.rules.vl.vl0036_volume_contraction import evaluate_vl0036
from engine.rules.vl.vl0037_volume_climax import evaluate_vl0037
from engine.rules.vl.vl0038_volume_dry_up import evaluate_vl0038
from engine.rules.vl.vl0039_volume_spike_above_prior_spike import evaluate_vl0039
from engine.rules.vl.vl0040_volume_spike_below_prior_spike import evaluate_vl0040
from engine.rules.vl.vl0041_up_bar_volume_above_average import evaluate_vl0041
from engine.rules.vl.vl0042_down_bar_volume_above_average import evaluate_vl0042
from engine.rules.vl.vl0043_up_bar_volume_below_average import evaluate_vl0043
from engine.rules.vl.vl0044_down_bar_volume_below_average import evaluate_vl0044
from engine.rules.vl.vl0045_up_bar_volume_above_prior_up_bar import evaluate_vl0045
from engine.rules.vl.vl0046_down_bar_volume_above_prior_down_bar import evaluate_vl0046
from engine.rules.vl.vl0047_price_up_volume_up import evaluate_vl0047
from engine.rules.vl.vl0048_price_down_volume_up import evaluate_vl0048
from engine.rules.vl.vl0049_price_up_volume_down import evaluate_vl0049
from engine.rules.vl.vl0050_price_down_volume_down import evaluate_vl0050
from engine.rules.vl.vl0051_obv_rising import evaluate_vl0051
from engine.rules.vl.vl0052_obv_falling import evaluate_vl0052
from engine.rules.vl.vl0053_obv_above_prior_obv import evaluate_vl0053
from engine.rules.vl.vl0054_obv_below_prior_obv import evaluate_vl0054
from engine.rules.vl.vl0055_obv_slope_increasing import evaluate_vl0055
from engine.rules.vl.vl0056_obv_slope_decreasing import evaluate_vl0056
from engine.rules.vl.vl0057_money_flow_positive import evaluate_vl0057
from engine.rules.vl.vl0058_money_flow_negative import evaluate_vl0058
from engine.rules.vl.vl0059_volume_structure_stable import evaluate_vl0059
from engine.rules.vl.vl0060_volume_pattern_consistent import evaluate_vl0060

RuleEvaluator = Callable[[pd.DataFrame], RuleResult]

VL_EVALUATORS: dict[str, RuleEvaluator] = {
    "VL0001": evaluate_vl0001,
    "VL0002": evaluate_vl0002,
    "VL0003": evaluate_vl0003,
    "VL0004": evaluate_vl0004,
    "VL0005": evaluate_vl0005,
    "VL0006": evaluate_vl0006,
    "VL0007": evaluate_vl0007,
    "VL0008": evaluate_vl0008,
    "VL0009": evaluate_vl0009,
    "VL0010": evaluate_vl0010,
    "VL0011": evaluate_vl0011,
    "VL0012": evaluate_vl0012,
    "VL0013": evaluate_vl0013,
    "VL0014": evaluate_vl0014,
    "VL0015": evaluate_vl0015,
    "VL0016": evaluate_vl0016,
    "VL0017": evaluate_vl0017,
    "VL0018": evaluate_vl0018,
    "VL0019": evaluate_vl0019,
    "VL0020": evaluate_vl0020,
    "VL0021": evaluate_vl0021,
    "VL0022": evaluate_vl0022,
    "VL0023": evaluate_vl0023,
    "VL0024": evaluate_vl0024,
    "VL0025": evaluate_vl0025,
    "VL0026": evaluate_vl0026,
    "VL0027": evaluate_vl0027,
    "VL0028": evaluate_vl0028,
    "VL0029": evaluate_vl0029,
    "VL0030": evaluate_vl0030,
    "VL0031": evaluate_vl0031,
    "VL0032": evaluate_vl0032,
    "VL0033": evaluate_vl0033,
    "VL0034": evaluate_vl0034,
    "VL0035": evaluate_vl0035,
    "VL0036": evaluate_vl0036,
    "VL0037": evaluate_vl0037,
    "VL0038": evaluate_vl0038,
    "VL0039": evaluate_vl0039,
    "VL0040": evaluate_vl0040,
    "VL0041": evaluate_vl0041,
    "VL0042": evaluate_vl0042,
    "VL0043": evaluate_vl0043,
    "VL0044": evaluate_vl0044,
    "VL0045": evaluate_vl0045,
    "VL0046": evaluate_vl0046,
    "VL0047": evaluate_vl0047,
    "VL0048": evaluate_vl0048,
    "VL0049": evaluate_vl0049,
    "VL0050": evaluate_vl0050,
    "VL0051": evaluate_vl0051,
    "VL0052": evaluate_vl0052,
    "VL0053": evaluate_vl0053,
    "VL0054": evaluate_vl0054,
    "VL0055": evaluate_vl0055,
    "VL0056": evaluate_vl0056,
    "VL0057": evaluate_vl0057,
    "VL0058": evaluate_vl0058,
    "VL0059": evaluate_vl0059,
    "VL0060": evaluate_vl0060,
}

VL_ENGINE_RULES: tuple[str, ...] = (
    "VL0001",
    "VL0004",
    "VL0021",
    "VL0041",
    "VL0027",
    "VL0059",
)

VL_ENGINE_WEIGHTS: dict[str, float] = {
    "VL0001": 1.2,
    "VL0004": 1.0,
    "VL0021": 1.1,
    "VL0041": 1.2,
    "VL0027": 1.1,
    "VL0059": 1.0,
}


def get_vl_evaluator(rule_id: str) -> RuleEvaluator:
    """Return evaluator for VL rule ID."""
    return VL_EVALUATORS[rule_id]
