"""CS rule evaluator registry (auto-generated)."""

from __future__ import annotations

from collections.abc import Callable

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.cs.cs0001_cs0060 import evaluate_cs0001
from engine.rules.cs.cs0002_inverted_hammer_formed import evaluate_cs0002
from engine.rules.cs.cs0003_bullish_marubozu_formed import evaluate_cs0003
from engine.rules.cs.cs0004_bullish_engulfing_formed import evaluate_cs0004
from engine.rules.cs.cs0005_piercing_line_formed import evaluate_cs0005
from engine.rules.cs.cs0006_morning_star_formed import evaluate_cs0006
from engine.rules.cs.cs0007_three_white_soldiers_formed import evaluate_cs0007
from engine.rules.cs.cs0008_bullish_harami_formed import evaluate_cs0008
from engine.rules.cs.cs0009_bullish_belt_hold_formed import evaluate_cs0009
from engine.rules.cs.cs0010_bullish_kicker_formed import evaluate_cs0010
from engine.rules.cs.cs0011_hanging_man_formed import evaluate_cs0011
from engine.rules.cs.cs0012_shooting_star_formed import evaluate_cs0012
from engine.rules.cs.cs0013_bearish_marubozu_formed import evaluate_cs0013
from engine.rules.cs.cs0014_bearish_engulfing_formed import evaluate_cs0014
from engine.rules.cs.cs0015_dark_cloud_cover_formed import evaluate_cs0015
from engine.rules.cs.cs0016_evening_star_formed import evaluate_cs0016
from engine.rules.cs.cs0017_three_black_crows_formed import evaluate_cs0017
from engine.rules.cs.cs0018_bearish_harami_formed import evaluate_cs0018
from engine.rules.cs.cs0019_bearish_belt_hold_formed import evaluate_cs0019
from engine.rules.cs.cs0020_bearish_kicker_formed import evaluate_cs0020
from engine.rules.cs.cs0021_tweezer_bottom_formed import evaluate_cs0021
from engine.rules.cs.cs0022_tweezer_top_formed import evaluate_cs0022
from engine.rules.cs.cs0023_bullish_abandoned_baby_formed import evaluate_cs0023
from engine.rules.cs.cs0024_bearish_abandoned_baby_formed import evaluate_cs0024
from engine.rules.cs.cs0025_island_reversal_bottom_formed import evaluate_cs0025
from engine.rules.cs.cs0026_island_reversal_top_formed import evaluate_cs0026
from engine.rules.cs.cs0027_bullish_key_reversal_formed import evaluate_cs0027
from engine.rules.cs.cs0028_bearish_key_reversal_formed import evaluate_cs0028
from engine.rules.cs.cs0029_morning_doji_star_formed import evaluate_cs0029
from engine.rules.cs.cs0030_evening_doji_star_formed import evaluate_cs0030
from engine.rules.cs.cs0031_rising_three_methods_formed import evaluate_cs0031
from engine.rules.cs.cs0032_falling_three_methods_formed import evaluate_cs0032
from engine.rules.cs.cs0033_bullish_mat_hold_formed import evaluate_cs0033
from engine.rules.cs.cs0034_bearish_mat_hold_formed import evaluate_cs0034
from engine.rules.cs.cs0035_upside_tasuki_gap_formed import evaluate_cs0035
from engine.rules.cs.cs0036_downside_tasuki_gap_formed import evaluate_cs0036
from engine.rules.cs.cs0037_bullish_side_by_side_white_lines_formed import evaluate_cs0037
from engine.rules.cs.cs0038_bearish_side_by_side_white_lines_formed import evaluate_cs0038
from engine.rules.cs.cs0039_bullish_separating_lines_formed import evaluate_cs0039
from engine.rules.cs.cs0040_bearish_separating_lines_formed import evaluate_cs0040
from engine.rules.cs.cs0041_standard_doji_formed import evaluate_cs0041
from engine.rules.cs.cs0042_long_legged_doji_formed import evaluate_cs0042
from engine.rules.cs.cs0043_dragonfly_doji_formed import evaluate_cs0043
from engine.rules.cs.cs0044_gravestone_doji_formed import evaluate_cs0044
from engine.rules.cs.cs0045_four_price_doji_formed import evaluate_cs0045
from engine.rules.cs.cs0046_rickshaw_man_doji_formed import evaluate_cs0046
from engine.rules.cs.cs0047_spinning_top_formed import evaluate_cs0047
from engine.rules.cs.cs0048_high_wave_candle_formed import evaluate_cs0048
from engine.rules.cs.cs0049_doji_star_formed import evaluate_cs0049
from engine.rules.cs.cs0050_double_doji_formed import evaluate_cs0050
from engine.rules.cs.cs0051_strong_bullish_candle import evaluate_cs0051
from engine.rules.cs.cs0052_strong_bearish_candle import evaluate_cs0052
from engine.rules.cs.cs0053_body_larger_than_n_period_average import evaluate_cs0053
from engine.rules.cs.cs0054_body_smaller_than_n_period_average import evaluate_cs0054
from engine.rules.cs.cs0055_range_larger_than_n_period_average import evaluate_cs0055
from engine.rules.cs.cs0056_range_smaller_than_n_period_average import evaluate_cs0056
from engine.rules.cs.cs0057_body_dominates_candle_range import evaluate_cs0057
from engine.rules.cs.cs0058_wick_dominates_candle_range import evaluate_cs0058
from engine.rules.cs.cs0059_three_bullish_candles_in_sequence import evaluate_cs0059
from engine.rules.cs.cs0060_three_bearish_candles_in_sequence import evaluate_cs0060

