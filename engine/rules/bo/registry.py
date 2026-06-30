"""BO rule evaluator registry (auto-generated)."""

from __future__ import annotations

from collections.abc import Callable

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.bo.bo0001_close_above_n_period_high import evaluate_bo0001
from engine.rules.bo.bo0002_close_below_n_period_low import evaluate_bo0002
from engine.rules.bo.bo0003_high_above_n_period_high import evaluate_bo0003
from engine.rules.bo.bo0004_low_below_n_period_low import evaluate_bo0004
from engine.rules.bo.bo0005_open_above_n_period_high import evaluate_bo0005
from engine.rules.bo.bo0006_open_below_n_period_low import evaluate_bo0006
from engine.rules.bo.bo0007_close_above_prior_high import evaluate_bo0007
from engine.rules.bo.bo0008_close_below_prior_low import evaluate_bo0008
from engine.rules.bo.bo0009_price_above_52_week_high import evaluate_bo0009
from engine.rules.bo.bo0010_price_below_52_week_low import evaluate_bo0010
from engine.rules.bo.bo0011_breakout_bar_volume_above_n_period_average import evaluate_bo0011
from engine.rules.bo.bo0012_breakout_bar_volume_below_n_period_average import evaluate_bo0012
from engine.rules.bo.bo0013_breakout_bar_volume_above_prior_volume import evaluate_bo0013
from engine.rules.bo.bo0014_breakout_bar_volume_below_prior_volume import evaluate_bo0014
from engine.rules.bo.bo0015_breakout_bar_volume_above_n_period_high import evaluate_bo0015
from engine.rules.bo.bo0016_breakout_bar_volume_at_n_period_high import evaluate_bo0016
from engine.rules.bo.bo0017_breakout_bar_relative_volume_above_1 import evaluate_bo0017
from engine.rules.bo.bo0018_breakout_bar_relative_volume_above_2 import evaluate_bo0018
from engine.rules.bo.bo0019_breakout_bar_volume_spike import evaluate_bo0019
from engine.rules.bo.bo0020_breakout_bar_volume_rising import evaluate_bo0020
from engine.rules.bo.bo0021_close_cross_above_sma5 import evaluate_bo0021
from engine.rules.bo.bo0022_close_cross_below_sma5 import evaluate_bo0022
from engine.rules.bo.bo0023_close_cross_above_sma20 import evaluate_bo0023
from engine.rules.bo.bo0024_close_cross_below_sma20 import evaluate_bo0024
from engine.rules.bo.bo0025_close_cross_above_sma60 import evaluate_bo0025
from engine.rules.bo.bo0026_close_cross_below_sma60 import evaluate_bo0026
from engine.rules.bo.bo0027_close_cross_above_ema20 import evaluate_bo0027
from engine.rules.bo.bo0028_close_cross_below_ema20 import evaluate_bo0028
from engine.rules.bo.bo0029_close_cross_above_ema60 import evaluate_bo0029
from engine.rules.bo.bo0030_close_cross_below_ema60 import evaluate_bo0030
from engine.rules.bo.bo0031_breakout_bar_true_range_above_n_period_average import evaluate_bo0031
from engine.rules.bo.bo0032_breakout_bar_true_range_above_n_period_high import evaluate_bo0032
from engine.rules.bo.bo0033_breakout_bar_atr_above_n_period_average import evaluate_bo0033
from engine.rules.bo.bo0034_breakout_bar_atr_above_prior_atr import evaluate_bo0034
from engine.rules.bo.bo0035_price_above_upper_bollinger_band import evaluate_bo0035
from engine.rules.bo.bo0036_price_below_lower_bollinger_band import evaluate_bo0036
from engine.rules.bo.bo0037_breakout_bar_bollinger_band_width_expanding import evaluate_bo0037
from engine.rules.bo.bo0038_breakout_bar_volatility_expanding import evaluate_bo0038
from engine.rules.bo.bo0039_breakout_bar_historical_volatility_above_n_period_average import evaluate_bo0039
from engine.rules.bo.bo0040_breakout_bar_bollinger_band_width_at_n_period_high import evaluate_bo0040
from engine.rules.bo.bo0041_close_above_horizontal_resistance import evaluate_bo0041
from engine.rules.bo.bo0042_close_below_horizontal_support import evaluate_bo0042
from engine.rules.bo.bo0043_high_above_horizontal_resistance import evaluate_bo0043
from engine.rules.bo.bo0044_low_below_horizontal_support import evaluate_bo0044
from engine.rules.bo.bo0045_close_above_prior_swing_high import evaluate_bo0045
from engine.rules.bo.bo0046_close_below_prior_swing_low import evaluate_bo0046
from engine.rules.bo.bo0047_close_above_trendline_resistance import evaluate_bo0047
from engine.rules.bo.bo0048_close_below_trendline_support import evaluate_bo0048
from engine.rules.bo.bo0049_close_above_r1 import evaluate_bo0049
from engine.rules.bo.bo0050_close_below_s1 import evaluate_bo0050
from engine.rules.bo.bo0051_breakout_bar_bullish import evaluate_bo0051
from engine.rules.bo.bo0052_breakout_bar_bearish import evaluate_bo0052
from engine.rules.bo.bo0053_breakout_bar_wide_range import evaluate_bo0053
from engine.rules.bo.bo0054_breakout_bar_narrow_range import evaluate_bo0054
from engine.rules.bo.bo0055_breakout_close_near_high import evaluate_bo0055
from engine.rules.bo.bo0056_breakout_close_near_low import evaluate_bo0056
from engine.rules.bo.bo0057_breakout_body_above_half_range import evaluate_bo0057
from engine.rules.bo.bo0058_breakout_body_below_half_range import evaluate_bo0058
from engine.rules.bo.bo0059_breakout_gap_up import evaluate_bo0059
from engine.rules.bo.bo0060_breakout_gap_down import evaluate_bo0060

