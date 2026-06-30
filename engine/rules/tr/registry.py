"""TR rule evaluator registry (auto-generated)."""

from __future__ import annotations

from collections.abc import Callable

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.tr.tr0001_higher_high import evaluate_higher_high as evaluate_tr0001
from engine.rules.tr.atomic import evaluate_higher_low as evaluate_tr0002
from engine.rules.tr.atomic import evaluate_lower_high as evaluate_tr0003
from engine.rules.tr.atomic import evaluate_lower_low as evaluate_tr0004
from engine.rules.tr.tr0005_uptrend import evaluate_tr0005
from engine.rules.tr.tr0006_downtrend import evaluate_tr0006
from engine.rules.tr.tr0007_sideways_trend import evaluate_tr0007
from engine.rules.tr.tr0008_trend_reversal_up import evaluate_tr0008
from engine.rules.tr.tr0009_trend_reversal_down import evaluate_tr0009
from engine.rules.tr.tr0010_trend_continuation import evaluate_tr0010
from engine.rules.tr.tr0011_strong_uptrend import evaluate_tr0011
from engine.rules.tr.tr0012_weak_uptrend import evaluate_tr0012
from engine.rules.tr.tr0013_strong_downtrend import evaluate_tr0013
from engine.rules.tr.tr0014_weak_downtrend import evaluate_tr0014
from engine.rules.tr.tr0015_adx_rising import evaluate_tr0015
from engine.rules.tr.tr0016_adx_falling import evaluate_tr0016
from engine.rules.tr.tr0017_adx_above_threshold import evaluate_tr0017
from engine.rules.tr.tr0018_adx_below_threshold import evaluate_tr0018
from engine.rules.tr.tr0019_trend_momentum_increasing import evaluate_tr0019
from engine.rules.tr.tr0020_trend_momentum_decreasing import evaluate_tr0020
from engine.rules.tr.tr0021_clean_uptrend import evaluate_tr0021
from engine.rules.tr.tr0022_clean_downtrend import evaluate_tr0022
from engine.rules.tr.tr0023_choppy_trend import evaluate_tr0023
from engine.rules.tr.tr0024_smooth_trend import evaluate_tr0024
from engine.rules.tr.tr0025_noisy_trend import evaluate_tr0025
from engine.rules.tr.tr0026_stable_trend import evaluate_tr0026
from engine.rules.tr.tr0027_unstable_trend import evaluate_tr0027
from engine.rules.tr.tr0028_trend_consistency_high import evaluate_tr0028
from engine.rules.tr.tr0029_trend_consistency_low import evaluate_tr0029
from engine.rules.tr.tr0030_trend_integrity import evaluate_tr0030
from engine.rules.tr.tr0031_positive_slope import evaluate_tr0031
from engine.rules.tr.tr0032_negative_slope import evaluate_tr0032
from engine.rules.tr.tr0033_flat_slope import evaluate_tr0033
from engine.rules.tr.tr0034_increasing_slope import evaluate_tr0034
from engine.rules.tr.tr0035_decreasing_slope import evaluate_tr0035
from engine.rules.tr.tr0036_accelerating_trend import evaluate_tr0036
from engine.rules.tr.tr0037_decelerating_trend import evaluate_tr0037
from engine.rules.tr.tr0038_slope_breakout import evaluate_tr0038
from engine.rules.tr.tr0039_slope_reversal import evaluate_tr0039
from engine.rules.tr.tr0040_slope_stability import evaluate_tr0040
from engine.rules.tr.tr0041_consecutive_higher_highs import evaluate_tr0041
from engine.rules.tr.tr0042_consecutive_higher_lows import evaluate_tr0042
from engine.rules.tr.tr0043_consecutive_lower_highs import evaluate_tr0043
from engine.rules.tr.tr0044_consecutive_lower_lows import evaluate_tr0044
from engine.rules.tr.tr0045_trend_persistence_high import evaluate_tr0045
from engine.rules.tr.tr0046_trend_persistence_low import evaluate_tr0046
from engine.rules.tr.tr0047_trend_duration_short import evaluate_tr0047
from engine.rules.tr.tr0048_trend_duration_medium import evaluate_tr0048
from engine.rules.tr.tr0049_trend_duration_long import evaluate_tr0049
from engine.rules.tr.tr0050_trend_age_increasing import evaluate_tr0050
from engine.rules.tr.tr0051_trend_exhaustion_up import evaluate_tr0051
from engine.rules.tr.tr0052_trend_exhaustion_down import evaluate_tr0052
from engine.rules.tr.tr0053_buying_exhaustion import evaluate_tr0053
from engine.rules.tr.tr0054_selling_exhaustion import evaluate_tr0054
from engine.rules.tr.tr0055_trend_climax import evaluate_tr0055
from engine.rules.tr.tr0056_trend_weakening import evaluate_tr0056
from engine.rules.tr.tr0057_trend_failure import evaluate_tr0057
from engine.rules.tr.tr0058_failed_trend_continuation import evaluate_tr0058
from engine.rules.tr.tr0059_failed_trend_reversal import evaluate_tr0059
from engine.rules.tr.tr0060_exhaustion_recovery import evaluate_tr0060
from engine.rules.tr.tr0061_price_confirms_trend import evaluate_tr0061
from engine.rules.tr.tr0062_volume_confirms_trend import evaluate_tr0062
from engine.rules.tr.tr0063_momentum_confirms_trend import evaluate_tr0063
from engine.rules.tr.tr0064_volatility_confirms_trend import evaluate_tr0064
from engine.rules.tr.tr0065_multi_indicator_confirmation import evaluate_tr0065
from engine.rules.tr.tr0066_multi_timeframe_confirmation import evaluate_tr0066
from engine.rules.tr.tr0067_trend_confirmation_strong import evaluate_tr0067
from engine.rules.tr.tr0068_trend_confirmation_weak import evaluate_tr0068
from engine.rules.tr.tr0069_trend_confirmation_lost import evaluate_tr0069
from engine.rules.tr.tr0070_trend_confirmation_restored import evaluate_tr0070
from engine.rules.tr.tr0071_trend_established import evaluate_tr0071
from engine.rules.tr.tr0072_trend_emerging import evaluate_tr0072
from engine.rules.tr.tr0073_trend_maturing import evaluate_tr0073
from engine.rules.tr.tr0074_trend_ending import evaluate_tr0074
from engine.rules.tr.tr0075_trend_restarting import evaluate_tr0075
from engine.rules.tr.tr0076_bull_trend_state import evaluate_tr0076
from engine.rules.tr.tr0077_bear_trend_state import evaluate_tr0077
from engine.rules.tr.tr0078_neutral_trend_state import evaluate_tr0078
from engine.rules.tr.tr0079_trend_transition import evaluate_tr0079
from engine.rules.tr.tr0080_trend_undefined import evaluate_tr0080

