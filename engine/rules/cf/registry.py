"""CF rule evaluator registry (auto-generated)."""

from __future__ import annotations

from collections.abc import Callable

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.cf.cf0001_close_confirms_bullish_trend import evaluate_cf0001
from engine.rules.cf.cf0002_close_confirms_bearish_trend import evaluate_cf0002
from engine.rules.cf.cf0003_sma20_confirms_bullish_trend import evaluate_cf0003
from engine.rules.cf.cf0004_sma20_confirms_bearish_trend import evaluate_cf0004
from engine.rules.cf.cf0005_ema20_confirms_bullish_trend import evaluate_cf0005
from engine.rules.cf.cf0006_ema20_confirms_bearish_trend import evaluate_cf0006
from engine.rules.cf.cf0007_sma_alignment_confirms_bullish_trend import evaluate_cf0007
from engine.rules.cf.cf0008_sma_alignment_confirms_bearish_trend import evaluate_cf0008
from engine.rules.cf.cf0009_higher_high_confirms_bullish_trend import evaluate_cf0009
from engine.rules.cf.cf0010_lower_low_confirms_bearish_trend import evaluate_cf0010
from engine.rules.cf.cf0011_volume_confirms_bullish_trend import evaluate_cf0011
from engine.rules.cf.cf0012_volume_confirms_bearish_trend import evaluate_cf0012
from engine.rules.cf.cf0013_up_bar_volume_confirms_uptrend import evaluate_cf0013
from engine.rules.cf.cf0014_down_bar_volume_confirms_downtrend import evaluate_cf0014
from engine.rules.cf.cf0015_obv_rising_confirms_bullish_trend import evaluate_cf0015
from engine.rules.cf.cf0016_obv_falling_confirms_bearish_trend import evaluate_cf0016
from engine.rules.cf.cf0017_volume_above_average_confirms_bullish_trend import evaluate_cf0017
from engine.rules.cf.cf0018_volume_above_average_confirms_bearish_trend import evaluate_cf0018
from engine.rules.cf.cf0019_volume_spike_confirms_bullish_trend import evaluate_cf0019
from engine.rules.cf.cf0020_volume_spike_confirms_bearish_trend import evaluate_cf0020
from engine.rules.cf.cf0021_rsi_confirms_bullish_trend import evaluate_cf0021
from engine.rules.cf.cf0022_rsi_confirms_bearish_trend import evaluate_cf0022
from engine.rules.cf.cf0023_macd_confirms_bullish_trend import evaluate_cf0023
from engine.rules.cf.cf0024_macd_confirms_bearish_trend import evaluate_cf0024
from engine.rules.cf.cf0025_stochastic_confirms_bullish_trend import evaluate_cf0025
from engine.rules.cf.cf0026_stochastic_confirms_bearish_trend import evaluate_cf0026
from engine.rules.cf.cf0027_cci_confirms_bullish_trend import evaluate_cf0027
from engine.rules.cf.cf0028_cci_confirms_bearish_trend import evaluate_cf0028
from engine.rules.cf.cf0029_rate_of_change_confirms_bullish_trend import evaluate_cf0029
from engine.rules.cf.cf0030_rate_of_change_confirms_bearish_trend import evaluate_cf0030
from engine.rules.cf.cf0031_atr_rising_confirms_bullish_trend import evaluate_cf0031
from engine.rules.cf.cf0032_atr_rising_confirms_bearish_trend import evaluate_cf0032
from engine.rules.cf.cf0033_bollinger_band_width_expanding_confirms_breakout import evaluate_cf0033
from engine.rules.cf.cf0034_bollinger_band_width_contracting_confirms_consolidation import evaluate_cf0034
from engine.rules.cf.cf0035_volatility_above_average_confirms_bullish_trend import evaluate_cf0035
from engine.rules.cf.cf0036_volatility_above_average_confirms_bearish_trend import evaluate_cf0036
from engine.rules.cf.cf0037_true_range_above_average_confirms_bullish_trend import evaluate_cf0037
from engine.rules.cf.cf0038_true_range_above_average_confirms_bearish_trend import evaluate_cf0038
from engine.rules.cf.cf0039_historical_volatility_rising_confirms_bullish_trend import evaluate_cf0039
from engine.rules.cf.cf0040_historical_volatility_rising_confirms_bearish_trend import evaluate_cf0040
from engine.rules.cf.cf0041_price_and_volume_agreement import evaluate_cf0041
from engine.rules.cf.cf0042_price_and_momentum_agreement import evaluate_cf0042
from engine.rules.cf.cf0043_price_and_volatility_agreement import evaluate_cf0043
from engine.rules.cf.cf0044_trend_and_volume_agreement import evaluate_cf0044
from engine.rules.cf.cf0045_trend_and_momentum_agreement import evaluate_cf0045
from engine.rules.cf.cf0046_trend_and_volatility_agreement import evaluate_cf0046
from engine.rules.cf.cf0047_momentum_and_volume_agreement import evaluate_cf0047
from engine.rules.cf.cf0048_macd_and_rsi_agreement import evaluate_cf0048
from engine.rules.cf.cf0049_sma_and_ema_agreement import evaluate_cf0049
from engine.rules.cf.cf0050_multi_indicator_agreement import evaluate_cf0050
from engine.rules.cf.cf0051_confirmation_present import evaluate_cf0051
from engine.rules.cf.cf0052_confirmation_absent import evaluate_cf0052
from engine.rules.cf.cf0053_confirmation_sustained import evaluate_cf0053
from engine.rules.cf.cf0054_confirmation_lost import evaluate_cf0054
from engine.rules.cf.cf0055_confirmation_restored import evaluate_cf0055
from engine.rules.cf.cf0056_confirmation_increasing import evaluate_cf0056
from engine.rules.cf.cf0057_confirmation_decreasing import evaluate_cf0057
from engine.rules.cf.cf0058_confirmation_duration_long import evaluate_cf0058
from engine.rules.cf.cf0059_confirmation_duration_short import evaluate_cf0059
from engine.rules.cf.cf0060_confirmation_structure_stable import evaluate_cf0060

