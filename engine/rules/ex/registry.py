"""EX rule evaluator registry (auto-generated)."""

from __future__ import annotations

from collections.abc import Callable

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.ex.ex0001_exit_close_below_sma20 import evaluate_ex0001
from engine.rules.ex.ex0002_exit_close_below_sma60 import evaluate_ex0002
from engine.rules.ex.ex0003_exit_close_below_ema20 import evaluate_ex0003
from engine.rules.ex.ex0004_exit_close_below_ema60 import evaluate_ex0004
from engine.rules.ex.ex0005_exit_high_below_prior_bar_high import evaluate_ex0005
from engine.rules.ex.ex0006_exit_low_below_prior_bar_low import evaluate_ex0006
from engine.rules.ex.ex0007_exit_close_below_prior_close import evaluate_ex0007
from engine.rules.ex.ex0008_exit_close_below_n_period_high import evaluate_ex0008
from engine.rules.ex.ex0009_exit_open_above_exit_close import evaluate_ex0009
from engine.rules.ex.ex0010_exit_close_below_prior_bar_open import evaluate_ex0010
from engine.rules.ex.ex0011_exit_close_below_prior_swing_high import evaluate_ex0011
from engine.rules.ex.ex0012_exit_close_above_prior_swing_low import evaluate_ex0012
from engine.rules.ex.ex0013_exit_close_below_horizontal_resistance import evaluate_ex0013
from engine.rules.ex.ex0014_exit_close_above_horizontal_support import evaluate_ex0014
from engine.rules.ex.ex0015_exit_close_below_52_week_high import evaluate_ex0015
from engine.rules.ex.ex0016_exit_close_above_52_week_low import evaluate_ex0016
from engine.rules.ex.ex0017_exit_close_below_upper_bollinger_band import evaluate_ex0017
from engine.rules.ex.ex0018_exit_close_above_lower_bollinger_band import evaluate_ex0018
from engine.rules.ex.ex0019_exit_close_below_r1 import evaluate_ex0019
from engine.rules.ex.ex0020_exit_close_above_s1 import evaluate_ex0020
from engine.rules.ex.ex0021_exit_close_below_pullback_low import evaluate_ex0021
from engine.rules.ex.ex0022_exit_low_below_pullback_low import evaluate_ex0022
from engine.rules.ex.ex0023_exit_close_below_sma20_after_touch import evaluate_ex0023
from engine.rules.ex.ex0024_exit_close_below_ema20_after_touch import evaluate_ex0024
from engine.rules.ex.ex0025_exit_close_below_38_2_percent_retracement import evaluate_ex0025
from engine.rules.ex.ex0026_exit_close_below_50_percent_retracement import evaluate_ex0026
from engine.rules.ex.ex0027_exit_close_below_61_8_percent_retracement import evaluate_ex0027
from engine.rules.ex.ex0028_exit_bar_following_pullback_low import evaluate_ex0028
from engine.rules.ex.ex0029_exit_close_below_prior_pullback_high import evaluate_ex0029
from engine.rules.ex.ex0030_exit_low_at_pullback_support_level import evaluate_ex0030
from engine.rules.ex.ex0031_exit_close_below_prior_swing_low import evaluate_ex0031
from engine.rules.ex.ex0032_exit_close_above_prior_swing_high import evaluate_ex0032
from engine.rules.ex.ex0033_exit_low_at_n_period_low import evaluate_ex0033
from engine.rules.ex.ex0034_exit_high_at_n_period_high import evaluate_ex0034
from engine.rules.ex.ex0035_exit_close_below_support_level import evaluate_ex0035
from engine.rules.ex.ex0036_exit_close_above_resistance_level import evaluate_ex0036
from engine.rules.ex.ex0037_exit_close_below_reversal_bar_high import evaluate_ex0037
from engine.rules.ex.ex0038_exit_close_above_reversal_bar_low import evaluate_ex0038
from engine.rules.ex.ex0039_exit_close_below_double_bottom_level import evaluate_ex0039
from engine.rules.ex.ex0040_exit_close_above_double_top_level import evaluate_ex0040
from engine.rules.ex.ex0041_exit_bar_volume_below_n_period_average import evaluate_ex0041
from engine.rules.ex.ex0042_exit_bar_volume_above_n_period_average import evaluate_ex0042
from engine.rules.ex.ex0043_exit_bar_volume_below_prior_bar import evaluate_ex0043
from engine.rules.ex.ex0044_exit_bar_volume_above_prior_bar import evaluate_ex0044
from engine.rules.ex.ex0045_exit_bar_relative_volume_below_1 import evaluate_ex0045
from engine.rules.ex.ex0046_exit_bar_relative_volume_below_2 import evaluate_ex0046
from engine.rules.ex.ex0047_exit_bar_bearish import evaluate_ex0047
from engine.rules.ex.ex0048_exit_bar_bullish import evaluate_ex0048
from engine.rules.ex.ex0049_exit_bar_rsi_below_50 import evaluate_ex0049
from engine.rules.ex.ex0050_exit_bar_rsi_above_50 import evaluate_ex0050
from engine.rules.ex.ex0051_exit_bar_wide_range import evaluate_ex0051
from engine.rules.ex.ex0052_exit_bar_narrow_range import evaluate_ex0052
from engine.rules.ex.ex0053_exit_close_near_bar_low import evaluate_ex0053
from engine.rules.ex.ex0054_exit_close_near_bar_high import evaluate_ex0054
from engine.rules.ex.ex0055_exit_bar_body_below_half_range import evaluate_ex0055
from engine.rules.ex.ex0056_exit_bar_body_above_half_range import evaluate_ex0056
from engine.rules.ex.ex0057_exit_bar_overlapping_prior_bar import evaluate_ex0057
from engine.rules.ex.ex0058_exit_gap_down_at_exit_bar import evaluate_ex0058
from engine.rules.ex.ex0059_exit_gap_up_at_exit_bar import evaluate_ex0059
from engine.rules.ex.ex0060_exit_wick_rejection_at_resistance import evaluate_ex0060