RuleEvaluator = Callable[[pd.DataFrame], RuleResult]

TR_EVALUATORS: dict[str, RuleEvaluator] = {
    "TR0001": evaluate_tr0001,
    "TR0002": evaluate_tr0002,
    "TR0003": evaluate_tr0003,
    "TR0004": evaluate_tr0004,
    "TR0005": evaluate_tr0005,
    "TR0006": evaluate_tr0006,
    "TR0007": evaluate_tr0007,
    "TR0008": evaluate_tr0008,
    "TR0009": evaluate_tr0009,
    "TR0010": evaluate_tr0010,
    "TR0011": evaluate_tr0011,
    "TR0012": evaluate_tr0012,
    "TR0013": evaluate_tr0013,
    "TR0014": evaluate_tr0014,
    "TR0015": evaluate_tr0015,
    "TR0016": evaluate_tr0016,
    "TR0017": evaluate_tr0017,
    "TR0018": evaluate_tr0018,
    "TR0019": evaluate_tr0019,
    "TR0020": evaluate_tr0020,
    "TR0021": evaluate_tr0021,
    "TR0022": evaluate_tr0022,
    "TR0023": evaluate_tr0023,
    "TR0024": evaluate_tr0024,
    "TR0025": evaluate_tr0025,
    "TR0026": evaluate_tr0026,
    "TR0027": evaluate_tr0027,
    "TR0028": evaluate_tr0028,
    "TR0029": evaluate_tr0029,
    "TR0030": evaluate_tr0030,
    "TR0031": evaluate_tr0031,
    "TR0032": evaluate_tr0032,
    "TR0033": evaluate_tr0033,
    "TR0034": evaluate_tr0034,
    "TR0035": evaluate_tr0035,
    "TR0036": evaluate_tr0036,
    "TR0037": evaluate_tr0037,
    "TR0038": evaluate_tr0038,
    "TR0039": evaluate_tr0039,
    "TR0040": evaluate_tr0040,
    "TR0041": evaluate_tr0041,
    "TR0042": evaluate_tr0042,
    "TR0043": evaluate_tr0043,
    "TR0044": evaluate_tr0044,
    "TR0045": evaluate_tr0045,
    "TR0046": evaluate_tr0046,
    "TR0047": evaluate_tr0047,
    "TR0048": evaluate_tr0048,
    "TR0049": evaluate_tr0049,
    "TR0050": evaluate_tr0050,
    "TR0051": evaluate_tr0051,
    "TR0052": evaluate_tr0052,
    "TR0053": evaluate_tr0053,
    "TR0054": evaluate_tr0054,
    "TR0055": evaluate_tr0055,
    "TR0056": evaluate_tr0056,
    "TR0057": evaluate_tr0057,
    "TR0058": evaluate_tr0058,
    "TR0059": evaluate_tr0059,
    "TR0060": evaluate_tr0060,
    "TR0061": evaluate_tr0061,
    "TR0062": evaluate_tr0062,
    "TR0063": evaluate_tr0063,
    "TR0064": evaluate_tr0064,
    "TR0065": evaluate_tr0065,
    "TR0066": evaluate_tr0066,
    "TR0067": evaluate_tr0067,
    "TR0068": evaluate_tr0068,
    "TR0069": evaluate_tr0069,
    "TR0070": evaluate_tr0070,
    "TR0071": evaluate_tr0071,
    "TR0072": evaluate_tr0072,
    "TR0073": evaluate_tr0073,
    "TR0074": evaluate_tr0074,
    "TR0075": evaluate_tr0075,
    "TR0076": evaluate_tr0076,
    "TR0077": evaluate_tr0077,
    "TR0078": evaluate_tr0078,
    "TR0079": evaluate_tr0079,
    "TR0080": evaluate_tr0080,
}


def get_tr_evaluator(rule_id: str) -> RuleEvaluator:
    """Return evaluator for TR rule ID."""
    return TR_EVALUATORS[rule_id]
