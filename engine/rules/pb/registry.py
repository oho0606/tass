"""PB rule evaluator registry (auto-generated)."""

from __future__ import annotations

from collections.abc import Callable

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.pb.pb0001_pullback_in_progress import evaluate_pb0001
from engine.rules.pb.pb0002_retracement_below_38_2_percent import evaluate_pb0002
from engine.rules.pb.pb0003_retracement_between_38_2_and_50_percent import evaluate_pb0003
from engine.rules.pb.pb0004_retracement_between_50_and_61_8_percent import evaluate_pb0004
from engine.rules.pb.pb0005_pullback_low_above_prior_swing_low import evaluate_pb0005
from engine.rules.pb.pb0006_pullback_high_below_prior_swing_high import evaluate_pb0006
from engine.rules.pb.pb0007_pullback_duration_fewer_than_n_bars import evaluate_pb0007
from engine.rules.pb.pb0008_pullback_range_narrower_than_prior_leg import evaluate_pb0008
from engine.rules.pb.pb0009_pullback_close_above_prior_leg_midpoint import evaluate_pb0009
from engine.rules.pb.pb0010_pullback_bar_count_fewer_than_n import evaluate_pb0010
from engine.rules.pb.pb0011_retracement_above_61_8_percent import evaluate_pb0011
from engine.rules.pb.pb0012_retracement_above_78_6_percent import evaluate_pb0012
from engine.rules.pb.pb0013_pullback_low_below_prior_swing_low import evaluate_pb0013
from engine.rules.pb.pb0014_pullback_low_below_prior_higher_low import evaluate_pb0014
from engine.rules.pb.pb0015_pullback_duration_greater_than_n_bars import evaluate_pb0015
from engine.rules.pb.pb0016_pullback_range_wider_than_prior_leg import evaluate_pb0016
from engine.rules.pb.pb0017_pullback_depth_above_n_period_average import evaluate_pb0017
from engine.rules.pb.pb0018_price_below_50_percent_retracement_level import evaluate_pb0018
from engine.rules.pb.pb0019_pullback_low_at_n_period_low import evaluate_pb0019
from engine.rules.pb.pb0020_pullback_bar_count_greater_than_n import evaluate_pb0020
from engine.rules.pb.pb0021_price_touching_sma20_during_pullback import evaluate_pb0021
from engine.rules.pb.pb0022_price_touching_sma60_during_pullback import evaluate_pb0022
from engine.rules.pb.pb0023_price_touching_ema20_during_pullback import evaluate_pb0023
from engine.rules.pb.pb0024_price_touching_ema60_during_pullback import evaluate_pb0024
from engine.rules.pb.pb0025_price_closing_above_sma20_during_pullback import evaluate_pb0025
from engine.rules.pb.pb0026_price_closing_below_sma20_during_pullback import evaluate_pb0026
from engine.rules.pb.pb0027_price_closed_above_sma20_after_touch import evaluate_pb0027
from engine.rules.pb.pb0028_price_closed_above_sma60_after_touch import evaluate_pb0028
from engine.rules.pb.pb0029_price_above_sma_during_pullback import evaluate_pb0029
from engine.rules.pb.pb0030_price_below_sma_during_pullback import evaluate_pb0030
from engine.rules.pb.pb0031_pullback_volume_below_n_period_average import evaluate_pb0031
from engine.rules.pb.pb0032_pullback_volume_decreasing import evaluate_pb0032
from engine.rules.pb.pb0033_pullback_volume_lower_than_advance_volume import evaluate_pb0033
from engine.rules.pb.pb0034_pullback_volume_at_n_period_low import evaluate_pb0034
from engine.rules.pb.pb0035_pullback_volume_below_prior_bar import evaluate_pb0035
from engine.rules.pb.pb0036_pullback_volume_increasing import evaluate_pb0036
from engine.rules.pb.pb0037_pullback_volume_above_n_period_average import evaluate_pb0037
from engine.rules.pb.pb0038_pullback_volume_higher_than_advance_volume import evaluate_pb0038
from engine.rules.pb.pb0039_pullback_volume_spike import evaluate_pb0039
from engine.rules.pb.pb0040_pullback_volume_flat import evaluate_pb0040
from engine.rules.pb.pb0041_pullback_following_advance_leg import evaluate_pb0041
from engine.rules.pb.pb0042_pullback_following_decline_leg import evaluate_pb0042
from engine.rules.pb.pb0043_pullback_low_above_prior_higher_low import evaluate_pb0043
from engine.rules.pb.pb0044_pullback_high_below_prior_lower_high import evaluate_pb0044
from engine.rules.pb.pb0045_higher_low_formed_during_pullback import evaluate_pb0045
from engine.rules.pb.pb0046_lower_high_formed_during_pullback import evaluate_pb0046
from engine.rules.pb.pb0047_pullback_low_above_rising_sma import evaluate_pb0047
from engine.rules.pb.pb0048_pullback_high_below_falling_sma import evaluate_pb0048
from engine.rules.pb.pb0049_pullback_within_up_trend_channel import evaluate_pb0049
from engine.rules.pb.pb0050_pullback_within_down_trend_channel import evaluate_pb0050
from engine.rules.pb.pb0051_pullback_overlapping_prior_bars import evaluate_pb0051
from engine.rules.pb.pb0052_pullback_body_size_decreasing import evaluate_pb0052
from engine.rules.pb.pb0053_pullback_range_contracting import evaluate_pb0053
from engine.rules.pb.pb0054_pullback_range_expanding import evaluate_pb0054
from engine.rules.pb.pb0055_pullback_gap_present import evaluate_pb0055
from engine.rules.pb.pb0056_pullback_close_near_bar_high import evaluate_pb0056
from engine.rules.pb.pb0057_pullback_close_near_bar_low import evaluate_pb0057
from engine.rules.pb.pb0058_pullback_wick_rejection_at_support import evaluate_pb0058
from engine.rules.pb.pb0059_pullback_wick_rejection_at_ma import evaluate_pb0059
from engine.rules.pb.pb0060_pullback_candle_count_decreasing import evaluate_pb0060