RuleEvaluator = Callable[[pd.DataFrame], RuleResult]

CS_EVALUATORS: dict[str, RuleEvaluator] = {
    "CS0001": evaluate_cs0001,
    "CS0002": evaluate_cs0002,
    "CS0003": evaluate_cs0003,
    "CS0004": evaluate_cs0004,
    "CS0005": evaluate_cs0005,
    "CS0006": evaluate_cs0006,
    "CS0007": evaluate_cs0007,
    "CS0008": evaluate_cs0008,
    "CS0009": evaluate_cs0009,
    "CS0010": evaluate_cs0010,
    "CS0011": evaluate_cs0011,
    "CS0012": evaluate_cs0012,
    "CS0013": evaluate_cs0013,
    "CS0014": evaluate_cs0014,
    "CS0015": evaluate_cs0015,
    "CS0016": evaluate_cs0016,
    "CS0017": evaluate_cs0017,
    "CS0018": evaluate_cs0018,
    "CS0019": evaluate_cs0019,
    "CS0020": evaluate_cs0020,
    "CS0021": evaluate_cs0021,
    "CS0022": evaluate_cs0022,
    "CS0023": evaluate_cs0023,
    "CS0024": evaluate_cs0024,
    "CS0025": evaluate_cs0025,
    "CS0026": evaluate_cs0026,
    "CS0027": evaluate_cs0027,
    "CS0028": evaluate_cs0028,
    "CS0029": evaluate_cs0029,
    "CS0030": evaluate_cs0030,
    "CS0031": evaluate_cs0031,
    "CS0032": evaluate_cs0032,
    "CS0033": evaluate_cs0033,
    "CS0034": evaluate_cs0034,
    "CS0035": evaluate_cs0035,
    "CS0036": evaluate_cs0036,
    "CS0037": evaluate_cs0037,
    "CS0038": evaluate_cs0038,
    "CS0039": evaluate_cs0039,
    "CS0040": evaluate_cs0040,
    "CS0041": evaluate_cs0041,
    "CS0042": evaluate_cs0042,
    "CS0043": evaluate_cs0043,
    "CS0044": evaluate_cs0044,
    "CS0045": evaluate_cs0045,
    "CS0046": evaluate_cs0046,
    "CS0047": evaluate_cs0047,
    "CS0048": evaluate_cs0048,
    "CS0049": evaluate_cs0049,
    "CS0050": evaluate_cs0050,
    "CS0051": evaluate_cs0051,
    "CS0052": evaluate_cs0052,
    "CS0053": evaluate_cs0053,
    "CS0054": evaluate_cs0054,
    "CS0055": evaluate_cs0055,
    "CS0056": evaluate_cs0056,
    "CS0057": evaluate_cs0057,
    "CS0058": evaluate_cs0058,
    "CS0059": evaluate_cs0059,
    "CS0060": evaluate_cs0060,
}


def get_cs_evaluator(rule_id: str) -> RuleEvaluator:
    """Return evaluator for CS rule ID."""
    return CS_EVALUATORS[rule_id]
