"""PA rule evaluator registry (auto-generated)."""

from __future__ import annotations

from collections.abc import Callable

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.pa.pa0001_pa0060 import evaluate_pa0001
from engine.rules.pa.pa0002_current_high_below_prior_high import evaluate_pa0002
from engine.rules.pa.pa0003_current_high_equal_prior_high import evaluate_pa0003
from engine.rules.pa.pa0004_current_low_above_prior_low import evaluate_pa0004
from engine.rules.pa.pa0005_current_low_below_prior_low import evaluate_pa0005
from engine.rules.pa.pa0006_current_low_equal_prior_low import evaluate_pa0006
from engine.rules.pa.pa0007_current_high_above_n_period_high import evaluate_pa0007
from engine.rules.pa.pa0008_current_low_below_n_period_low import evaluate_pa0008
from engine.rules.pa.pa0009_current_high_at_n_period_high import evaluate_pa0009
from engine.rules.pa.pa0010_current_low_at_n_period_low import evaluate_pa0010
from engine.rules.pa.pa0011_bullish_candle import evaluate_pa0011
from engine.rules.pa.pa0012_bearish_candle import evaluate_pa0012
from engine.rules.pa.pa0013_doji_candle import evaluate_pa0013
from engine.rules.pa.pa0014_long_body_candle import evaluate_pa0014
from engine.rules.pa.pa0015_short_body_candle import evaluate_pa0015
from engine.rules.pa.pa0016_body_larger_than_prior_body import evaluate_pa0016
from engine.rules.pa.pa0017_body_smaller_than_prior_body import evaluate_pa0017
from engine.rules.pa.pa0018_body_above_half_range import evaluate_pa0018
from engine.rules.pa.pa0019_body_below_half_range import evaluate_pa0019
from engine.rules.pa.pa0020_marubozu_body import evaluate_pa0020
from engine.rules.pa.pa0021_long_upper_wick import evaluate_pa0021
from engine.rules.pa.pa0022_long_lower_wick import evaluate_pa0022
from engine.rules.pa.pa0023_short_upper_wick import evaluate_pa0023
from engine.rules.pa.pa0024_short_lower_wick import evaluate_pa0024
from engine.rules.pa.pa0025_upper_wick_larger_than_body import evaluate_pa0025
from engine.rules.pa.pa0026_lower_wick_larger_than_body import evaluate_pa0026
from engine.rules.pa.pa0027_upper_wick_larger_than_prior_wick import evaluate_pa0027
from engine.rules.pa.pa0028_lower_wick_larger_than_prior_wick import evaluate_pa0028
from engine.rules.pa.pa0029_no_upper_wick import evaluate_pa0029
from engine.rules.pa.pa0030_no_lower_wick import evaluate_pa0030
from engine.rules.pa.pa0031_wide_range_bar import evaluate_pa0031
from engine.rules.pa.pa0032_narrow_range_bar import evaluate_pa0032
from engine.rules.pa.pa0033_range_larger_than_prior_range import evaluate_pa0033
from engine.rules.pa.pa0034_range_smaller_than_prior_range import evaluate_pa0034
from engine.rules.pa.pa0035_inside_bar import evaluate_pa0035
from engine.rules.pa.pa0036_outside_bar import evaluate_pa0036
from engine.rules.pa.pa0037_range_above_n_period_average import evaluate_pa0037
from engine.rules.pa.pa0038_range_below_n_period_average import evaluate_pa0038
from engine.rules.pa.pa0039_range_expanding import evaluate_pa0039
from engine.rules.pa.pa0040_range_contracting import evaluate_pa0040
from engine.rules.pa.pa0041_swing_high_formed import evaluate_pa0041
from engine.rules.pa.pa0042_swing_low_formed import evaluate_pa0042
from engine.rules.pa.pa0043_higher_swing_high import evaluate_pa0043
from engine.rules.pa.pa0044_lower_swing_high import evaluate_pa0044
from engine.rules.pa.pa0045_higher_swing_low import evaluate_pa0045
from engine.rules.pa.pa0046_lower_swing_low import evaluate_pa0046
from engine.rules.pa.pa0047_equal_swing_highs import evaluate_pa0047
from engine.rules.pa.pa0048_equal_swing_lows import evaluate_pa0048
from engine.rules.pa.pa0049_price_above_last_swing_high import evaluate_pa0049
from engine.rules.pa.pa0050_price_below_last_swing_low import evaluate_pa0050
from engine.rules.pa.pa0051_strong_close import evaluate_pa0051
from engine.rules.pa.pa0052_weak_close import evaluate_pa0052
from engine.rules.pa.pa0053_close_near_high import evaluate_pa0053
from engine.rules.pa.pa0054_close_near_low import evaluate_pa0054
from engine.rules.pa.pa0055_close_above_midpoint import evaluate_pa0055
from engine.rules.pa.pa0056_close_below_midpoint import evaluate_pa0056
from engine.rules.pa.pa0057_close_above_prior_close import evaluate_pa0057
from engine.rules.pa.pa0058_close_below_prior_close import evaluate_pa0058
from engine.rules.pa.pa0059_close_at_period_high import evaluate_pa0059
from engine.rules.pa.pa0060_close_at_period_low import evaluate_pa0060

