"""MT rule evaluator registry (auto-generated)."""

from __future__ import annotations

from collections.abc import Callable

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.mt.mt0001_weekly_daily_uptrend_match import evaluate_mt0001
from engine.rules.mt.mt0002_weekly_daily_uptrend_conflict import evaluate_mt0002
from engine.rules.mt.mt0003_weekly_daily_downtrend_match import evaluate_mt0003
from engine.rules.mt.mt0004_weekly_daily_downtrend_conflict import evaluate_mt0004
from engine.rules.mt.mt0005_daily_4h_uptrend_match import evaluate_mt0005
from engine.rules.mt.mt0006_daily_4h_uptrend_conflict import evaluate_mt0006
from engine.rules.mt.mt0007_daily_4h_downtrend_match import evaluate_mt0007
from engine.rules.mt.mt0008_daily_4h_downtrend_conflict import evaluate_mt0008
from engine.rules.mt.mt0009_4h_1h_uptrend_match import evaluate_mt0009
from engine.rules.mt.mt0010_4h_1h_uptrend_conflict import evaluate_mt0010
from engine.rules.mt.mt0011_weekly_daily_price_above_sma20 import evaluate_mt0011
from engine.rules.mt.mt0012_weekly_daily_price_below_sma20 import evaluate_mt0012
from engine.rules.mt.mt0013_weekly_above_sma20_daily_below_sma20 import evaluate_mt0013
from engine.rules.mt.mt0014_daily_4h_price_above_sma20 import evaluate_mt0014
from engine.rules.mt.mt0015_daily_above_sma20_4h_below_sma20 import evaluate_mt0015
from engine.rules.mt.mt0016_daily_4h_price_below_sma20 import evaluate_mt0016
from engine.rules.mt.mt0017_weekly_daily_sma_bullish_alignment import evaluate_mt0017
from engine.rules.mt.mt0018_weekly_daily_sma_bearish_alignment import evaluate_mt0018
from engine.rules.mt.mt0019_weekly_daily_sma_golden_cross import evaluate_mt0019
from engine.rules.mt.mt0020_weekly_daily_sma_death_cross import evaluate_mt0020
from engine.rules.mt.mt0021_weekly_daily_rsi_above_50 import evaluate_mt0021
from engine.rules.mt.mt0022_weekly_daily_rsi_below_50 import evaluate_mt0022
from engine.rules.mt.mt0023_weekly_rsi_above_50_daily_below_50 import evaluate_mt0023
from engine.rules.mt.mt0024_weekly_daily_macd_above_zero import evaluate_mt0024
from engine.rules.mt.mt0025_weekly_daily_macd_below_zero import evaluate_mt0025
from engine.rules.mt.mt0026_daily_4h_macd_above_signal import evaluate_mt0026
from engine.rules.mt.mt0027_daily_4h_macd_below_signal import evaluate_mt0027
from engine.rules.mt.mt0028_weekly_daily_rsi_rising import evaluate_mt0028
from engine.rules.mt.mt0029_weekly_daily_rsi_falling import evaluate_mt0029
from engine.rules.mt.mt0030_daily_4h_stochastic_above_50 import evaluate_mt0030
from engine.rules.mt.mt0031_weekly_daily_close_above_n_period_high import evaluate_mt0031
from engine.rules.mt.mt0032_weekly_daily_close_below_n_period_low import evaluate_mt0032
from engine.rules.mt.mt0033_weekly_daily_swing_high_break import evaluate_mt0033
from engine.rules.mt.mt0034_weekly_daily_swing_low_break import evaluate_mt0034
from engine.rules.mt.mt0035_weekly_daily_resistance_break import evaluate_mt0035
from engine.rules.mt.mt0036_weekly_daily_support_break import evaluate_mt0036
from engine.rules.mt.mt0037_daily_4h_breakout_above_range import evaluate_mt0037
from engine.rules.mt.mt0038_daily_4h_breakout_below_range import evaluate_mt0038
from engine.rules.mt.mt0039_weekly_breakout_confirmed_by_daily_close import evaluate_mt0039
from engine.rules.mt.mt0040_daily_breakout_rejected_by_weekly_close import evaluate_mt0040
from engine.rules.mt.mt0041_weekly_daily_4h_trend_match import evaluate_mt0041
from engine.rules.mt.mt0042_weekly_daily_4h_trend_conflict import evaluate_mt0042
from engine.rules.mt.mt0043_daily_4h_1h_trend_match import evaluate_mt0043
from engine.rules.mt.mt0044_daily_4h_1h_trend_conflict import evaluate_mt0044
from engine.rules.mt.mt0045_higher_timeframe_trend_matches_lower_timeframe import evaluate_mt0045
from engine.rules.mt.mt0046_higher_timeframe_trend_opposes_lower_timeframe import evaluate_mt0046
from engine.rules.mt.mt0047_primary_secondary_uptrend_match import evaluate_mt0047
from engine.rules.mt.mt0048_primary_uptrend_secondary_downtrend import evaluate_mt0048
from engine.rules.mt.mt0049_primary_secondary_downtrend_match import evaluate_mt0049
from engine.rules.mt.mt0050_primary_downtrend_secondary_uptrend import evaluate_mt0050
from engine.rules.mt.mt0051_weekly_trend_supports_daily_trend import evaluate_mt0051
from engine.rules.mt.mt0052_weekly_trend_opposes_daily_trend import evaluate_mt0052
from engine.rules.mt.mt0053_higher_timeframe_range_contains_lower_timeframe import evaluate_mt0053
from engine.rules.mt.mt0054_lower_timeframe_range_extends_beyond_higher_timeframe import evaluate_mt0054
from engine.rules.mt.mt0055_multi_timeframe_higher_high_match import evaluate_mt0055
from engine.rules.mt.mt0056_multi_timeframe_lower_low_match import evaluate_mt0056
from engine.rules.mt.mt0057_multi_timeframe_volume_expansion_match import evaluate_mt0057
from engine.rules.mt.mt0058_multi_timeframe_volume_contraction_match import evaluate_mt0058
from engine.rules.mt.mt0059_multi_timeframe_bars_synchronized import evaluate_mt0059
from engine.rules.mt.mt0060_multi_timeframe_bars_desynchronized import evaluate_mt0060

