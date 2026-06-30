"""EN rule evaluator registry (auto-generated)."""

from __future__ import annotations

from collections.abc import Callable

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.en.en0001_entry_close_above_sma20 import evaluate_en0001
from engine.rules.en.en0002_entry_close_above_sma60 import evaluate_en0002
from engine.rules.en.en0003_entry_close_above_ema20 import evaluate_en0003
from engine.rules.en.en0004_entry_close_above_ema60 import evaluate_en0004
from engine.rules.en.en0005_entry_high_above_prior_bar_high import evaluate_en0005
from engine.rules.en.en0006_entry_low_above_prior_bar_low import evaluate_en0006
from engine.rules.en.en0007_entry_close_above_prior_close import evaluate_en0007
from engine.rules.en.en0008_entry_close_above_n_period_high import evaluate_en0008
from engine.rules.en.en0009_entry_open_below_entry_close import evaluate_en0009
from engine.rules.en.en0010_entry_close_above_prior_bar_open import evaluate_en0010
from engine.rules.en.en0011_entry_close_above_prior_swing_high import evaluate_en0011
from engine.rules.en.en0012_entry_close_below_prior_swing_low import evaluate_en0012
from engine.rules.en.en0013_entry_close_above_horizontal_resistance import evaluate_en0013
from engine.rules.en.en0014_entry_close_below_horizontal_support import evaluate_en0014
from engine.rules.en.en0015_entry_close_above_52_week_high import evaluate_en0015
from engine.rules.en.en0016_entry_close_below_52_week_low import evaluate_en0016
from engine.rules.en.en0017_entry_close_above_upper_bollinger_band import evaluate_en0017
from engine.rules.en.en0018_entry_close_below_lower_bollinger_band import evaluate_en0018
from engine.rules.en.en0019_entry_close_above_r1 import evaluate_en0019
from engine.rules.en.en0020_entry_close_below_s1 import evaluate_en0020
from engine.rules.en.en0021_entry_close_above_pullback_low import evaluate_en0021
from engine.rules.en.en0022_entry_low_above_pullback_low import evaluate_en0022
from engine.rules.en.en0023_entry_close_above_sma20_after_touch import evaluate_en0023
from engine.rules.en.en0024_entry_close_above_ema20_after_touch import evaluate_en0024
from engine.rules.en.en0025_entry_close_above_38_2_percent_retracement import evaluate_en0025
from engine.rules.en.en0026_entry_close_above_50_percent_retracement import evaluate_en0026
from engine.rules.en.en0027_entry_close_above_61_8_percent_retracement import evaluate_en0027
from engine.rules.en.en0028_entry_bar_following_pullback_low import evaluate_en0028
from engine.rules.en.en0029_entry_close_above_prior_pullback_high import evaluate_en0029
from engine.rules.en.en0030_entry_low_at_pullback_support_level import evaluate_en0030
from engine.rules.en.en0031_entry_close_above_prior_swing_low import evaluate_en0031
from engine.rules.en.en0032_entry_close_below_prior_swing_high import evaluate_en0032
from engine.rules.en.en0033_entry_low_at_n_period_low import evaluate_en0033
from engine.rules.en.en0034_entry_high_at_n_period_high import evaluate_en0034
from engine.rules.en.en0035_entry_close_above_support_level import evaluate_en0035
from engine.rules.en.en0036_entry_close_below_resistance_level import evaluate_en0036
from engine.rules.en.en0037_entry_close_above_reversal_bar_high import evaluate_en0037
from engine.rules.en.en0038_entry_close_below_reversal_bar_low import evaluate_en0038
from engine.rules.en.en0039_entry_close_above_double_bottom_level import evaluate_en0039
from engine.rules.en.en0040_entry_close_below_double_top_level import evaluate_en0040
from engine.rules.en.en0041_entry_bar_volume_above_n_period_average import evaluate_en0041
from engine.rules.en.en0042_entry_bar_volume_below_n_period_average import evaluate_en0042
from engine.rules.en.en0043_entry_bar_volume_above_prior_bar import evaluate_en0043
from engine.rules.en.en0044_entry_bar_volume_below_prior_bar import evaluate_en0044
from engine.rules.en.en0045_entry_bar_relative_volume_above_1 import evaluate_en0045
from engine.rules.en.en0046_entry_bar_relative_volume_above_2 import evaluate_en0046
from engine.rules.en.en0047_entry_bar_bullish import evaluate_en0047
from engine.rules.en.en0048_entry_bar_bearish import evaluate_en0048
from engine.rules.en.en0049_entry_bar_rsi_above_50 import evaluate_en0049
from engine.rules.en.en0050_entry_bar_rsi_below_50 import evaluate_en0050
from engine.rules.en.en0051_entry_bar_wide_range import evaluate_en0051
from engine.rules.en.en0052_entry_bar_narrow_range import evaluate_en0052
from engine.rules.en.en0053_entry_close_near_bar_high import evaluate_en0053
from engine.rules.en.en0054_entry_close_near_bar_low import evaluate_en0054
from engine.rules.en.en0055_entry_bar_body_above_half_range import evaluate_en0055
from engine.rules.en.en0056_entry_bar_body_below_half_range import evaluate_en0056
from engine.rules.en.en0057_entry_bar_overlapping_prior_bar import evaluate_en0057
from engine.rules.en.en0058_entry_gap_up_at_entry_bar import evaluate_en0058
from engine.rules.en.en0059_entry_gap_down_at_entry_bar import evaluate_en0059
from engine.rules.en.en0060_entry_wick_rejection_at_support import evaluate_en0060