RuleEvaluator = Callable[[pd.DataFrame], RuleResult]

BO_EVALUATORS: dict[str, RuleEvaluator] = {
    "BO0001": evaluate_bo0001,
    "BO0002": evaluate_bo0002,
    "BO0003": evaluate_bo0003,
    "BO0004": evaluate_bo0004,
    "BO0005": evaluate_bo0005,
    "BO0006": evaluate_bo0006,
    "BO0007": evaluate_bo0007,
    "BO0008": evaluate_bo0008,
    "BO0009": evaluate_bo0009,
    "BO0010": evaluate_bo0010,
    "BO0011": evaluate_bo0011,
    "BO0012": evaluate_bo0012,
    "BO0013": evaluate_bo0013,
    "BO0014": evaluate_bo0014,
    "BO0015": evaluate_bo0015,
    "BO0016": evaluate_bo0016,
    "BO0017": evaluate_bo0017,
    "BO0018": evaluate_bo0018,
    "BO0019": evaluate_bo0019,
    "BO0020": evaluate_bo0020,
    "BO0021": evaluate_bo0021,
    "BO0022": evaluate_bo0022,
    "BO0023": evaluate_bo0023,
    "BO0024": evaluate_bo0024,
    "BO0025": evaluate_bo0025,
    "BO0026": evaluate_bo0026,
    "BO0027": evaluate_bo0027,
    "BO0028": evaluate_bo0028,
    "BO0029": evaluate_bo0029,
    "BO0030": evaluate_bo0030,
    "BO0031": evaluate_bo0031,
    "BO0032": evaluate_bo0032,
    "BO0033": evaluate_bo0033,
    "BO0034": evaluate_bo0034,
    "BO0035": evaluate_bo0035,
    "BO0036": evaluate_bo0036,
    "BO0037": evaluate_bo0037,
    "BO0038": evaluate_bo0038,
    "BO0039": evaluate_bo0039,
    "BO0040": evaluate_bo0040,
    "BO0041": evaluate_bo0041,
    "BO0042": evaluate_bo0042,
    "BO0043": evaluate_bo0043,
    "BO0044": evaluate_bo0044,
    "BO0045": evaluate_bo0045,
    "BO0046": evaluate_bo0046,
    "BO0047": evaluate_bo0047,
    "BO0048": evaluate_bo0048,
    "BO0049": evaluate_bo0049,
    "BO0050": evaluate_bo0050,
    "BO0051": evaluate_bo0051,
    "BO0052": evaluate_bo0052,
    "BO0053": evaluate_bo0053,
    "BO0054": evaluate_bo0054,
    "BO0055": evaluate_bo0055,
    "BO0056": evaluate_bo0056,
    "BO0057": evaluate_bo0057,
    "BO0058": evaluate_bo0058,
    "BO0059": evaluate_bo0059,
    "BO0060": evaluate_bo0060,
}


def get_bo_evaluator(rule_id: str) -> RuleEvaluator:
    """Return evaluator for BO rule ID."""
    return BO_EVALUATORS[rule_id]