RuleEvaluator = Callable[[pd.DataFrame], RuleResult]

MT_EVALUATORS: dict[str, RuleEvaluator] = {
    "MT0001": evaluate_mt0001,
    "MT0002": evaluate_mt0002,
    "MT0003": evaluate_mt0003,
    "MT0004": evaluate_mt0004,
    "MT0005": evaluate_mt0005,
    "MT0006": evaluate_mt0006,
    "MT0007": evaluate_mt0007,
    "MT0008": evaluate_mt0008,
    "MT0009": evaluate_mt0009,
    "MT0010": evaluate_mt0010,
    "MT0011": evaluate_mt0011,
    "MT0012": evaluate_mt0012,
    "MT0013": evaluate_mt0013,
    "MT0014": evaluate_mt0014,
    "MT0015": evaluate_mt0015,
    "MT0016": evaluate_mt0016,
    "MT0017": evaluate_mt0017,
    "MT0018": evaluate_mt0018,
    "MT0019": evaluate_mt0019,
    "MT0020": evaluate_mt0020,
    "MT0021": evaluate_mt0021,
    "MT0022": evaluate_mt0022,
    "MT0023": evaluate_mt0023,
    "MT0024": evaluate_mt0024,
    "MT0025": evaluate_mt0025,
    "MT0026": evaluate_mt0026,
    "MT0027": evaluate_mt0027,
    "MT0028": evaluate_mt0028,
    "MT0029": evaluate_mt0029,
    "MT0030": evaluate_mt0030,
    "MT0031": evaluate_mt0031,
    "MT0032": evaluate_mt0032,
    "MT0033": evaluate_mt0033,
    "MT0034": evaluate_mt0034,
    "MT0035": evaluate_mt0035,
    "MT0036": evaluate_mt0036,
    "MT0037": evaluate_mt0037,
    "MT0038": evaluate_mt0038,
    "MT0039": evaluate_mt0039,
    "MT0040": evaluate_mt0040,
    "MT0041": evaluate_mt0041,
    "MT0042": evaluate_mt0042,
    "MT0043": evaluate_mt0043,
    "MT0044": evaluate_mt0044,
    "MT0045": evaluate_mt0045,
    "MT0046": evaluate_mt0046,
    "MT0047": evaluate_mt0047,
    "MT0048": evaluate_mt0048,
    "MT0049": evaluate_mt0049,
    "MT0050": evaluate_mt0050,
    "MT0051": evaluate_mt0051,
    "MT0052": evaluate_mt0052,
    "MT0053": evaluate_mt0053,
    "MT0054": evaluate_mt0054,
    "MT0055": evaluate_mt0055,
    "MT0056": evaluate_mt0056,
    "MT0057": evaluate_mt0057,
    "MT0058": evaluate_mt0058,
    "MT0059": evaluate_mt0059,
    "MT0060": evaluate_mt0060,
}


def get_mt_evaluator(rule_id: str) -> RuleEvaluator:
    """Return evaluator for MT rule ID."""
    return MT_EVALUATORS[rule_id]