RuleEvaluator = Callable[[pd.DataFrame], RuleResult]

EN_EVALUATORS: dict[str, RuleEvaluator] = {
    "EN0001": evaluate_en0001,
    "EN0002": evaluate_en0002,
    "EN0003": evaluate_en0003,
    "EN0004": evaluate_en0004,
    "EN0005": evaluate_en0005,
    "EN0006": evaluate_en0006,
    "EN0007": evaluate_en0007,
    "EN0008": evaluate_en0008,
    "EN0009": evaluate_en0009,
    "EN0010": evaluate_en0010,
    "EN0011": evaluate_en0011,
    "EN0012": evaluate_en0012,
    "EN0013": evaluate_en0013,
    "EN0014": evaluate_en0014,
    "EN0015": evaluate_en0015,
    "EN0016": evaluate_en0016,
    "EN0017": evaluate_en0017,
    "EN0018": evaluate_en0018,
    "EN0019": evaluate_en0019,
    "EN0020": evaluate_en0020,
    "EN0021": evaluate_en0021,
    "EN0022": evaluate_en0022,
    "EN0023": evaluate_en0023,
    "EN0024": evaluate_en0024,
    "EN0025": evaluate_en0025,
    "EN0026": evaluate_en0026,
    "EN0027": evaluate_en0027,
    "EN0028": evaluate_en0028,
    "EN0029": evaluate_en0029,
    "EN0030": evaluate_en0030,
    "EN0031": evaluate_en0031,
    "EN0032": evaluate_en0032,
    "EN0033": evaluate_en0033,
    "EN0034": evaluate_en0034,
    "EN0035": evaluate_en0035,
    "EN0036": evaluate_en0036,
    "EN0037": evaluate_en0037,
    "EN0038": evaluate_en0038,
    "EN0039": evaluate_en0039,
    "EN0040": evaluate_en0040,
    "EN0041": evaluate_en0041,
    "EN0042": evaluate_en0042,
    "EN0043": evaluate_en0043,
    "EN0044": evaluate_en0044,
    "EN0045": evaluate_en0045,
    "EN0046": evaluate_en0046,
    "EN0047": evaluate_en0047,
    "EN0048": evaluate_en0048,
    "EN0049": evaluate_en0049,
    "EN0050": evaluate_en0050,
    "EN0051": evaluate_en0051,
    "EN0052": evaluate_en0052,
    "EN0053": evaluate_en0053,
    "EN0054": evaluate_en0054,
    "EN0055": evaluate_en0055,
    "EN0056": evaluate_en0056,
    "EN0057": evaluate_en0057,
    "EN0058": evaluate_en0058,
    "EN0059": evaluate_en0059,
    "EN0060": evaluate_en0060,
}


def get_en_evaluator(rule_id: str) -> RuleEvaluator:
    """Return evaluator for EN rule ID."""
    return EN_EVALUATORS[rule_id]