RuleEvaluator = Callable[[pd.DataFrame], RuleResult]

PA_EVALUATORS: dict[str, RuleEvaluator] = {
    "PA0001": evaluate_pa0001,
    "PA0002": evaluate_pa0002,
    "PA0003": evaluate_pa0003,
    "PA0004": evaluate_pa0004,
    "PA0005": evaluate_pa0005,
    "PA0006": evaluate_pa0006,
    "PA0007": evaluate_pa0007,
    "PA0008": evaluate_pa0008,
    "PA0009": evaluate_pa0009,
    "PA0010": evaluate_pa0010,
    "PA0011": evaluate_pa0011,
    "PA0012": evaluate_pa0012,
    "PA0013": evaluate_pa0013,
    "PA0014": evaluate_pa0014,
    "PA0015": evaluate_pa0015,
    "PA0016": evaluate_pa0016,
    "PA0017": evaluate_pa0017,
    "PA0018": evaluate_pa0018,
    "PA0019": evaluate_pa0019,
    "PA0020": evaluate_pa0020,
    "PA0021": evaluate_pa0021,
    "PA0022": evaluate_pa0022,
    "PA0023": evaluate_pa0023,
    "PA0024": evaluate_pa0024,
    "PA0025": evaluate_pa0025,
    "PA0026": evaluate_pa0026,
    "PA0027": evaluate_pa0027,
    "PA0028": evaluate_pa0028,
    "PA0029": evaluate_pa0029,
    "PA0030": evaluate_pa0030,
    "PA0031": evaluate_pa0031,
    "PA0032": evaluate_pa0032,
    "PA0033": evaluate_pa0033,
    "PA0034": evaluate_pa0034,
    "PA0035": evaluate_pa0035,
    "PA0036": evaluate_pa0036,
    "PA0037": evaluate_pa0037,
    "PA0038": evaluate_pa0038,
    "PA0039": evaluate_pa0039,
    "PA0040": evaluate_pa0040,
    "PA0041": evaluate_pa0041,
    "PA0042": evaluate_pa0042,
    "PA0043": evaluate_pa0043,
    "PA0044": evaluate_pa0044,
    "PA0045": evaluate_pa0045,
    "PA0046": evaluate_pa0046,
    "PA0047": evaluate_pa0047,
    "PA0048": evaluate_pa0048,
    "PA0049": evaluate_pa0049,
    "PA0050": evaluate_pa0050,
    "PA0051": evaluate_pa0051,
    "PA0052": evaluate_pa0052,
    "PA0053": evaluate_pa0053,
    "PA0054": evaluate_pa0054,
    "PA0055": evaluate_pa0055,
    "PA0056": evaluate_pa0056,
    "PA0057": evaluate_pa0057,
    "PA0058": evaluate_pa0058,
    "PA0059": evaluate_pa0059,
    "PA0060": evaluate_pa0060,
}


def get_pa_evaluator(rule_id: str) -> RuleEvaluator:
    """Return evaluator for PA rule ID."""
    return PA_EVALUATORS[rule_id]
