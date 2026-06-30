"""MR rule evaluator registry (auto-generated)."""

from __future__ import annotations

from collections.abc import Callable

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.mr.mr0001_close_above_sma200 import evaluate_mr0001
from engine.rules.mr.mr0002_close_above_sma60 import evaluate_mr0002
from engine.rules.mr.mr0003_close_above_sma20 import evaluate_mr0003
from engine.rules.mr.mr0004_sma20_above_sma60 import evaluate_mr0004
from engine.rules.mr.mr0005_sma60_above_sma200 import evaluate_mr0005
from engine.rules.mr.mr0006_sma20_rising import evaluate_mr0006
from engine.rules.mr.mr0007_sma60_rising import evaluate_mr0007
from engine.rules.mr.mr0008_sma200_rising import evaluate_mr0008
from engine.rules.mr.mr0009_n_period_return_positive import evaluate_mr0009
from engine.rules.mr.mr0010_close_at_n_period_high import evaluate_mr0010
from engine.rules.mr.mr0011_close_below_sma200 import evaluate_mr0011
from engine.rules.mr.mr0012_close_below_sma60 import evaluate_mr0012
from engine.rules.mr.mr0013_close_below_sma20 import evaluate_mr0013
from engine.rules.mr.mr0014_sma20_below_sma60 import evaluate_mr0014
from engine.rules.mr.mr0015_sma60_below_sma200 import evaluate_mr0015
from engine.rules.mr.mr0016_sma20_falling import evaluate_mr0016
from engine.rules.mr.mr0017_sma60_falling import evaluate_mr0017
from engine.rules.mr.mr0018_sma200_falling import evaluate_mr0018
from engine.rules.mr.mr0019_n_period_return_negative import evaluate_mr0019
from engine.rules.mr.mr0020_close_at_n_period_low import evaluate_mr0020
from engine.rules.mr.mr0021_close_between_sma20_and_sma60 import evaluate_mr0021
from engine.rules.mr.mr0022_sma20_flat import evaluate_mr0022
from engine.rules.mr.mr0023_sma60_flat import evaluate_mr0023
from engine.rules.mr.mr0024_close_within_n_period_range import evaluate_mr0024
from engine.rules.mr.mr0025_n_period_return_near_zero import evaluate_mr0025
from engine.rules.mr.mr0026_sma20_near_sma60 import evaluate_mr0026
from engine.rules.mr.mr0027_price_range_narrow import evaluate_mr0027
from engine.rules.mr.mr0028_adx_below_threshold import evaluate_mr0028
from engine.rules.mr.mr0029_close_near_n_period_midpoint import evaluate_mr0029
from engine.rules.mr.mr0030_overlapping_range_bars_present import evaluate_mr0030
from engine.rules.mr.mr0031_atr_above_n_period_average import evaluate_mr0031
from engine.rules.mr.mr0032_atr_at_n_period_high import evaluate_mr0032
from engine.rules.mr.mr0033_historical_volatility_above_n_period_average import evaluate_mr0033
from engine.rules.mr.mr0034_historical_volatility_at_n_period_high import evaluate_mr0034
from engine.rules.mr.mr0035_bollinger_band_width_above_average import evaluate_mr0035
from engine.rules.mr.mr0036_bollinger_band_width_at_n_period_high import evaluate_mr0036
from engine.rules.mr.mr0037_true_range_above_n_period_average import evaluate_mr0037
from engine.rules.mr.mr0038_wide_daily_range import evaluate_mr0038
from engine.rules.mr.mr0039_volatility_above_prior_period import evaluate_mr0039
from engine.rules.mr.mr0040_consecutive_wide_range_bars import evaluate_mr0040
from engine.rules.mr.mr0041_atr_below_n_period_average import evaluate_mr0041
from engine.rules.mr.mr0042_atr_at_n_period_low import evaluate_mr0042
from engine.rules.mr.mr0043_historical_volatility_below_n_period_average import evaluate_mr0043
from engine.rules.mr.mr0044_historical_volatility_at_n_period_low import evaluate_mr0044
from engine.rules.mr.mr0045_bollinger_band_width_below_average import evaluate_mr0045
from engine.rules.mr.mr0046_bollinger_band_width_at_n_period_low import evaluate_mr0046
from engine.rules.mr.mr0047_true_range_below_n_period_average import evaluate_mr0047
from engine.rules.mr.mr0048_narrow_daily_range import evaluate_mr0048
from engine.rules.mr.mr0049_volatility_below_prior_period import evaluate_mr0049
from engine.rules.mr.mr0050_consecutive_narrow_range_bars import evaluate_mr0050
from engine.rules.mr.mr0051_adx_above_threshold import evaluate_mr0051
from engine.rules.mr.mr0052_adx_rising import evaluate_mr0052
from engine.rules.mr.mr0053_adx_at_n_period_high import evaluate_mr0053
from engine.rules.mr.mr0054_adx_falling import evaluate_mr0054
from engine.rules.mr.mr0055_consecutive_close_above_sma200 import evaluate_mr0055
from engine.rules.mr.mr0056_consecutive_close_below_sma200 import evaluate_mr0056
from engine.rules.mr.mr0057_sma200_slope_steep import evaluate_mr0057
from engine.rules.mr.mr0058_sma200_slope_flat import evaluate_mr0058
from engine.rules.mr.mr0059_plus_di_above_minus_di import evaluate_mr0059
from engine.rules.mr.mr0060_minus_di_above_plus_di import evaluate_mr0060

