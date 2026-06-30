"""VO rule evaluator registry (auto-generated)."""

from __future__ import annotations

from collections.abc import Callable

import pandas as pd

from engine.core.types import RuleResult
from engine.rules.vo.vo0001_atr_rising import evaluate_vo0001
from engine.rules.vo.vo0002_atr_falling import evaluate_vo0002
from engine.rules.vo.vo0003_atr_above_prior_atr import evaluate_vo0003
from engine.rules.vo.vo0004_atr_below_prior_atr import evaluate_vo0004
from engine.rules.vo.vo0005_atr_above_n_period_average import evaluate_vo0005
from engine.rules.vo.vo0006_atr_below_n_period_average import evaluate_vo0006
from engine.rules.vo.vo0007_atr_at_n_period_high import evaluate_vo0007
from engine.rules.vo.vo0008_atr_at_n_period_low import evaluate_vo0008
from engine.rules.vo.vo0009_atr_flat import evaluate_vo0009
from engine.rules.vo.vo0010_atr_turning import evaluate_vo0010
from engine.rules.vo.vo0011_true_range_above_prior_true_range import evaluate_vo0011
from engine.rules.vo.vo0012_true_range_below_prior_true_range import evaluate_vo0012
from engine.rules.vo.vo0013_true_range_above_n_period_average import evaluate_vo0013
from engine.rules.vo.vo0014_true_range_below_n_period_average import evaluate_vo0014
from engine.rules.vo.vo0015_true_range_at_n_period_high import evaluate_vo0015
from engine.rules.vo.vo0016_true_range_at_n_period_low import evaluate_vo0016
from engine.rules.vo.vo0017_wide_true_range import evaluate_vo0017
from engine.rules.vo.vo0018_narrow_true_range import evaluate_vo0018
from engine.rules.vo.vo0019_true_range_expanding import evaluate_vo0019
from engine.rules.vo.vo0020_true_range_contracting import evaluate_vo0020
from engine.rules.vo.vo0021_historical_volatility_rising import evaluate_vo0021
from engine.rules.vo.vo0022_historical_volatility_falling import evaluate_vo0022
from engine.rules.vo.vo0023_historical_volatility_above_prior import evaluate_vo0023
from engine.rules.vo.vo0024_historical_volatility_below_prior import evaluate_vo0024
from engine.rules.vo.vo0025_historical_volatility_above_n_period_average import evaluate_vo0025
from engine.rules.vo.vo0026_historical_volatility_below_n_period_average import evaluate_vo0026
from engine.rules.vo.vo0027_historical_volatility_at_n_period_high import evaluate_vo0027
from engine.rules.vo.vo0028_historical_volatility_at_n_period_low import evaluate_vo0028
from engine.rules.vo.vo0029_historical_volatility_flat import evaluate_vo0029
from engine.rules.vo.vo0030_historical_volatility_turning import evaluate_vo0030
from engine.rules.vo.vo0031_price_above_upper_bollinger_band import evaluate_vo0031
from engine.rules.vo.vo0032_price_below_lower_bollinger_band import evaluate_vo0032
from engine.rules.vo.vo0033_price_at_upper_bollinger_band import evaluate_vo0033
from engine.rules.vo.vo0034_price_at_lower_bollinger_band import evaluate_vo0034
from engine.rules.vo.vo0035_price_at_middle_bollinger_band import evaluate_vo0035
from engine.rules.vo.vo0036_price_inside_bollinger_bands import evaluate_vo0036
from engine.rules.vo.vo0037_bollinger_band_width_above_average import evaluate_vo0037
from engine.rules.vo.vo0038_bollinger_band_width_below_average import evaluate_vo0038
from engine.rules.vo.vo0039_bollinger_band_width_at_n_period_low import evaluate_vo0039
from engine.rules.vo.vo0040_bollinger_band_width_at_n_period_high import evaluate_vo0040
from engine.rules.vo.vo0041_volatility_expanding import evaluate_vo0041
from engine.rules.vo.vo0042_volatility_contracting import evaluate_vo0042
from engine.rules.vo.vo0043_atr_expanding import evaluate_vo0043
from engine.rules.vo.vo0044_atr_contracting import evaluate_vo0044
from engine.rules.vo.vo0045_bollinger_band_width_expanding import evaluate_vo0045
from engine.rules.vo.vo0046_bollinger_band_width_contracting import evaluate_vo0046
from engine.rules.vo.vo0047_historical_volatility_expanding import evaluate_vo0047
from engine.rules.vo.vo0048_historical_volatility_contracting import evaluate_vo0048
from engine.rules.vo.vo0049_volatility_at_n_period_high import evaluate_vo0049
from engine.rules.vo.vo0050_volatility_at_n_period_low import evaluate_vo0050
from engine.rules.vo.vo0051_atr_stable import evaluate_vo0051
from engine.rules.vo.vo0052_historical_volatility_stable import evaluate_vo0052
from engine.rules.vo.vo0053_bollinger_band_width_stable import evaluate_vo0053
from engine.rules.vo.vo0054_true_range_stable import evaluate_vo0054
from engine.rules.vo.vo0055_atr_within_n_period_range import evaluate_vo0055
from engine.rules.vo.vo0056_historical_volatility_within_n_period_range import evaluate_vo0056
from engine.rules.vo.vo0057_bollinger_band_width_within_n_period_range import evaluate_vo0057
from engine.rules.vo.vo0058_consecutive_stable_atr import evaluate_vo0058
from engine.rules.vo.vo0059_volatility_consistency_high import evaluate_vo0059
from engine.rules.vo.vo0060_volatility_consistency_low import evaluate_vo0060