RuleEvaluator = Callable[[pd.DataFrame], RuleResult]

CF_EVALUATORS: dict[str, RuleEvaluator] = {
    "CF0001": evaluate_cf0001,
    "CF0002": evaluate_cf0002,
    "CF0003": evaluate_cf0003,
    "CF0004": evaluate_cf0004,
    "CF0005": evaluate_cf0005,
    "CF0006": evaluate_cf0006,
    "CF0007": evaluate_cf0007,
    "CF0008": evaluate_cf0008,
    "CF0009": evaluate_cf0009,
    "CF0010": evaluate_cf0010,
    "CF0011": evaluate_cf0011,
    "CF0012": evaluate_cf0012,
    "CF0013": evaluate_cf0013,
    "CF0014": evaluate_cf0014,
    "CF0015": evaluate_cf0015,
    "CF0016": evaluate_cf0016,
    "CF0017": evaluate_cf0017,
    "CF0018": evaluate_cf0018,
    "CF0019": evaluate_cf0019,
    "CF0020": evaluate_cf0020,
    "CF0021": evaluate_cf0021,
    "CF0022": evaluate_cf0022,
    "CF0023": evaluate_cf0023,
    "CF0024": evaluate_cf0024,
    "CF0025": evaluate_cf0025,
    "CF0026": evaluate_cf0026,
    "CF0027": evaluate_cf0027,
    "CF0028": evaluate_cf0028,
    "CF0029": evaluate_cf0029,
    "CF0030": evaluate_cf0030,
    "CF0031": evaluate_cf0031,
    "CF0032": evaluate_cf0032,
    "CF0033": evaluate_cf0033,
    "CF0034": evaluate_cf0034,
    "CF0035": evaluate_cf0035,
    "CF0036": evaluate_cf0036,
    "CF0037": evaluate_cf0037,
    "CF0038": evaluate_cf0038,
    "CF0039": evaluate_cf0039,
    "CF0040": evaluate_cf0040,
    "CF0041": evaluate_cf0041,
    "CF0042": evaluate_cf0042,
    "CF0043": evaluate_cf0043,
    "CF0044": evaluate_cf0044,
    "CF0045": evaluate_cf0045,
    "CF0046": evaluate_cf0046,
    "CF0047": evaluate_cf0047,
    "CF0048": evaluate_cf0048,
    "CF0049": evaluate_cf0049,
    "CF0050": evaluate_cf0050,
    "CF0051": evaluate_cf0051,
    "CF0052": evaluate_cf0052,
    "CF0053": evaluate_cf0053,
    "CF0054": evaluate_cf0054,
    "CF0055": evaluate_cf0055,
    "CF0056": evaluate_cf0056,
    "CF0057": evaluate_cf0057,
    "CF0058": evaluate_cf0058,
    "CF0059": evaluate_cf0059,
    "CF0060": evaluate_cf0060,
}


def get_cf_evaluator(rule_id: str) -> RuleEvaluator:
    """Return evaluator for CF rule ID."""
    return CF_EVALUATORS[rule_id]