RuleEvaluator = Callable[[pd.DataFrame], RuleResult]

MR_EVALUATORS: dict[str, RuleEvaluator] = {
    "MR0001": evaluate_mr0001,
    "MR0002": evaluate_mr0002,
    "MR0003": evaluate_mr0003,
    "MR0004": evaluate_mr0004,
    "MR0005": evaluate_mr0005,
    "MR0006": evaluate_mr0006,
    "MR0007": evaluate_mr0007,
    "MR0008": evaluate_mr0008,
    "MR0009": evaluate_mr0009,
    "MR0010": evaluate_mr0010,
    "MR0011": evaluate_mr0011,
    "MR0012": evaluate_mr0012,
    "MR0013": evaluate_mr0013,
    "MR0014": evaluate_mr0014,
    "MR0015": evaluate_mr0015,
    "MR0016": evaluate_mr0016,
    "MR0017": evaluate_mr0017,
    "MR0018": evaluate_mr0018,
    "MR0019": evaluate_mr0019,
    "MR0020": evaluate_mr0020,
    "MR0021": evaluate_mr0021,
    "MR0022": evaluate_mr0022,
    "MR0023": evaluate_mr0023,
    "MR0024": evaluate_mr0024,
    "MR0025": evaluate_mr0025,
    "MR0026": evaluate_mr0026,
    "MR0027": evaluate_mr0027,
    "MR0028": evaluate_mr0028,
    "MR0029": evaluate_mr0029,
    "MR0030": evaluate_mr0030,
    "MR0031": evaluate_mr0031,
    "MR0032": evaluate_mr0032,
    "MR0033": evaluate_mr0033,
    "MR0034": evaluate_mr0034,
    "MR0035": evaluate_mr0035,
    "MR0036": evaluate_mr0036,
    "MR0037": evaluate_mr0037,
    "MR0038": evaluate_mr0038,
    "MR0039": evaluate_mr0039,
    "MR0040": evaluate_mr0040,
    "MR0041": evaluate_mr0041,
    "MR0042": evaluate_mr0042,
    "MR0043": evaluate_mr0043,
    "MR0044": evaluate_mr0044,
    "MR0045": evaluate_mr0045,
    "MR0046": evaluate_mr0046,
    "MR0047": evaluate_mr0047,
    "MR0048": evaluate_mr0048,
    "MR0049": evaluate_mr0049,
    "MR0050": evaluate_mr0050,
    "MR0051": evaluate_mr0051,
    "MR0052": evaluate_mr0052,
    "MR0053": evaluate_mr0053,
    "MR0054": evaluate_mr0054,
    "MR0055": evaluate_mr0055,
    "MR0056": evaluate_mr0056,
    "MR0057": evaluate_mr0057,
    "MR0058": evaluate_mr0058,
    "MR0059": evaluate_mr0059,
    "MR0060": evaluate_mr0060,
}


def get_mr_evaluator(rule_id: str) -> RuleEvaluator:
    """Return evaluator for MR rule ID."""
    return MR_EVALUATORS[rule_id]