RuleEvaluator = Callable[[pd.DataFrame], RuleResult]

VO_EVALUATORS: dict[str, RuleEvaluator] = {
    "VO0001": evaluate_vo0001,
    "VO0002": evaluate_vo0002,
    "VO0003": evaluate_vo0003,
    "VO0004": evaluate_vo0004,
    "VO0005": evaluate_vo0005,
    "VO0006": evaluate_vo0006,
    "VO0007": evaluate_vo0007,
    "VO0008": evaluate_vo0008,
    "VO0009": evaluate_vo0009,
    "VO0010": evaluate_vo0010,
    "VO0011": evaluate_vo0011,
    "VO0012": evaluate_vo0012,
    "VO0013": evaluate_vo0013,
    "VO0014": evaluate_vo0014,
    "VO0015": evaluate_vo0015,
    "VO0016": evaluate_vo0016,
    "VO0017": evaluate_vo0017,
    "VO0018": evaluate_vo0018,
    "VO0019": evaluate_vo0019,
    "VO0020": evaluate_vo0020,
    "VO0021": evaluate_vo0021,
    "VO0022": evaluate_vo0022,
    "VO0023": evaluate_vo0023,
    "VO0024": evaluate_vo0024,
    "VO0025": evaluate_vo0025,
    "VO0026": evaluate_vo0026,
    "VO0027": evaluate_vo0027,
    "VO0028": evaluate_vo0028,
    "VO0029": evaluate_vo0029,
    "VO0030": evaluate_vo0030,
    "VO0031": evaluate_vo0031,
    "VO0032": evaluate_vo0032,
    "VO0033": evaluate_vo0033,
    "VO0034": evaluate_vo0034,
    "VO0035": evaluate_vo0035,
    "VO0036": evaluate_vo0036,
    "VO0037": evaluate_vo0037,
    "VO0038": evaluate_vo0038,
    "VO0039": evaluate_vo0039,
    "VO0040": evaluate_vo0040,
    "VO0041": evaluate_vo0041,
    "VO0042": evaluate_vo0042,
    "VO0043": evaluate_vo0043,
    "VO0044": evaluate_vo0044,
    "VO0045": evaluate_vo0045,
    "VO0046": evaluate_vo0046,
    "VO0047": evaluate_vo0047,
    "VO0048": evaluate_vo0048,
    "VO0049": evaluate_vo0049,
    "VO0050": evaluate_vo0050,
    "VO0051": evaluate_vo0051,
    "VO0052": evaluate_vo0052,
    "VO0053": evaluate_vo0053,
    "VO0054": evaluate_vo0054,
    "VO0055": evaluate_vo0055,
    "VO0056": evaluate_vo0056,
    "VO0057": evaluate_vo0057,
    "VO0058": evaluate_vo0058,
    "VO0059": evaluate_vo0059,
    "VO0060": evaluate_vo0060,
}


def get_vo_evaluator(rule_id: str) -> RuleEvaluator:
    """Return evaluator for VO rule ID."""
    return VO_EVALUATORS[rule_id]