RuleEvaluator = Callable[[pd.DataFrame], RuleResult]

EX_EVALUATORS: dict[str, RuleEvaluator] = {
    "EX0001": evaluate_ex0001,
    "EX0002": evaluate_ex0002,
    "EX0003": evaluate_ex0003,
    "EX0004": evaluate_ex0004,
    "EX0005": evaluate_ex0005,
    "EX0006": evaluate_ex0006,
    "EX0007": evaluate_ex0007,
    "EX0008": evaluate_ex0008,
    "EX0009": evaluate_ex0009,
    "EX0010": evaluate_ex0010,
    "EX0011": evaluate_ex0011,
    "EX0012": evaluate_ex0012,
    "EX0013": evaluate_ex0013,
    "EX0014": evaluate_ex0014,
    "EX0015": evaluate_ex0015,
    "EX0016": evaluate_ex0016,
    "EX0017": evaluate_ex0017,
    "EX0018": evaluate_ex0018,
    "EX0019": evaluate_ex0019,
    "EX0020": evaluate_ex0020,
    "EX0021": evaluate_ex0021,
    "EX0022": evaluate_ex0022,
    "EX0023": evaluate_ex0023,
    "EX0024": evaluate_ex0024,
    "EX0025": evaluate_ex0025,
    "EX0026": evaluate_ex0026,
    "EX0027": evaluate_ex0027,
    "EX0028": evaluate_ex0028,
    "EX0029": evaluate_ex0029,
    "EX0030": evaluate_ex0030,
    "EX0031": evaluate_ex0031,
    "EX0032": evaluate_ex0032,
    "EX0033": evaluate_ex0033,
    "EX0034": evaluate_ex0034,
    "EX0035": evaluate_ex0035,
    "EX0036": evaluate_ex0036,
    "EX0037": evaluate_ex0037,
    "EX0038": evaluate_ex0038,
    "EX0039": evaluate_ex0039,
    "EX0040": evaluate_ex0040,
    "EX0041": evaluate_ex0041,
    "EX0042": evaluate_ex0042,
    "EX0043": evaluate_ex0043,
    "EX0044": evaluate_ex0044,
    "EX0045": evaluate_ex0045,
    "EX0046": evaluate_ex0046,
    "EX0047": evaluate_ex0047,
    "EX0048": evaluate_ex0048,
    "EX0049": evaluate_ex0049,
    "EX0050": evaluate_ex0050,
    "EX0051": evaluate_ex0051,
    "EX0052": evaluate_ex0052,
    "EX0053": evaluate_ex0053,
    "EX0054": evaluate_ex0054,
    "EX0055": evaluate_ex0055,
    "EX0056": evaluate_ex0056,
    "EX0057": evaluate_ex0057,
    "EX0058": evaluate_ex0058,
    "EX0059": evaluate_ex0059,
    "EX0060": evaluate_ex0060,
}


def get_ex_evaluator(rule_id: str) -> RuleEvaluator:
    """Return evaluator for EX rule ID."""
    return EX_EVALUATORS[rule_id]