RuleEvaluator = Callable[[pd.DataFrame], RuleResult]

PB_EVALUATORS: dict[str, RuleEvaluator] = {
    "PB0001": evaluate_pb0001,
    "PB0002": evaluate_pb0002,
    "PB0003": evaluate_pb0003,
    "PB0004": evaluate_pb0004,
    "PB0005": evaluate_pb0005,
    "PB0006": evaluate_pb0006,
    "PB0007": evaluate_pb0007,
    "PB0008": evaluate_pb0008,
    "PB0009": evaluate_pb0009,
    "PB0010": evaluate_pb0010,
    "PB0011": evaluate_pb0011,
    "PB0012": evaluate_pb0012,
    "PB0013": evaluate_pb0013,
    "PB0014": evaluate_pb0014,
    "PB0015": evaluate_pb0015,
    "PB0016": evaluate_pb0016,
    "PB0017": evaluate_pb0017,
    "PB0018": evaluate_pb0018,
    "PB0019": evaluate_pb0019,
    "PB0020": evaluate_pb0020,
    "PB0021": evaluate_pb0021,
    "PB0022": evaluate_pb0022,
    "PB0023": evaluate_pb0023,
    "PB0024": evaluate_pb0024,
    "PB0025": evaluate_pb0025,
    "PB0026": evaluate_pb0026,
    "PB0027": evaluate_pb0027,
    "PB0028": evaluate_pb0028,
    "PB0029": evaluate_pb0029,
    "PB0030": evaluate_pb0030,
    "PB0031": evaluate_pb0031,
    "PB0032": evaluate_pb0032,
    "PB0033": evaluate_pb0033,
    "PB0034": evaluate_pb0034,
    "PB0035": evaluate_pb0035,
    "PB0036": evaluate_pb0036,
    "PB0037": evaluate_pb0037,
    "PB0038": evaluate_pb0038,
    "PB0039": evaluate_pb0039,
    "PB0040": evaluate_pb0040,
    "PB0041": evaluate_pb0041,
    "PB0042": evaluate_pb0042,
    "PB0043": evaluate_pb0043,
    "PB0044": evaluate_pb0044,
    "PB0045": evaluate_pb0045,
    "PB0046": evaluate_pb0046,
    "PB0047": evaluate_pb0047,
    "PB0048": evaluate_pb0048,
    "PB0049": evaluate_pb0049,
    "PB0050": evaluate_pb0050,
    "PB0051": evaluate_pb0051,
    "PB0052": evaluate_pb0052,
    "PB0053": evaluate_pb0053,
    "PB0054": evaluate_pb0054,
    "PB0055": evaluate_pb0055,
    "PB0056": evaluate_pb0056,
    "PB0057": evaluate_pb0057,
    "PB0058": evaluate_pb0058,
    "PB0059": evaluate_pb0059,
    "PB0060": evaluate_pb0060,
}


def get_pb_evaluator(rule_id: str) -> RuleEvaluator:
    """Return evaluator for PB rule ID."""
    return PB_EVALUATORS[rule_id]
